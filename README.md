# Time Series Analysis and Forecasting

## Objective
The aim of this project is time series analysis and forecasting, specifically focused on sensor data. By exploring basic concepts, developing MA and autoregressive models, and applying them to sensor data.

## Data Description
The dataset used in this project consists of IoT sensor data from a chiller. It contains the following columns:

- Time: Timestamp at which the sensor reading was taken.
- IOT_Sensor_Reading: Reading obtained from the primary sensor at the corresponding timestamp.
- Error_Present: Indicates whether an error was present while taking the sensor reading (binary variable).
- Sensor 2: Reading obtained from a subordinate sensor at the same timestamp.
- Sensor_Value: Final value to be predicted, potentially derived from the primary sensor reading.

## Tech Stack
- Language: Python
- Libraries: pandas, numpy, matplotlib, scipy.stats, statsmodels, seaborn

## Approach
- Read the data.
- Preprocess the data.
- Perform Exploratory Data Analysis (EDA).
- Check for stationarity in the data.
- Analyze ACF and PACF plots.
- Build the following models:
-- Moving average (MA).
-- First order autoregressive (AR).
-- Second/general order autoregressive (AR).
-- Third order autoregressive (AR).
-- Fourth order autoregressive (AR).
- Evaluate the models' performance.

## Project Structure
|-- InputFiles
    -- sensor_data.csv
|-- SourceFolder
    |-- ML_Pipeline
        -- acf.py
        -- autocovariance.py
        -- Autoregressor.py
        -- EDA.py
        -- MA_model.py
        -- RandomWalk.py
        -- Stationarity.py
        -- Whitenoise.py
        -- preprocessingpy
    |-- Engine.py
