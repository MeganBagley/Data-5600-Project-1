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
    snow_making = (6, 1, size=n)  # based on a slight premium compared to the actual price
    days_open_last = (1, 0.3, size=n)  # AI wrote these two lines making discount contingent on promotion
    runs = 
    avgsnow = rng.normal(5, 1, size=n)  # determined based on average 16oz peanut butter grocery pricing
    error = rng.normal(0, sigma, size=n)
    sentiment = beta_0 + beta_promotion * promotion + beta_competitor_pricing * competitor_pricing + beta_discount * discount + beta_price * effective_price + error
    return snow_making, days_open_last, runs, avgsnow, competitor_pricing, error

sentiment, snow_making, days_open_last, runs, avgsnow, error = sim_data(
    n=200, beta_0=500, beta_promotion=0.3, beta_competitor_pricing=6,
    beta_discount=-0.3, beta_price=5, sigma=1
)
