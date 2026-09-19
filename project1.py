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
def sim_data(n, beta_0, beta_snow_making, beta_days_open_last, beta_runs, beta_avgsnow, beta_sigma):
    snow_making = rng.normal(300, 200, size=n)  # 
    days_open_last = rng.normal(130, 20, size=n)  # 
    runs = rng.normal(
    avgsnow = rng.normal(5, 1, size=n)  # 
    error = rng.normal(0, sigma, size=n)
    sentiment = beta_0 + beta_snow_making * snow_making + beta_days_open_last * days_open_last + beta_runs * runs + beta_avgsnow * avgsnow + error
    return snow_making, days_open_last, runs, avgsnow, competitor_pricing, error

sentiment, snow_making, days_open_last, runs, avgsnow, error = sim_data(
    n=200, beta_0=500, snow_making=0.3, days_open_last=6,
    runs=-0.3, avgsnow=5, sigma=1
)
