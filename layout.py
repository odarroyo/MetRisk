# -----------------------------------------------------------------------------
# ---------------- GRAPHICAL INTERFACE TO PROCESS RISK RESULTS ----------------
# -----------------------------------------------------------------------------
"""
-------------------------------------------------------------------------------
---------------------------- Author: Daniela Novoa ----------------------------
-------------------------------------------------------------------------------
"""
#%% ====== Import libraries ===================================================
# -------- Tkinter Library ----------------------------------------------------
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk
# -------- Graphics TKinter Library -------------------------------------------
from PIL import Image, ImageTk
import matplotlib.ticker as ticker
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# -------- Directory Library --------------------------------------------------
import os
# -------- Data processing libraries ------------------------------------------
import pandas as pd
import numpy as np
# -------- Libraries to generate summary tables -------------------------------
from openpyxl import Workbook
from openpyxl.styles import Alignment, Border, Side
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
# -------- Own libraries ------------------------------------------------------
import Libreria as lb
import win_functions as fun
import Lib_pross as prs
#%% ====== WINDOW COLORS ======================================================
cnt_color = "#FFFFFF"
upcnt_color = "#274151"
navbar_color = "#37586B"
#%% ====== FUNCTIONS ==========================================================
boton_DLS = ["btn_clb_DLS","btn_dsp_DLS", "btn_ebr_DLS",
             "btn_mtl_DLS"]
DLS_boton = {}
for btn in boton_DLS:
    DLS_boton[btn] = None
Exp_Tabs_Gen = None
def Expand_Loss():
    print('------------------------------------------')
    print('-------------- Expand Loss ---------------')
    print('------------------------------------------')
    Und_Tabs = ''
    Exp_Tabs = [DLS_boton["btn_clb_DLS"],DLS_boton["btn_dsp_DLS"],DLS_boton["btn_ebr_DLS"]]
    Var_Exp = LSS_boton["btn_dsg_LSS"]
    Rec_Select = LSS_rectg["rec_slc_LSS"]
    Tabs_titles = ["Calibration","Dispersion","Event Based Risk"]
    command_function = [Show_Loss_CLB,Show_Loss_DSP,Show_Loss_EBR]
    rx = [0.497, 0.497, 0.585]
    ry = [0.26, 0.33, 0.40]
    global Exp_Tabs_Gen
    Exp_Tabs_Gen = fun.Elements_ExpLoss(Und_Tabs,Exp_Tabs,Var_Exp, Rec_Select, navigation_bar,Tabs_titles,navbar_color,cnt_color,command_function,rx,ry,0.87,0.19,HideExpand_Loss)

def HideExpand_Loss():
    print('------------------------------------------')
    print('------------ Hide Expand Loss ------------')
    print('------------------------------------------')
    Var_Exp = LSS_boton["btn_dsg_LSS"]
    Rec_Select = LSS_rectg["rec_slc_LSS"]
    fun.Elements_HdEpLoss(Exp_Tabs_Gen,Var_Exp,Rec_Select,navigation_bar,Expand_Loss,0.87,0.19)
    
def Show_Loss_CLB():
    print('------------------------------------------')
    print('----------- Loss > Calibration -----------')
    print('------------------------------------------')
    Elements_Loss_CLB()

def Show_Loss_DSP():
    print('------------------------------------------')
    print('----------- Loss > Dispersion ------------')
    print('------------------------------------------')
    Elements_Loss_DSP()
def Show_Loss_EBR():
    print('------------------------------------------')
    print('-------- Loss > Event Based Risk ---------')
    print('------------------------------------------')
    Elements_Loss_EBR()
#%% ====== TAB >> HOME ========================================================
"""
-------------------------------------------------------------------------------
Define Home Variables
-------------------------------------------------------------------------------
"""
# -------- Label Variables ----------------------------------------------------
label_HME = ["lbl_log_HME"]
HME_label = {}
for lbl in label_HME:
    HME_label[lbl] = None
# -------- Text Variables -----------------------------------------------------
text_HME = ["txt_cnt_HME1","txt_cnt_HME2","txt_cnt_HME3",
            "txt_gid_HME1","txt_gid_HME2","txt_gid_HME3"]
HME_text = {}
for txt in text_HME:
    HME_text[txt] = None
# -------- Rectangle Variables ------------------------------------------------
rectg_HME = ["rec_gid_HME"]
HME_rectg = {}
for rec in rectg_HME:
    HME_rectg[rec] = None
"""
-------------------------------------------------------------------------------
Functions for displaying content in other tabs
-------------------------------------------------------------------------------
"""
def Show_Home():
    print('------------------------------------------')
    print('------------------ HOME ------------------')
    print('------------------------------------------')
    Elements_Home()
def Elements_Home():   
    # -------------------------------------------------------------------------
    """
                     The elements of the other tabs are hidden
    """
    Hide_Loss()
    Hide_Loss_CLB()
    Hide_Loss_DSP()
    Hide_Loss_EBR()
    # -------------------------------------------------------------------------
    """
                                  HOME Tab Elements
    """
    
    # ---- Interface logo:
    if HME_label["lbl_log_HME"] is None:
        HME_label["lbl_log_HME"] = fun.Label_Image('/Metrisk_Home.png', 750, 180, cnt_container,cnt_color,0.495,0.3)
    # ---- Content Text:
    if HME_text["txt_cnt_HME1"] is None:
        HME_text["txt_cnt_HME1"] = tk.Label(cnt_container, text="METRISK  empowers  you  to  measure  and  analyze ", 
                         font=("Abadi MT", 25), bg="white", fg="#274151")
        HME_text["txt_cnt_HME1"].place(relx=0.496, rely=0.53, anchor=tk.CENTER) 
    if HME_text["txt_cnt_HME2"] is None:
        HME_text["txt_cnt_HME2"] = tk.Label(cnt_container, text="risks  through  comprehensive  metrics,  helping  you ", 
                         font=("Abadi MT", 25), bg="white", fg="#274151")
        HME_text["txt_cnt_HME2"].place(relx=0.498, rely=0.59, anchor=tk.CENTER)
    if HME_text["txt_cnt_HME3"] is None:
        HME_text["txt_cnt_HME3"] = tk.Label(cnt_container, text="make informed decisions and shape better outcomes. ", 
                         font=("Abadi MT", 25), bg="white", fg="#274151")
        HME_text["txt_cnt_HME3"].place(relx=0.5, rely=0.65, anchor=tk.CENTER)
    # ---- Guide Text:
    if HME_text["txt_gid_HME1"] is None:
        HME_text["txt_gid_HME1"] = tk.Label(cnt_container, text="Download our user's guide,", 
                         font=("Abadi MT", 22), bg="white", fg="#C07960")
        HME_text["txt_gid_HME1"].place(relx=0.333, rely=0.76, anchor=tk.CENTER)
    if HME_text["txt_gid_HME2"] is None:
        HME_text["txt_gid_HME2"] = tk.Label(cnt_container, text="and start using METRISK ", 
                         font=("Abadi MT", 22), bg="white", fg="#C07960")
        HME_text["txt_gid_HME2"].place(relx=0.322, rely=0.81, anchor=tk.CENTER)
    if HME_rectg["rec_gid_HME"] is None:
        HME_rectg["rec_gid_HME"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        HME_rectg["rec_gid_HME"].place(relx=0.67, rely=0.78, anchor=tk.CENTER, width=281, height=61)
        x2, y2 = 280, 60
        x1, y1 = 10,10
        radio_esquinas = 5
        color = "#C07960"
        fun.rec_redond(HME_rectg["rec_gid_HME"], x1, y1, x2, y2, radio_esquinas, color)
    if HME_text["txt_gid_HME3"] is None:
        HME_text["txt_gid_HME3"] = tk.Label(HME_rectg["rec_gid_HME"], text="QUICK USER GUIDE", 
                         font=("Abadi MT", 17), bg="#C07960", fg="white")
        HME_text["txt_gid_HME3"].place(relx=0.51, rely=0.57, anchor=tk.CENTER)
"""
-------------------------------------------------------------------------------
Functions to hide content in other tabs
-------------------------------------------------------------------------------
"""
def Hide_Home():
    # ---- Label Variables ----------------------------------------------------
    for lbl in label_HME:
        if HME_label[lbl] is not None:
            HME_label[lbl].place_forget()
            HME_label[lbl] = None
    # ---- Text Variables -----------------------------------------------------
    for txt in text_HME:
        if HME_text[txt] is not None:
            HME_text[txt].place_forget()
            HME_text[txt] = None
    # ---- Rectangle Variables ------------------------------------------------
    for rec in rectg_HME:
        if HME_rectg[rec] is not None: 
            HME_rectg[rec].place_forget()
            HME_rectg[rec] = None
#%% ====== TAB >> LOSS ESTIMATIONS ============================================
"""
-------------------------------------------------------------------------------
Define LOSS ESTIMATIONS Variables
-------------------------------------------------------------------------------
"""
# -------- Button Variables ---------------------------------------------------
boton_LSS = ["btn_slc_LSS","btn_dsg_LSS",
             "btn_sclb_LSS","btn_sebr_LSS","btn_sdsp_LSS"]
LSS_boton = {}
for btn in boton_LSS:
    LSS_boton[btn] = None
# -------- Title Variables ----------------------------------------------------
title_LSS = ["tlt_tlt_LSS","tlt_clb_LSS", "tlt_ebr_LSS", "tlt_dsp_LSS"]
LSS_title = {}
for tlt in title_LSS:
    LSS_title[tlt] = None
# -------- Text Variables -----------------------------------------------------
text_LSS = ["txt_tlt_LSS1","txt_tlt_LSS2","txt_tlt_LSS3",
            "txt_clb_LSS1","txt_clb_LSS2","txt_ebr_LSS1","txt_ebr_LSS2","txt_ebr_LSS3","txt_dsp_LSS"]
LSS_text = {}
for txt in text_LSS:
    LSS_text[txt] = None
# -------- Rectangle Variables ------------------------------------------------
rectg_LSS = ["rec_slc_LSS","rec_clb_LSS","rec_dsp_LSS","rec_ebr_LSS",
             "rec_sclb_LSS","rec_sebr_LSS","rec_sdsp_LSS"]
LSS_rectg = {}
for rec in rectg_LSS:
    LSS_rectg[rec] = None
# -------- Label Variables ---------------------------------------------------- 
label_LSS = ["lbl_slc_LSS","lbl_bkg_LSS"]
LSS_label = {}
for lbl in label_LSS:
    LSS_label[lbl] = None
"""
-------------------------------------------------------------------------------
Functions for displaying content in other tabs
-------------------------------------------------------------------------------
"""
def Show_Loss():
    print('------------------------------------------')
    print('--------- Se seleccionó Pérdidas ---------')
    print('------------------------------------------')
    Elements_Loss()
    
def Elements_Loss():
    # -------------------------------------------------------------------------
    """
                     The elements of the other tabs are hidden
    """
    Hide_Home()
    Hide_Loss_CLB()
    Hide_Loss_DSP()
    Hide_Loss_EBR()
    # -------------------------------------------------------------------------
    """
                                  LOSS Tab Elements
    """
    # ---- Select Loss: -------------------------------------------------------
    # When "Loss Estimations" is selected, the color of the title, icon and 
    # "expands" changes.
    # 1). Delete Loss button >>
    if LSS_boton["btn_slc_LSS"] is not None:
        LSS_boton["btn_slc_LSS"].place_forget()
        LSS_boton["btn_slc_LSS"] = None
    if LSS_label["lbl_slc_LSS"] is not None:
        LSS_label["lbl_slc_LSS"].place_forget()
        LSS_label["lbl_slc_LSS"] = None
    if LSS_boton["btn_dsg_LSS"] is not None:
        LSS_boton["btn_dsg_LSS"].place_forget()
        LSS_boton["btn_dsg_LSS"] = None
    # 2). When "Loss estimations" is selected >>
    if LSS_rectg["rec_slc_LSS"] is None:
        LSS_rectg["rec_slc_LSS"] = tk.Canvas(navigation_bar, bg="#37586B", bd=0, highlightthickness=0)
        LSS_rectg["rec_slc_LSS"].place(relx=0.57, rely=0.18, anchor=tk.CENTER, width=261, height=61)
        x2, y2 = 260, 60
        x1, y1 = 10,10
        radio_esquinas = 20
        color = "white"
        fun.rec_redond(LSS_rectg["rec_slc_LSS"], x1, y1, x2, y2, radio_esquinas, color)
    if LSS_boton["btn_slc_LSS"] is None:
        LSS_boton["btn_slc_LSS"] = tk.Button(navigation_bar, text="Loss estimations", font=("Abadi MT", 13), 
                                      bd=0, bg="white", fg="#37586B", relief=tk.FLAT, command=Show_Loss, padx=20)
        LSS_boton["btn_slc_LSS"].place(relx=0.53, rely=0.19, anchor=tk.CENTER)
    if LSS_label["lbl_slc_LSS"] is None:
        LSS_label["lbl_slc_LSS"] = fun.Label_Image('/LossSelect.png', 25, 25, navigation_bar, cnt_color,0.185,0.185)
    if Exp_Tabs_Gen is not None:
        if LSS_boton["btn_dsg_LSS"] is None:
            LSS_boton["btn_dsg_LSS"] = fun.Button_Image('/mtlSelect.png', 9, 7, navigation_bar,cnt_color,0.87,0.19,HideExpand_Loss)
    else:
        if LSS_boton["btn_dsg_LSS"] is None:
            LSS_boton["btn_dsg_LSS"] = fun.Button_Image('/desgloSelect.png', 9, 7, navigation_bar,cnt_color,0.87,0.19,Expand_Loss)
    # ---- Loss Content:
    if LSS_title["tlt_tlt_LSS"] is None:
        LSS_title["tlt_tlt_LSS"] = tk.Label(cnt_container, text="Loss estimations", 
                         font=("Abadi MT", 30), bg="white", fg="#274151")
        LSS_title["tlt_tlt_LSS"].place(relx=0.15, rely=0.1, anchor=tk.CENTER)
    if LSS_text["txt_tlt_LSS1"] is None:
        LSS_text["txt_tlt_LSS1"] = tk.Label(cnt_container, text="Welcome  to  the 'Loss Estimations'  section. Here,  you can fine - tune your risk assessments and gain  insights  into ", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        LSS_text["txt_tlt_LSS1"].place(relx=0.439, rely=0.17, anchor=tk.CENTER)
    if LSS_text["txt_tlt_LSS2"] is None:
        LSS_text["txt_tlt_LSS2"] = tk.Label(cnt_container, text="potential losses. Explore the following tabs to calibrate stochastic events, analyze simulation dispersion, and examine ", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        LSS_text["txt_tlt_LSS2"].place(relx=0.440, rely=0.207, anchor=tk.CENTER)
    if LSS_text["txt_tlt_LSS3"] is None:
        LSS_text["txt_tlt_LSS3"] = tk.Label(cnt_container, text="exceedance loss curves for a comprehensive understanding of risk and resilience.", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        LSS_text["txt_tlt_LSS3"].place(relx=0.317, rely=0.244, anchor=tk.CENTER)
    # ---- Loss Tabs: 
    if LSS_label["lbl_bkg_LSS"] is None:
        imagen_Loss = Image.open(os.path.join(os.getcwd(),"icon") + '/Fondo1.png')
        imagen_Loss = imagen_Loss.resize((800, 800), Image.LANCZOS)
        imagen_Loss = ImageTk.PhotoImage(imagen_Loss)
        LSS_label["lbl_bkg_LSS"] = tk.Label(cnt_container, image=imagen_Loss, bd=0, bg="white")
        LSS_label["lbl_bkg_LSS"].image = imagen_Loss
        LSS_label["lbl_bkg_LSS"].place(relx=0.8, rely=0.85, anchor=tk.CENTER)
    if LSS_rectg["rec_clb_LSS"] is None:
        LSS_rectg["rec_clb_LSS"] = tk.Canvas(cnt_container, bg="#C5B7AF", bd=0, highlightthickness=0)
        LSS_rectg["rec_clb_LSS"].place(relx=0.18, rely=0.56, anchor=tk.CENTER, width=350, height=280)
    if LSS_rectg["rec_dsp_LSS"] is None:
        LSS_rectg["rec_dsp_LSS"] = tk.Canvas(cnt_container, bg="#A8BAC4", bd=0, highlightthickness=0)
        LSS_rectg["rec_dsp_LSS"].place(relx=0.50, rely=0.56, anchor=tk.CENTER, width=350, height=280)
    if LSS_rectg["rec_ebr_LSS"] is None:
        LSS_rectg["rec_ebr_LSS"] = tk.Canvas(cnt_container, bg="#C5B7AF", bd=0, highlightthickness=0)
        LSS_rectg["rec_ebr_LSS"].place(relx=0.82, rely=0.56, anchor=tk.CENTER, width=350, height=280)
    # -------------------------------------------------------------------------
    if LSS_title["tlt_clb_LSS"] is None:
        LSS_title["tlt_clb_LSS"] = tk.Label(LSS_rectg["rec_clb_LSS"], text="Calibration", 
                         font=("Abadi MT", 19), bg="#C5B7AF", fg="#7D4C4B")
        LSS_title["tlt_clb_LSS"].place(relx=0.3, rely=0.25, anchor=tk.CENTER)
    if LSS_text["txt_clb_LSS1"] is None:
        LSS_text["txt_clb_LSS1"] = tk.Label(LSS_rectg["rec_clb_LSS"], text="Calibration of number of", 
                         font=("Abadi MT", 14), bg="#C5B7AF", fg="#404040")
        LSS_text["txt_clb_LSS1"].place(relx=0.42, rely=0.4, anchor=tk.CENTER)
    if LSS_text["txt_clb_LSS2"] is None:
        LSS_text["txt_clb_LSS2"] = tk.Label(LSS_rectg["rec_clb_LSS"], text="stochastic events. ", 
                         font=("Abadi MT", 14), bg="#C5B7AF", fg="#404040")
        LSS_text["txt_clb_LSS2"].place(relx=0.345, rely=0.48, anchor=tk.CENTER)
    if LSS_rectg["rec_sclb_LSS"] is None:
        LSS_rectg["rec_sclb_LSS"] = tk.Canvas(LSS_rectg["rec_clb_LSS"], bg="#C5B7AF", bd=0, highlightthickness=0)
        LSS_rectg["rec_sclb_LSS"].place(relx=0.48, rely=0.7, anchor=tk.CENTER, width=181, height=61)
        x2, y2 = 180, 60
        x1, y1 = 10,10
        radio_esquinas = 10
        color = "#B97F73"
        fun.rec_redond(LSS_rectg["rec_sclb_LSS"], x1, y1, x2, y2, radio_esquinas, color)
    if LSS_boton["btn_sclb_LSS"] is None:
        LSS_boton["btn_sclb_LSS"] = tk.Button(LSS_rectg["rec_sclb_LSS"], text="Go to page >", font=("Abadi MT", 15), 
                                     bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=Show_Loss_CLB, padx=20)
        LSS_boton["btn_sclb_LSS"].place(relx=0.55, rely=0.56, anchor=tk.CENTER)    
    # -------------------------------------------------------------------------
    if LSS_title["tlt_dsp_LSS"] is None:
        LSS_title["tlt_dsp_LSS"] = tk.Label(LSS_rectg["rec_dsp_LSS"], text="Dispersion", 
                         font=("Abadi MT", 19), bg="#A8BAC4", fg="#37586B")
        LSS_title["tlt_dsp_LSS"].place(relx=0.298, rely=0.25, anchor=tk.CENTER)
    if LSS_text["txt_dsp_LSS"] is None:
        LSS_text["txt_dsp_LSS"] = tk.Label(LSS_rectg["rec_dsp_LSS"], text="Simulation dispersion", 
                         font=("Abadi MT", 14), bg="#A8BAC4", fg="#404040")
        LSS_text["txt_dsp_LSS"].place(relx=0.39, rely=0.4, anchor=tk.CENTER)
    if LSS_rectg["rec_sdsp_LSS"] is None:
        LSS_rectg["rec_sdsp_LSS"] = tk.Canvas(LSS_rectg["rec_dsp_LSS"], bg="#A8BAC4", bd=0, highlightthickness=0)
        LSS_rectg["rec_sdsp_LSS"].place(relx=0.48, rely=0.7, anchor=tk.CENTER, width=181, height=61)
        x2, y2 = 180, 60
        x1, y1 = 10,10
        radio_esquinas = 10
        color = "#37586B"
        fun.rec_redond(LSS_rectg["rec_sdsp_LSS"], x1, y1, x2, y2, radio_esquinas, color)
    if LSS_boton["btn_sdsp_LSS"] is None:
        LSS_boton["btn_sdsp_LSS"] = tk.Button(LSS_rectg["rec_sdsp_LSS"], text="Go to page >", font=("Abadi MT", 15), 
                                     bd=0, bg="#37586B", fg="white", relief=tk.FLAT, command=Show_Loss_DSP, padx=20)
        LSS_boton["btn_sdsp_LSS"].place(relx=0.55, rely=0.56, anchor=tk.CENTER) 
    # -------------------------------------------------------------------------
    if LSS_title["tlt_ebr_LSS"] is None:
        LSS_title["tlt_ebr_LSS"] = tk.Label(LSS_rectg["rec_ebr_LSS"], text="Event Based Risk", 
                         font=("Abadi MT", 19), bg="#C5B7AF", fg="#7D4C4B")
        LSS_title["tlt_ebr_LSS"].place(relx=0.418, rely=0.25, anchor=tk.CENTER)
    if LSS_text["txt_ebr_LSS1"] is None:
        LSS_text["txt_ebr_LSS1"] = tk.Label(LSS_rectg["rec_ebr_LSS"], text="Exceedance loss curve and", 
                         font=("Abadi MT", 14), bg="#C5B7AF", fg="#404040")
        LSS_text["txt_ebr_LSS1"].place(relx=0.448, rely=0.4, anchor=tk.CENTER)
    if LSS_text["txt_ebr_LSS2"] is None:
        LSS_text["txt_ebr_LSS2"] = tk.Label(LSS_rectg["rec_ebr_LSS"], text="APE (Annual Probability of ", 
                         font=("Abadi MT", 14), bg="#C5B7AF", fg="#404040")
        LSS_text["txt_ebr_LSS2"].place(relx=0.462, rely=0.48, anchor=tk.CENTER)
    if LSS_text["txt_ebr_LSS3"] is None:
        LSS_text["txt_ebr_LSS3"] = tk.Label(LSS_rectg["rec_ebr_LSS"], text="Exceedance). ", 
                         font=("Abadi MT", 14), bg="#C5B7AF", fg="#404040")
        LSS_text["txt_ebr_LSS3"].place(relx=0.3, rely=0.56, anchor=tk.CENTER)
    if LSS_rectg["rec_sebr_LSS"] is None:
        LSS_rectg["rec_sebr_LSS"] = tk.Canvas(LSS_rectg["rec_ebr_LSS"], bg="#C5B7AF", bd=0, highlightthickness=0)
        LSS_rectg["rec_sebr_LSS"].place(relx=0.48, rely=0.7, anchor=tk.CENTER, width=181, height=61)
        x2, y2 = 180, 60
        x1, y1 = 10,10
        radio_esquinas = 10
        color = "#B97F73"
        fun.rec_redond(LSS_rectg["rec_sebr_LSS"], x1, y1, x2, y2, radio_esquinas, color)
    if LSS_boton["btn_sebr_LSS"] is None:
        LSS_boton["btn_sebr_LSS"] = tk.Button(LSS_rectg["rec_sebr_LSS"], text="Go to page >", font=("Abadi MT", 15), 
                                     bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=Show_Loss_EBR, padx=20)
        LSS_boton["btn_sebr_LSS"].place(relx=0.55, rely=0.56, anchor=tk.CENTER)  
"""
-------------------------------------------------------------------------------
Functions to hide content in other tabs
-------------------------------------------------------------------------------
"""
def Hide_Loss():
    # ---- Label Variables ----------------------------------------------------
    for lbl in label_LSS:
        if LSS_label[lbl] is not None:
            LSS_label[lbl].place_forget()
            LSS_label[lbl] = None
    # ---- Text Variables -----------------------------------------------------
    for txt in text_LSS:
        if LSS_text[txt] is not None:
            LSS_text[txt].place_forget()
            LSS_text[txt] = None
    # ---- Rectangle Variables  -----------------------------------------------
    for rec in rectg_LSS:
        if LSS_rectg[rec] is not None: 
            LSS_rectg[rec].place_forget()
            LSS_rectg[rec] = None
    # ---- Title Variables ----------------------------------------------------
    for tlt in title_LSS:
        if LSS_title[tlt] is not None: 
            LSS_title[tlt].place_forget()
            LSS_title[tlt] = None
    # ---- Button Variables ---------------------------------------------------
    for btn in boton_LSS:
        if LSS_boton[btn] is not None: 
            LSS_boton[btn].place_forget()
            LSS_boton[btn] = None
    # ---- Show the Tab -------------------------------------------------------
    if LSS_boton["btn_slc_LSS"] is None:
        LSS_boton["btn_slc_LSS"] = tk.Button(navigation_bar, text="Loss estimations", font=("Abadi MT", 13), 
                                      bd=0, bg=navbar_color, fg=cnt_color, relief=tk.FLAT, command=Show_Loss, padx=20)
        LSS_boton["btn_slc_LSS"].place(relx=0.53, rely=0.19, anchor=tk.CENTER)
    if LSS_label["lbl_slc_LSS"] is None:
        LSS_label["lbl_slc_LSS"] = fun.Label_Image('/Loss.png', 25, 25, navigation_bar, navbar_color ,0.185,0.185)
    # if LSS_boton["btn_dsg_LSS"] is None:
    #     LSS_boton["btn_dsg_LSS"] = fun.Button_Image('/desglo.png', 9, 7, navigation_bar, navbar_color,0.87,0.19, Expand_Loss)
        
    if Exp_Tabs_Gen is not None:
        if LSS_boton["btn_dsg_LSS"] is None:
            LSS_boton["btn_dsg_LSS"] = fun.Button_Image('/mtl.png', 9, 7, navigation_bar,navbar_color,0.87,0.19,HideExpand_Loss)
    else:
        if LSS_boton["btn_dsg_LSS"] is None:
            LSS_boton["btn_dsg_LSS"] = fun.Button_Image('/desglo.png', 9, 7, navigation_bar,navbar_color,0.87,0.19,Expand_Loss)
#%% ====== TAB >> LOSS / CLB ==================================================
"""
-------------------------------------------------------------------------------
Define Variables
-------------------------------------------------------------------------------
"""
rectg_CLB = ["rec_slc_CLB","rec_gen_CLB","rec_exp_CLB","rec_Cmnz_CLB"]
CLB_rectg = {}
for rec in rectg_CLB:
    CLB_rectg[rec] = None
boton_CLB = ["btn_slc_CLB","btn_crp_CLB","btn_gen_CLB","btn_exp_CLB","btn_Cmnz_CLB"]
CLB_boton = {}
for btn in boton_CLB:
    CLB_boton[btn] = None
title_CLB = ["tlt_tlt_CLB","tlt_cp_CLB","tlt_mnz_CLB"]
CLB_title = {}
for tlt in title_CLB:
    CLB_title[tlt] = None
text_CLB = ["txt_tlt_CLB1","txt_tlt_CLB2","txt_crp_CLB"]
CLB_text = {}
for txt in text_CLB:
    CLB_text[txt] = None
label_CLB = ["lbl_exp_CLB"]
CLB_label = {}
for lbl in label_CLB:
    CLB_label[lbl] = None
canva_CLB = ["cnv_cp_CLB","cnv_mnz_CLB"]
CLB_canva = {}
for cnv in canva_CLB:
    CLB_canva[cnv] = None
expcsv_CLB = ['exp_AGR_sts','exp_AGR_mnz','Nu_sim']
expcsv = {}
for exp in expcsv_CLB:
    expcsv[exp] = None
canva_CLB_expo =[ "cnv_Cp_CLB_event","cnv_Mnz_CLB_event"]
canva_expo = {}
for cnv in canva_CLB_expo:
    canva_expo[cnv] = None
carpeta_seleccionada = None
cmb_Mnz_CLB = None
CP_Name = None
opciones = None
codigomnzs = None
simmnz_losses = None
simmnz_losses2 = None
newNsim = None
def Elements_Loss_CLB():
    """
    ---------------------------------------------------------------------------
                         The elements of other tabs are hiden
    ---------------------------------------------------------------------------
    """
    Hide_Loss()
    Hide_Home()
    Hide_Loss_DSP()
    Hide_Loss_EBR()
    """
    ---------------------------------------------------------------------------
                                   Tab Elements
    ---------------------------------------------------------------------------
    """
    # ---- Select Loss: -------------------------------------------------------
    # When "Loss Estimations >> Calibration" is selected, the color of the title
    # changes.
    if CLB_rectg["rec_slc_CLB"] is None:
        CLB_rectg["rec_slc_CLB"] = tk.Canvas(navigation_bar, bg="#37586B", bd=0, highlightthickness=0)
        CLB_rectg["rec_slc_CLB"].place(relx=0.67, rely=0.25, anchor=tk.CENTER, width=231, height=51)
        x2, y2 = 230, 50
        x1, y1 = 10,10
        radio_esquinas = 18
        color = "white"
        fun.rec_redond(CLB_rectg["rec_slc_CLB"], x1, y1, x2, y2, radio_esquinas, color)
    if CLB_boton["btn_slc_CLB"] is None:
        CLB_boton["btn_slc_CLB"] = tk.Button(CLB_rectg["rec_slc_CLB"], text="Calibration", font=("Abadi MT", 13), 
                                      bd=0, bg="white", fg="#37586B", relief=tk.FLAT, command=Show_Loss_CLB, padx=2)
        CLB_boton["btn_slc_CLB"].place(relx=0.497, rely=0.6, anchor="e") 
    # --- Titulo de la pagina -------------------------------------------------
    if CLB_title["tlt_tlt_CLB"] is None:
        CLB_title["tlt_tlt_CLB"] = tk.Label(cnt_container, text="Calibrate number of stochastic events", 
                         font=("Abadi MT", 30), bg="white", fg="#274151")
        CLB_title["tlt_tlt_CLB"].place(relx=0.29, rely=0.1, anchor=tk.CENTER)
    if CLB_text["txt_tlt_CLB1"] is None:
        CLB_text["txt_tlt_CLB1"] = tk.Label(cnt_container, text="The number of stochastic events per branch of the logical tree is calibrated to  achieve ", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        CLB_text["txt_tlt_CLB1"].place(relx=0.335, rely=0.17, anchor=tk.CENTER)
    if CLB_text["txt_tlt_CLB2"] is None:
        CLB_text["txt_tlt_CLB2"] = tk.Label(cnt_container, text="stability in the average annual loss for both the municipality and its predominant block.", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        CLB_text["txt_tlt_CLB2"].place(relx=0.336, rely=0.207, anchor=tk.CENTER)
    # --- Seleccionar carpeta -------------------------------------------------
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/carpeta.png')
    img_crp = img_crp.resize((45, 40), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if CLB_boton["btn_crp_CLB"] is None:
        CLB_boton["btn_crp_CLB"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda:select_folder_CLB(0.15,0.28))
        CLB_boton["btn_crp_CLB"].image = img_crp
        CLB_boton["btn_crp_CLB"].place(relx=0.15, rely=0.28, anchor=tk.CENTER) 
    if CLB_text["txt_crp_CLB"] is None:
        CLB_text["txt_crp_CLB"] = tk.Label(cnt_container, text="Select folder", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        CLB_text["txt_crp_CLB"].place(relx=0.225, rely=0.28, anchor=tk.CENTER) 
    # --- Boton generar -------------------------------------------------------
    if CLB_rectg["rec_gen_CLB"] is None:
        CLB_rectg["rec_gen_CLB"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
        CLB_rectg["rec_gen_CLB"].place(relx=0.36, rely=0.28, anchor=tk.CENTER, width=150, height=38) 
    if CLB_boton["btn_gen_CLB"] is None:
        CLB_boton["btn_gen_CLB"] = tk.Button(CLB_rectg["rec_gen_CLB"], text="CALIBRATE", font=("Abadi MT", 15), 
                                          bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: prueba_aggrisk(resultado_label))
        CLB_boton["btn_gen_CLB"].place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=100, height=45)
    # --- Botones generados al generar el grafico -----------------------------
    if CLB_canva["cnv_cp_CLB"] is not None and CLB_canva["cnv_mnz_CLB"] is not None:
        # Titulo de graficos --------------------------------------------------
        if CLB_title["tlt_cp_CLB"] is None:
            texto = "Average annual municipal loss (" + CP_Name +")"
            CLB_title["tlt_cp_CLB"] = tk.Label(cnt_container, text=texto,font=("Abadi MT", 15), bg="white", fg="#3B3838")
            CLB_title["tlt_cp_CLB"].place(relx=0.28, rely=0.35, anchor=tk.CENTER)
        if CLB_title["tlt_mnz_CLB"] is None:
            texto = "Average annual loss per block (" + CP_Name +")"
            CLB_title["tlt_mnz_CLB"] = tk.Label(cnt_container, text=texto,font=("Abadi MT", 15), bg="white", fg="#3B3838")
            CLB_title["tlt_mnz_CLB"].place(relx=0.73, rely=0.35, anchor=tk.CENTER)
        # ---- boton exportar resultados --------------------------------------
        if CLB_rectg["rec_exp_CLB"] is None:
            CLB_rectg["rec_exp_CLB"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
            CLB_rectg["rec_exp_CLB"].place(relx=0.1, rely=0.95, anchor=tk.CENTER, width=180, height=40) 
        if CLB_boton["btn_exp_CLB"] is None:
            CLB_boton["btn_exp_CLB"] = tk.Button(CLB_rectg["rec_exp_CLB"], text="Export results", font=("Abadi MT", 15), bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: lb.ExportarGraficos_Perdidas_Calibrar(CLB_canva["cnv_cp_CLB"], CLB_canva["cnv_mnz_CLB"], canva_expo["cnv_Cp_CLB_event"], canva_expo["cnv_Mnz_CLB_event"], expcsv['exp_AGR_sts'], expcsv['exp_AGR_mnz'], expcsv['Nu_sim']))
            CLB_boton["btn_exp_CLB"].place(relx=0.565, rely=0.5, anchor=tk.CENTER, width=135, height=40)
        if CLB_label["lbl_exp_CLB"] is None:
            img_exp = Image.open(os.path.join(os.getcwd(),"icon") + '/exportar.png')
            img_exp = img_exp.resize((23, 20), Image.LANCZOS)
            img_exp = ImageTk.PhotoImage(img_exp)
            CLB_label["lbl_exp_CLB"] = tk.Label(CLB_rectg["rec_exp_CLB"], image=img_exp, bd=0, bg="#B97F73")
            CLB_label["lbl_exp_CLB"].image = img_exp
            CLB_label["lbl_exp_CLB"].place(relx=0.13, rely=0.5, anchor=tk.CENTER)
        # ---- Mostrar combo cambiar manzana ----------------------------------
        if CLB_rectg["rec_Cmnz_CLB"] is None:
            CLB_rectg["rec_Cmnz_CLB"] = tk.Canvas(cnt_container, bg="#37586B", bd=0, highlightthickness=0)
            CLB_rectg["rec_Cmnz_CLB"].place(relx=0.73, rely=0.93, anchor=tk.CENTER, width=200, height=35) 
        global cmb_Mnz_CLB
        if cmb_Mnz_CLB is None:
            cmb_Mnz_CLB = ttk.Combobox(CLB_rectg["rec_Cmnz_CLB"],values=opciones)
            cmb_Mnz_CLB.place(relx=0.82, rely=0.48, anchor=tk.CENTER, width=65, height=25)
        if CLB_boton["btn_Cmnz_CLB"] is None:
            CLB_boton["btn_Cmnz_CLB"] = tk.Button(CLB_rectg["rec_Cmnz_CLB"], text="Select block", font=("Abadi MT", 14), bd=0, bg="#37586B", fg="white", relief=tk.FLAT, command=lambda: Cambiar_Mnz(cmb_Mnz_CLB.get(),CLB_canva["cnv_mnz_CLB"]))
            CLB_boton["btn_Cmnz_CLB"].place(relx=0.34, rely=0.52, anchor=tk.CENTER, width=119, height=25)
        
    resultado_label = tk.Label(cnt_container, text="", fg="red")
    resultado_label.pack()                                   
    resultado_label.pack_forget()
"""
-------------------------------------------------------------------------------
Funciones Ocultar contenido de otras pestanas
-------------------------------------------------------------------------------
"""
def Hide_Loss_CLB():
    for rec in rectg_CLB:
        if CLB_rectg[rec] is not None:
            CLB_rectg[rec].place_forget()
            CLB_rectg[rec] = None
    for btn in boton_CLB:
        if CLB_boton[btn] is not None:
            CLB_boton[btn].place_forget()
            CLB_boton[btn] = None
    for tlt in title_CLB:
        if CLB_title[tlt] is not None:
            CLB_title[tlt].place_forget()
            CLB_title[tlt] = None
    for txt in text_CLB:
        if CLB_text[txt] is not None:
            CLB_text[txt].place_forget()
            CLB_text[txt] = None
    for cnv in canva_CLB:
        if CLB_canva[cnv] is not None:
            CLB_canva[cnv].get_tk_widget().destroy()
            CLB_canva[cnv] = None
    for lbl in label_CLB:
        if CLB_label[lbl] is not None:
            CLB_label[lbl].place_forget()
            CLB_label[lbl] = None
#%% ====== TAB >> LOSS / DSP ================================================== 
"""
-------------------------------------------------------------------------------
Define Variables
-------------------------------------------------------------------------------
"""
rectg_DSP = ["rec_slc_DSP","rec_gen_DSP","rec_exp_DSP"]
DSP_rectg = {}
for rec in rectg_DSP:
    DSP_rectg[rec] = None
boton_DSP = ["btn_slc_DSP","btn_crp_DSP","btn_gen_DSP","btn_exp_DSP"]
DSP_boton = {}
for btn in boton_DSP:
    DSP_boton[btn] = None
title_DSP = ["tlt_tlt_DSP","tlt_ses_DSP","tlt_evt_DSP"]
DSP_title = {}
for tlt in title_DSP:
    DSP_title[tlt] = None
text_DSP = ["txt_tlt_DSP1","txt_tlt_DSP2","txt_tlt_DSP3","txt_crp_DSP"]
DSP_text = {}
for txt in text_DSP:
    DSP_text[txt] = None
canva_DSP = ["cnv_ses_DSP","cnv_evt_DSP"]
DSP_canva = {}
for cnv in canva_DSP:
    DSP_canva[cnv] = None
expcsv_DSP = ['exp_AGR_sts','exp_AGR_mnz','Nu_sim']
DSP_expcsv = {}
for exp in expcsv_DSP:
    DSP_expcsv[exp] = None
label_DSP = ["lbl_exp_DSP"]
DSP_label = {}
for lbl in label_DSP:
    DSP_label[lbl] = None
"""
-------------------------------------------------------------------------------
Funciones para Mostrar contenido de otras pestanas
-------------------------------------------------------------------------------
"""
def Elements_Loss_DSP():
    """
    ---------------------------------------------------------------------------
                         The elements of other tabs are hiden
    ---------------------------------------------------------------------------
    """
    Hide_Loss()
    Hide_Home()
    Hide_Loss_CLB()
    Hide_Loss_EBR()
    """
    ---------------------------------------------------------------------------
                                   Tab Elements
    ---------------------------------------------------------------------------
    """
    # ---- Select Loss: -------------------------------------------------------
    # When "Loss Estimations >> Calibration" is selected, the color of the title
    # changes.
    if DSP_rectg["rec_slc_DSP"] is None:
        DSP_rectg["rec_slc_DSP"] = tk.Canvas(navigation_bar, bg="#37586B", bd=0, highlightthickness=0)
        DSP_rectg["rec_slc_DSP"].place(relx=0.67, rely=0.322, anchor=tk.CENTER, width=231, height=51)
        x2, y2 = 230, 50
        x1, y1 = 10,10
        radio_esquinas = 18
        color = "white"
        fun.rec_redond(DSP_rectg["rec_slc_DSP"], x1, y1, x2, y2, radio_esquinas, color)
    if DSP_boton["btn_slc_DSP"] is None:
        DSP_boton["btn_slc_DSP"] = tk.Button(DSP_rectg["rec_slc_DSP"], text="Dispersion", font=("Abadi MT", 13), 
                                      bd=0, bg="white", fg="#37586B", relief=tk.FLAT, command=Show_Loss_DSP, padx=2)
        DSP_boton["btn_slc_DSP"].place(relx=0.497, rely=0.6, anchor="e") 
    # --- Titulo de la pagina -------------------------------------------------
    if DSP_title["tlt_tlt_DSP"] is None:
        DSP_title["tlt_tlt_DSP"] = tk.Label(cnt_container, text="Dispersion of expected annual losses", 
                         font=("Abadi MT", 30), bg="white", fg="#274151")
        DSP_title["tlt_tlt_DSP"].place(relx=0.291, rely=0.1, anchor=tk.CENTER)
    if DSP_text["txt_tlt_DSP1"] is None:
        DSP_text["txt_tlt_DSP1"] = tk.Label(cnt_container, text="Calculate the dispersion of the expected annual loss (EAL) for the municipality based on the number of", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        DSP_text["txt_tlt_DSP1"].place(relx=0.389, rely=0.17, anchor=tk.CENTER)
    if DSP_text["txt_tlt_DSP2"] is None:
        DSP_text["txt_tlt_DSP2"] = tk.Label(cnt_container, text="stochastic events per branch of the programmed logic tree (ses_per_logic_tree) and based on the total", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        DSP_text["txt_tlt_DSP2"].place(relx=0.387, rely=0.207, anchor=tk.CENTER)
    if DSP_text["txt_tlt_DSP3"] is None:
        DSP_text["txt_tlt_DSP3"] = tk.Label(cnt_container, text="number of events that occurred.", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        DSP_text["txt_tlt_DSP3"].place(relx=0.1458, rely=0.244, anchor=tk.CENTER)
    # --- Seleccionar carpeta -------------------------------------------------
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/carpeta.png')
    img_crp = img_crp.resize((45, 40), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if DSP_boton["btn_crp_DSP"] is None:
        DSP_boton["btn_crp_DSP"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=seleccionar_carpeta_DSP)
        DSP_boton["btn_crp_DSP"].image = img_crp
        DSP_boton["btn_crp_DSP"].place(relx=0.15, rely=0.315, anchor=tk.CENTER) 
    if DSP_text["txt_crp_DSP"] is None:
        DSP_text["txt_crp_DSP"] = tk.Label(cnt_container, text="Select folder", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        DSP_text["txt_crp_DSP"].place(relx=0.225, rely=0.315, anchor=tk.CENTER)
    # --- Boton generar -------------------------------------------------------
    if DSP_rectg["rec_gen_DSP"] is None:
        DSP_rectg["rec_gen_DSP"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
        DSP_rectg["rec_gen_DSP"].place(relx=0.36, rely=0.315, anchor=tk.CENTER, width=150, height=38) 
    if DSP_boton["btn_gen_DSP"] is None:
        DSP_boton["btn_gen_DSP"] = tk.Button(DSP_rectg["rec_gen_DSP"], text="GENERATE", font=("Abadi MT", 15), 
                                          bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: dispersion_aggrisk(resultado_labelDSP))
        DSP_boton["btn_gen_DSP"].place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=100, height=45)
    # --- Botones generados al generar el grafico -----------------------------
    if DSP_canva["cnv_ses_DSP"] is not None and DSP_canva["cnv_evt_DSP"] is not None:
        # Titulo de graficos --------------------------------------------------
        if DSP_title["tlt_ses_DSP"] is None:
            texto = "Municipal dispersion - ses_per_logic_tree (" + CP_Name +")"
            DSP_title["tlt_ses_DSP"] = tk.Label(cnt_container, text=texto,font=("Abadi MT", 15), bg="white", fg="#3B3838")
            DSP_title["tlt_ses_DSP"].place(relx=0.28, rely=0.38, anchor=tk.CENTER)
        if DSP_title["tlt_evt_DSP"] is None:
            texto = "Municipal dispersion - Number of events (" + CP_Name +")"
            DSP_title["tlt_evt_DSP"] = tk.Label(cnt_container, text=texto,font=("Abadi MT", 15), bg="white", fg="#3B3838")
            DSP_title["tlt_evt_DSP"].place(relx=0.73, rely=0.38, anchor=tk.CENTER)
        # ---- Boton exportar resultados --------------------------------------
        if DSP_rectg["rec_exp_DSP"] is None:
            DSP_rectg["rec_exp_DSP"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
            DSP_rectg["rec_exp_DSP"].place(relx=0.1, rely=0.95, anchor=tk.CENTER, width=180, height=40) 
        if DSP_boton["btn_exp_DSP"] is None:
            DSP_boton["btn_exp_DSP"] = tk.Button(DSP_rectg["rec_exp_DSP"], text="Export results", font=("Abadi MT", 15), bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: lb.ExportarGraficos_Perdidas_Dispersion(DSP_canva["cnv_ses_DSP"], DSP_canva["cnv_evt_DSP"]))
            DSP_boton["btn_exp_DSP"].place(relx=0.565, rely=0.5, anchor=tk.CENTER, width=135, height=40)
        if DSP_label["lbl_exp_DSP"] is None:
            img_exp = Image.open(os.path.join(os.getcwd(),"icon") + '/exportar.png')
            img_exp = img_exp.resize((23, 20), Image.LANCZOS)
            img_exp = ImageTk.PhotoImage(img_exp)
            DSP_label["lbl_exp_DSP"] = tk.Label(DSP_rectg["rec_exp_DSP"], image=img_exp, bd=0, bg="#B97F73")
            DSP_label["lbl_exp_DSP"].image = img_exp
            DSP_label["lbl_exp_DSP"].place(relx=0.13, rely=0.5, anchor=tk.CENTER)
            
    resultado_labelDSP = tk.Label(cnt_container, text="", fg="red")
    resultado_labelDSP.pack()                                   
    resultado_labelDSP.pack_forget()
"""
-------------------------------------------------------------------------------
Funciones Ocultar contenido de otras pestanas
-------------------------------------------------------------------------------
"""
def Hide_Loss_DSP():
    for rec in rectg_DSP:
        if DSP_rectg[rec] is not None:
            DSP_rectg[rec].place_forget()
            DSP_rectg[rec] = None
    for btn in boton_DSP:
        if DSP_boton[btn] is not None:
            DSP_boton[btn].place_forget()
            DSP_boton[btn] = None
    for tlt in title_DSP:
        if DSP_title[tlt] is not None:
            DSP_title[tlt].place_forget()
            DSP_title[tlt] = None
    for txt in text_DSP:
        if DSP_text[txt] is not None:
            DSP_text[txt].place_forget()
            DSP_text[txt] = None
    for cnv in canva_DSP:
        if DSP_canva[cnv] is not None:
            DSP_canva[cnv].get_tk_widget().destroy()
            DSP_canva[cnv] = None
    for lbl in label_DSP:
        if DSP_label[lbl] is not None:
            DSP_label[lbl].place_forget()
            DSP_label[lbl] = None  
#%% ====== TAB >> LOSS / EBR ================================================== 
"""
-------------------------------------------------------------------------------
Define Variables
-------------------------------------------------------------------------------
"""
rectg_EBR = ["rec_slc_EBR","rec_per_EBR","rec_gen_EBR","rec_exp_EBR","rec_mas_EBR1"]
EBR_rectg = {}
for rec in rectg_EBR:
    EBR_rectg[rec] = None
boton_EBR = ["btn_slc_EBR","btn_crp_EBR","btn_gen_EBR","btn_exp_EBR","btn_crp_EBR2","btn_crp_EBR3"
             ,"btn_mas_EBR1"]
EBR_boton = {}
for btn in boton_EBR:
    EBR_boton[btn] = None
title_EBR = ["tlt_tlt_EBR"]
EBR_title = {}
for tlt in title_EBR:
    EBR_title[tlt] = None
text_EBR = ["txt_tlt_EBR1","txt_tlt_EBR2","txt_tlt_EBR3","txt_tlt_EBR4","txt_crp_EBR","txt_per_EBR",
            "txt_crv_EBR","txt_crp_EBR2","txt_crp_EBR3"]
EBR_text = {}
for txt in text_EBR:
    EBR_text[txt] = None
entry_EBR = ["ent_per_EBR"]
EBR_entry = {}
for ent in entry_EBR:
    EBR_entry[ent] = None
label_EBR = ["lbl_per_EBR","lbl_exp_EBR"]
EBR_label = {}
for lbl in label_EBR:
    EBR_label[lbl] = None
canva_EBR = ["cnv_crv_EBR","cnv_EBR_taxo","cnv_map_COP"]
EBR_canva = {}
for cnv in canva_EBR:
    EBR_canva[cnv] = None
archivo_seleccionado = None
df_EBR = None 
valexpuesto = None
aggsts_loss = None
PE_mill = None
df_resultados = None
Pr50_Val = None
Table_Resu = None
Table_Resu_tax = None
CP_Name = None
df_expotax = None
taxo_description = None
valorperiodo = None
# ------ Variables procesamiento ----------------------------------------------
recPAE_EBR = ['rec_vlx_tlt','rec_vlx_cop','rec_vlx_val',
              'rec_pae_tlt','rec_pae_cop','rec_pae_prc','rec_pae_val_cop','rec_pae_val_val',
              'rec_pmp_tlt','rec_pdr_tlt','rec_exd_tlt','rec_pe_tlt',
              'rec_pdran_tlt','rec_exdprd_tlt','rec_pecop_tlt','rec_peprc_tlt',
              'rec_pdran_val','rec_exdprd_val','rec_pecop_val','rec_peprc_val']
EBR_recPAE = {}
for rec in recPAE_EBR: 
    EBR_recPAE[rec] = None
txtPAE_EBR = ['txt_vlx_tlt','txt_vlx_cop','txt_vlx_val',
              'txt_pae_tlt1','txt_pae_tlt2','txt_pae_cop','txt_pae_prc','txt_pae_val_cop','txt_pae_val_val',
              'txt_pmp_tlt','txt_pdr_tlt1','txt_pdr_tlt2','txt_exd_tlt1','txt_exd_tlt2','txt_pe_tlt',
              'txt_pdran_tlt','txt_exdprd_tlt','txt_pecop_tlt','txt_peprc_tlt',
              'txt_pdran_val1','txt_pdran_val2','txt_pdran_val3','txt_pdran_val4','txt_pdran_val5',
              'txt_exdprd_val1','txt_exdprd_val2','txt_exdprd_val3','txt_exdprd_val4','txt_exdprd_val5',
              'txt_pecop_val1','txt_pecop_val2','txt_pecop_val3','txt_pecop_val4','txt_pecop_val5',
              'txt_peprc_val1','txt_peprc_val2','txt_peprc_val3','txt_peprc_val4','txt_peprc_val5']
EBR_txtPAE = {}
for rec in txtPAE_EBR: 
    EBR_txtPAE[rec] = None
def Elements_Loss_EBR():
    """
    ---------------------------------------------------------------------------
                         The elements of other tabs are hiden
    ---------------------------------------------------------------------------
    """
    Hide_Loss()
    Hide_Home()
    Hide_Loss_CLB()
    Hide_Loss_DSP()
    """
    ---------------------------------------------------------------------------
                                   Tab Elements
    ---------------------------------------------------------------------------
    """
    # --- Elegir Loss/Calibration ---------------------------------------------
    if EBR_rectg["rec_slc_EBR"] is None:
        EBR_rectg["rec_slc_EBR"] = tk.Canvas(navigation_bar, bg="#37586B", bd=0, highlightthickness=0)
        EBR_rectg["rec_slc_EBR"].place(relx=0.67, rely=0.39, anchor=tk.CENTER, width=231, height=51)
        x2, y2 = 230, 50
        x1, y1 = 10,10
        radio_esquinas = 18
        color = "white"
        fun.rec_redond(EBR_rectg["rec_slc_EBR"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_boton["btn_slc_EBR"] is None:
        EBR_boton["btn_slc_EBR"] = tk.Button(EBR_rectg["rec_slc_EBR"], text="Event Based Risk", font=("Abadi MT", 13), 
                                      bd=0, bg="white", fg="#37586B", relief=tk.FLAT, command=Show_Loss_EBR, padx=2)
        EBR_boton["btn_slc_EBR"].place(relx=0.70, rely=0.59, anchor="e") 
    # --- Titulo de la pagina -------------------------------------------------
    if EBR_title["tlt_tlt_EBR"] is None:
        EBR_title["tlt_tlt_EBR"] = tk.Label(cnt_container, text="Resultados de Riesgo Basado en Eventos", 
                         font=("Abadi MT", 30), bg="white", fg="#274151")
        EBR_title["tlt_tlt_EBR"].place(relx=0.318, rely=0.09, anchor=tk.CENTER)
    if EBR_text["txt_tlt_EBR1"] is None:
        EBR_text["txt_tlt_EBR1"] = tk.Label(cnt_container, text="En esta sección, se genera la curva de excedencia utilizando la pérdida anual esperada para un periodo de retorno especificado.", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR1"].place(relx=0.478, rely=0.16, anchor=tk.CENTER)
    if EBR_text["txt_tlt_EBR2"] is None:
        EBR_text["txt_tlt_EBR2"] = tk.Label(cnt_container, text="También se proporciona la pérdida máxima probable para periodos de retorno de 31, 225, 475, 975 y 1475 años. Además, se ", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR2"].place(relx=0.479, rely=0.197, anchor=tk.CENTER)
    if EBR_text["txt_tlt_EBR3"] is None:
        EBR_text["txt_tlt_EBR3"] = tk.Label(cnt_container, text="encuentra la pérdida anual esperada agregada basada en la tipología del edificio, junto con representaciones gráficas y espaciales,", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR3"].place(relx=0.488, rely=0.234, anchor=tk.CENTER)
    if EBR_text["txt_tlt_EBR4"] is None:
        EBR_text["txt_tlt_EBR4"] = tk.Label(cnt_container, text="tanto en valores absolutos como relativos a nivel de manzana censal.", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR4"].place(relx=0.276, rely=0.271, anchor=tk.CENTER)
    # --- Seleccionar archivo -------------------------------------------------
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/archivo.png')
    img_crp = img_crp.resize((37, 33), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if EBR_boton["btn_crp_EBR"] is None:
        EBR_boton["btn_crp_EBR"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda: select_file(0.15,0.32))
        EBR_boton["btn_crp_EBR"].image = img_crp
        EBR_boton["btn_crp_EBR"].place(relx=0.15, rely=0.32, anchor=tk.CENTER) 
    if EBR_text["txt_crp_EBR"] is None:
        EBR_text["txt_crp_EBR"] = tk.Label(cnt_container, text="Seleccionar hdf5 agregado por manzana", 
                          font=("Abadi MT", 13), bg="white", fg="#000000")
        EBR_text["txt_crp_EBR"].place(relx=0.29, rely=0.32, anchor=tk.CENTER) 
    # --- Seleccionar archivo -------------------------------------------------
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/archivo.png')
    img_crp = img_crp.resize((37, 33), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if EBR_boton["btn_crp_EBR3"] is None:
        EBR_boton["btn_crp_EBR3"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda:select_file_tax(0.15,0.375))
        EBR_boton["btn_crp_EBR3"].image = img_crp
        EBR_boton["btn_crp_EBR3"].place(relx=0.15, rely=0.375, anchor=tk.CENTER) 
    if EBR_text["txt_crp_EBR3"] is None:
        EBR_text["txt_crp_EBR3"] = tk.Label(cnt_container, text="Seleccionar hdf5 agregado por taxonomía", 
                          font=("Abadi MT", 13), bg="white", fg="#000000")
        EBR_text["txt_crp_EBR3"].place(relx=0.295, rely=0.375, anchor=tk.CENTER)
    # --- Seleccionar carpeta -------------------------------------------------
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/carpeta.png')
    img_crp = img_crp.resize((37, 33), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if EBR_boton["btn_crp_EBR2"] is None:
        EBR_boton["btn_crp_EBR2"] = tk.Button(cnt_container, image=img_crp, 
                                    bd=0, bg="white", command=lambda:select_folder(0.446,0.32))
        EBR_boton["btn_crp_EBR2"].image = img_crp
        EBR_boton["btn_crp_EBR2"].place(relx=0.446, rely=0.32, anchor=tk.CENTER) 
    if EBR_text["txt_crp_EBR2"] is None:
        EBR_text["txt_crp_EBR2"] = tk.Label(cnt_container, text="Seleccionar carpeta de shapes", 
                          font=("Abadi MT", 13), bg="white", fg="#000000")
        EBR_text["txt_crp_EBR2"].place(relx=0.555, rely=0.32, anchor=tk.CENTER)
    # --- Ingresar periodo de analisis ----------------------------------------
    if EBR_rectg["rec_per_EBR"] is None:
        EBR_rectg["rec_per_EBR"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_rectg["rec_per_EBR"].place(relx=0.655, rely=0.372, anchor=tk.CENTER, width=71, height=36)
        x2, y2 = 70, 35
        x1, y1 = 10,10
        radio_esquinas = 5
        color = "#D0CECE"
        fun.rec_redond(EBR_rectg["rec_per_EBR"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_entry["ent_per_EBR"] is None:
        EBR_entry["ent_per_EBR"] = tk.Entry(EBR_rectg["rec_per_EBR"], bg = "#D0CECE", bd=0, highlightthickness=0)
        EBR_entry["ent_per_EBR"].place(relx=0.55, rely=0.62, anchor=tk.CENTER, width=40, height=20)
    if EBR_label["lbl_per_EBR"] is None:
        imagen_per = Image.open(os.path.join(os.getcwd(),"icon") + '/periodo.png')
        imagen_per = imagen_per.resize((40, 40), Image.LANCZOS)
        imagen_per = ImageTk.PhotoImage(imagen_per)
        EBR_label["lbl_per_EBR"] = tk.Label(cnt_container, image=imagen_per, bd=0, bg="white")
        EBR_label["lbl_per_EBR"].image = imagen_per
        EBR_label["lbl_per_EBR"].place(relx=0.446, rely=0.375, anchor=tk.CENTER)
    if EBR_text["txt_per_EBR"] is None:
        EBR_text["txt_per_EBR"] = tk.Label(cnt_container, text="Ingresar periodo de análisis", 
                                    font=("Abadi MT", 13), bg="white", fg="#000000")
        EBR_text["txt_per_EBR"].place(relx=0.55, rely=0.375, anchor=tk.CENTER)
    # --- Boton generar -------------------------------------------------------
    if EBR_rectg["rec_gen_EBR"] is None:
        EBR_rectg["rec_gen_EBR"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
        EBR_rectg["rec_gen_EBR"].place(relx=0.78, rely=0.35, anchor=tk.CENTER, width=150, height=38) 
    if EBR_boton["btn_gen_EBR"] is None:
        EBR_boton["btn_gen_EBR"] = tk.Button(EBR_rectg["rec_gen_EBR"], text="GENERATE", font=("Abadi MT", 15), 
                                          bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: procs_riskbyevent(riskbyevent_label))
        EBR_boton["btn_gen_EBR"].place(relx=0.5, rely=0.5, anchor=tk.CENTER, width=100, height=45)
    # --- botones generados al generar el grafico -----------------------------
    if EBR_canva["cnv_crv_EBR"] is not None:
        # ---- titulo de graficos ---------------------------------------------
        if EBR_text["txt_crv_EBR"] is None:
            texto = "Curva de excedencia (" + CP_Name +")"
            EBR_text["txt_crv_EBR"] = tk.Label(cnt_container, text=texto, font=("Abadi MT", 14), bg="white", fg="#3B3838")
            EBR_text["txt_crv_EBR"].place(relx=0.275, rely=0.435, anchor=tk.CENTER)
        # ---- Boton exportar resultados --------------------------------------
        if EBR_rectg["rec_exp_EBR"] is None:
            EBR_rectg["rec_exp_EBR"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
            EBR_rectg["rec_exp_EBR"].place(relx=0.09, rely=0.965, anchor=tk.CENTER, width=180, height=33) 
        if EBR_boton["btn_exp_EBR"] is None:
            EBR_boton["btn_exp_EBR"] = tk.Button(EBR_rectg["rec_exp_EBR"], text="Exportar resultados", font=("Abadi MT", 13), bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: lb.Exportar_Perdidas_RiskByevent(EBR_canva["cnv_crv_EBR"],Table_Resu,Table_Resu_tax,EBR_canva["cnv_EBR_taxo"]))
            EBR_boton["btn_exp_EBR"].place(relx=0.55, rely=0.5, anchor=tk.CENTER, width=140, height=40)
        if EBR_label["lbl_exp_EBR"] is None:
            img_exp = Image.open(os.path.join(os.getcwd(),"icon") + '/exportar.png')
            img_exp = img_exp.resize((18, 16), Image.LANCZOS)
            img_exp = ImageTk.PhotoImage(img_exp)
            EBR_label["lbl_exp_EBR"] = tk.Label(EBR_rectg["rec_exp_EBR"], image=img_exp, bd=0, bg="#B97F73")
            EBR_label["lbl_exp_EBR"].image = img_exp
            EBR_label["lbl_exp_EBR"].place(relx=0.09, rely=0.5, anchor=tk.CENTER)
        # ---- Boton mas resultados -------------------------------------------
        if EBR_rectg["rec_mas_EBR1"] is None:
            EBR_rectg["rec_mas_EBR1"] = tk.Canvas(cnt_container, bg="#659B7D", bd=0, highlightthickness=0)
            EBR_rectg["rec_mas_EBR1"].place(relx=0.889, rely=0.965, anchor=tk.CENTER, width=130, height=29) 
        if EBR_boton["btn_mas_EBR1"] is None:
            EBR_boton["btn_mas_EBR1"] = tk.Button(EBR_rectg["rec_mas_EBR1"], text="Siguiente >>", font=("Abadi MT", 13), bd=0, bg="#659B7D", fg="white", relief=tk.FLAT, command=lambda: results_taxonomy_EBR())
            EBR_boton["btn_mas_EBR1"].place(relx=0.55, rely=0.5, anchor=tk.CENTER, width=140, height=40)
        # ---- tabla de resumen PAE -------------------------------------------
        semy = 0.445
        semx = 0.58
        # 1). Valor expuesto --------------------------------------------------
        if EBR_recPAE["rec_vlx_tlt"] is None:
            EBR_recPAE["rec_vlx_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_vlx_tlt"].place(relx=semx, rely=semy, anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#274151'
            fun.rec_redond(EBR_recPAE["rec_vlx_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_vlx_tlt"] is None:
            EBR_txtPAE["txt_vlx_tlt"] = tk.Label(EBR_recPAE["rec_vlx_tlt"], text="Valor expuesto", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_vlx_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_vlx_cop"] is None:
            EBR_recPAE["rec_vlx_cop"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_vlx_cop"].place(relx=(semx+0.145), rely=semy, anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_vlx_cop"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_vlx_cop"] is None:
            EBR_txtPAE["txt_vlx_cop"] = tk.Label(EBR_recPAE["rec_vlx_cop"], text="COP [Millones]", 
                                        font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_vlx_cop"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_vlx_val"] is None:
            EBR_recPAE["rec_vlx_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_vlx_val"].place(relx=(semx+0.29), rely=semy, anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_vlx_val"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_vlx_val"] is None:
            texto = np.around(df_resultados.Col2[0]*1e6,2)
            EBR_txtPAE["txt_vlx_val"] = tk.Label(EBR_recPAE["rec_vlx_val"], text=str(texto), 
                                        font=("Abadi MT", 13), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_vlx_val"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
        # 2). Perdida anual esperada del municipio ----------------------------
        if EBR_recPAE["rec_pae_tlt"] is None:
            EBR_recPAE["rec_pae_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pae_tlt"].place(relx=semx, rely=(semy+0.086), anchor=tk.CENTER, width=181, height=89) 
            x2, y2 = 180, 88
            x1, y1 = 10,10
            radio_esquinas = 4
            color = '#274151'
            fun.rec_redond(EBR_recPAE["rec_pae_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pae_tlt1"] is None:
            EBR_txtPAE["txt_pae_tlt1"] = tk.Label(EBR_recPAE["rec_pae_tlt"], text="Pérdida anual", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_pae_tlt1"].place(relx=0.53, rely=0.43, anchor=tk.CENTER, width=132, height=22)
        if EBR_txtPAE["txt_pae_tlt2"] is None:
            EBR_txtPAE["txt_pae_tlt2"] = tk.Label(EBR_recPAE["rec_pae_tlt"], text="esperada", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_pae_tlt2"].place(relx=0.53, rely=0.63, anchor=tk.CENTER, width=132, height=22)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pae_cop"] is None:
            EBR_recPAE["rec_pae_cop"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pae_cop"].place(relx=(semx+0.145), rely=(semy+0.058), anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_pae_cop"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pae_cop"] is None:
            EBR_txtPAE["txt_pae_cop"] = tk.Label(EBR_recPAE["rec_pae_cop"], text="COP [Millones]", 
                                        font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_pae_cop"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pae_prc"] is None:
            EBR_recPAE["rec_pae_prc"]= tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pae_prc"].place(relx=(semx+0.145), rely=(semy+0.114), anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_pae_prc"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pae_prc"] is None:
            EBR_txtPAE["txt_pae_prc"] = tk.Label(EBR_recPAE["rec_pae_prc"], text="[‰]", 
                                        font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_pae_prc"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pae_val_cop"] is None:
            EBR_recPAE["rec_pae_val_cop"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pae_val_cop"].place(relx=(semx+0.29), rely=(semy+0.058), anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_pae_val_cop"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pae_val_cop"] is None:
            texto = np.around(df_resultados.Col2[1],2)
            EBR_txtPAE["txt_pae_val_cop"] = tk.Label(EBR_recPAE["rec_pae_val_cop"], text=str(texto), 
                                        font=("Abadi MT", 13), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pae_val_cop"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pae_val_val"] is None:
            EBR_recPAE["rec_pae_val_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pae_val_val"].place(relx=(semx+0.29), rely=(semy+0.114), anchor=tk.CENTER, width=181, height=45) 
            x2, y2 = 180, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_pae_val_val"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pae_val_val"] is None:
            texto = np.around(df_resultados.Col2[2],3)
            EBR_txtPAE["txt_pae_val_val"] = tk.Label(EBR_recPAE["rec_pae_val_val"], text=str(texto), 
                                        font=("Abadi MT", 13), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pae_val_val"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
        # 3). Titulos resumen curvas ------------------------------------------
        if EBR_recPAE["rec_pmp_tlt"] is None:
            EBR_recPAE["rec_pmp_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pmp_tlt"].place(relx=(semx+0.145), rely=(semy+0.173), anchor=tk.CENTER, width=544, height=45) 
            x2, y2 = 543, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#274151'
            fun.rec_redond(EBR_recPAE["rec_pmp_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pmp_tlt"] is None:
            EBR_txtPAE["txt_pmp_tlt"] = tk.Label(EBR_recPAE["rec_pmp_tlt"], text="Pérdida máxima probable", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_pmp_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pdr_tlt"] is None:
            EBR_recPAE["rec_pdr_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pdr_tlt"].place(relx=(semx-0.018), rely=(semy+0.247), anchor=tk.CENTER, width=136, height=71) 
            x2, y2 = 135, 70
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#274151'
            fun.rec_redond(EBR_recPAE["rec_pdr_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pdr_tlt1"] is None:
            EBR_txtPAE["txt_pdr_tlt1"] = tk.Label(EBR_recPAE["rec_pdr_tlt"], text="retorno", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_pdr_tlt1"].place(relx=0.53, rely=0.67, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pdr_tlt2"] is None:
            EBR_txtPAE["txt_pdr_tlt2"] = tk.Label(EBR_recPAE["rec_pdr_tlt"], text="Periodo de", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_pdr_tlt2"].place(relx=0.53, rely=0.41, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_exd_tlt"] is None:
            EBR_recPAE["rec_exd_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_exd_tlt"].place(relx=(semx+0.128), rely=(semy+0.247), anchor=tk.CENTER, width=231, height=71) 
            x2, y2 = 230, 70
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#274151'
            fun.rec_redond(EBR_recPAE["rec_exd_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_exd_tlt1"] is None:
            EBR_txtPAE["txt_exd_tlt1"] = tk.Label(EBR_recPAE["rec_exd_tlt"], text="excedencia en 50 años", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_exd_tlt1"].place(relx=0.53, rely=0.7, anchor=tk.CENTER)
        if EBR_txtPAE["txt_exd_tlt2"] is None:
            EBR_txtPAE["txt_exd_tlt2"] = tk.Label(EBR_recPAE["rec_exd_tlt"], text="Probabilidad de", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_exd_tlt2"].place(relx=0.53, rely=0.40, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pe_tlt"] is None:
            EBR_recPAE["rec_pe_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pe_tlt"].place(relx=(semx+0.292), rely=(semy+0.247), anchor=tk.CENTER, width=176, height=71) 
            x2, y2 = 175, 70
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#274151'
            fun.rec_redond(EBR_recPAE["rec_pe_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pe_tlt"] is None:
            EBR_txtPAE["txt_pe_tlt"] = tk.Label(EBR_recPAE["rec_pe_tlt"], text="Pérdida esperada", 
                                        font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
            EBR_txtPAE["txt_pe_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # 4). subtitulos resumen PAE ------------------------------------------
        if EBR_recPAE["rec_pdran_tlt"] is None:
            EBR_recPAE["rec_pdran_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pdran_tlt"].place(relx=(semx-0.018), rely=(semy+0.322), anchor=tk.CENTER, width=136, height=45) 
            x2, y2 = 135, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_pdran_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pdran_tlt"] is None:
            EBR_txtPAE["txt_pdran_tlt"] = tk.Label(EBR_recPAE["rec_pdran_tlt"], text="[años]", 
                                        font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_pdran_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_exdprd_tlt"] is None:
            EBR_recPAE["rec_exdprd_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_exdprd_tlt"].place(relx=(semx+0.128), rely=(semy+0.322), anchor=tk.CENTER, width=231, height=45) 
            x2, y2 = 230, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_exdprd_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_exdprd_tlt"] is None:
            EBR_txtPAE["txt_exdprd_tlt"] = tk.Label(EBR_recPAE["rec_exdprd_tlt"], text="[%]", 
                                        font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_exdprd_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pecop_tlt"] is None:
            EBR_recPAE["rec_pecop_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pecop_tlt"].place(relx=(semx+0.266), rely=(semy+0.322), anchor=tk.CENTER, width=111, height=45) 
            x2, y2 = 110, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_pecop_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pecop_tlt"] is None:
            EBR_txtPAE["txt_pecop_tlt"] = tk.Label(EBR_recPAE["rec_pecop_tlt"], text="[COP Mll]", 
                                        font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_pecop_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_peprc_tlt"] is None:
            EBR_recPAE["rec_peprc_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_peprc_tlt"].place(relx=(semx+0.337), rely=(semy+0.322), anchor=tk.CENTER, width=61, height=45) 
            x2, y2 = 60, 44
            x1, y1 = 10,10
            radio_esquinas = 3
            color = '#456883'
            fun.rec_redond(EBR_recPAE["rec_peprc_tlt"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_peprc_tlt"] is None:
            EBR_txtPAE["txt_peprc_tlt"] = tk.Label(EBR_recPAE["rec_peprc_tlt"], text="[%]", 
                                        font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
            EBR_txtPAE["txt_peprc_tlt"].place(relx=0.57, rely=0.57, anchor=tk.CENTER)
        # 5). Valores tabla de resumen ----------------------------------------    
        if EBR_recPAE["rec_pdran_val"] is None:
            EBR_recPAE["rec_pdran_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pdran_val"].place(relx=(semx-0.018), rely=(semy+0.423), anchor=tk.CENTER, width=136, height=111) 
            x2, y2 = 135, 110
            x1, y1 = 10,10
            radio_esquinas = 4
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_pdran_val"], x1, y1, x2, y2, radio_esquinas, color)
        if EBR_txtPAE["txt_pdran_val1"] is None:
            EBR_txtPAE["txt_pdran_val1"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="31", 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pdran_val1"].place(relx=0.53, rely=0.22, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pdran_val2"] is None:
            EBR_txtPAE["txt_pdran_val2"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="225", 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pdran_val2"].place(relx=0.53, rely=0.375, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pdran_val3"] is None:
            EBR_txtPAE["txt_pdran_val3"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="475", 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pdran_val3"].place(relx=0.53, rely=0.53, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pdran_val4"] is None:
            EBR_txtPAE["txt_pdran_val4"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="975", 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pdran_val4"].place(relx=0.53, rely=0.685, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pdran_val5"] is None:
            EBR_txtPAE["txt_pdran_val5"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="1475", 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pdran_val5"].place(relx=0.53, rely=0.85, anchor=tk.CENTER)  
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_exdprd_val"] is None:
            EBR_recPAE["rec_exdprd_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_exdprd_val"].place(relx=(semx+0.128), rely=(semy+0.423), anchor=tk.CENTER, width=231, height=111) 
            x2, y2 = 230, 110
            x1, y1 = 10,10
            radio_esquinas = 4
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_exdprd_val"], x1, y1, x2, y2, radio_esquinas, color)                                 
        if EBR_txtPAE["txt_exdprd_val1"] is None:
            text = np.around(Pr50_Val[0],1)
            EBR_txtPAE["txt_exdprd_val1"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_exdprd_val1"].place(relx=0.53, rely=0.22, anchor=tk.CENTER)
        if EBR_txtPAE["txt_exdprd_val2"] is None:
            text = np.around(Pr50_Val[1],1)
            EBR_txtPAE["txt_exdprd_val2"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_exdprd_val2"].place(relx=0.53, rely=0.375, anchor=tk.CENTER)
        if EBR_txtPAE["txt_exdprd_val3"] is None:
            text = np.around(Pr50_Val[2],1)
            EBR_txtPAE["txt_exdprd_val3"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_exdprd_val3"].place(relx=0.53, rely=0.53, anchor=tk.CENTER)
        if EBR_txtPAE["txt_exdprd_val4"] is None:
            text = np.around(Pr50_Val[3],1)
            EBR_txtPAE["txt_exdprd_val4"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_exdprd_val4"].place(relx=0.53, rely=0.685, anchor=tk.CENTER)
        if EBR_txtPAE["txt_exdprd_val5"] is None:
            text = np.around(Pr50_Val[4],1)
            EBR_txtPAE["txt_exdprd_val5"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_exdprd_val5"].place(relx=0.53, rely=0.85, anchor=tk.CENTER) 
        # ---------------------------------------------------------------------
        if EBR_recPAE["rec_pecop_val"] is None:
            EBR_recPAE["rec_pecop_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_pecop_val"].place(relx=(semx+0.266), rely=(semy+0.423), anchor=tk.CENTER, width=111, height=111) 
            x2, y2 = 110, 110
            x1, y1 = 10,10
            radio_esquinas = 4
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_pecop_val"], x1, y1, x2, y2, radio_esquinas, color)                                 
        if EBR_txtPAE["txt_pecop_val1"] is None:
            text = np.around(PE_mill[0],1)
            EBR_txtPAE["txt_pecop_val1"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pecop_val1"].place(relx=0.53, rely=0.22, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pecop_val2"] is None:
            text = np.around(PE_mill[1],1)
            EBR_txtPAE["txt_pecop_val2"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pecop_val2"].place(relx=0.53, rely=0.375, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pecop_val3"] is None:
            text = np.around(PE_mill[2],1)
            EBR_txtPAE["txt_pecop_val3"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pecop_val3"].place(relx=0.53, rely=0.53, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pecop_val4"] is None:
            text = np.around(PE_mill[3],1)
            EBR_txtPAE["txt_pecop_val4"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pecop_val4"].place(relx=0.53, rely=0.685, anchor=tk.CENTER)
        if EBR_txtPAE["txt_pecop_val5"] is None:
            text = np.around(PE_mill[4],1)
            EBR_txtPAE["txt_pecop_val5"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_pecop_val5"].place(relx=0.53, rely=0.85, anchor=tk.CENTER) 
        # --------------------------------------------------------------------- 
        if EBR_recPAE["rec_peprc_val"] is None:   
            EBR_recPAE["rec_peprc_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
            EBR_recPAE["rec_peprc_val"].place(relx=(semx+0.337), rely=(semy+0.423), anchor=tk.CENTER, width=61, height=111) 
            x2, y2 = 60, 110
            x1, y1 = 10,10
            radio_esquinas = 4
            color = '#C6CFD4'
            fun.rec_redond(EBR_recPAE["rec_peprc_val"], x1, y1, x2, y2, radio_esquinas, color) 
        if EBR_txtPAE["txt_peprc_val1"] is None:
            text = np.around((PE_mill[0]/(df_resultados.Col2[0]*1e6))*100,1)
            EBR_txtPAE["txt_peprc_val1"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_peprc_val1"].place(relx=0.55, rely=0.22, anchor=tk.CENTER)
        if EBR_txtPAE["txt_peprc_val2"] is None:
            text = np.around((PE_mill[1]/(df_resultados.Col2[0]*1e6))*100,1)
            EBR_txtPAE["txt_peprc_val2"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_peprc_val2"].place(relx=0.55, rely=0.375, anchor=tk.CENTER)
        if EBR_txtPAE["txt_peprc_val3"] is None:
            text = np.around((PE_mill[2]/(df_resultados.Col2[0]*1e6))*100,1)
            EBR_txtPAE["txt_peprc_val3"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_peprc_val3"].place(relx=0.55, rely=0.53, anchor=tk.CENTER)
        if EBR_txtPAE["txt_peprc_val4"] is None:
            text = np.around((PE_mill[3]/(df_resultados.Col2[0]*1e6))*100,1)
            EBR_txtPAE["txt_peprc_val4"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_peprc_val4"].place(relx=0.55, rely=0.685, anchor=tk.CENTER)
        if EBR_txtPAE["txt_peprc_val5"] is None:
            text = np.around((PE_mill[4]/(df_resultados.Col2[0]*1e6))*100,1)
            EBR_txtPAE["txt_peprc_val5"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
            EBR_txtPAE["txt_peprc_val5"].place(relx=0.55, rely=0.85, anchor=tk.CENTER)

    riskbyevent_label = tk.Label(cnt_container, text="", fg="red")
    riskbyevent_label.pack()                                   
    riskbyevent_label.pack_forget()
def Hide_Loss_EBR():
    for rec in rectg_EBR:
        if EBR_rectg[rec] is not None:
            EBR_rectg[rec].place_forget()
            EBR_rectg[rec] = None
    for btn in boton_EBR:
        if EBR_boton[btn] is not None:
            EBR_boton[btn].place_forget()
            EBR_boton[btn] = None
    for tlt in title_EBR:
        if EBR_title[tlt] is not None:
            EBR_title[tlt].place_forget()
            EBR_title[tlt] = None
    for txt in text_EBR:
        if EBR_text[txt] is not None:
            EBR_text[txt].place_forget()
            EBR_text[txt] = None
    for ent in entry_EBR:
        if EBR_entry[ent] is not None:
            EBR_entry[ent].place_forget()
            EBR_entry[ent] = None
    for lbl in label_EBR:
        if EBR_label[lbl] is not None:
            EBR_label[lbl].place_forget()
            EBR_label[lbl] = None
    for cnv in canva_EBR:
        if EBR_canva[cnv] is not None:
            EBR_canva[cnv].get_tk_widget().destroy()
            EBR_canva[cnv] = None
    for rec in recPAE_EBR:
        if EBR_recPAE[rec] is not None:
            EBR_recPAE[rec].place_forget()
            EBR_recPAE[rec] = None
    for txt in txtPAE_EBR:
        if EBR_txtPAE[txt] is not None:
            EBR_txtPAE[txt].place_forget()
            EBR_txtPAE[txt] = None 
#%% ====== FUNCTION >> LOSS/CLB ===============================================
"""
-------------------------------------------------------------------------------
Procesado perdidas>calibrar
-------------------------------------------------------------------------------
"""
def prueba_aggrisk(resultado_label):
    global CP_Name,opciones,codigomnzs,simmnz_losses,simmnz_losses2,newNsim
    if carpeta_seleccionada is not None:
        # 0). Borrar los graficos anteriores
        if CLB_canva["cnv_cp_CLB"] is not None and CLB_canva["cnv_mnz_CLB"] is not None:
            CLB_canva["cnv_cp_CLB"].get_tk_widget().destroy()
            CLB_canva["cnv_cp_CLB"] = None
            CLB_canva["cnv_mnz_CLB"].get_tk_widget().destroy()
            CLB_canva["cnv_mnz_CLB"] = None
        df_AGR_list, df_AGRmnz_list, Nsim2, datos_CP, datos_events_CP, datos_MNZ, datos_events_MNZ,manzanapred,CP_Name,opciones,codigomnzs,simmnz_losses,simmnz_losses2,newNsim = prs.function_CLB(carpeta_seleccionada)
        # ---------------------------------------------------------------------
        # --- Guardar en esa variable la lista de dataframes por simulacion ---
        # ---------------------------------------------------------------------
        expcsv['exp_AGR_sts'] = df_AGR_list                                     # Centro poblado
        expcsv['exp_AGR_mnz'] = df_AGRmnz_list                                  # Agregate by
        expcsv['Nu_sim'] = Nsim2                                                # Numero de simulaciones
        # ---- Generar grafico ------------------------------------------------
        CLB_canva["cnv_cp_CLB"] = lb.canva_CLB_In(datos_CP, 'Number of simulated events', 'Average annual loss [M$]','',cnt_container,0.28,0.647)
        canva_expo["cnv_Cp_CLB_event"] = lb.canva_events(datos_events_CP, 'Number of events', 'Average annual loss [M$]','',cnt_container,0.28,0.647)
        # ---- Generar grafico ------------------------------------------------
        CLB_canva["cnv_mnz_CLB"] = lb.canva_CLB_In(datos_MNZ, 'Number of simulated events', 'Average annual loss [%]','CodDANE:'+str(manzanapred)[1:],cnt_container,0.73,0.647)
        canva_expo["cnv_Mnz_CLB_event"] = lb.canva_events(datos_events_MNZ, 'Number of events', 'Average annual loss [%]','CodDANE:'+str(manzanapred)[1:],cnt_container,0.73,0.647)
        
        # ---------------------------------------------------------------------
        # --- Cuando se escoge otra ruta de archivos sobre la misma ventana ---
        # ---------------------------------------------------------------------
        
        # ---- Ocultar boton exportar resultados ------------------------------
        if CLB_rectg["rec_exp_CLB"] is not None and CLB_boton["btn_exp_CLB"] is not None and CLB_label["lbl_exp_CLB"] is not None:
            CLB_rectg["rec_exp_CLB"].place_forget()
            CLB_rectg["rec_exp_CLB"] = None
            CLB_boton["btn_exp_CLB"].place_forget()
            CLB_boton["btn_exp_CLB"] = None
            CLB_label["lbl_exp_CLB"].place_forget()
            CLB_label["lbl_exp_CLB"] = None
        # ---- Ocultar titulo graficas ----------------------------------------
        if CLB_title["tlt_cp_CLB"] is not None and CLB_title["tlt_mnz_CLB"] is not None:
            CLB_title["tlt_cp_CLB"].place_forget()
            CLB_title["tlt_cp_CLB"] = None
            CLB_title["tlt_mnz_CLB"].place_forget()
            CLB_title["tlt_mnz_CLB"] = None
        # ---- Ocultar boton seleccionar manzana ------------------------------
        global cmb_Mnz_CLB
        if cmb_Mnz_CLB is not None:
            cmb_Mnz_CLB.place_forget()
            cmb_Mnz_CLB = None
        if CLB_boton["btn_Cmnz_CLB"] is not None and CLB_rectg["rec_Cmnz_CLB"] is not None:
            CLB_boton["btn_Cmnz_CLB"].place_forget()
            CLB_boton["btn_Cmnz_CLB"] = None
            CLB_rectg["rec_Cmnz_CLB"].place_forget()
            CLB_rectg["rec_Cmnz_CLB"] = None
    
        # ---------------------------------------------------------------------
        # --------- Se muestran los elementos de la pestana Calibrar ----------
        # ---------------------------------------------------------------------
        
        Show_Loss_CLB()
        
    else:
        # Si no se encuentra la carpeta, la consola bota:
        resultado_label.config(text="Carpeta no seleccionada") 
        tk.messagebox.showinfo("Select folder", "The folder has not been selected")
        
    return CP_Name,opciones,codigomnzs,simmnz_losses,simmnz_losses2,newNsim
#%% ====== FUNCTION >> LOSS/DSP ===============================================
"""
-------------------------------------------------------------------------------
Procesado perdidas>Dispersion
-------------------------------------------------------------------------------
"""
def dispersion_aggrisk(resultado_labelDSP):
    # -------------------------------------------------------------------------
    # ---------------------- Si se selecciona una carpeta ---------------------
    # -------------------------------------------------------------------------
    if carpeta_seleccionada is not None:
        # 0). Borrar los graficos anteriores
        if DSP_canva["cnv_ses_DSP"] is not None and DSP_canva["cnv_evt_DSP"] is not None:
            DSP_canva["cnv_ses_DSP"].get_tk_widget().destroy()
            DSP_canva["cnv_ses_DSP"] = None
            DSP_canva["cnv_evt_DSP"].get_tk_widget().destroy()
            DSP_canva["cnv_evt_DSP"] = None
        datos,datos_events = prs.function_DSP(carpeta_seleccionada)
        
        # ---- Generar grafico ------------------------------------------------
        DSP_canva["cnv_ses_DSP"] = lb.canva_DSP(datos, 'Number of simulated events', 'Dispersion','',cnt_container,0.28,0.66)
        DSP_canva["cnv_evt_DSP"] = lb.canva_DSP(datos_events, 'Number of events', 'Dispersion','',cnt_container,0.73,0.66)
        
        # ---------------------------------------------------------------------
        # --- Cuando se escoge otra ruta de archivos sobre la misma ventana ---
        # ---------------------------------------------------------------------
        
        # ---- Ocultar boton exportar resultados ------------------------------
        if DSP_rectg["rec_exp_DSP"] is not None and DSP_boton["btn_exp_DSP"] is not None and DSP_label["lbl_exp_DSP"] is not None:
            DSP_rectg["rec_exp_DSP"].place_forget()
            DSP_rectg["rec_exp_DSP"] = None
            DSP_boton["btn_exp_DSP"].place_forget()
            DSP_boton["btn_exp_DSP"] = None
            DSP_label["lbl_exp_DSP"].place_forget()
            DSP_label["lbl_exp_DSP"] = None
        # ---- Ocultar titulo graficas ----------------------------------------
        if DSP_title["tlt_ses_DSP"] is not None and DSP_title["tlt_evt_DSP"] is not None:
            DSP_title["tlt_ses_DSP"].place_forget()
            DSP_title["tlt_ses_DSP"] = None
            DSP_title["tlt_evt_DSP"].place_forget()
            DSP_title["tlt_evt_DSP"] = None

        # ---------------------------------------------------------------------
        # --------- Se muestran los elementos de la pestana Calibrar ----------
        # ---------------------------------------------------------------------
        
        Show_Loss_DSP()
        
    else:
        # Si no se encuentra la carpeta, la consola bota:
        resultado_labelDSP.config(text="Carpeta no seleccionada") 
        tk.messagebox.showinfo("Select folder", "The folder has not been selected")

#%% ====== FUNCTION >> LOSS/EBR ===============================================
"""
-------------------------------------------------------------------------------
Procesado perdidas>Dispersion
-------------------------------------------------------------------------------
"""
def procs_riskbyevent(riskbyevent_label):
    # ---- Variables globales -------------------------------------------------
    if EBR_text["txt_tlt_EBR1"] is not None:
        print('entra')
        EBR_text["txt_tlt_EBR1"].place_forget()
        EBR_text["txt_tlt_EBR1"] = None
    
    
    global archivo_seleccionado, archivo_seleccionado_tax, carpeta_seleccionada
    global valorperiodo
    global df_EBR, valexpuesto,aggsts_loss,PE_mill,df_resultados,Pr50_Val,Table_Resu,CP_Name,Table_Resu_tax,df_expotax,taxo_description,map_data,seccion_shp,area_shpe,COD_mun,ruta_shp
    
    valorperiodo = EBR_entry["ent_per_EBR"].get()                               # Obtener el periodo de analisis ingresado desde la plataforma
    if valorperiodo == '':
        valorperiodo = None                                                     # Cuando no hay nada, se convierte en una variable vacía
    else:
        valorperiodo = int(EBR_entry["ent_per_EBR"].get())                      # Cuando si se ingresó un periodo de análisis
    # -------------------------------------------------------------------------
    # ---------------------- Si se selecciona una carpeta ---------------------
    # -------------------------------------------------------------------------
    if archivo_seleccionado is not None and archivo_seleccionado_tax is not None and carpeta_seleccionada is not None:
        ruta_shp = carpeta_seleccionada
        # ----- Obtener los archivos de la carpeta que se van a procesar ------
        # En la carpeta debe haber un archivo .shp, .shx, .cpg, .dbf, .prj, .qmd para 
        # las manzanas, area y seccion del municipio, además del hdf5 que contiene los 
        # resultados de la corrida

        # Se le debe explicar al usuario qué es lo que debe tener la carpeta que leerá 
        # el programa. Si falta algún dato de los shapes o si hay más de un hdf5 el 
        # programa deberá mandar un mensaje de error o advertencia. 

        # El nombre de los archivos del MGN deben estar como Hector lo sugirió

        fileswork = []
        mnz_shp, mnz_shx, mnz_files = [], [], []
        area_shp, area_shx, area_files = [], [], []
        scc_shp, scc_shx, scc_files = [], [], []
        for archivo in os.listdir(ruta_shp): 
            # Archivos MGN_Manzana:
            # Archivo .shp:
            if "MANZANA" in archivo and archivo.endswith(".shp"):
                mnz_shp.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            else:
                fileswork = None
            # Archivo .shx:
            if "MANZANA" in archivo and archivo.endswith(".shx"):
                mnz_shx.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            else:
                fileswork = None
            # Demás archivos:
            if "MANZANA" in archivo and archivo.endswith(".cpg"):
                mnz_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            if "MANZANA" in archivo and archivo.endswith(".dbf"):
                mnz_files.append(os.path.join(ruta_shp, archivo)) 
                fileswork = 1
            if "MANZANA" in archivo and archivo.endswith(".prj"):
                mnz_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            if "MANZANA" in archivo and archivo.endswith(".qmd"):
                mnz_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            # Archivos MGN_Area:
            # Archivo .shp:
            if "AREA" in archivo and archivo.endswith(".shp"):
                area_shp.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            else:
                fileswork = None   
            # Archivo .shx:
            if "AREA" in archivo and archivo.endswith(".shx"):
                area_shx.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            else:
                fileswork = None 
            # Demas archivos:
            if "AREA" in archivo and archivo.endswith(".cpg"):
                area_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            if "AREA" in archivo and archivo.endswith(".dbf"):
                area_files.append(os.path.join(ruta_shp, archivo)) 
                fileswork = 1
            if "AREA" in archivo and archivo.endswith(".prj"):
                area_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            if "AREA" in archivo and archivo.endswith(".qmd"):
                area_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            # Archivos MGN_Seccion:
            # Archivo .shp:
            if "SECCION" in archivo and archivo.endswith(".shp"):
                scc_shp.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            else:
                fileswork = None 
            # Archivo .shx:
            if "SECCION" in archivo and archivo.endswith(".shx"):
                scc_shx.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            else:
                fileswork = None 
            # Demas archivos:
            if "SECCION" in archivo and archivo.endswith(".cpg"):
                scc_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            if "SECCION" in archivo and archivo.endswith(".dbf"):
                scc_files.append(os.path.join(ruta_shp, archivo)) 
                fileswork = 1
            if "SECCION" in archivo and archivo.endswith(".prj"):
                scc_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1
            if "SECCION" in archivo and archivo.endswith(".qmd"):
                scc_files.append(os.path.join(ruta_shp, archivo))
                fileswork = 1

        Files_List = [mnz_shp,mnz_shx,area_shp,area_shx,scc_shp,scc_shx]
        FilesMGN_List = [mnz_files,area_files,scc_files]
        Text_List = ['MANZANA.shp','MANZANA.shx','AREA.shp','AREA.shx','SECCION.shp','SECCION.shx']
        TextMGN_List = ['MANZANA','AREA','SECCION']
        for index, file in enumerate(Files_List):
            if len(file) > 1:
                fileswork = None
                warning = 'En la carpeta seleccionada hay más de un archivo ' + Text_List[index]
                tk.messagebox.showinfo("File error", warning)
            elif file is None:
                warning = 'En la carpeta seleccionada no existe el archivo ' + Text_List[index]
                tk.messagebox.showinfo("File error", warning)
                fileswork = None
            else:
                fileswork = 1
        for index, file in enumerate(FilesMGN_List):
            if len(file) < 4:
                fileswork = None
                warning = 'En la carpeta seleccionada no se encuentran todos los archivos del shape para MGN_' + TextMGN_List[index]
                tk.messagebox.showinfo("File error", warning)
            elif len(file) > 4:
                fileswork = None
                warning = 'En la carpeta seleccionada hay mas de un archivo MGN_' + TextMGN_List[index]
                tk.messagebox.showinfo("File error", warning)
            else:
                fileswork = 1
                
        if fileswork is not None:
            # 0). Borrar los graficos anteriores
            if EBR_canva["cnv_crv_EBR"] is not None:
                EBR_canva["cnv_crv_EBR"].get_tk_widget().destroy()
                EBR_canva["cnv_crv_EBR"] = None
                
            df_EBR, valexpuesto,aggsts_loss,PE_mill,df_resultados,Pr50_Val,CP_Name,df_expotax,taxo_description,map_data,seccion_shp,area_shpe,COD_mun,ruta_shp = prs.function_EBR(archivo_seleccionado,archivo_seleccionado_tax,carpeta_seleccionada,valorperiodo)
            EBR_canva["cnv_crv_EBR"] = lb.canva_crv_EBR(df_EBR, valexpuesto, valorperiodo, 'Pérdida anual [% Valor expuesto]', 'Tasa de Excedencia [1/año] ', '', cnt_container, 0.26, 0.70)
            Table_Resu = lb.gen_tabla(valexpuesto*1e6,aggsts_loss[0],PE_mill)
            Table_Resu_tax = lb.gen_tabla_tax(df_expotax,taxo_description)
            
            # ---------------------------------------------------------------------
            # --- Cuando se escoge otra ruta de archivos sobre la misma ventana ---
            # ---------------------------------------------------------------------
            
            # ---- Ocultar boton exportar resultados ------------------------------
            if EBR_rectg["rec_exp_EBR"] is not None and EBR_boton["btn_exp_EBR"]is not None and EBR_label["lbl_exp_EBR"] is not None:
                EBR_rectg["rec_exp_EBR"].place_forget()
                EBR_rectg["rec_exp_EBR"] = None
                EBR_boton["btn_exp_EBR"].place_forget()
                EBR_boton["btn_exp_EBR"] = None
                EBR_label["lbl_exp_EBR"].place_forget()
                EBR_label["lbl_exp_EBR"] = None
            # ---- Ocultar titulo graficas ----------------------------------------
            if EBR_text["txt_crv_EBR"] is not None:
                EBR_text["txt_crv_EBR"].place_forget()
                EBR_text["txt_crv_EBR"] = None
            # ---- Ocultar tabla de resumen --------------------------------------- 
            for rec in recPAE_EBR:
                if EBR_recPAE[rec] is not None:
                    EBR_recPAE[rec].place_forget()
                    EBR_recPAE[rec] = None 
            for rec in txtPAE_EBR:
                if EBR_txtPAE[rec] is not None:
                    EBR_txtPAE[rec].place_forget()
                    EBR_txtPAE[rec] = None
                
            # ---------------------------------------------------------------------
            # --------- Se muestran los elementos de la pestana Calibrar ----------
            # ---------------------------------------------------------------------
            
            Show_Loss_EBR()
        else:
            tk.messagebox.showinfo("Select file", "Los archivos requeridos no fueron seleccionados 2")
    else:
        # Si no se encuentra la carpeta, la consola bota:
        riskbyevent_label.config(text="Carpeta no seleccionada")
        tk.messagebox.showinfo("Select file", "Los archivos requeridos no fueron seleccionados")
        
    return df_EBR, valexpuesto,aggsts_loss,PE_mill,df_resultados,Pr50_Val,Table_Resu,CP_Name,Table_Resu_tax

def results_taxonomy_EBR():
    Hide_Loss_EBR()
    EBR_canva["cnv_map_COP"] = None
    EBR_recPAE["rec_representacion"] = None
    EBR_txtPAE["txt_representacion1"] = None
    EBR_boton["btn_representacion"] = None
    if EBR_canva["cnv_EBR_taxo"] is not None:
        EBR_canva["cnv_EBR_taxo"].get_tk_widget().destroy()
        EBR_canva["cnv_EBR_taxo"] = None
    
    # --- Elegir Loss/Calibration ---------------------------------------------
    if EBR_rectg["rec_slc_EBR"] is None:
        EBR_rectg["rec_slc_EBR"] = tk.Canvas(navigation_bar, bg="#37586B", bd=0, highlightthickness=0)
        EBR_rectg["rec_slc_EBR"].place(relx=0.67, rely=0.39, anchor=tk.CENTER, width=231, height=51)
        x2, y2 = 230, 50
        x1, y1 = 10,10
        radio_esquinas = 18
        color = "white"
        fun.rec_redond(EBR_rectg["rec_slc_EBR"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_boton["btn_slc_EBR"] is None:
        EBR_boton["btn_slc_EBR"] = tk.Button(EBR_rectg["rec_slc_EBR"], text="Event Based Risk", font=("Abadi MT", 13), 
                                      bd=0, bg="white", fg="#37586B", relief=tk.FLAT, command=Show_Loss_EBR, padx=2)
        EBR_boton["btn_slc_EBR"].place(relx=0.70, rely=0.59, anchor="e") 
    # --- Titulo de la pagina -------------------------------------------------
    if EBR_title["tlt_tlt_EBR"] is None:
        EBR_title["tlt_tlt_EBR"] = tk.Label(cnt_container, text="Resultados de Riesgo Basado en Eventos", 
                         font=("Abadi MT", 30), bg="white", fg="#274151")
        EBR_title["tlt_tlt_EBR"].place(relx=0.318, rely=0.09, anchor=tk.CENTER)
    if EBR_text["txt_tlt_EBR1"] is None:
        EBR_text["txt_tlt_EBR1"] = tk.Label(cnt_container, text="Pérdida anual esperada agregada por tipología constructiva.", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR1"].place(relx=0.244, rely=0.16, anchor=tk.CENTER)
    # ---- Boton exportar resultados --------------------------------------
    if EBR_rectg["rec_exp_EBR"] is None:
        EBR_rectg["rec_exp_EBR"] = tk.Canvas(cnt_container, bg="#B97F73", bd=0, highlightthickness=0)
        EBR_rectg["rec_exp_EBR"].place(relx=0.09, rely=0.965, anchor=tk.CENTER, width=180, height=33) 
    if EBR_boton["btn_exp_EBR"] is None:
        EBR_boton["btn_exp_EBR"] = tk.Button(EBR_rectg["rec_exp_EBR"], text="Exportar resultados", font=("Abadi MT", 13), bd=0, bg="#B97F73", fg="white", relief=tk.FLAT, command=lambda: lb.Exportar_Perdidas_RiskByevent(EBR_canva["cnv_crv_EBR"],Table_Resu,Table_Resu_tax))
        EBR_boton["btn_exp_EBR"].place(relx=0.55, rely=0.5, anchor=tk.CENTER, width=140, height=40)
    if EBR_label["lbl_exp_EBR"] is None:
        img_exp = Image.open(os.path.join(os.getcwd(),"icon") + '/exportar.png')
        img_exp = img_exp.resize((18, 16), Image.LANCZOS)
        img_exp = ImageTk.PhotoImage(img_exp)
        EBR_label["lbl_exp_EBR"] = tk.Label(EBR_rectg["rec_exp_EBR"], image=img_exp, bd=0, bg="#B97F73")
        EBR_label["lbl_exp_EBR"].image = img_exp
        EBR_label["lbl_exp_EBR"].place(relx=0.09, rely=0.5, anchor=tk.CENTER)

    # ---- Tabla taxonomia ----------------------------------------------------
    rlx = 0.15
    rly = 0.35
    # 1). Tipologia constructiva ----------------------------------------------
    EBR_recPAE["rec_tip_tlt"] = None
    EBR_txtPAE["txt_tip_tlt"] = None
    if EBR_recPAE["rec_tip_tlt"] is None:
        EBR_recPAE["rec_tip_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_tip_tlt"].place(relx=rlx+0.0725, rely=rly-0.13, anchor=tk.CENTER, width=461, height=45) 
        x2, y2 = 460, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_tip_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_tip_tlt"] is None:
        EBR_txtPAE["txt_tip_tlt"] = tk.Label(EBR_recPAE["rec_tip_tlt"], text="Tipología constructiva", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_tip_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 1.1). Descripcion --------------------------------------------------
    EBR_recPAE["rec_dsc_tlt"] = None
    EBR_txtPAE["txt_dsc_tlt"] = None
    if EBR_recPAE["rec_dsc_tlt"] is None:
        EBR_recPAE["rec_dsc_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_dsc_tlt"].place(relx=rlx, rely=rly-0.07, anchor=tk.CENTER, width=280, height=45) 
        x2, y2 = 279, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_dsc_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_dsc_tlt"] is None:
        EBR_txtPAE["txt_dsc_tlt"] = tk.Label(EBR_recPAE["rec_dsc_tlt"], text="Descripción", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_dsc_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 1.2). Tipologia --------------------------------------------------
    EBR_recPAE["rec_dtip_tlt"] = None
    EBR_txtPAE["txt_dtip_tlt"] = None
    if EBR_recPAE["rec_dtip_tlt"] is None:
        EBR_recPAE["rec_dtip_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_dtip_tlt"].place(relx=rlx+0.185, rely=rly-0.07, anchor=tk.CENTER, width=180, height=45) 
        x2, y2 = 179, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_dtip_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_dtip_tlt"] is None:
        EBR_txtPAE["txt_dtip_tlt"] = tk.Label(EBR_recPAE["rec_dtip_tlt"], text="Taxonomía", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_dtip_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 2). Valor expuesto ------------------------------------------------------
    EBR_recPAE["rec_valex_tlt"] = None
    EBR_txtPAE["txt_valex_tlt"] = None
    if EBR_recPAE["rec_valex_tlt"] is None:
        EBR_recPAE["rec_valex_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_valex_tlt"].place(relx=rlx+0.374, rely=rly-0.13, anchor=tk.CENTER, width=290, height=45) 
        x2, y2 = 289, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_valex_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_valex_tlt"] is None:
        EBR_txtPAE["txt_valex_tlt"] = tk.Label(EBR_recPAE["rec_valex_tlt"], text="Valor expuesto", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_valex_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 2.1). Valor expuesto en COP ---------------------------------------------
    EBR_recPAE["rec_valexCOP_tlt"] = None
    EBR_txtPAE["txt_valexCOP_tlt"] = None
    if EBR_recPAE["rec_valexCOP_tlt"] is None:
        EBR_recPAE["rec_valexCOP_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_valexCOP_tlt"].place(relx=rlx+0.33, rely=rly-0.07, anchor=tk.CENTER, width=180, height=45) 
        x2, y2 = 179, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_valexCOP_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_valexCOP_tlt"] is None:
        EBR_txtPAE["txt_valexCOP_tlt"] = tk.Label(EBR_recPAE["rec_valexCOP_tlt"], text="[COP Millones]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_valexCOP_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 2.1). Valor expuesto en % ---------------------------------------------
    EBR_recPAE["rec_valexPRC_tlt"] = None
    EBR_txtPAE["txt_valexPRC_tlt"] = None
    if EBR_recPAE["rec_valexPRC_tlt"] is None:
        EBR_recPAE["rec_valexPRC_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_valexPRC_tlt"].place(relx=rlx+0.446, rely=rly-0.07, anchor=tk.CENTER, width=110, height=45) 
        x2, y2 = 109, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_valexPRC_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_valexPRC_tlt"] is None:
        EBR_txtPAE["txt_valexPRC_tlt"] = tk.Label(EBR_recPAE["rec_valexPRC_tlt"], text="[%]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_valexPRC_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 3). Perdida anual esperada ----------------------------------------------
    EBR_recPAE["rec_PAEtxn_tlt"] = None
    EBR_txtPAE["txt_PAEtxn_tlt"] = None
    if EBR_recPAE["rec_PAEtxn_tlt"] is None:
        EBR_recPAE["rec_PAEtxn_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_PAEtxn_tlt"].place(relx=rlx+0.649, rely=rly-0.13, anchor=tk.CENTER, width=401, height=45) 
        x2, y2 = 400, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_PAEtxn_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_PAEtxn_tlt"] is None:
        EBR_txtPAE["txt_PAEtxn_tlt"] = tk.Label(EBR_recPAE["rec_PAEtxn_tlt"], text="Pérdida anual esperada", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_PAEtxn_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 3.1). Perdida anual esperada --------------------------------------------
    EBR_recPAE["rec_paeCOP_tlt"] = None
    EBR_txtPAE["txt_paeCOP_tlt"] = None
    if EBR_recPAE["rec_paeCOP_tlt"] is None:
        EBR_recPAE["rec_paeCOP_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_paeCOP_tlt"].place(relx=rlx+0.562, rely=rly-0.07, anchor=tk.CENTER, width=180, height=45) 
        x2, y2 = 179, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_paeCOP_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_paeCOP_tlt"] is None:
        EBR_txtPAE["txt_paeCOP_tlt"] = tk.Label(EBR_recPAE["rec_paeCOP_tlt"], text="[COP Millones]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_paeCOP_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 3.1). Perdida anual esperada en % ---------------------------------------
    EBR_recPAE["rec_paePRC_tlt"] = None
    EBR_txtPAE["txt_paePRC_tlt"] = None
    if EBR_recPAE["rec_paePRC_tlt"] is None:
        EBR_recPAE["rec_paePRC_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_paePRC_tlt"].place(relx=rlx+0.678, rely=rly-0.07, anchor=tk.CENTER, width=110, height=45) 
        x2, y2 = 109, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_paePRC_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_paePRC_tlt"] is None:
        EBR_txtPAE["txt_paePRC_tlt"] = tk.Label(EBR_recPAE["rec_paePRC_tlt"], text="[%]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_paePRC_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 3.1). Perdida anual esperada en %. --------------------------------------
    EBR_recPAE["rec_paePMLL_tlt"] = None
    EBR_txtPAE["txt_paePMLL_tlt"] = None
    if EBR_recPAE["rec_paePMLL_tlt"] is None:
        EBR_recPAE["rec_paePMLL_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_paePMLL_tlt"].place(relx=rlx+0.766, rely=rly-0.07, anchor=tk.CENTER, width=110, height=45) 
        x2, y2 = 109, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_paePMLL_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_paePMLL_tlt"] is None:
        EBR_txtPAE["txt_paePMLL_tlt"] = tk.Label(EBR_recPAE["rec_paePMLL_tlt"], text="[‰]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_paePMLL_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    
    
    txtPAE_EBR_tax, recPAE_EBR_tax, recPAE_EBR_tip, txtPAE_EBR_tip = [],[],[],[]
    txtPAE_EBR_vlx_cop, recPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc, recPAE_EBR_vlx_prc = [], [],[], []
    txtPAE_EBR_pae_cop, recPAE_EBR_pae_cop, txtPAE_EBR_pae_prc, recPAE_EBR_pae_prc = [], [], [], []
    txtPAE_EBR_pae_pmll, recPAE_EBR_pae_pmll = [], []
    for tax in range(len(df_expotax.taxonomy)):
        txtPAE_EBR_tax.append("txt_dsc_EBRtxn"+str(tax+1))
        recPAE_EBR_tax.append("rec_dsc_EBRtxn"+str(tax+1))
        txtPAE_EBR_tip.append("txt_tip_EBRtxn"+str(tax+1))
        recPAE_EBR_tip.append("rec_tip_EBRtxn"+str(tax+1))
        txtPAE_EBR_vlx_cop.append("txt_vlxCop_EBRtxn"+str(tax+1))
        recPAE_EBR_vlx_cop.append("rec_vlxCop_EBRtxn"+str(tax+1))
        txtPAE_EBR_vlx_prc.append("txt_vlxPrc_EBRtxn"+str(tax+1))
        recPAE_EBR_vlx_prc.append("rec_vlxPrc_EBRtxn"+str(tax+1))
        txtPAE_EBR_pae_cop.append("txt_paeCop_EBRtxn"+str(tax+1))
        recPAE_EBR_pae_cop.append("rec_paeCop_EBRtxn"+str(tax+1))
        txtPAE_EBR_pae_prc.append("txt_paePRC_EBRtxn"+str(tax+1))
        recPAE_EBR_pae_prc.append("rec_paePRC_EBRtxn"+str(tax+1))
        txtPAE_EBR_pae_pmll.append("txt_paePmll_EBRtxn"+str(tax+1))
        recPAE_EBR_pae_pmll.append("rec_paePmll_EBRtxn"+str(tax+1))
        
    EBR_tax_txtPAE = {}
    for txt in txtPAE_EBR_tax:
        EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_tip:
        EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_vlx_cop:
        EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_vlx_prc:
        EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_pae_cop:
        EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_pae_prc:
        EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_pae_pmll:
        EBR_tax_txtPAE[txt] = None
    
    
    EBR_tax_recPAE = {}
    for rec in recPAE_EBR_tax:
        EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_tip:
        EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_vlx_cop:
        EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_vlx_prc:
        EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_pae_cop:
        EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_pae_prc:
        EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_pae_pmll:
        EBR_tax_recPAE[rec] = None
        
        
    suma_indx = []
    for index,txt in enumerate(txtPAE_EBR_tax):
        parte = taxo_description[index].split(' ') 
        suma_indx.append(len(parte))
        if len(parte) >= 5:
            EBR_tax_txtPAE["txt_dsc_EBRtxn_0"+str(index+1)] = None
    
    sumydef = []
    for index in range(len(suma_indx)-1):
        if suma_indx[index] >=5 and suma_indx[index+1] >=5:
            sumydef.append(0.0745)
        if suma_indx[index] >=5 and suma_indx[index+1] <5:
            sumydef.append(0.065)
        if suma_indx[index] <5 and suma_indx[index+1] <5:
            sumydef.append(0.052)
        if suma_indx[index] <5 and suma_indx[index+1] >=5:
            sumydef.append(0.065)
    sumydef.append(0.065)
    
    suma = 0
    for index in range(len(txtPAE_EBR_tax)):
        parte = taxo_description[index].split(' ')
        if len(parte) >= 5:
            # -------- Descripcion tipologia ----------------------------------
            if EBR_tax_recPAE[recPAE_EBR_tax[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_tax[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_tax[index]].place(relx=rlx, rely=(rly+suma), anchor=tk.CENTER, width=280, height=58) 
                x2, y2 = 279, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_tax[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_tax[index]] is None:
                texto_description = parte[0]+' '+parte[1]+' '+parte[2]+' '+parte[3]
                EBR_tax_txtPAE[txtPAE_EBR_tax[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_tax[index]], text=texto_description, 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_tax[index]].place(relx=0.52, rely=0.39, anchor=tk.CENTER)
            
            texto_description2 = []
            sumaprt = ''
            for index2 in range(4,len(parte)):
                sumaprt = sumaprt + ' ' + parte[index2]
                texto_description2.append(sumaprt)

            if EBR_tax_txtPAE["txt_dsc_EBRtxn_0"+str(index+1)] is None:
                EBR_tax_txtPAE["txt_dsc_EBRtxn_0"+str(index+1)] = tk.Label(EBR_tax_recPAE[recPAE_EBR_tax[index]], text=texto_description2[-1], 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE["txt_dsc_EBRtxn_0"+str(index+1)].place(relx=0.52, rely=0.70, anchor=tk.CENTER)
            
            # -------- Tipologia ----------------------------------------------
            if EBR_tax_recPAE[recPAE_EBR_tip[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_tip[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_tip[index]].place(relx=rlx+0.185, rely=(rly+suma), anchor=tk.CENTER, width=180, height=58) 
                x2, y2 = 179, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_tip[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_tip[index]] is None:
                texto_tipologia = df_expotax.taxonomy[index]
                EBR_tax_txtPAE[txtPAE_EBR_tip[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_tip[index]], text=texto_tipologia, 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_tip[index]].place(relx=0.52, rely=0.59, anchor=tk.CENTER)
            
            # -------- Valor expuesto en COP ----------------------------------
            if EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]].place(relx=rlx+0.33, rely=(rly+suma), anchor=tk.CENTER, width=180, height=58) 
                x2, y2 = 179, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_vlx_cop[index]] is None:
                valex_Cop = np.around(df_expotax.valex[index],3)
                EBR_tax_txtPAE[txtPAE_EBR_vlx_cop[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]], text=str(valex_Cop), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_vlx_cop[index]].place(relx=0.52, rely=0.59, anchor=tk.CENTER)
            
            # -------- Valor expuesto en % ------------------------------------
            if EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]].place(relx=rlx+0.446, rely=(rly+suma), anchor=tk.CENTER, width=110, height=58) 
                x2, y2 = 109, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_vlx_prc[index]] is None:
                valex_Prc = np.around((df_expotax.valex[index]/np.sum(df_expotax.valex))*100,3)
                EBR_tax_txtPAE[txtPAE_EBR_vlx_prc[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]], text=str(valex_Prc), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_vlx_prc[index]].place(relx=0.52, rely=0.59, anchor=tk.CENTER)
            
            # -------- Perdida anual esperada en COP --------------------------
            if EBR_tax_recPAE[recPAE_EBR_pae_cop[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_pae_cop[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_pae_cop[index]].place(relx=rlx+0.562, rely=(rly+suma), anchor=tk.CENTER, width=180, height=58) 
                x2, y2 = 179, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_pae_cop[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_pae_cop[index]] is None:
                valex_Cop = np.around(df_expotax.loss[index],3)
                EBR_tax_txtPAE[txtPAE_EBR_pae_cop[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_pae_cop[index]], text=str(valex_Cop), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_pae_cop[index]].place(relx=0.52, rely=0.59, anchor=tk.CENTER)
            
            # -------- Perdida anual esperada en % ----------------------------
            if EBR_tax_recPAE[recPAE_EBR_pae_prc[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_pae_prc[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_pae_prc[index]].place(relx=rlx+0.678, rely=(rly+suma), anchor=tk.CENTER, width=110, height=58) 
                x2, y2 = 109, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_pae_prc[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_pae_prc[index]] is None:
                valex_Prc = np.around((df_expotax.loss[index]/df_expotax.valex[index])*100,3)
                EBR_tax_txtPAE[txtPAE_EBR_pae_prc[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_pae_prc[index]], text=str(valex_Prc), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_pae_prc[index]].place(relx=0.52, rely=0.59, anchor=tk.CENTER)
            
            # -------- Perdida anual esperada en %. ---------------------------
            if EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]].place(relx=rlx+0.766, rely=(rly+suma), anchor=tk.CENTER, width=110, height=58) 
                x2, y2 = 109, 57
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_pae_pmll[index]] is None:
                valex_Pmll = np.around((df_expotax.loss[index]/df_expotax.valex[index])*1000,3)
                EBR_tax_txtPAE[txtPAE_EBR_pae_pmll[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]], text=str(valex_Pmll), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_pae_pmll[index]].place(relx=0.52, rely=0.59, anchor=tk.CENTER)
                
            suma = suma + sumydef[index]
        else:
            # -------- Descripcion tipologia ----------------------------------           
            if EBR_tax_recPAE[recPAE_EBR_tax[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_tax[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_tax[index]].place(relx=rlx, rely=(rly+suma), anchor=tk.CENTER, width=280, height=40) 
                x2, y2 = 279, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_tax[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_tax[index]] is None:
                EBR_tax_txtPAE[txtPAE_EBR_tax[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_tax[index]], text=taxo_description[index], 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_tax[index]].place(relx=0.52, rely=0.60, anchor=tk.CENTER)
            # -------- Tipologia ----------------------------------------------
            if EBR_tax_recPAE[recPAE_EBR_tip[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_tip[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_tip[index]].place(relx=rlx+0.185, rely=(rly+suma), anchor=tk.CENTER, width=180, height=40) 
                x2, y2 = 179, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_tip[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_tip[index]] is None:
                texto_tipologia = df_expotax.taxonomy[index]
                EBR_tax_txtPAE[txtPAE_EBR_tip[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_tip[index]], text=texto_tipologia, 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_tip[index]].place(relx=0.52, rely=0.63, anchor=tk.CENTER)
            # -------- Valor expuesto en COP ----------------------------------
            if EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]].place(relx=rlx+0.33, rely=(rly+suma), anchor=tk.CENTER, width=180, height=40) 
                x2, y2 = 179, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_vlx_cop[index]] is None:
                valex_Cop = np.around(df_expotax.valex[index],3)
                EBR_tax_txtPAE[txtPAE_EBR_vlx_cop[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_vlx_cop[index]], text=str(valex_Cop), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_vlx_cop[index]].place(relx=0.52, rely=0.63, anchor=tk.CENTER)
            # -------- Valor expuesto en % ----------------------------------
            if EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]].place(relx=rlx+0.446, rely=(rly+suma), anchor=tk.CENTER, width=110, height=40) 
                x2, y2 = 109, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_vlx_prc[index]] is None:
                valex_Prc = np.around((df_expotax.valex[index]/np.sum(df_expotax.valex))*100,3)
                EBR_tax_txtPAE[txtPAE_EBR_vlx_prc[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_vlx_prc[index]], text=str(valex_Prc), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_vlx_prc[index]].place(relx=0.52, rely=0.63, anchor=tk.CENTER)
            # -------- Perdida anual esperada en COP --------------------------
            if EBR_tax_recPAE[recPAE_EBR_pae_cop[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_pae_cop[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_pae_cop[index]].place(relx=rlx+0.562, rely=(rly+suma), anchor=tk.CENTER, width=180, height=40) 
                x2, y2 = 179, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_pae_cop[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_pae_cop[index]] is None:
                valex_Cop = np.around(df_expotax.loss[index],3)
                EBR_tax_txtPAE[txtPAE_EBR_pae_cop[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_pae_cop[index]], text=str(valex_Cop), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_pae_cop[index]].place(relx=0.52, rely=0.63, anchor=tk.CENTER)
            # -------- Perdida anual esperada en % ----------------------------
            if EBR_tax_recPAE[recPAE_EBR_pae_prc[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_pae_prc[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_pae_prc[index]].place(relx=rlx+0.678, rely=(rly+suma), anchor=tk.CENTER, width=110, height=40) 
                x2, y2 = 109, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_pae_prc[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_pae_prc[index]] is None:
                valex_Prc = np.around((df_expotax.loss[index]/df_expotax.valex[index])*100,3)
                EBR_tax_txtPAE[txtPAE_EBR_pae_prc[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_pae_prc[index]], text=str(valex_Prc), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_pae_prc[index]].place(relx=0.52, rely=0.63, anchor=tk.CENTER)
            # -------- Perdida anual esperada en %. ---------------------------
            if EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]] is None:
                EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
                EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]].place(relx=rlx+0.766, rely=(rly+suma), anchor=tk.CENTER, width=110, height=40) 
                x2, y2 = 109, 39
                x1, y1 = 10,10
                radio_esquinas = 4
                color = '#C6CFD4'
                fun.rec_redond(EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]], x1, y1, x2, y2, radio_esquinas, color)
            if EBR_tax_txtPAE[txtPAE_EBR_pae_pmll[index]] is None:
                valex_Pmll = np.around((df_expotax.loss[index]/df_expotax.valex[index])*1000,3)
                EBR_tax_txtPAE[txtPAE_EBR_pae_pmll[index]] = tk.Label(EBR_tax_recPAE[recPAE_EBR_pae_pmll[index]], text=str(valex_Pmll), 
                                        font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
                EBR_tax_txtPAE[txtPAE_EBR_pae_pmll[index]].place(relx=0.52, rely=0.63, anchor=tk.CENTER)
            suma = suma + sumydef[index]
            
    # ---- Representacion grafica de los resultados ---------------------------
    EBR_recPAE["rec_representacion"] = None
    EBR_txtPAE["txt_representacion1"] = None
    EBR_boton["btn_representacion"] = None
    if EBR_recPAE["rec_representacion"] is None:
        EBR_recPAE["rec_representacion"] = tk.Canvas(cnt_container, bg="#274151", bd=0, highlightthickness=0)
        EBR_recPAE["rec_representacion"].place(relx=0.5, rely=0.9, anchor=tk.CENTER, width=200, height=47) 
    if EBR_boton["btn_representacion"] is None:
        EBR_boton["btn_representacion"] = tk.Button(EBR_recPAE["rec_representacion"], text="Representación gráfica", 
                                    font=("Abadi MT", 13), bd=0, bg="#274151", fg="white", relief=tk.FLAT, command=lambda: results_taxonomy_Diagram_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll))
        EBR_boton["btn_representacion"].place(relx=0.50, rely=0.26, anchor=tk.CENTER)
    if EBR_txtPAE["txt_representacion1"] is None:
        EBR_txtPAE["txt_representacion1"] = tk.Label(EBR_recPAE["rec_representacion"], text="de los resultados", 
                                    font=("Abadi MT", 13), bg='#274151', fg='white')
        EBR_txtPAE["txt_representacion1"].place(relx=0.50, rely=0.71, anchor=tk.CENTER)
    
    # ---- Boton mas resultados -------------------------------------------
    if EBR_rectg["rec_mas_EBR1"] is None:
        EBR_rectg["rec_mas_EBR1"] = tk.Canvas(cnt_container, bg="#659B7D", bd=0, highlightthickness=0)
        EBR_rectg["rec_mas_EBR1"].place(relx=0.889, rely=0.965, anchor=tk.CENTER, width=130, height=29) 
    if EBR_boton["btn_mas_EBR1"] is None:
        EBR_boton["btn_mas_EBR1"] = tk.Button(EBR_rectg["rec_mas_EBR1"], text="Siguiente >>", font=("Abadi MT", 13), bd=0, bg="#659B7D", fg="white", relief=tk.FLAT, command=lambda: results_Maps_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll))
        EBR_boton["btn_mas_EBR1"].place(relx=0.55, rely=0.5, anchor=tk.CENTER, width=140, height=40)
        
    # ---- Boton atras --------------------------------------------------------
    
    EBR_rectg["rec_menos_EBR1"] = None
    EBR_boton["btn_menos_EBR1"] = None
    
    if EBR_rectg["rec_menos_EBR1"] is None:
        EBR_rectg["rec_menos_EBR1"] = tk.Canvas(cnt_container, bg="#659B7D", bd=0, highlightthickness=0)
        EBR_rectg["rec_menos_EBR1"].place(relx=0.76, rely=0.965, anchor=tk.CENTER, width=130, height=29) 
    if EBR_boton["btn_menos_EBR1"] is None:
        EBR_boton["btn_menos_EBR1"] = tk.Button(EBR_rectg["rec_menos_EBR1"], text="<< Atrás", font=("Abadi MT", 13), bd=0, bg="#659B7D", fg="white", relief=tk.FLAT, command=lambda: results_curvexce_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll))
        EBR_boton["btn_menos_EBR1"].place(relx=0.45, rely=0.5, anchor=tk.CENTER, width=140, height=40)
    
def results_curvexce_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll):
    hide_results_taxonomy_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll)
    EBR_canva["cnv_map_COP"] = None

    if EBR_text["txt_tlt_EBR1"] is not None:
        print('entra')
        EBR_text["txt_tlt_EBR1"].place_forget()
        EBR_text["txt_tlt_EBR1"] = None
    
    if EBR_recPAE["rec_representacion"] is not None and EBR_txtPAE["txt_representacion1"] is not None and EBR_boton["btn_representacion"] is not None:
        EBR_recPAE["rec_representacion"].place_forget()
        EBR_recPAE["rec_representacion"] = None
        EBR_txtPAE["txt_representacion1"].place_forget()
        EBR_txtPAE["txt_representacion1"] = None
        EBR_boton["btn_representacion"].place_forget()
        EBR_boton["btn_representacion"] = None
        
    EBR_canva["cnv_EBR_taxo"] = None
    if EBR_text["txt_tlt_EBR1"] is not None:
        EBR_text["txt_tlt_EBR1"].place_forget()
        EBR_text["txt_tlt_EBR1"] = None
    
    if EBR_rectg["rec_mas_EBR1"] is not None:
        EBR_rectg["rec_mas_EBR1"].place_forget()
        EBR_rectg["rec_mas_EBR1"] = None
    if EBR_boton["btn_mas_EBR1"] is not None:
        EBR_boton["btn_mas_EBR1"].place_forget()
        EBR_boton["btn_mas_EBR1"] = None
    if EBR_rectg["rec_menos_EBR1"] is not None:
        EBR_rectg["rec_menos_EBR1"].place_forget()
        EBR_rectg["rec_menos_EBR1"] = None
    if EBR_boton["btn_menos_EBR1"] is not None:
        EBR_boton["btn_menos_EBR1"].place_forget()
        EBR_boton["btn_menos_EBR1"] = None
    
    if EBR_text["txt_tlt_EBR1"] is None:
        EBR_text["txt_tlt_EBR1"] = tk.Label(cnt_container, text="Pérdida económica directa y Curva de excedencia de pérdidas (Promedio ponderado)", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR1"].place(relx=0.329, rely=0.16, anchor=tk.CENTER)
    
    EBR_canva["cnv_crv_EBR"] = lb.canva_crv_EBR(df_EBR, valexpuesto, valorperiodo, 'Pérdida anual [% Valor expuesto]', 'Tasa de Excedencia [1/año] ', '', cnt_container, 0.26, 0.55)
    # ---- titulo de graficos ---------------------------------------------
    if EBR_text["txt_crv_EBR"] is None:
        texto = "Curva de excedencia (" + CP_Name +")"
        EBR_text["txt_crv_EBR"] = tk.Label(cnt_container, text=texto, font=("Abadi MT", 14), bg="white", fg="#3B3838")
        EBR_text["txt_crv_EBR"].place(relx=0.275, rely=0.28, anchor=tk.CENTER)
        
    # ---- Boton mas resultados -------------------------------------------
    if EBR_rectg["rec_mas_EBR1"] is None:
        EBR_rectg["rec_mas_EBR1"] = tk.Canvas(cnt_container, bg="#659B7D", bd=0, highlightthickness=0)
        EBR_rectg["rec_mas_EBR1"].place(relx=0.889, rely=0.965, anchor=tk.CENTER, width=130, height=29) 
    if EBR_boton["btn_mas_EBR1"] is None:
        EBR_boton["btn_mas_EBR1"] = tk.Button(EBR_rectg["rec_mas_EBR1"], text="Siguiente >>", font=("Abadi MT", 13), bd=0, bg="#659B7D", fg="white", relief=tk.FLAT, command= lambda: results_taxonomy_EBR())
        EBR_boton["btn_mas_EBR1"].place(relx=0.55, rely=0.5, anchor=tk.CENTER, width=140, height=40)
        
    # ---- tabla de resumen PAE -------------------------------------------
    semy = 0.30
    semx = 0.58
    # 1). Valor expuesto --------------------------------------------------
    if EBR_recPAE["rec_vlx_tlt"] is None:
        EBR_recPAE["rec_vlx_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_vlx_tlt"].place(relx=semx, rely=semy, anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_vlx_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_vlx_tlt"] is None:
        EBR_txtPAE["txt_vlx_tlt"] = tk.Label(EBR_recPAE["rec_vlx_tlt"], text="Valor expuesto", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_vlx_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_vlx_cop"] is None:
        EBR_recPAE["rec_vlx_cop"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_vlx_cop"].place(relx=(semx+0.145), rely=semy, anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_vlx_cop"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_vlx_cop"] is None:
        EBR_txtPAE["txt_vlx_cop"] = tk.Label(EBR_recPAE["rec_vlx_cop"], text="COP [Millones]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_vlx_cop"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_vlx_val"] is None:
        EBR_recPAE["rec_vlx_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_vlx_val"].place(relx=(semx+0.29), rely=semy, anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_vlx_val"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_vlx_val"] is None:
        texto = np.around(df_resultados.Col2[0]*1e6,2)
        EBR_txtPAE["txt_vlx_val"] = tk.Label(EBR_recPAE["rec_vlx_val"], text=str(texto), 
                                    font=("Abadi MT", 13), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_vlx_val"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
    # 2). Perdida anual esperada del municipio ----------------------------
    if EBR_recPAE["rec_pae_tlt"] is None:
        EBR_recPAE["rec_pae_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pae_tlt"].place(relx=semx, rely=(semy+0.086), anchor=tk.CENTER, width=181, height=89) 
        x2, y2 = 180, 88
        x1, y1 = 10,10
        radio_esquinas = 4
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_pae_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pae_tlt1"] is None:
        EBR_txtPAE["txt_pae_tlt1"] = tk.Label(EBR_recPAE["rec_pae_tlt"], text="Pérdida anual", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_pae_tlt1"].place(relx=0.53, rely=0.43, anchor=tk.CENTER, width=132, height=22)
    if EBR_txtPAE["txt_pae_tlt2"] is None:
        EBR_txtPAE["txt_pae_tlt2"] = tk.Label(EBR_recPAE["rec_pae_tlt"], text="esperada", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_pae_tlt2"].place(relx=0.53, rely=0.63, anchor=tk.CENTER, width=132, height=22)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pae_cop"] is None:
        EBR_recPAE["rec_pae_cop"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pae_cop"].place(relx=(semx+0.145), rely=(semy+0.058), anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_pae_cop"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pae_cop"] is None:
        EBR_txtPAE["txt_pae_cop"] = tk.Label(EBR_recPAE["rec_pae_cop"], text="COP [Millones]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_pae_cop"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pae_prc"] is None:
        EBR_recPAE["rec_pae_prc"]= tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pae_prc"].place(relx=(semx+0.145), rely=(semy+0.114), anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_pae_prc"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pae_prc"] is None:
        EBR_txtPAE["txt_pae_prc"] = tk.Label(EBR_recPAE["rec_pae_prc"], text="[‰]", 
                                    font=("Abadi MT", 13,"bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_pae_prc"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pae_val_cop"] is None:
        EBR_recPAE["rec_pae_val_cop"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pae_val_cop"].place(relx=(semx+0.29), rely=(semy+0.058), anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_pae_val_cop"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pae_val_cop"] is None:
        texto = np.around(df_resultados.Col2[1],2)
        EBR_txtPAE["txt_pae_val_cop"] = tk.Label(EBR_recPAE["rec_pae_val_cop"], text=str(texto), 
                                    font=("Abadi MT", 13), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pae_val_cop"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pae_val_val"] is None:
        EBR_recPAE["rec_pae_val_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pae_val_val"].place(relx=(semx+0.29), rely=(semy+0.114), anchor=tk.CENTER, width=181, height=45) 
        x2, y2 = 180, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_pae_val_val"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pae_val_val"] is None:
        texto = np.around(df_resultados.Col2[2],3)
        EBR_txtPAE["txt_pae_val_val"] = tk.Label(EBR_recPAE["rec_pae_val_val"], text=str(texto), 
                                    font=("Abadi MT", 13), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pae_val_val"].place(relx=0.53, rely=0.57, anchor=tk.CENTER, width=132, height=22)
    # 3). Titulos resumen curvas ------------------------------------------
    if EBR_recPAE["rec_pmp_tlt"] is None:
        EBR_recPAE["rec_pmp_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pmp_tlt"].place(relx=(semx+0.145), rely=(semy+0.173), anchor=tk.CENTER, width=544, height=45) 
        x2, y2 = 543, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_pmp_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pmp_tlt"] is None:
        EBR_txtPAE["txt_pmp_tlt"] = tk.Label(EBR_recPAE["rec_pmp_tlt"], text="Pérdida máxima probable", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_pmp_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pdr_tlt"] is None:
        EBR_recPAE["rec_pdr_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pdr_tlt"].place(relx=(semx-0.018), rely=(semy+0.247), anchor=tk.CENTER, width=136, height=71) 
        x2, y2 = 135, 70
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_pdr_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pdr_tlt1"] is None:
        EBR_txtPAE["txt_pdr_tlt1"] = tk.Label(EBR_recPAE["rec_pdr_tlt"], text="retorno", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_pdr_tlt1"].place(relx=0.53, rely=0.67, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pdr_tlt2"] is None:
        EBR_txtPAE["txt_pdr_tlt2"] = tk.Label(EBR_recPAE["rec_pdr_tlt"], text="Periodo de", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_pdr_tlt2"].place(relx=0.53, rely=0.41, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_exd_tlt"] is None:
        EBR_recPAE["rec_exd_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_exd_tlt"].place(relx=(semx+0.128), rely=(semy+0.247), anchor=tk.CENTER, width=231, height=71) 
        x2, y2 = 230, 70
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_exd_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_exd_tlt1"] is None:
        EBR_txtPAE["txt_exd_tlt1"] = tk.Label(EBR_recPAE["rec_exd_tlt"], text="excedencia en 50 años", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_exd_tlt1"].place(relx=0.53, rely=0.7, anchor=tk.CENTER)
    if EBR_txtPAE["txt_exd_tlt2"] is None:
        EBR_txtPAE["txt_exd_tlt2"] = tk.Label(EBR_recPAE["rec_exd_tlt"], text="Probabilidad de", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_exd_tlt2"].place(relx=0.53, rely=0.40, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pe_tlt"] is None:
        EBR_recPAE["rec_pe_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pe_tlt"].place(relx=(semx+0.292), rely=(semy+0.247), anchor=tk.CENTER, width=176, height=71) 
        x2, y2 = 175, 70
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#274151'
        fun.rec_redond(EBR_recPAE["rec_pe_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pe_tlt"] is None:
        EBR_txtPAE["txt_pe_tlt"] = tk.Label(EBR_recPAE["rec_pe_tlt"], text="Pérdida esperada", 
                                    font=("Abadi MT", 14,"bold"), bg='#274151', fg='white')
        EBR_txtPAE["txt_pe_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # 4). subtitulos resumen PAE ------------------------------------------
    if EBR_recPAE["rec_pdran_tlt"] is None:
        EBR_recPAE["rec_pdran_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pdran_tlt"].place(relx=(semx-0.018), rely=(semy+0.322), anchor=tk.CENTER, width=136, height=45) 
        x2, y2 = 135, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_pdran_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pdran_tlt"] is None:
        EBR_txtPAE["txt_pdran_tlt"] = tk.Label(EBR_recPAE["rec_pdran_tlt"], text="[años]", 
                                    font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_pdran_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_exdprd_tlt"] is None:
        EBR_recPAE["rec_exdprd_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_exdprd_tlt"].place(relx=(semx+0.128), rely=(semy+0.322), anchor=tk.CENTER, width=231, height=45) 
        x2, y2 = 230, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_exdprd_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_exdprd_tlt"] is None:
        EBR_txtPAE["txt_exdprd_tlt"] = tk.Label(EBR_recPAE["rec_exdprd_tlt"], text="[%]", 
                                    font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_exdprd_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pecop_tlt"] is None:
        EBR_recPAE["rec_pecop_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pecop_tlt"].place(relx=(semx+0.266), rely=(semy+0.322), anchor=tk.CENTER, width=111, height=45) 
        x2, y2 = 110, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_pecop_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pecop_tlt"] is None:
        EBR_txtPAE["txt_pecop_tlt"] = tk.Label(EBR_recPAE["rec_pecop_tlt"], text="[COP Mll]", 
                                    font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_pecop_tlt"].place(relx=0.53, rely=0.57, anchor=tk.CENTER)
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_peprc_tlt"] is None:
        EBR_recPAE["rec_peprc_tlt"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_peprc_tlt"].place(relx=(semx+0.337), rely=(semy+0.322), anchor=tk.CENTER, width=61, height=45) 
        x2, y2 = 60, 44
        x1, y1 = 10,10
        radio_esquinas = 3
        color = '#456883'
        fun.rec_redond(EBR_recPAE["rec_peprc_tlt"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_peprc_tlt"] is None:
        EBR_txtPAE["txt_peprc_tlt"] = tk.Label(EBR_recPAE["rec_peprc_tlt"], text="[%]", 
                                    font=("Abadi MT", 13, "bold"), bg='#456883', fg='white')
        EBR_txtPAE["txt_peprc_tlt"].place(relx=0.57, rely=0.57, anchor=tk.CENTER)
    # 5). Valores tabla de resumen ----------------------------------------    
    if EBR_recPAE["rec_pdran_val"] is None:
        EBR_recPAE["rec_pdran_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pdran_val"].place(relx=(semx-0.018), rely=(semy+0.423), anchor=tk.CENTER, width=136, height=111) 
        x2, y2 = 135, 110
        x1, y1 = 10,10
        radio_esquinas = 4
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_pdran_val"], x1, y1, x2, y2, radio_esquinas, color)
    if EBR_txtPAE["txt_pdran_val1"] is None:
        EBR_txtPAE["txt_pdran_val1"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="31", 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pdran_val1"].place(relx=0.53, rely=0.22, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pdran_val2"] is None:
        EBR_txtPAE["txt_pdran_val2"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="225", 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pdran_val2"].place(relx=0.53, rely=0.375, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pdran_val3"] is None:
        EBR_txtPAE["txt_pdran_val3"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="475", 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pdran_val3"].place(relx=0.53, rely=0.53, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pdran_val4"] is None:
        EBR_txtPAE["txt_pdran_val4"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="975", 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pdran_val4"].place(relx=0.53, rely=0.685, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pdran_val5"] is None:
        EBR_txtPAE["txt_pdran_val5"] = tk.Label(EBR_recPAE["rec_pdran_val"], text="1475", 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pdran_val5"].place(relx=0.53, rely=0.85, anchor=tk.CENTER)  
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_exdprd_val"] is None:
        EBR_recPAE["rec_exdprd_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_exdprd_val"].place(relx=(semx+0.128), rely=(semy+0.423), anchor=tk.CENTER, width=231, height=111) 
        x2, y2 = 230, 110
        x1, y1 = 10,10
        radio_esquinas = 4
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_exdprd_val"], x1, y1, x2, y2, radio_esquinas, color)                                 
    if EBR_txtPAE["txt_exdprd_val1"] is None:
        text = np.around(Pr50_Val[0],1)
        EBR_txtPAE["txt_exdprd_val1"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_exdprd_val1"].place(relx=0.53, rely=0.22, anchor=tk.CENTER)
    if EBR_txtPAE["txt_exdprd_val2"] is None:
        text = np.around(Pr50_Val[1],1)
        EBR_txtPAE["txt_exdprd_val2"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_exdprd_val2"].place(relx=0.53, rely=0.375, anchor=tk.CENTER)
    if EBR_txtPAE["txt_exdprd_val3"] is None:
        text = np.around(Pr50_Val[2],1)
        EBR_txtPAE["txt_exdprd_val3"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_exdprd_val3"].place(relx=0.53, rely=0.53, anchor=tk.CENTER)
    if EBR_txtPAE["txt_exdprd_val4"] is None:
        text = np.around(Pr50_Val[3],1)
        EBR_txtPAE["txt_exdprd_val4"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_exdprd_val4"].place(relx=0.53, rely=0.685, anchor=tk.CENTER)
    if EBR_txtPAE["txt_exdprd_val5"] is None:
        text = np.around(Pr50_Val[4],1)
        EBR_txtPAE["txt_exdprd_val5"] = tk.Label(EBR_recPAE["rec_exdprd_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_exdprd_val5"].place(relx=0.53, rely=0.85, anchor=tk.CENTER) 
    # ---------------------------------------------------------------------
    if EBR_recPAE["rec_pecop_val"] is None:
        EBR_recPAE["rec_pecop_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_pecop_val"].place(relx=(semx+0.266), rely=(semy+0.423), anchor=tk.CENTER, width=111, height=111) 
        x2, y2 = 110, 110
        x1, y1 = 10,10
        radio_esquinas = 4
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_pecop_val"], x1, y1, x2, y2, radio_esquinas, color)                                 
    if EBR_txtPAE["txt_pecop_val1"] is None:
        text = np.around(PE_mill[0],1)
        EBR_txtPAE["txt_pecop_val1"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pecop_val1"].place(relx=0.53, rely=0.22, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pecop_val2"] is None:
        text = np.around(PE_mill[1],1)
        EBR_txtPAE["txt_pecop_val2"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pecop_val2"].place(relx=0.53, rely=0.375, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pecop_val3"] is None:
        text = np.around(PE_mill[2],1)
        EBR_txtPAE["txt_pecop_val3"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pecop_val3"].place(relx=0.53, rely=0.53, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pecop_val4"] is None:
        text = np.around(PE_mill[3],1)
        EBR_txtPAE["txt_pecop_val4"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pecop_val4"].place(relx=0.53, rely=0.685, anchor=tk.CENTER)
    if EBR_txtPAE["txt_pecop_val5"] is None:
        text = np.around(PE_mill[4],1)
        EBR_txtPAE["txt_pecop_val5"] = tk.Label(EBR_recPAE["rec_pecop_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_pecop_val5"].place(relx=0.53, rely=0.85, anchor=tk.CENTER) 
    # --------------------------------------------------------------------- 
    if EBR_recPAE["rec_peprc_val"] is None:   
        EBR_recPAE["rec_peprc_val"] = tk.Canvas(cnt_container, bg="white", bd=0, highlightthickness=0)
        EBR_recPAE["rec_peprc_val"].place(relx=(semx+0.337), rely=(semy+0.423), anchor=tk.CENTER, width=61, height=111) 
        x2, y2 = 60, 110
        x1, y1 = 10,10
        radio_esquinas = 4
        color = '#C6CFD4'
        fun.rec_redond(EBR_recPAE["rec_peprc_val"], x1, y1, x2, y2, radio_esquinas, color) 
    if EBR_txtPAE["txt_peprc_val1"] is None:
        text = np.around((PE_mill[0]/(df_resultados.Col2[0]*1e6))*100,1)
        EBR_txtPAE["txt_peprc_val1"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_peprc_val1"].place(relx=0.55, rely=0.22, anchor=tk.CENTER)
    if EBR_txtPAE["txt_peprc_val2"] is None:
        text = np.around((PE_mill[1]/(df_resultados.Col2[0]*1e6))*100,1)
        EBR_txtPAE["txt_peprc_val2"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_peprc_val2"].place(relx=0.55, rely=0.375, anchor=tk.CENTER)
    if EBR_txtPAE["txt_peprc_val3"] is None:
        text = np.around((PE_mill[2]/(df_resultados.Col2[0]*1e6))*100,1)
        EBR_txtPAE["txt_peprc_val3"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_peprc_val3"].place(relx=0.55, rely=0.53, anchor=tk.CENTER)
    if EBR_txtPAE["txt_peprc_val4"] is None:
        text = np.around((PE_mill[3]/(df_resultados.Col2[0]*1e6))*100,1)
        EBR_txtPAE["txt_peprc_val4"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_peprc_val4"].place(relx=0.55, rely=0.685, anchor=tk.CENTER)
    if EBR_txtPAE["txt_peprc_val5"] is None:
        text = np.around((PE_mill[4]/(df_resultados.Col2[0]*1e6))*100,1)
        EBR_txtPAE["txt_peprc_val5"] = tk.Label(EBR_recPAE["rec_peprc_val"], text=str(text), 
                                    font=("Abadi MT", 12), bg='#C6CFD4', fg='#000000')
        EBR_txtPAE["txt_peprc_val5"].place(relx=0.55, rely=0.85, anchor=tk.CENTER)

def results_taxonomy_Diagram_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll):
    hide_results_taxonomy_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll)
    if EBR_canva["cnv_crv_EBR"] is not None:
        EBR_canva["cnv_crv_EBR"].get_tk_widget().destroy()
        EBR_canva["cnv_crv_EBR"] = None
    
    if EBR_canva["cnv_map_COP"] is not None:
        EBR_canva["cnv_map_COP"].get_tk_widget().destroy()
        EBR_canva["cnv_map_COP"] = None
        
    EBR_canva["cnv_EBR_taxo"] = lb.canva_EBR_taxo(df_expotax,cnt_container, 0.5, 0.5)
    
    # ---- Representacion grafica de los resultados ---------------------------
    if EBR_recPAE["rec_representacion"] is not None and EBR_txtPAE["txt_representacion1"] is not None and EBR_boton["btn_representacion"] is not None:
        EBR_recPAE["rec_representacion"].place_forget()
        EBR_recPAE["rec_representacion"] = None
        EBR_txtPAE["txt_representacion1"].place_forget()
        EBR_txtPAE["txt_representacion1"] = None
        EBR_boton["btn_representacion"].place_forget()
        EBR_boton["btn_representacion"] = None
    
    
    if EBR_recPAE["rec_representacion"] is None:
        EBR_recPAE["rec_representacion"] = tk.Canvas(cnt_container, bg="#274151", bd=0, highlightthickness=0)
        EBR_recPAE["rec_representacion"].place(relx=0.5, rely=0.9, anchor=tk.CENTER, width=200, height=47) 
    if EBR_boton["btn_representacion"] is None:
        EBR_boton["btn_representacion"] = tk.Button(EBR_recPAE["rec_representacion"], text="Volver a la tabla de", 
                                    font=("Abadi MT", 13), bd=0, bg="#274151", fg="white", relief=tk.FLAT, command=lambda: results_taxonomy_EBR() )
        EBR_boton["btn_representacion"].place(relx=0.50, rely=0.26, anchor=tk.CENTER)
    if EBR_txtPAE["txt_representacion1"] is None:
        EBR_txtPAE["txt_representacion1"] = tk.Label(EBR_recPAE["rec_representacion"], text="pérdidas por taxonomía", 
                                    font=("Abadi MT", 13), bg='#274151', fg='white')
        EBR_txtPAE["txt_representacion1"].place(relx=0.50, rely=0.71, anchor=tk.CENTER)
        
def hide_results_taxonomy_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll):
    if EBR_recPAE["rec_representacion"] is not None and EBR_txtPAE["txt_representacion1"] is not None and EBR_boton["btn_representacion"] is not None:
        EBR_recPAE["rec_representacion"] .place_forget()
        EBR_recPAE["rec_representacion"]  = None
        EBR_txtPAE["txt_representacion1"].place_forget()
        EBR_txtPAE["txt_representacion1"] = None
        EBR_boton["btn_representacion"].place_forget()
        EBR_boton["btn_representacion"] = None

    for txt in txtPAE_EBR_tax:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_tip:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_vlx_cop:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_vlx_prc:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_pae_cop:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_pae_prc:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    for txt in txtPAE_EBR_pae_pmll:
        if EBR_tax_txtPAE[txt] is not None:
            EBR_tax_txtPAE[txt].place_forget()
            EBR_tax_txtPAE[txt] = None
    
    for rec in recPAE_EBR_tax:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_tip:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_vlx_cop:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_vlx_prc:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_pae_cop:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_pae_prc:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    for rec in recPAE_EBR_pae_pmll:
        if EBR_tax_recPAE[rec]is not None:
            EBR_tax_recPAE[rec].place_forget()
            EBR_tax_recPAE[rec] = None
    if EBR_recPAE["rec_tip_tlt"] is not None and EBR_txtPAE["txt_tip_tlt"] is not None:
        EBR_recPAE["rec_tip_tlt"] .place_forget()
        EBR_recPAE["rec_tip_tlt"]  = None
        EBR_txtPAE["txt_tip_tlt"].place_forget()
        EBR_txtPAE["txt_tip_tlt"] = None
    if EBR_recPAE["rec_dsc_tlt"] is not None and EBR_txtPAE["txt_dsc_tlt"] is not None:
        EBR_recPAE["rec_dsc_tlt"] .place_forget()
        EBR_recPAE["rec_dsc_tlt"]  = None
        EBR_txtPAE["txt_dsc_tlt"].place_forget()
        EBR_txtPAE["txt_dsc_tlt"] = None
    if EBR_recPAE["rec_dtip_tlt"] is not None and EBR_txtPAE["txt_dtip_tlt"] is not None:
        EBR_recPAE["rec_dtip_tlt"] .place_forget()
        EBR_recPAE["rec_dtip_tlt"]  = None
        EBR_txtPAE["txt_dtip_tlt"].place_forget()
        EBR_txtPAE["txt_dtip_tlt"] = None
    if EBR_recPAE["rec_valex_tlt"] is not None and EBR_txtPAE["txt_valex_tlt"] is not None:
        EBR_recPAE["rec_valex_tlt"] .place_forget()
        EBR_recPAE["rec_valex_tlt"]  = None
        EBR_txtPAE["txt_valex_tlt"].place_forget()
        EBR_txtPAE["txt_valex_tlt"] = None
    if EBR_recPAE["rec_valexCOP_tlt"] is not None and EBR_txtPAE["txt_valexCOP_tlt"] is not None:
        EBR_recPAE["rec_valexCOP_tlt"] .place_forget()
        EBR_recPAE["rec_valexCOP_tlt"]  = None
        EBR_txtPAE["txt_valexCOP_tlt"].place_forget()
        EBR_txtPAE["txt_valexCOP_tlt"] = None
    if EBR_recPAE["rec_valexPRC_tlt"] is not None and EBR_txtPAE["txt_valexPRC_tlt"] is not None:
        EBR_recPAE["rec_valexPRC_tlt"] .place_forget()
        EBR_recPAE["rec_valexPRC_tlt"]  = None
        EBR_txtPAE["txt_valexPRC_tlt"].place_forget()
        EBR_txtPAE["txt_valexPRC_tlt"] = None
    if EBR_recPAE["rec_PAEtxn_tlt"] is not None and EBR_txtPAE["txt_PAEtxn_tlt"] is not None:
        EBR_recPAE["rec_PAEtxn_tlt"] .place_forget()
        EBR_recPAE["rec_PAEtxn_tlt"]  = None
        EBR_txtPAE["txt_PAEtxn_tlt"].place_forget()
        EBR_txtPAE["txt_PAEtxn_tlt"] = None
    if EBR_recPAE["rec_paeCOP_tlt"] is not None and EBR_txtPAE["txt_paeCOP_tlt"] is not None:
        EBR_recPAE["rec_paeCOP_tlt"] .place_forget()
        EBR_recPAE["rec_paeCOP_tlt"]  = None
        EBR_txtPAE["txt_paeCOP_tlt"].place_forget()
        EBR_txtPAE["txt_paeCOP_tlt"] = None
    if EBR_recPAE["rec_paePRC_tlt"] is not None and EBR_txtPAE["txt_paePRC_tlt"] is not None:
        EBR_recPAE["rec_paePRC_tlt"] .place_forget()
        EBR_recPAE["rec_paePRC_tlt"]  = None
        EBR_txtPAE["txt_paePRC_tlt"].place_forget()
        EBR_txtPAE["txt_paePRC_tlt"] = None
    if EBR_recPAE["rec_paePMLL_tlt"] is not None and EBR_txtPAE["txt_paePMLL_tlt"] is not None:
        EBR_recPAE["rec_paePMLL_tlt"] .place_forget()
        EBR_recPAE["rec_paePMLL_tlt"]  = None
        EBR_txtPAE["txt_paePMLL_tlt"].place_forget()
        EBR_txtPAE["txt_paePMLL_tlt"] = None
        
def results_Maps_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll):
    hide_results_taxonomy_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll)
    
    if EBR_canva["cnv_crv_EBR"] is not None:
        EBR_canva["cnv_crv_EBR"].get_tk_widget().destroy()
        EBR_canva["cnv_crv_EBR"] = None
    
    if EBR_text["txt_tlt_EBR1"] is not None:
        print('entra')
        EBR_text["txt_tlt_EBR1"].place_forget()
        EBR_text["txt_tlt_EBR1"] = None
    
    if EBR_canva["cnv_map_COP"] is not None:
        EBR_canva["cnv_map_COP"].get_tk_widget().destroy()
        EBR_canva["cnv_map_COP"] = None
    
    if EBR_canva["cnv_EBR_taxo"]  is not None:
        EBR_canva["cnv_EBR_taxo"].get_tk_widget().destroy()
        EBR_canva["cnv_EBR_taxo"] = None
        
    if EBR_recPAE["rec_representacion"] is not None and EBR_txtPAE["txt_representacion1"] is not None and EBR_boton["btn_representacion"] is not None:
        EBR_recPAE["rec_representacion"].place_forget()
        EBR_recPAE["rec_representacion"] = None
        EBR_txtPAE["txt_representacion1"].place_forget()
        EBR_txtPAE["txt_representacion1"] = None
        EBR_boton["btn_representacion"].place_forget()
        EBR_boton["btn_representacion"] = None
        
    if EBR_recPAE["rec_representacion"] is None:
        EBR_recPAE["rec_representacion"] = tk.Canvas(cnt_container, bg="#274151", bd=0, highlightthickness=0)
        EBR_recPAE["rec_representacion"].place(relx=0.5, rely=0.9, anchor=tk.CENTER, width=200, height=47) 
    if EBR_boton["btn_representacion"] is None:
        EBR_boton["btn_representacion"] = tk.Button(EBR_recPAE["rec_representacion"], text="Mapa PAE en", 
                                    font=("Abadi MT", 11), bd=0, bg="#274151", fg="white", relief=tk.FLAT, command=lambda: results_Maps_prc_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll))
        EBR_boton["btn_representacion"].place(relx=0.50, rely=0.26, anchor=tk.CENTER)
    if EBR_txtPAE["txt_representacion1"] is None:
        EBR_txtPAE["txt_representacion1"] = tk.Label(EBR_recPAE["rec_representacion"], text="[‰] (pérdida/valor expuesto)", 
                                    font=("Abadi MT", 11), bg='#274151', fg='white')
        EBR_txtPAE["txt_representacion1"].place(relx=0.50, rely=0.71, anchor=tk.CENTER)
    
    if EBR_text["txt_tlt_EBR1"] is None:
        EBR_text["txt_tlt_EBR1"] = tk.Label(cnt_container, text="Representación espacial de los resultados (manzana censal) - valor absoluto", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR1"].place(relx=0.298, rely=0.16, anchor=tk.CENTER)
    
    EBR_canva["cnv_map_COP"] = lb.canva_mapa_COP(map_data,seccion_shp,area_shpe,COD_mun,CP_Name,ruta_shp,cnt_container, 0.5, 0.55)
    
    if EBR_rectg["rec_mas_EBR1"] is not None:
        EBR_rectg["rec_mas_EBR1"].place_forget()
        EBR_rectg["rec_mas_EBR1"] = None
    if EBR_boton["btn_mas_EBR1"] is not None:
        EBR_boton["btn_mas_EBR1"].place_forget()
        EBR_boton["btn_mas_EBR1"] = None
    if EBR_rectg["rec_menos_EBR1"] is not None:
        EBR_rectg["rec_menos_EBR1"].place_forget()
        EBR_rectg["rec_menos_EBR1"] = None
    if EBR_boton["btn_menos_EBR1"] is not None:
        EBR_boton["btn_menos_EBR1"].place_forget()
        EBR_boton["btn_menos_EBR1"] = None

    
    if EBR_rectg["rec_menos_EBR1"] is None:
        EBR_rectg["rec_menos_EBR1"] = tk.Canvas(cnt_container, bg="#659B7D", bd=0, highlightthickness=0)
        EBR_rectg["rec_menos_EBR1"].place(relx=0.76, rely=0.965, anchor=tk.CENTER, width=130, height=29) 
    if EBR_boton["btn_menos_EBR1"] is None:
        EBR_boton["btn_menos_EBR1"] = tk.Button(EBR_rectg["rec_menos_EBR1"], text="<< Atrás", font=("Abadi MT", 13), bd=0, bg="#659B7D", fg="white", relief=tk.FLAT, command=lambda: results_taxonomy_EBR())
        EBR_boton["btn_menos_EBR1"].place(relx=0.45, rely=0.5, anchor=tk.CENTER, width=140, height=40)
    
def results_Maps_prc_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll):
    hide_results_taxonomy_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll)
    
    if EBR_canva["cnv_crv_EBR"] is not None:
        EBR_canva["cnv_crv_EBR"].get_tk_widget().destroy()
        EBR_canva["cnv_crv_EBR"] = None
    
    if EBR_canva["cnv_map_COP"] is not None:
        EBR_canva["cnv_map_COP"].get_tk_widget().destroy()
        EBR_canva["cnv_map_COP"] = None
    
    if EBR_canva["cnv_EBR_taxo"]  is not None:
        EBR_canva["cnv_EBR_taxo"].get_tk_widget().destroy()
        EBR_canva["cnv_EBR_taxo"] = None
    if EBR_recPAE["rec_representacion"] is not None and EBR_txtPAE["txt_representacion1"] is not None and EBR_boton["btn_representacion"] is not None:
        EBR_recPAE["rec_representacion"].place_forget()
        EBR_recPAE["rec_representacion"] = None
        EBR_txtPAE["txt_representacion1"].place_forget()
        EBR_txtPAE["txt_representacion1"] = None
        EBR_boton["btn_representacion"].place_forget()
        EBR_boton["btn_representacion"] = None
        
    if EBR_recPAE["rec_representacion"] is None:
        EBR_recPAE["rec_representacion"] = tk.Canvas(cnt_container, bg="#274151", bd=0, highlightthickness=0)
        EBR_recPAE["rec_representacion"].place(relx=0.5, rely=0.9, anchor=tk.CENTER, width=200, height=47) 
    if EBR_boton["btn_representacion"] is None:
        EBR_boton["btn_representacion"] = tk.Button(EBR_recPAE["rec_representacion"], text="Mapa PAE en", 
                                    font=("Abadi MT", 13), bd=0, bg="#274151", fg="white", relief=tk.FLAT, command=lambda: results_Maps_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll))
        EBR_boton["btn_representacion"].place(relx=0.50, rely=0.26, anchor=tk.CENTER)
    if EBR_txtPAE["txt_representacion1"] is None:
        EBR_txtPAE["txt_representacion1"] = tk.Label(EBR_recPAE["rec_representacion"], text="[COP Millones]", 
                                    font=("Abadi MT", 13), bg='#274151', fg='white')
        EBR_txtPAE["txt_representacion1"].place(relx=0.50, rely=0.71, anchor=tk.CENTER)
    
    if EBR_text["txt_tlt_EBR1"] is not None:
        EBR_text["txt_tlt_EBR1"].place_forget()
        EBR_text["txt_tlt_EBR1"] = None
    if EBR_text["txt_tlt_EBR1"] is None:
        EBR_text["txt_tlt_EBR1"] = tk.Label(cnt_container, text="Representación espacial de los resultados (manzana censal) - valor absoluto", 
                         font=("Abadi MT", 15), bg="white", fg="#3B3838")
        EBR_text["txt_tlt_EBR1"].place(relx=0.298, rely=0.16, anchor=tk.CENTER)
    
    EBR_canva["cnv_map_COP"] = lb.canva_mapa_prc(map_data,seccion_shp,area_shpe,COD_mun,CP_Name,ruta_shp,cnt_container, 0.5, 0.55)
    
    if EBR_rectg["rec_mas_EBR1"] is not None:
        EBR_rectg["rec_mas_EBR1"].place_forget()
        EBR_rectg["rec_mas_EBR1"] = None
    if EBR_boton["btn_mas_EBR1"] is not None:
        EBR_boton["btn_mas_EBR1"].place_forget()
        EBR_boton["btn_mas_EBR1"] = None
    if EBR_rectg["rec_menos_EBR1"] is not None:
        EBR_rectg["rec_menos_EBR1"].place_forget()
        EBR_rectg["rec_menos_EBR1"] = None
    if EBR_boton["btn_menos_EBR1"] is not None:
        EBR_boton["btn_menos_EBR1"].place_forget()
        EBR_boton["btn_menos_EBR1"] = None
    
    if EBR_rectg["rec_menos_EBR1"] is None:
        EBR_rectg["rec_menos_EBR1"] = tk.Canvas(cnt_container, bg="#659B7D", bd=0, highlightthickness=0)
        EBR_rectg["rec_menos_EBR1"].place(relx=0.76, rely=0.965, anchor=tk.CENTER, width=130, height=29) 
    if EBR_boton["btn_menos_EBR1"] is None:
        EBR_boton["btn_menos_EBR1"] = tk.Button(EBR_rectg["rec_menos_EBR1"], text="<< Atrás", font=("Abadi MT", 13), bd=0, bg="#659B7D", fg="white", relief=tk.FLAT, command=lambda: results_taxonomy_EBR())
        EBR_boton["btn_menos_EBR1"].place(relx=0.45, rely=0.5, anchor=tk.CENTER, width=140, height=40)

def hide_results_Maps_prc_EBR(EBR_tax_txtPAE,EBR_tax_recPAE,txtPAE_EBR_tax,txtPAE_EBR_tip,txtPAE_EBR_vlx_cop,txtPAE_EBR_vlx_prc,txtPAE_EBR_pae_cop,txtPAE_EBR_pae_prc,txtPAE_EBR_pae_pmll,recPAE_EBR_tax,recPAE_EBR_tip,recPAE_EBR_vlx_cop,recPAE_EBR_vlx_prc,recPAE_EBR_pae_cop,recPAE_EBR_pae_prc,recPAE_EBR_pae_pmll):
    if EBR_recPAE["rec_representacion"] is not None and EBR_txtPAE["txt_representacion1"] is not None and EBR_boton["btn_representacion"] is not None:
        print('entra')
        EBR_recPAE["rec_representacion"].place_forget()
        EBR_recPAE["rec_representacion"] = None
        EBR_txtPAE["txt_representacion1"].place_forget()
        EBR_txtPAE["txt_representacion1"] = None
        EBR_boton["btn_representacion"].place_forget()
        EBR_boton["btn_representacion"] = None
    if EBR_text["txt_tlt_EBR1"] is not None:
        EBR_text["txt_tlt_EBR1"].place_forget()
        EBR_text["txt_tlt_EBR1"] = None
    if EBR_canva["cnv_map_COP"] is not None:
        EBR_canva["cnv_map_COP"].get_tk_widget().destroy()
        EBR_canva["cnv_map_COP"] = None
    

#%% ====== FUNCTION >> SELECT_FOLDER ==========================================
"""
-------------------------------------------------------------------------------
Funcion para seleccion de carpeta
-------------------------------------------------------------------------------
"""
def select_folder_CLB(rx,ry):
    print('------------------------------------------')
    print('-------- Se selecciono una carpeta -------')
    print('------------------------------------------')
    global carpeta_seleccionada                                                 # El directorio lo hace una variable global
    # filedialog.askdirectory() devuelve la ruta completa del directorio 
    # seleccionado por el usuario
    carpeta_seleccionada = filedialog.askdirectory()                            # Deja que el usuario seleccione la carpeta en donde estan los resultados
    
    CLB_boton["btn_crp_CLB"].place_forget()
    CLB_boton["btn_crp_CLB"] = None
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/carpetaSelect.png')
    img_crp = img_crp.resize((44, 40), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if CLB_boton["btn_crp_CLB"] is None:
        CLB_boton["btn_crp_CLB"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda:select_folder(rx,ry))
        CLB_boton["btn_crp_CLB"].image = img_crp
        CLB_boton["btn_crp_CLB"].place(relx=rx, rely=ry, anchor=tk.CENTER)
    
    return carpeta_seleccionada

def select_folder(rx,ry):
    print('------------------------------------------')
    print('-------- Se selecciono una carpeta -------')
    print('------------------------------------------')
    global carpeta_seleccionada                                                 # El directorio lo hace una variable global
    # filedialog.askdirectory() devuelve la ruta completa del directorio 
    # seleccionado por el usuario
    carpeta_seleccionada = filedialog.askdirectory()                            # Deja que el usuario seleccione la carpeta en donde estan los resultados
    
    EBR_boton["btn_crp_EBR2"].place_forget()
    EBR_boton["btn_crp_EBR2"] = None
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/carpetaSelect.png')
    img_crp = img_crp.resize((37, 33), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if EBR_boton["btn_crp_EBR2"] is None:
        EBR_boton["btn_crp_EBR2"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda:select_folder(rx,ry))
        EBR_boton["btn_crp_EBR2"].image = img_crp
        EBR_boton["btn_crp_EBR2"].place(relx=rx, rely=ry, anchor=tk.CENTER)
    
    return carpeta_seleccionada

def seleccionar_carpeta_DSP():
    print('------------------------------------------')
    print('-------- Se selecciono una carpeta -------')
    print('------------------------------------------')
    global carpeta_seleccionada                                                 # El directorio lo hace una variable global
    # filedialog.askdirectory() devuelve la ruta completa del directorio 
    # seleccionado por el usuario
    carpeta_seleccionada = filedialog.askdirectory()                            # Deja que el usuario seleccione la carpeta en donde estan los resultados
    
    DSP_boton["btn_crp_DSP"].place_forget()
    DSP_boton["btn_crp_DSP"] = None
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/carpetaSelect.png')
    img_crp = img_crp.resize((44, 40), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if DSP_boton["btn_crp_DSP"] is None:
        DSP_boton["btn_crp_DSP"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=seleccionar_carpeta_DSP)
        DSP_boton["btn_crp_DSP"].image = img_crp
        DSP_boton["btn_crp_DSP"].place(relx=0.15, rely=0.315, anchor=tk.CENTER)
    
    return carpeta_seleccionada

def select_file(rx,ry):
    global archivo_seleccionado
    print('------------------------------------------')
    print('-------- Se seleccionó un archivo -------')
    print('------------------------------------------')
    archivo_seleccionado = filedialog.askopenfilename()  # Permite al usuario seleccionar un archivo
    
    EBR_boton["btn_crp_EBR"].place_forget()
    EBR_boton["btn_crp_EBR"] = None
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/archivoSelect.png')
    img_crp = img_crp.resize((37, 33), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if EBR_boton["btn_crp_EBR"] is None:
        EBR_boton["btn_crp_EBR"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda:select_file(rx,ry))
        EBR_boton["btn_crp_EBR"].image = img_crp
        EBR_boton["btn_crp_EBR"].place(relx=rx, rely=ry, anchor=tk.CENTER)
    
    return archivo_seleccionado

def select_file_tax(rx,ry):
    global archivo_seleccionado_tax
    print('------------------------------------------')
    print('-------- Se seleccionó un archivo -------')
    print('------------------------------------------')
    archivo_seleccionado_tax = filedialog.askopenfilename()  # Permite al usuario seleccionar un archivo
    
    EBR_boton["btn_crp_EBR3"].place_forget()
    EBR_boton["btn_crp_EBR3"] = None
    img_crp = Image.open(os.path.join(os.getcwd(),"icon") + '/archivoSelect.png')
    img_crp = img_crp.resize((37, 33), Image.LANCZOS)
    img_crp = ImageTk.PhotoImage(img_crp)
    if EBR_boton["btn_crp_EBR3"] is None:
        EBR_boton["btn_crp_EBR3"] = tk.Button(cnt_container, image=img_crp, 
                                   bd=0, bg="white", command=lambda:select_file_tax(rx,ry))
        EBR_boton["btn_crp_EBR3"].image = img_crp
        EBR_boton["btn_crp_EBR3"].place(relx=rx, rely=ry, anchor=tk.CENTER)
    
    return archivo_seleccionado_tax
#%% ====== FUNCTION >> CHANGE BLOCK ===========================================
"""
-------------------------------------------------------------------------------
Funcion cambiar manzana. perdidas>calibrar
-------------------------------------------------------------------------------
"""
def Cambiar_Mnz(combo,canvas1):
    if combo == '':
        combo = None 
        tk.messagebox.showinfo("Select block", "The block has not been selected")                                          
    else:
        # Borrar el grafico canvas 1 para generar uno nuevo
        # ---- Borrar el grafico canvas 2 para generar uno nuevo ------------------'
        if canvas1 is not None:
            canvas1.get_tk_widget().destroy()
            canvas1 = None
        # Ocultar boton seleccionar manzana
        global cmb_Mnz_CLB
        cmb_Mnz_CLB.place_forget()
        cmb_Mnz_CLB = None
        CLB_boton["btn_Cmnz_CLB"].place_forget()
        CLB_boton["btn_Cmnz_CLB"] = None
        CLB_rectg["rec_Cmnz_CLB"].place_forget()
        CLB_rectg["rec_Cmnz_CLB"] = None
        # ---- Ocultar titulo graficas --------------------------------------------
        CLB_title["tlt_cp_CLB"].place_forget()
        CLB_title["tlt_cp_CLB"] = None
        CLB_title["tlt_mnz_CLB"].place_forget()
        CLB_title["tlt_mnz_CLB"] = None
        
        # Generar nuevamente el grafico
        # ------- Generar grafico (manzana) ---------------------------------------
        manzanapred = str(codigomnzs[0])+str(combo)
        fila_a_graficar = simmnz_losses.loc[simmnz_losses['Manzana'] == manzanapred]
        fila_a_graficar2 = simmnz_losses2.loc[simmnz_losses2['Manzana'] == manzanapred]
        fila_a_graficar = fila_a_graficar[['Manzana']+['Sim_{}'.format(i) for i in newNsim]]
        fila_a_graficar2 = fila_a_graficar2[['Manzana']+['Sim_{}'.format(i) for i in newNsim]]
        fila_a_graficar = fila_a_graficar.drop(columns=['Manzana'])
        fila_a_graficar2 = fila_a_graficar2.drop(columns=['Manzana'])
        datos_fila = fila_a_graficar.values[0]*100
        datos_fila2 = fila_a_graficar2.values[0]
        
        datos_fila_error = [0] 
        for i in range(1, len(datos_fila2)-1):
            error1 = np.abs(1-(datos_fila2[i]/datos_fila2[i-1]))*100
            error2 = np.abs(1-(datos_fila2[i+1]/datos_fila2[i]))*100
            error_promedio = np.mean([error1,error2])
            datos_fila_error.append(float(error_promedio))
        datos_fila_error.append(np.abs(1-(datos_fila2[i+1]/datos_fila2[i]))*100)
        
        datos = {'Num_Sim':newNsim,'loss':datos_fila, 'error':datos_fila_error}
        CLB_canva["cnv_mnz_CLB"] = lb.canva_CLB_In(datos, 'Number of simulated events', 'Average annual loss [%]','CodDANE:'+str(manzanapred)[1:],cnt_container,0.73,0.647)
       
        # ------- Generar titulo graficas -----------------------------------------
        if CLB_title["tlt_cp_CLB"] is None:
           texto = "Average annual municipal loss (" + CP_Name +")"
           CLB_title["tlt_cp_CLB"] = tk.Label(cnt_container, text=texto, font=("Abadi MT", 15), bg="white", fg="#3B3838")
           CLB_title["tlt_cp_CLB"].place(relx=0.28, rely=0.35, anchor=tk.CENTER) 
        if CLB_title["tlt_mnz_CLB"] is None:
           texto = "Average annual loss per block (" + CP_Name +")"
           CLB_title["tlt_mnz_CLB"] = tk.Label(cnt_container, text=texto, font=("Abadi MT", 15), bg="white", fg="#3B3838")
           CLB_title["tlt_mnz_CLB"].place(relx=0.73, rely=0.35, anchor=tk.CENTER)   
        # ---- Mostrar combo cambiar manzana ----------------------------------
        CLB_rectg["rec_Cmnz_CLB"] = tk.Canvas(cnt_container, bg="#37586B", bd=0, highlightthickness=0)
        CLB_rectg["rec_Cmnz_CLB"].place(relx=0.73, rely=0.93, anchor=tk.CENTER, width=200, height=35) 
        cmb_Mnz_CLB = ttk.Combobox(CLB_rectg["rec_Cmnz_CLB"],values=opciones)
        cmb_Mnz_CLB.place(relx=0.82, rely=0.55, anchor=tk.CENTER, width=65, height=25)
        CLB_boton["btn_Cmnz_CLB"] = tk.Button(CLB_rectg["rec_Cmnz_CLB"], text="Select block", font=("Abadi MT", 15), bd=0, bg="#37586B", fg="white", relief=tk.FLAT, command=lambda: Cambiar_Mnz(cmb_Mnz_CLB.get(),CLB_canva["cnv_mnz_CLB"]))
        CLB_boton["btn_Cmnz_CLB"].place(relx=0.34, rely=0.52, anchor=tk.CENTER, width=119, height=25)
#%% ====== MAIN WINDOW ========================================================
"""
-------------------------------------------------------------------------------
Create the interface
-------------------------------------------------------------------------------
"""
ventana = tk.Tk()
ventana.title("METRISK")
"""
-------------------------------------------------------------------------------
                               Modify upper container
                    Logo of the application and universities
-------------------------------------------------------------------------------
"""
up_container = tk.Frame(ventana, height=100, bg=upcnt_color)
up_container.pack(side=tk.TOP, fill=tk.X)    
# 1). -------- Interface logo: ------------------------------------------------
logo_container = tk.Frame(up_container, bg=upcnt_color, width=250, height=100)    
logo_container.pack(side=tk.LEFT)
logo_image = Image.open(os.path.join(os.getcwd(),"icon") + '/metrisk.png')
logo_image = logo_image.resize((185, 37), Image.LANCZOS)
logo_image = ImageTk.PhotoImage(logo_image)
logo_Button = tk.Button(logo_container, image=logo_image,bd=0, bg=upcnt_color, command=Show_Home)
logo_Button.image = logo_image
logo_Button.place(relx=0.5, rely=0.5, anchor=tk.CENTER) 
# 2). -------- UMedellin logo: ------------------------------------------------
UM_container = tk.Frame(up_container, bg=upcnt_color, height=100, width=200)
UM_container.pack(side=tk.RIGHT)
UM_image = Image.open(os.path.join(os.getcwd(),"icon") + '/Medellin.png')
UM_image = UM_image.resize((142, 40), Image.LANCZOS)
UM_image = ImageTk.PhotoImage(UM_image)
UM_label = tk.Label(UM_container, image=UM_image, bd=0, bg=upcnt_color)
UM_label.image = UM_image
UM_label.place(relx=0.4, rely=0.5, anchor=tk.CENTER)
# 3). -------- USabana logo: --------------------------------------------------
US_container = tk.Frame(up_container, bg=upcnt_color, height=100, width=200)
US_container.pack(side=tk.RIGHT)
US_image = Image.open(os.path.join(os.getcwd(),"icon") + '/Sabana.png')
US_image = US_image.resize((142, 40), Image.LANCZOS)
US_image = ImageTk.PhotoImage(US_image)
US_label = tk.Label(US_container, image=US_image, bd=0, bg=upcnt_color)
US_label.image = US_image
US_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
"""
-------------------------------------------------------------------------------
                       Modify container or navigation bar
-------------------------------------------------------------------------------
"""
left_container = tk.Frame(ventana, width=250)
left_container.pack(side=tk.LEFT,fill=tk.Y)
# 1). -------- Navigation bar: ------------------------------------------------
navigation_bar = tk.Frame(left_container, bg = navbar_color, width = 250, height=570)
navigation_bar.pack(side=tk.TOP)
# 2). -------- HOME TAB: ------------------------------------------------------
HOME_tab = tk.Button(navigation_bar, text="Home", font=("Abadi MT", 13), bd=0, 
                            bg=navbar_color, fg="white", relief=tk.FLAT, command=Show_Home, padx=20)
HOME_tab.place(relx=0.375, rely=0.1, anchor=tk.CENTER) 
Home_image = Image.open(os.path.join(os.getcwd(),"icon") + '/Home.png')
Home_image = Home_image.resize((25, 25), Image.LANCZOS)
Home_image = ImageTk.PhotoImage(Home_image)
Home_label = tk.Label(navigation_bar, image=Home_image, bd=0, bg="#37586B")
Home_label.image = Home_image
Home_label.place(relx=0.185, rely=0.095, anchor=tk.CENTER)
# 2). -------- LOSS ESTIMATIONS TAB: ------------------------------------------
LSS_boton["btn_slc_LSS"] = tk.Button(navigation_bar, text="Loss estimations", font=("Abadi MT", 13), 
                              bd=0, bg=navbar_color, fg="white", relief=tk.FLAT, command=Show_Loss, padx=20)
LSS_boton["btn_slc_LSS"].place(relx=0.53, rely=0.19, anchor=tk.CENTER) 
loss_image = Image.open(os.path.join(os.getcwd(),"icon") + '/Loss.png')
loss_image = loss_image.resize((25, 25), Image.LANCZOS)
loss_image = ImageTk.PhotoImage(loss_image)
LSS_label["lbl_slc_LSS"] = tk.Label(navigation_bar, image=loss_image, bd=0, bg=navbar_color)
LSS_label["lbl_slc_LSS"].image = loss_image
LSS_label["lbl_slc_LSS"].place(relx=0.185, rely=0.185, anchor=tk.CENTER)

# desglosar
imagen_desglos = Image.open(os.path.join(os.getcwd(),"icon") + '/desglo.png')
imagen_desglos = imagen_desglos.resize((9,7), Image.LANCZOS)
imagen_desglos = ImageTk.PhotoImage(imagen_desglos)
LSS_boton["btn_dsg_LSS"] = tk.Button(navigation_bar, image=imagen_desglos, 
                           bd=0, bg=navbar_color, command=Expand_Loss)
LSS_boton["btn_dsg_LSS"].image = imagen_desglos
LSS_boton["btn_dsg_LSS"].place(relx=0.87, rely=0.19, anchor=tk.CENTER) 

"""
-------------------------------------------------------------------------------
                            Modify content container
-------------------------------------------------------------------------------
"""
cnt_container = tk.Frame(ventana, bg=cnt_color, width=1400, height=780)
cnt_container.pack(side=tk.BOTTOM, after=left_container)

Show_Home()

ventana.geometry("1500x880")
# -------- Ejecutar la aplicación ---------------------------------------------
ventana.mainloop()