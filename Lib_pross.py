# -----------------------------------------------------------------------------
# ------------------------------ LIBRERIA RIESGO ------------------------------
# -----------------------------------------------------------------------------
"""
-------------------------------------------------------------------------------
Este script contiene las funciones que permiten procesar los resultados de 
riesgo
---------------------------- Autor: Daniela Novoa -----------------------------
"""
#%% ====== Import libraries ===================================================
# -------- Tkinter Library ----------------------------------------------------
import tkinter as tk
# -------- Directory Library --------------------------------------------------
import os
# -------- Data processing libraries ------------------------------------------
import pandas as pd
import numpy as np
# -------- HDF5 libraries -----------------------------------------------------
import h5py
import json
# -------- Generar mapas ------------------------------------------------------
import geopandas as gpd
import contextily as ctx
from matplotlib.colors import Normalize
import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.axes_grid1.anchored_artists import AnchoredSizeBar
import matplotlib.font_manager as fm
import matplotlib.offsetbox as offsetbox
from matplotlib.patches import Patch
from matplotlib.patches import Rectangle
import re
#%% ====== Funcion: Loss/CLB ==================================================
"""
-------------------------------------------------------------------------------
Procesado perdidas>calibrar
-------------------------------------------------------------------------------
"""
def function_CLB(carpeta_seleccionada):
    # 1). Esta sección busca los directorios que hay en la carpeta 
    rootdir1 = carpeta_seleccionada                                         # Obtiene el directorio actual                                              
    directorios = []
    for subdir in os.listdir(rootdir1):                                     # Ciclo for para la lista de directorios dentro del directorio actual
        a = os.path.join(rootdir1, subdir)                                  # Obtiene las rutas de las carpetas dentro del directorio actual
        directorios.append(a)    
    # 2). Obtener la lista de archivos en el directorio actual.
    # Esta lista de archivos obtiene unicamente los que comienzan con calc_
    # y terminan en .hdf5
    archivos_hdf5 = []
    for archivo in os.listdir(rootdir1): 
        if archivo.startswith("calc_") and archivo.endswith(".hdf5"):
            archivos_hdf5.append(os.path.join(rootdir1, archivo))
    # 3). Procesar datos del hdf5.
    Nsim2, agg_risk, agg_risk_mnz, df_AGRmnz_list, df_AGR_list, Nevents = [], [], [], [], [], []
    for arch_hdf5 in archivos_hdf5:
        ruta_hdf5 = arch_hdf5
        # 3.1). Cargar archivos de entrada.
        with h5py.File(ruta_hdf5, 'r') as archivo: 
            oqparam_dict = json.loads(archivo["oqparam"][()].decode('utf-8'))     # Lista de parametros de OpenQuake
            mnz_list_bytes = archivo["assetcol"]["tagcol"]["cod_mnz"][()][1:]     # Lista de manzanas
            mnz_list = [item.decode('utf-8') for item in mnz_list_bytes]
            txn_list_bytes  = archivo["assetcol"]["tagcol"]["taxonomy"][()][1:]   # Lista de taxonomias
            txn_list = [item.decode('utf-8') for item in txn_list_bytes]
            aggrisk_aggid = archivo["aggrisk"]["agg_id"][()]                      # ID del agregado
            aggrisk_loss = archivo["aggrisk"]["loss"][()]                         # Perdidas segun el aggregate ID
            events = archivo["events"][()]                                        # eventos de la simulacion
        Nevents.append(len(events))
        list_stats = ['mean']
        for quant in oqparam_dict['quantiles']:
            list_stats.append('quantile-'+str(quant))                       # Lista de estadisticas
        Nsim2.append(oqparam_dict['ses_per_logic_tree_path'])               # Numero de simulaciones
        opcion = mnz_list                                                   # Opcion catalogo de manzanas
        CP_Name = oqparam_dict['description'].split('-')[-1].strip()        # Nombre del centro poblado inicial
        if CP_Name[0].islower():
            CP_Name = CP_Name[0].upper() + CP_Name[1:]                      # Si el nombre del centro poblado no comienza con una mayuscula
        # 3.2). Procesado:
        df_group = pd.DataFrame({'agg_id':aggrisk_aggid, 'loss':aggrisk_loss})  # Dataframe perdidas por aggid
        grp_aggid = df_group.groupby('agg_id')['loss']                          # Agrupa las perdidas por aggid
        stats_agg = grp_aggid.describe(percentiles=oqparam_dict['quantiles'])   # Calcula mediana y percentiles de las perdidas por aggid
        stats_agg.reset_index(level=0, inplace=True)                            # Genera un indice, agg_id se vuelve en columna
        stats_agg_mnp = stats_agg[stats_agg['agg_id'] == oqparam_dict['K']]     # Genera un dataframe para municipio
        stats_agg.drop(stats_agg_mnp.index, inplace=True)                       # Dataframe de perdidas por manzana o por manzana + taxonomia
        stats_agg_mnp.reset_index(level=0, inplace=True)                        # Resetea el indice municipio
        stats_agg.reset_index(level=0, inplace=True)                            # Resetea el indice agregado
        # Agrupar por estadisticas
        dfmelted_mnp = stats_agg_mnp.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
        dfmelted_mnz = stats_agg.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
        dfmelted_mnz.sort_values(by='agg_id', inplace=True)                 # Ordenar de menor a mayor los agg_id
        # Cambiar el nombre de las estadisticas
        dfmelted_mnz['stat'] = dfmelted_mnz['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
        dfmelted_mnp['stat'] = dfmelted_mnp['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
        dfmelted_mnp = dfmelted_mnp.drop(columns=['agg_id'])                # Eliminar la columna agg_id
        # -----------------------------------------------------------------
        # --------------------- Segun el aggregate by ---------------------
        # -----------------------------------------------------------------
        if oqparam_dict['aggregate_by'] == [['cod_mnz']]:                   # Si esta agregado por manzanas
            dfmelted_mnz['cod_mnz'] = np.array(mnz_list)[(dfmelted_mnz['agg_id'] / 1).astype(int)]
            
            lossopcion = dfmelted_mnz.loc[dfmelted_mnz.stat=='mean'].loss   # Perdidas por manzana
            dfopcion = pd.DataFrame({'cod_mnz':opcion,'loss':lossopcion})   # Dataframe de perdidas por manzana
            df_sorted = dfopcion.sort_values(by='loss', ascending=False)    # Organizar de mayor a menor perdida las manzanas
            sorted_opcion = df_sorted.cod_mnz.tolist()                      # Obtener la lista de manzanas ordenada 
            
        elif oqparam_dict['aggregate_by'] == [['cod_mnz', 'taxonomy']]:     # Si esta agregado por manzana y taxonomia
            txn_index1 = [int(str(x)[-1]) if len(str(x)) == 1 else (int(str(x)[-1]) if int(str(x)[-2]) % 2 == 0 else int('1'+str(x)[-1])) for x in dfmelted_mnz.agg_id]
            dfmelted_mnz['cod_mnz'] = np.array(mnz_list)[(dfmelted_mnz['agg_id'] / len(txn_list)).astype(int)] 
            dfmelted_mnz['taxonomy'] = np.array(txn_list)[txn_index1]
            
            lossop1 = dfmelted_mnz[dfmelted_mnz['stat'] == 'mean']
            lossopcion = lossop1.groupby('cod_mnz')['loss'].sum()           # Perdidas por manzana
            dfopcion = pd.DataFrame({'cod_mnz':opcion,'loss':lossopcion})   # Dataframe de perdidas por manzana
            df_sorted = dfopcion.sort_values(by='loss', ascending=False)    # Organizar de mayor a menor perdida las manzanas
            sorted_opcion = df_sorted.cod_mnz.tolist()                      # Obtener la lista de manzanas ordenada 
            
        dfmelted_mnz = dfmelted_mnz.drop(columns=['agg_id'])                # Eliminar la columna agg_id
        dfmelted_mnz = dfmelted_mnz.reset_index(drop=True)                  # Resetear el index
        
        # ------------------ LISTAS A EXPORTAR/ PROCESAR ------------------
        df_AGR_list.append(dfmelted_mnp)                                    # Lista de los dataframes de cada simulacion (Municipio)
        agg_risk.append(dfmelted_mnp.loc[dfmelted_mnp.stat=='mean'].loss)   # Lista de las perdidas por simulacion (Municipio) 
        df_AGRmnz_list.append(dfmelted_mnz)                                 # Lista de los dataframes de cada simulacion (Aggregate by)
        agg_risk_mnz.append(dfmelted_mnz.loc[dfmelted_mnz.stat=='mean'].loss) # Lista de las perdidas por simulacion (Aggregate by) 

    # 4). Genera el grafico de perdida anual promedio por simulacion del 
    # centro poblado
                
    # Cálculo del error promedio entre datos adyacentes
    agg_risk_error = [0] 
    for i in range(1, len(agg_risk)-1):
        error1 = np.abs(1-(agg_risk[i]/agg_risk[i-1]))*100
        error2 = np.abs(1-(agg_risk[i+1]/agg_risk[i]))*100
        error_promedio = np.mean([error1,error2])
        agg_risk_error.append(float(error_promedio))
    agg_risk_error.append(np.abs(1-(agg_risk[i+1]/agg_risk[i]))*100)
    
    datos_CP = {'Num_Sim':Nsim2,'loss':agg_risk, 'error':agg_risk_error}
    datos_events_CP = {'Num_Sim':Nevents,'loss':agg_risk, 'error':agg_risk_error}
    
    # 5). Genera el grafico de perdida anual promedio por simulacion por
    # manzana.
    # Se crea la lista que ira en el combo de las manzanas
    opciones, codigomnzs = [], []
    for op in sorted_opcion:
        opciones.append(op[-8:])
        codigomnzs.append(op[:-8])
    # 5.1). Se generan los datos a graficar
    # Se debe obtener una lista con las perdidas promedio de una manzana en 
    # especifico por simulacion. En porcentaje
    lossnew, agg_riskmnz, max_loss_manzana = [], [], []
    for ind, loss in enumerate(df_AGRmnz_list):
        # Obtener una lista con los resultados del dataframe filtrado 
        # solamente para los valores promedio
        lossnew.append(loss[loss['stat']=='mean']) 
        # Obtener un dataframe con solamente las manzanas y la perdida 
        # promedio correspondiente                       
        agg_riskmnz.append(lossnew[ind].groupby('cod_mnz')['loss'].sum().reset_index())
        # Genera una nueva columna para calcular las perdidas en porcentaje
        # de esa manzana
        agg_riskmnz[ind]['Perdidas'] = agg_riskmnz[ind].loss/np.sum(agg_riskmnz[ind].loss)
        agg_riskmnz[ind]['Perdidas2'] = agg_riskmnz[ind].loss
        # Otener la manzana predominante del municipio
        max_loss_manzana.append(agg_riskmnz[ind][agg_riskmnz[ind]['loss']==agg_riskmnz[ind]['loss'].max()])
    
    simmnz_losses = pd.concat([df.set_index('cod_mnz')['Perdidas'] for df in agg_riskmnz], axis=1).reset_index()     
    simmnz_losses2 = pd.concat([df.set_index('cod_mnz')['Perdidas2'] for df in agg_riskmnz], axis=1).reset_index()     
    nombres_simulaciones = ['Sim_{}'.format(i) for i in Nsim2]
    simmnz_losses.columns = ['Manzana'] + nombres_simulaciones
    simmnz_losses2.columns = ['Manzana'] + nombres_simulaciones
    maxloss = max_loss_manzana[0]
    manzanapred = maxloss['cod_mnz'].values[0]
    newNsim = sorted(Nsim2)
    fila_a_graficar = simmnz_losses.loc[simmnz_losses['Manzana'] == manzanapred]
    fila_a_graficar2 = simmnz_losses2.loc[simmnz_losses2['Manzana'] == manzanapred]
    fila_a_graficar = fila_a_graficar[['Manzana']+['Sim_{}'.format(i) for i in newNsim]]
    fila_a_graficar2 = fila_a_graficar2[['Manzana']+['Sim_{}'.format(i) for i in newNsim]]
    fila_a_graficar = fila_a_graficar.drop(columns=['Manzana'])
    fila_a_graficar2 = fila_a_graficar2.drop(columns=['Manzana'])
    datos_fila = fila_a_graficar.values[0]*100
    datos_fila2 = fila_a_graficar2.values[0]
    
    # Cálculo del error promedio entre datos adyacentes
    datos_fila_error = [0] 
    for i in range(1, len(datos_fila2)-1):
        error1 = np.abs(1-(datos_fila2[i]/datos_fila2[i-1]))*100
        error2 = np.abs(1-(datos_fila2[i+1]/datos_fila2[i]))*100
        error_promedio = np.mean([error1,error2])
        datos_fila_error.append(float(error_promedio))
    datos_fila_error.append(np.abs(1-(datos_fila2[i+1]/datos_fila2[i]))*100)
    
    datos_MNZ = {'Num_Sim':newNsim,'loss':datos_fila,'error':datos_fila_error}
    datos_events_MNZ = {'Num_Sim':sorted(Nevents),'loss':datos_fila,'error':datos_fila_error}
    
    return df_AGR_list, df_AGRmnz_list, Nsim2, datos_CP, datos_events_CP, datos_MNZ, datos_events_MNZ,manzanapred,CP_Name,opciones,codigomnzs,simmnz_losses,simmnz_losses2,newNsim
#%% ====== Funcion: Loss/DSP ==================================================
def function_DSP(carpeta_seleccionada):
    # 1). Esta sección busca los directorios que hay en la carpeta 
    rootdir1 = carpeta_seleccionada                                         # Obtiene el directorio actual                                              
    directorios = []
    for subdir in os.listdir(rootdir1):                                     # Ciclo for para la lista de directorios dentro del directorio actual
        a = os.path.join(rootdir1, subdir)                                  # Obtiene las rutas de las carpetas dentro del directorio actual
        directorios.append(a)    
    # 2). Obtener la lista de archivos en el directorio actual.
    # Esta lista de archivos obtiene unicamente los que comienzan con calc_
    # y terminan en .hdf5
    archivos_hdf5 = []
    for archivo in os.listdir(rootdir1): 
        if archivo.startswith("calc_") and archivo.endswith(".hdf5"):
            archivos_hdf5.append(os.path.join(rootdir1, archivo))
    # 3). Procesar datos del hdf5.
    Nsim2, agg_risk, agg_risk_mnz, df_AGRmnz_list, df_AGR_list, Nevents = [], [], [], [], [], []
    for arch_hdf5 in archivos_hdf5:
        ruta_hdf5 = arch_hdf5
        # 3.1). Cargar archivos de entrada.
        with h5py.File(ruta_hdf5, 'r') as archivo: 
            oqparam_dict = json.loads(archivo["oqparam"][()].decode('utf-8'))     # Lista de parametros de OpenQuake
            mnz_list_bytes = archivo["assetcol"]["tagcol"]["cod_mnz"][()][1:]     # Lista de manzanas
            mnz_list = [item.decode('utf-8') for item in mnz_list_bytes]
            txn_list_bytes  = archivo["assetcol"]["tagcol"]["taxonomy"][()][1:]   # Lista de taxonomias
            txn_list = [item.decode('utf-8') for item in txn_list_bytes]
            aggrisk_aggid = archivo["aggrisk"]["agg_id"][()]                      # ID del agregado
            aggrisk_loss = archivo["aggrisk"]["loss"][()]                         # Perdidas segun el aggregate ID
            events = archivo["events"][()]                                        # eventos de la simulacion
        Nevents.append(len(events))
        list_stats = ['mean']
        for quant in oqparam_dict['quantiles']:
            list_stats.append('quantile-'+str(quant))                       # Lista de estadisticas
        Nsim2.append(oqparam_dict['ses_per_logic_tree_path'])               # Numero de simulaciones
        CP_Name = oqparam_dict['description'].split('-')[-1].strip()        # Nombre del centro poblado inicial
        if CP_Name[0].islower():
            CP_Name = CP_Name[0].upper() + CP_Name[1:]                      # Si el nombre del centro poblado no comienza con una mayuscula
        # 3.2). Procesado:
        df_group = pd.DataFrame({'agg_id':aggrisk_aggid, 'loss':aggrisk_loss})  # Dataframe perdidas por aggid
        grp_aggid = df_group.groupby('agg_id')['loss']                          # Agrupa las perdidas por aggid
        stats_agg = grp_aggid.describe(percentiles=oqparam_dict['quantiles'])   # Calcula mediana y percentiles de las perdidas por aggid
        stats_agg.reset_index(level=0, inplace=True)                            # Genera un indice, agg_id se vuelve en columna
        stats_agg_mnp = stats_agg[stats_agg['agg_id'] == oqparam_dict['K']]     # Genera un dataframe para municipio
        stats_agg.drop(stats_agg_mnp.index, inplace=True)                       # Dataframe de perdidas por manzana o por manzana + taxonomia
        stats_agg_mnp.reset_index(level=0, inplace=True)                        # Resetea el indice municipio
        stats_agg.reset_index(level=0, inplace=True)                            # Resetea el indice agregado
        # Agrupar por estadisticas
        dfmelted_mnp = stats_agg_mnp.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
        dfmelted_mnz = stats_agg.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
        dfmelted_mnz.sort_values(by='agg_id', inplace=True)                 # Ordenar de menor a mayor los agg_id
        # Cambiar el nombre de las estadisticas
        dfmelted_mnz['stat'] = dfmelted_mnz['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
        dfmelted_mnp['stat'] = dfmelted_mnp['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
        dfmelted_mnp = dfmelted_mnp.drop(columns=['agg_id'])                # Eliminar la columna agg_id
        # -----------------------------------------------------------------
        # --------------------- Segun el aggregate by ---------------------
        # -----------------------------------------------------------------
        if oqparam_dict['aggregate_by'] == [['cod_mnz']]:                   # Si esta agregado por manzanas
            dfmelted_mnz['cod_mnz'] = np.array(mnz_list)[(dfmelted_mnz['agg_id'] / 1).astype(int)]
            
            
        elif oqparam_dict['aggregate_by'] == [['cod_mnz', 'taxonomy']]:     # Si esta agregado por manzana y taxonomia
            txn_index1 = [int(str(x)[-1]) if len(str(x)) == 1 else (int(str(x)[-1]) if int(str(x)[-2]) % 2 == 0 else int('1'+str(x)[-1])) for x in dfmelted_mnz.agg_id]
            dfmelted_mnz['cod_mnz'] = np.array(mnz_list)[(dfmelted_mnz['agg_id'] / len(txn_list)).astype(int)] 
            dfmelted_mnz['taxonomy'] = np.array(txn_list)[txn_index1]
                            
        dfmelted_mnz = dfmelted_mnz.drop(columns=['agg_id'])                # Eliminar la columna agg_id
        dfmelted_mnz = dfmelted_mnz.reset_index(drop=True)                  # Resetear el index
        
        # ------------------ LISTAS A EXPORTAR/ PROCESAR ------------------
        df_AGR_list.append(dfmelted_mnp)                                    # Lista de los dataframes de cada simulacion (Municipio)
        lnPAE85 = np.log(dfmelted_mnp.loc[dfmelted_mnp.stat=='quantile-0.85'].loss).values[0]
        lnPAE15 = np.log(dfmelted_mnp.loc[dfmelted_mnp.stat=='quantile-0.15'].loss).values[0]
        agg_risk.append((lnPAE85-lnPAE15)/2)
        df_AGRmnz_list.append(dfmelted_mnz)                                 # Lista de los dataframes de cada simulacion (Aggregate by)
        agg_risk_mnz.append(dfmelted_mnz.loc[dfmelted_mnz.stat=='mean'].loss) # Lista de las perdidas por simulacion (Aggregate by) 
        
        # 4). Genera el grafico de perdida anual promedio por simulacion del 
        # centro poblado

        datos = {'Num_Sim':Nsim2,'loss':agg_risk}
        datos_events = {'Num_Sim':Nevents,'loss':agg_risk}
        
        return datos,datos_events
#%% ====== Funcion: Loss/EBR ==================================================
def function_EBR(archivo_seleccionado,archivo_seleccionado_tax,carpeta_seleccionada,valorperiodo):
    # 1). Esta sección busca los directorios que hay en la carpeta 
    ruta_hdf5_tax = archivo_seleccionado_tax                                    # Obtiene la ruta del archivo hdf5 agregado por taxonomia
    ruta_hdf5 = archivo_seleccionado                                            # Obtiene la ruta del archivo hdf5 agregado por manzana                                        
    ruta_shp = carpeta_seleccionada                                             # Obtiene el directorio de la carpeta con los archivos shape
    # 2). Obtener archivos hdf5 agregado por manzana
    with h5py.File(ruta_hdf5, 'r') as archivo:
        # Para obtener los parametros ingresados desde Openquake del modelo
        oqparam = archivo["oqparam"][()].decode('utf-8') 
        oqparam_dict_mnz = json.loads(oqparam)                                  # Lista de los parámetros de OpenQuake
        # Para obtener valor expuesto
        exposicion_mnz = archivo["assetcol"]["array"]["value-structural"][()]   # Lista del valor de la pérdida segun agg_id
        # Para obtener datos risk by event
        riskbyevent_aggid = archivo["risk_by_event"]["agg_id"][()]              # Aggregate id
        riskbyevent_eventid = archivo["risk_by_event"]["event_id"][()]          # ID del evento
        riskbyevent_loss = archivo["risk_by_event"]["loss"][()]                 # Perdida
        event_eventid = archivo["events"]["id"][()]                             # ID del evento
        event_rupid = archivo["events"]["rup_id"][()]                           # ID de la ruptura
        event_year = archivo["events"]["year"][()]                              # Year (ventana de tiempo)
        # Para obtener datos aggrisk
        mnz_list_bytes = archivo["assetcol"]["tagcol"]["cod_mnz"][()][1:]       # Lista de manzanas
        mnz_list = [item.decode('utf-8') for item in mnz_list_bytes]
        agg_id_mnz = archivo["aggrisk"]["agg_id"][()]                           # ID del agregado
        loss_mnz = archivo["aggrisk"]["loss"][()]                               # Perdidas segun el aggregate ID
        # Codigo de la manzana segun modelo de exposicion
        cod_mnz_valex = archivo["assetcol"]["array"]["cod_mnz"][()] 
        # Para obtener datos aggcurves
        aggmnz_matrix = archivo["agg_curves-stats"]['structural'][()]
    # 3). Obtener archivos hdf5 agregado por taxonomia
    with h5py.File(ruta_hdf5_tax, 'r') as archivo:
        # Para obtener los parametros ingresados desde Openquake del modelo
        oqparam_dict_txn = json.loads(archivo["oqparam"][()].decode('utf-8'))   # Lista de parametros de OpenQuake
        # Valor expuesto
        exposicion_txn = archivo["assetcol"]["array"]["value-structural"][()] 
        # Para obtener datos aggrisk
        txn_list_bytes  = archivo["assetcol"]["tagcol"]["taxonomy"][()][1:]
        txn_list = [item.decode('utf-8') for item in txn_list_bytes]            # Lista de taxonomias
        agg_id_txn = archivo["aggrisk"]["agg_id"][()]                           # ID del agregado
        loss_txn = archivo["aggrisk"]["loss"][()]                               # Perdidas segun el aggregate ID
        # Codigo de la taxonomia segun modelo de exposicion
        txn_valex = archivo["assetcol"]["array"]["taxonomy"][()]                # Codigo de la taxonomia segun exposicion
    # 4). Obtener archivos shape del municipio
    # Cargar los archivos .shp
    mnz_shp,area_shp,scc_shp = [],[],[]
    for archivo in os.listdir(ruta_shp): 
        # Archivos MGN_Manzana:
        # Archivo .shp:
        if "MANZANA" in archivo and archivo.endswith(".shp"):
            mnz_shp.append(os.path.join(ruta_shp, archivo))
        if "AREA" in archivo and archivo.endswith(".shp"):
            area_shp.append(os.path.join(ruta_shp, archivo))
        if "SECCION" in archivo and archivo.endswith(".shp"):
            scc_shp.append(os.path.join(ruta_shp, archivo))
    
    manzana_shp = gpd.read_file(mnz_shp[0])
    area_shpe = gpd.read_file(area_shp[0])
    seccion_shp = gpd.read_file(scc_shp[0])
    
    COD_mun = manzana_shp['COD_MPIO'][0]
    # 5). Se obtienen los datos de entrada y se configuran los condicionales
    # ------- Valor expuesto --------------------------------------------------
    valexpuesto = np.sum(exposicion_mnz)/1e6                                    # Valor expuesto en billones de pesos            
    # ------- Nombre del municipio --------------------------------------------
    CP_Name = oqparam_dict_mnz['description'].split('-')[-1].strip()            # Nombre del centro poblado inicial
    if CP_Name[0].islower():
        CP_Name = CP_Name[0].upper() + CP_Name[1:]                              # Si el nombre del centro poblado no comienza con una mayuscula
    """
    ---------------------------------------------------------------------------
                                 Curva de excedencia
    ---------------------------------------------------------------------------
    """
    # Dataframe de ID_rupturas segun ID_evento
    dc1_EBR = {'event_id':event_eventid,'rup_id':event_rupid,'year':event_year} # Diccionario ruptura del evento
    df1_EBR = pd.DataFrame(dc1_EBR)                                             # Dataframe ruptura del evento
    # Dataframe de perdidas segun ID_evento
    index_addid = np.where(riskbyevent_aggid==oqparam_dict_mnz['K'])[0]         # Index de los resultados que hay que procesar
    event_id, loss, agg_id = [], [], []
    for index in index_addid:
        event_id.append(riskbyevent_eventid[index])
        loss.append(riskbyevent_loss[index])
        agg_id.append(riskbyevent_aggid[index])
    dc2_EBR = {'event_id':event_id,'loss':loss,'agg_id':agg_id}                 # Diccionario perdidas por evento
    df_EBR = pd.DataFrame(dc2_EBR)                                              # Dataframe perdidas por evento
    df_EBR = df_EBR.sort_values(by='event_id', ascending=True)                  # Organiza ID del elemento de menor a mayor
    df_EBR = df_EBR.merge(df1_EBR, on='event_id', how='left')                   # agrega columnas del DataFrame 1 que coincidan con el ID del evento
    # Dataframe risk-by-event
    df_EBR.rename(columns={'agg_id': 'loss_type'}, inplace=True)                # add_id por loss_type
    df_EBR['loss_type'] = df_EBR['loss_type'].replace({oqparam_dict_mnz['K']: 'structural'}) # Loss_type es structural
    df_EBR = df_EBR.reset_index(drop=True)                                      # Reset el index del dataframe
    # Agregar tasa anual de excedencia al dataframe
    df_EBR.sort_values(by='loss',ascending=True,inplace=True)                   # Valores de menor a mayor
    tasa_list = np.zeros(len(df_EBR))
    tasa_list[0] = 1
    for i in range(1,len(df_EBR)):
        tasa_list[i] = tasa_list[i-1]-1/len(df_EBR)
    df_EBR['perdidaTA'] = tasa_list
    """
    ---------------------------------------------------------------------------
                              Tabla de resumen PAE
    ---------------------------------------------------------------------------
    """
    index_addid = np.where(agg_id_mnz==oqparam_dict_mnz['K'])[0]                 # Indices de el aggid a utilizar
    agg_id, loss = [], []
    for index in index_addid:
        agg_id.append(agg_id_mnz[index])
        loss.append(loss_mnz[index])
    dc1_AGR = {'agg_id':agg_id,'loss':loss}   
    df1_AGR = pd.DataFrame(dc1_AGR) 
    aggsts_loss = [np.mean(df1_AGR.loss)]
    # Obtener el valor de perdida anual promedio de la simulacion
    for stats in oqparam_dict_mnz['quantiles']:
        aggsts_loss.append(np.quantile(df1_AGR.loss,stats))
    # Lista de estadisticas
    list_stats = ['mean']
    for quant in oqparam_dict_mnz['quantiles']:
        list_stats.append('quantile-'+str(quant))
    # Generar datos para el dataframe PAE
    aggcrv_loss,aggcrv_rtn,aggcrv_sts = [],[],[]
    for indT, per in enumerate(oqparam_dict_mnz['return_periods']):
        for indST, sts in enumerate(list_stats):
            aggcrv_loss.append(aggmnz_matrix[:,indST,:][:,indT][-1])
            aggcrv_rtn.append(per)
            aggcrv_sts.append(sts)    
    dc_AGcrv = {'return_period':aggcrv_rtn,'loss_type':[oqparam_dict_mnz['all_cost_types'][0]]*len(aggcrv_rtn),
                'loss':aggcrv_loss,'stat':aggcrv_sts}
    df_AGcrv = pd.DataFrame(dc_AGcrv)
    PE_mill = df_AGcrv[df_AGcrv['stat'] == 'mean']['loss'].tolist()
    dic = {'Col1':['Valor_expuesto[B$]','Perdida_anual_estimada[M$]','Perdida_anual_estimada[%.]']
                     , 'Col2':[valexpuesto,aggsts_loss[0],(aggsts_loss[0]/(valexpuesto*1e6))*1000]}
    df_resultados = pd.DataFrame(dic)
    Pr50_Val = []
    per = [31,225,475,975,1475]
    for pr in per:
        Pr50_Val.append((1-np.exp(-50/pr))*100)
    """
    ---------------------------------------------------------------------------
                       PAE agregada por tipologia constructiva
    ---------------------------------------------------------------------------
    """
    df_group = pd.DataFrame({'agg_id':agg_id_txn, 'loss':loss_txn})             # Dataframe perdidas por aggid
    grp_aggid = df_group.groupby('agg_id')['loss']                              # Agrupa las perdidas por aggid
    stats_agg = grp_aggid.describe(percentiles=oqparam_dict_txn['quantiles'])   # Calcula mediana y percentiles de las perdidas por aggid
    stats_agg.reset_index(level=0, inplace=True)                                # Genera un indice, agg_id se vuelve en columna
    stats_agg_mnp = stats_agg[stats_agg['agg_id'] == oqparam_dict_txn['K']]     # Genera un dataframe para municipio
    stats_agg.drop(stats_agg_mnp.index, inplace=True)                           # Dataframe de perdidas por manzana o por manzana + taxonomia
    stats_agg_mnp.reset_index(level=0, inplace=True)                            # Resetea el indice municipio
    stats_agg.reset_index(level=0, inplace=True)                                # Resetea el indice agregado
    dfmelted_mnp = stats_agg_mnp.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
    dfmelted_txn = stats_agg.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
    dfmelted_txn.sort_values(by='agg_id', inplace=True)
    dfmelted_txn['stat'] = dfmelted_txn['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
    dfmelted_mnp['stat'] = dfmelted_mnp['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
    dfmelted_mnp = dfmelted_mnp.drop(columns=['agg_id'])
    dfmelted_txn['taxonomy'] = np.array(txn_list)[(dfmelted_txn['agg_id'] / 1).astype(int)]
    dfmelted_txn = dfmelted_txn.drop(columns=['agg_id'])
    dfmelted_txn = dfmelted_txn.reset_index(drop=True)
    aggrisk_txn = dfmelted_txn.loc[dfmelted_txn.stat=='mean'].loss.tolist()
    taxonomias = dfmelted_txn.loc[dfmelted_txn.stat=='mean'].taxonomy.tolist()
    taxo_def = []
    for txn in taxonomias:
        parte = txn.split('/')
        taxo_def.append(parte[0]+'/'+parte[1]+'/'+parte[2])
    df_losses = pd.DataFrame({'loss':aggrisk_txn,'taxonomy':taxo_def})
    df_lossesgrup = df_losses.groupby('taxonomy')['loss'].sum().reset_index()
    df_valex = pd.DataFrame({'valex':exposicion_txn,'index':txn_valex})
    df_codtxn = pd.DataFrame({'taxonomy':taxo_def,'index':range(1,len(taxonomias)+1)})
    df_prom = pd.merge(df_valex, df_codtxn, on='index', how='left') 
    grouped_df = df_prom.groupby('taxonomy')['valex'].sum().reset_index()
    df_expotax = pd.merge(df_lossesgrup, grouped_df, on='taxonomy', how='left') 
    df_expotax['loss2'] = (df_expotax.loss/df_expotax.valex)*1000
    taxo_description = descriptiontaxo(df_expotax.taxonomy)
    """
    ---------------------------------------------------------------------------
                              Represetacion espacial
    ---------------------------------------------------------------------------
    """
    df_group_mnz = pd.DataFrame({'agg_id':agg_id_mnz, 'loss':loss_mnz})         # Dataframe perdidas por aggid
    grp_aggid_mnz = df_group_mnz.groupby('agg_id')['loss']  # agrupa las perdidas por aggid
    stats_agg_mnz = grp_aggid_mnz.describe(percentiles=oqparam_dict_mnz['quantiles']) # calcula mediana y percentiles de las perdidas por aggid
    stats_agg_mnz.reset_index(level=0, inplace=True) # genera un indice, agg_id se vuelve en columna
    stats_agg_mnp = stats_agg_mnz[stats_agg_mnz['agg_id'] == oqparam_dict_mnz['K']] # genera un dataframe para municipio
    stats_agg_mnz.drop(stats_agg_mnp.index, inplace=True) # dataframe de perdidas por manzana o por manzana + taxonomia
    stats_agg_mnp.reset_index(level=0, inplace=True) # resetea el indice municipio
    stats_agg_mnz.reset_index(level=0, inplace=True) # resetea el indice agregado

    dfmelted_mnp = stats_agg_mnp.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
    dfmelted_mnz = stats_agg_mnz.melt(id_vars=['agg_id'], value_vars=['mean', '15%', '50%', '85%'], var_name='stat', value_name='loss')
    dfmelted_mnz.sort_values(by='agg_id', inplace=True)
    dfmelted_mnz['stat'] = dfmelted_mnz['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
    dfmelted_mnp['stat'] = dfmelted_mnp['stat'].replace({'15%': 'quantile-0.15', '85%': 'quantile-0.85', '50%': 'quantile-0.5'})
    dfmelted_mnp = dfmelted_mnp.drop(columns=['agg_id'])
    dfmelted_mnz['cod_mnz'] = np.array(mnz_list)[(dfmelted_mnz['agg_id'] / 1).astype(int)]
    dfmelted_mnz = dfmelted_mnz.drop(columns=['agg_id'])
    dfmelted_mnz = dfmelted_mnz.reset_index(drop=True)
    
    aggrisk_mnz = dfmelted_mnz.loc[dfmelted_mnz.stat=='mean'].loss.tolist()
    manzanas_mnz = dfmelted_mnz.loc[dfmelted_mnz.stat=='mean'].cod_mnz.tolist()
    
    cod_mnzdef = []
    for mnz in manzanas_mnz:
        cod_mnzdef.append(str(mnz[1:]))
    df_losses_mnz = pd.DataFrame({'loss':aggrisk_mnz,'cod_mnz':cod_mnzdef})

    df_valex = pd.DataFrame({'valex':exposicion_mnz,'index':cod_mnz_valex})
    df_codmnz = pd.DataFrame({'cod_mnz':cod_mnzdef,'index':range(1,len(cod_mnzdef)+1)})
    df_prom = pd.merge(df_valex, df_codmnz, on='index', how='left') 
    grouped_df = df_prom.groupby('cod_mnz')['valex'].sum().reset_index()
    
    df_losses_prc = pd.merge(df_losses_mnz, grouped_df, on='cod_mnz', how='left') 
    df_losses_prc['loss2'] = (df_losses_prc.loss/df_losses_prc.valex)*1000
    # Mezclar modelo de exposicion con el shape file de las manzanas
    map_data = manzana_shp.merge(df_losses_prc, left_on='COD_DANE', right_on='cod_mnz', how='left')
    map_data2 = df_losses_mnz.merge(manzana_shp, left_on='cod_mnz', right_on='COD_DANE', how='left')
    map_data2.to_csv(os.path.join(ruta_shp,"Exposicion.csv"),index=False)
    
    return df_EBR, valexpuesto,aggsts_loss,PE_mill,df_resultados,Pr50_Val,CP_Name,df_expotax,taxo_description,map_data,seccion_shp,area_shpe,COD_mun,ruta_shp
#%% Descripcion de la taxonomia
def descriptiontaxo(taxonomy_list):
    taxo_description = []
    for txn in taxonomy_list:
        parte = txn.split('/')
        if parte[0] == 'VG':
            if parte[1] == 'CE':
                if parte[2] == 'DU':
                    taxo_description.append('Cerchas de material vegetal (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Cerchas de material vegetal (no ingenieril)')
                else:
                    taxo_description.append('Cerchas de material vegetal (NI)')
        elif parte[0] == 'AC':
            if parte[1] == 'CE':
                if parte[2] == 'DU':
                    taxo_description.append('Cerchas de acero (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Cerchas de acero (no ingenieril)')
                else:
                    taxo_description.append('Cerchas de acero (NI)')
            if parte[1] == 'MD':
                if parte[2] == 'DU':
                    taxo_description.append('Muros delgados en acero (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Muros delgados en acero (no ingenieril)')
                else:
                    taxo_description.append('Muros delgados en acero(NI)')
            elif parte[1] == 'PRM':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos resistentes a momento de acero (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos resistentes a momento de acero (no ingenieril)')
                else:
                    taxo_description.append('Pórticos resistentes a momento de acero (NI)')
            elif parte[1] == 'PA':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos arriostrados de acero (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos arriostrados de acero (no ingenieril)')
                else:
                    taxo_description.append('Pórticos arriostrados de acero (NI)')
            elif parte[1] == 'PI':
                if parte[2] == 'DU':
                    taxo_description.append('Péndulo invertido de acero (ingenieril)')
                else:
                    taxo_description.append('Péndulo invertido de acero (no ingenieril)')
        elif parte[0] == 'AD':
            taxo_description.append('Adobe no-reforzado')
        elif parte[0] == 'BQ':
            taxo_description.append('Bahareque no-reforzado')
        elif parte[0] == 'MZ':
            if parte[1] == 'OT':
                taxo_description.append('Madera-zinc')
            else:
                taxo_description.append('Madera-zinc no-reforzada')
        elif parte[0] == 'MX':
            taxo_description.append('Mixto (No ingenieril)')
        elif parte[0] == 'CR':
            if parte[1] == 'MR':
                if parte[2] == 'DU':
                    taxo_description.append('Muros de concreto reforzado (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Muros de concreto reforzado (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Muros de concreto reforzado (NI)')
            elif parte[1] == 'MD':
                if parte[2] == 'DU':
                    taxo_description.append('Muros delgados de concreto reforzado (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Muros delgados de concreto reforzado (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Muros delgados de concreto reforzado (NI)')
            elif parte[1] == 'PRM':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos resistentes a momento de concreto reforzado (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos resistentes a momento de concreto reforzado (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Pórticos resistentes a momento de concreto reforzado (NI)')
            elif parte[1] == 'PRMM':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos resistentes a momento de concreto reforzado con relleno en mampostería (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos resistentes a momento de concreto reforzado con relleno en mampostería (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Pórticos resistentes a momento de concreto reforzado con relleno en mampostería (NI)')
            elif parte[1] == 'PA':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos arriostrados de concreto reforzado (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos arriostrados de concreto reforzado (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Pórticos arriostrados de concreto reforzado (NI)')
            elif parte[1] == 'LC':
                taxo_description.append('Losa-Columna de concreto reforzado (ingenieril)')
            elif parte[1] == 'SC':
                if parte[2] == 'DU':
                    taxo_description.append('Sistema combinado (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Sistema combinado (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Sistema combinado (NI)')
        elif parte[0] == 'MA':
            if parte[1] == 'MR':
                if parte[2] == 'DU':
                    taxo_description.append('Muros de mampostería reforzada (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Muros de mampostería reforzada (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Muros de mampostería reforzada (NI)')
            elif parte[1] == 'PRM':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos resistentes a momento de mampostería reforzada (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos resistentes a momento de mampostería reforzada (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Pórticos resistentes a momento de mampostería reforzada (NI)')
            elif parte[1] == 'MNR':
                taxo_description.append('Mampostería no-reforzada')
            elif parte[1] == 'MPC':
                taxo_description.append('Mampostería parcialmente confinada')
            elif parte[1] == 'MC':
                if parte[2] == 'DU':
                    taxo_description.append('Mampostería confinada (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Mampostería confinada (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Mampostería confinada (NI)')
        elif parte[0] == 'MC':
            if parte[1] == 'MR':
                if parte[2] == 'DU':
                    taxo_description.append('Muros de mampostería en bloque de concreto reforzada (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Muros de mampostería en bloque de concreto reforzada (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Muros de mampostería en bloque de concreto reforzada (NI)')
            elif parte[1] == 'PRM':
                if parte[2] == 'DU':
                    taxo_description.append('Pórticos resistentes a momento de mampostería en bloque de concreto reforzada (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Pórticos resistentes a momento de mampostería en bloque de concreto reforzada (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Pórticos resistentes a momento de mampostería en bloque de concreto reforzada (NI)')
            elif parte[1] == 'MNR':
                taxo_description.append('Mampostería en bloque de concreto no-reforzada')
            elif parte[1] == 'MPC':
                taxo_description.append('Mampostería en bloque de concreto parcialmente confinada')
            elif parte[1] == 'MC':
                if parte[2] == 'DU':
                    taxo_description.append('Mampostería en bloque de concreto confinada (ingenieril)')
                elif parte[2] == 'ND':
                    taxo_description.append('Mampostería en bloque de concreto confinada (no ingenieril)')
                elif parte[2] == 'NI':
                    taxo_description.append('Mampostería en bloque de concreto confinada (NI)')
        elif parte[0]=='MD':
            taxo_description.append('Madera no-reforzada')
        elif parte[0] == 'PMC':
            taxo_description.append('Prefabricado (madera-concreto) no-reforzado')
        elif parte[0] == 'TA':
            taxo_description.append('Tapia pisada no-reforzada')
        elif parte[0] == 'MP':
            taxo_description.append('Mampostería de piedra no-reforzada')
    return taxo_description
