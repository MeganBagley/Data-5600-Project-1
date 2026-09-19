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
    
    snow_making = rng.normal(300, 200, size=n).clip(min=0) # based on average inches in US resorts
    days_open_last = rng.normal(130, 20, size=n).clip(min=0) # based on average days open 2018 season in US resorts
    runs = rng.normal(70, 20, size=n).clip(min=1) # based on average runs in US resorts
    avgsnow = rng.normal(400, 150, size=n).clip(min=0) # based on average snowfall in inches in US resorts
    error = rng.normal(0, sigma, size=n)

    sentiment_latent = ( #creating the sentiment function
        beta_0
        + beta_snow_making * snow_making
        + beta_days_open_last * days_open_last
        + beta_runs * runs
        + beta_avgsnow * avgsnow
        + error
    )
    sentiment = np.clip(np.round(sentiment_latent), 1, 7)  # editing sentiment_latent to fit the model to the 7-point scale
    return sentiment, snow_making, days_open_last, runs, avgsnow, error

sentiment, snow_making, days_open_last, runs, avgsnow, error = sim_data( # run coefficients based on simulation estimates
    n=200, beta_0=-1.0, beta_snow_making=0.002, beta_days_open_last=0.02,
    beta_runs=0.015, beta_avgsnow=0.002, sigma=0.8
)

# create dataframe for storage
df = pd.DataFrame({
   "sentiment": sentiment,
    "snow_making": snow_making,
    "days_open_last": days_open_last,
    "runs": runs,
    "avgsnow": avgsnow,
    "error": error
})

df.head()
