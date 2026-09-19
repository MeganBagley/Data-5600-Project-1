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
    
    snow_making = rng.normal(300, 200, size=n).clip(min=0)
    days_open_last = rng.normal(130, 20, size=n).clip(min=0)
    runs = rng.normal(70, 20, size=n).clip(min=1)
    avgsnow = rng.normal(400, 150, size=n).clip(min=0)
    error = rng.normal(0, sigma, size=n)
    return sentiment, snow_making, days_open_last, runs, avgsnow, error

    sentiment_latent = (
        beta_0
        + beta_snow_making * snow_making
        + beta_days_open_last * days_open_last
        + beta_runs * runs
        + beta_avgsnow * avgsnow
        + error
    )
    sentiment = np.clip(np.round(sentiment_latent), 1, 7)  # 7-point scale
)
sentiment, snow_making, runs, avgsnow, error = sim_data(
    n=200, beta_0=500, snow_making=0.3, runs=6,
    avgsnow=-0.3, sigma=1
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
