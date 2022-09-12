import sys
version=sys.version_info.major
import os
import numpy as np
import scipy as sp
import math
import scipy.linalg as spla
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib as mpl
import ipywidgets as widgets #Slider, Button, RadioButtons
import scipy.linalg as spla
import warnings
warnings.filterwarnings('ignore')

from ipywidgets import interact, interactive, fixed, interact_manual
from IPython.display import display
from IPython.display import clear_output
######################################################################################
#====================== Interactive notebook functions =============================
######################################################################################
# ------------------------------------ Lorentz-Oscillator----------------------------------------
def  poisson1(n_bar) :
          

########  Creating Dataset  ########################### 

    n = np.linspace(0,20,21) ;

    p = np.zeros(len(n));
    be = np.zeros(len(n));

#  Creating Distribution ############################

    for i in range(0,len(n)):
        p[i] = ((n_bar**n[i])/ math.factorial(n[i]))*math.exp(-n_bar);
        be[i] = (n_bar**n[i])/(((n_bar+1)**n[i])*(n_bar+1))

     
    
################## PLOT ################################  

    ax = plt.axes()  
    ax.grid(False)
    ax.set_facecolor("white")
    ax.spines['bottom'].set_color('black')
    ax.spines['top'].set_color('none') 
    ax.spines['right'].set_color('none')
    ax.spines['left'].set_color('black')
    ax.set_xlabel("n",fontweight = 'bold',fontsize = 12)
    ax.set_ylabel("P(n)",fontweight = 'bold',fontsize = 12,style ='italic')
    ax.set_xlim(0,20)
    plt.bar(n,p,width = 1,color = 'mediumslateblue' ,edgecolor ='black' )
    plt.plot(n,be,linewidth = 2,color = 'red' )
    plt.rcParams["font.serif"] = "Times New Roman"




