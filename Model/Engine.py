import pandas as pd
import numpy as np
import sys 
from datetime import datetime
from ML_Pipeline import Preprocess
from ML_Pipeline import EDA
from ML_Pipeline import Stationarity
from ML_Pipeline import acf
from ML_Pipeline import pacf
from ML_Pipeline import WhiteNoise 
from ML_Pipeline import RandomWalk
from ML_Pipeline import MA_model
from ML_Pipeline import Autoregressor




def main():
    # importing the data
    raw_csv_data = pd.read_csv('../input/'+ 'Data-Chillers.csv') 

    df = raw_csv_data.copy()     # create a copy


    # Preprocess
    df = Preprocess.preprocess(df) 
    
    #covariance matrix
    ac_data = df.set_index('time')
    
    with open('../output/'+ 'log.txt', 'a') as f:
        sys.stdout = f
        print("Run time:",datetime.now())
        print("****************Autocovariance matrix value is:***********************")
        print(np.cov(ac_data, rowvar=False))
    sys.stdout = sys.__stdout__
   
   #EDA
    components_plot = EDA.EDA(df.copy())
    
    #Stationary check
    Stationarity.Stationary(df.copy())
   
    #acf
    acf_plot = acf.acf(df.copy())
    
    #pacf
    pacf_plot = pacf.pacf(df.copy())
    
    #white noise
    whitenoise_plot = WhiteNoise.white_noise(df.copy())

    #randomwalk
    randomwalk_plot = RandomWalk.random_walk(df.copy())
    
    #Moving average model 
    MA_summary = MA_model.MA_model(df.copy())
    
    #First order AR model
    AR_summary = Autoregressor.AR_model(df.copy())
    
    return components_plot, acf_plot,pacf_plot, randomwalk_plot,whitenoise_plot,randomwalk_plot,MA_summary,AR_summary


main()


