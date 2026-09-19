import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statsmodels.formula.api as smf
import bambi as bmb
import arviz as az

# Set randomization seed
rng = np.random.default_rng(42)

# Specify a function to simulate data
# predictors: snow making (in), # of days open last year, # of runs at the resort, avg snow fall(in)
def sim_data(n, beta_0, beta_snow_making, beta_days_open_last, beta_runs, beta_avgsnow, sigma):
    
    snow_making = rng.normal(300, 200, size=n)  # based on average snow making in inches in US resorts
    days_open_last = rng.normal(130, 20, size=n)  # based on average days open in ski resorts in 2018 season
    runs = rng.normal(70,20,size=n) # based on the average run count in the ski resorts
    avgsnow = rng.normal(400, 150, size=n)  #  based on the average snowfall
    error = rng.normal(0, sigma, size=n) 
    sentiment = beta_0 + beta_snow_making * snow_making + beta_days_open_last * days_open_last + beta_runs * runs + beta_avgsnow * avgsnow + error
    return snow_making, days_open_last, runs, avgsnow, error

sentiment, snow_making, days_open_last, runs, avgsnow, error = sim_data(
    n=200, beta_0=500, snow_making=290, days_open_last=140,
    runs=72, avgsnow=420, sigma=1
)

# create dataframe for storage
df = pd.DataFrame({
   "sentiment": sentiment,
    "snow_making": sales,
    "days_open_last": price,
    "runs": discount,
    "avgsnow": promotion,
    "": competitor_pricing,
    "error": error
})

df.head()
