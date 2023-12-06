# -----------------------------------------------------------------------------
# ------------------------------ LIBRERIA RIESGO ------------------------------
# -----------------------------------------------------------------------------
"""
-------------------------------------------------------------------------------
Este script contiene las funciones que permiten procesar los resultados de 
riesgo
---------------------------- Autor: Daniela Novoa -----------------------------
"""
#%% ====== Importar librerias =================================================
""" 
-------------------------------------------------------------------------------
*** Ubicar secciones para guardar las librerias
-------------------------------------------------------------------------------
"""
# -------- Librerias Interfaz>> Tkinter ---------------------------------------
import tkinter as tk
# -------- Librerias Graficos Interfaz>> Tkinter ------------------------------
from PIL import Image, ImageTk
# -------- Librerias Directorios ----------------------------------------------
import os
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
#%% ====== Image ==============================================================
def Label_Image(image_name, lw, lh, container,bg_color,rx,ry):
    image = Image.open(os.path.join(os.getcwd(),"icon") + image_name)
    image = image.resize((lw, lh), Image.LANCZOS)
    image = ImageTk.PhotoImage(image)
    label = tk.Label(container, image=image, bd=0, bg=bg_color)
    label.image = image
    label.place(relx=rx, rely=ry, anchor=tk.CENTER)
    return label
#%% ====== Rectangle with rounded corners =====================================
def rec_redond(canvas, x1, y1, x2, y2, radio_esquinas, color):
    canvas.create_rectangle(x1 + radio_esquinas, y1, x2 - (radio_esquinas), y2 - radio_esquinas, fill=color, outline=color, width=0)
    canvas.create_rectangle(x1 + radio_esquinas, y1, x2 - (radio_esquinas), y2+1, fill=color, outline=color, width=0)
    canvas.create_rectangle(x1, y1 + radio_esquinas, x2+20, y2 - radio_esquinas, fill=color, outline=color, width=0)
    canvas.create_arc(x1, y1, x1 + 2 * radio_esquinas, y1 + 2 * radio_esquinas, start=90, extent=90, fill=color, outline=color)
    canvas.create_arc(x2 - 2 * radio_esquinas, y1, x2, y1 + 2 * radio_esquinas, start=0, extent=90, fill=color, outline=color)
    canvas.create_arc(x1, y2 - 2 * radio_esquinas, x1 + 2 * radio_esquinas, y2, start=180, extent=90, fill=color, outline=color)
    canvas.create_arc(x2 - 2 * radio_esquinas, y2 - 2 * radio_esquinas, x2, y2, start=270, extent=90, fill=color, outline=color)
#%% ====== Button -- Image ====================================================
def Button_Image(image_name, lw, lh, container,bg_color,rx,ry,command_function):
    imagen = Image.open(os.path.join(os.getcwd(),"icon") + image_name)
    imagen = imagen.resize((lw,lh), Image.LANCZOS)
    imagen = ImageTk.PhotoImage(imagen)
    button = tk.Button(container, image=imagen, bd=0, bg=bg_color, command=command_function)
    button.image = imagen
    button.place(relx=rx, rely=ry, anchor=tk.CENTER)
    return button
#%% ====== Expand -- Loss estimations =========================================
"""
-------------------------------------------------------------------------------
Expand functions 
-------------------------------------------------------------------------------
"""
def Elements_ExpLoss(Und_Tabs,Exp_Tabs,Var_Exp, Rec_Select, navbar_container,Tabs_titles,bg_color,fg_color,command_function,rx,ry,rxhd,ryhd,HideExpand_Loss):
    # Und_Tabs = Tabs under "Loss estimations" *List*
    # Exp_Tabs = Loss Estimatios Tabs *List*
    # Var_Exp = "Expand Loss" Variable
    # Rec_Select = Rectangle variable -- when the tab is selected
    # navbar_container = Navigation bar frame
    # Tabs_titles = Titles of each Tab *List*
    # bg_color = Background color
    # fg_color = Font color
    # command_function = Tab Function
    # -------------------------------------------------------------------------
    # When "Expand Loss" is selected, the tabs under "Loss estimatios" are deleted 
    if Und_Tabs == '':
        print('')
    else:
        for tabs in Und_Tabs:
            if tabs is not None:
                tabs.place_forget()
                tabs = None    
    # -------------------------------------------------------------------------
    # When the elements in "Expand Loss" are not None >> Run "Hide Expand Loss"
    if Exp_Tabs[0] is not None:
        Elements_HdEpLoss()
        # ---------------------------------------------------------------------
        # If "Expand Loss" exist then "Expand Loss" menu is deleted
        for index, tabs in enumerate(Exp_Tabs):
            if tabs is not None:
                tabs.place_forget()
                tabs = None
        # ---------------------------------------------------------------------   
        # "Expand Loss" menu is created
            if tabs is None:
                tabs = tk.Button(navbar_container, text=Tabs_titles[index], font=("Abadi MT", 13), 
                                         bd=0, bg=bg_color, fg=fg_color, relief=tk.FLAT, command=command_function[index], padx=20)
                tabs.place(relx=rx[index], rely=ry[index], anchor=tk.CENTER)
    else:
        # ---------------------------------------------------------------------
        # If "Expand Loss" exist then "Expand Loss" menu is deleted
        Exp_Tabs2 = []
        for index, tabs in enumerate(Exp_Tabs):
            if tabs is not None:
                tabs.place_forget()
                tabs = None
        # ---------------------------------------------------------------------   
        # "Expand Loss" menu is created
            if tabs is None:
                tabs = tk.Button(navbar_container, text=Tabs_titles[index], font=("Abadi MT", 13), 
                                         bd=0, bg=bg_color, fg=fg_color, relief=tk.FLAT, command=command_function[index], padx=20)
                tabs.place(relx=rx[index], rely=ry[index], anchor=tk.CENTER)
            Exp_Tabs2.append(tabs)
    # # -------------------------------------------------------------------------
    # Once the user select "Expand Loss" button, the button "Hide Expand Loss" 
    # should appear
    if Var_Exp is not None:
        Var_Exp.place_forget()
        Var_Exp = None
    # -------------------------------------------------------------------------
    if Rec_Select is not None:
        if Var_Exp is None:
            Var_Exp = Button_Image('/mtlSelect.png', 9, 7, navbar_container, "white",rxhd,ryhd,HideExpand_Loss)
    else:
        if Var_Exp is None:
            Var_Exp = Button_Image('/mtl.png', 9, 7, navbar_container, "#37586B",rxhd,ryhd,HideExpand_Loss)
    return Exp_Tabs2

#%% ====== Hide Expand -- Loss estimations =========================================
"""
-------------------------------------------------------------------------------
Hide Expand functions 
-------------------------------------------------------------------------------
"""
def Elements_HdEpLoss(Exp_Tabs,Var_Exp,Rec_Select,navigation_bar,Expand_Loss,rxhd,ryhd):
    #--------------------------------------------------------------------------
    # "Expand Loss" button is deleted
    if Var_Exp is not None:
        Var_Exp.place_forget()
        Var_Exp = None
    # -------------------------------------------------------------------------
    # "Expand Loss" menu is deleted
    for tabs in Exp_Tabs:
        if tabs is not None:
            tabs.place_forget()
            tabs = None
    # -------------------------------------------------------------------------
    if Rec_Select is not None:
        if Var_Exp is None:
            Var_Exp = Button_Image('/desgloSelect.png', 9, 7, navigation_bar, "white",rxhd,ryhd,Expand_Loss)  
    else:
        if Var_Exp is None:
            Var_Exp = Button_Image('/desglo.png', 9, 7, navigation_bar, "#37586B",rxhd,ryhd,Expand_Loss)
