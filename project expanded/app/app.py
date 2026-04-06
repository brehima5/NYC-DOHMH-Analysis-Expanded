import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import pickle

# Loading precomputed results
with open('Analysis/app/forecast_results.pkl', 'rb') as f:
    all_results = pickle.load(f)

st.title("NYC ILI/Pneumonia Visit Forecasts")
st.write("Select a zipcode to view monthly visit trends and the forecasted upcoming month.")

# Zipcode selector section
zip_code = st.selectbox("Select a Zipcode", sorted(all_results.keys()))

r = all_results[zip_code]
ts = r['ts']
next_month_forecast = r['next_month_forecast']

# --- Forecast Chart (last 6 months + forecast) ---
st.subheader("Monthly Visits & Next Month Forecast")
import matplotlib.dates as mdates

recent = ts.tail(6)
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(recent.index, recent, label='Historical', color='steelblue', marker='o', markersize=5)
ax.plot(next_month_forecast.index, next_month_forecast, label='Forecast', color='red', marker='o', markersize=8)
ax.axvline(x=ts.index[-1], color='gray', linestyle=':', alpha=0.7)
ax.set_title(f'ILI/Pneumonia Visits — Zipcode {zip_code}')
ax.set_xlabel('Month')
ax.set_ylabel('Monthly Visits')
ax.xaxis.set_major_formatter(mdates.DateFormatter('%b %Y'))
ax.xaxis.set_major_locator(mdates.MonthLocator())
plt.xticks(rotation=45, ha='right')
ax.legend()
plt.tight_layout()
st.pyplot(fig)

# --- Next Month Forecast ---
forecast_date = next_month_forecast.index[0]
forecast_value = int(round(next_month_forecast.iloc[0]))
st.subheader("Upcoming Month Forecast")
st.metric(label=forecast_date.strftime('%B %Y'), value=f"{forecast_value} visits")

# --- Last 6 Months Historical ---
st.subheader("Recent Monthly Visits (Last 6 Months)")
last_months = ts.tail(6)
history_df = pd.DataFrame({
    'Month': last_months.index.strftime('%B %Y'),
    'Visits': last_months.values.round(0).astype(int),
})
history_df.index = range(1, len(history_df) + 1)
st.table(history_df)

# --- Model Performance ---
with st.expander("Model Performance (RMSE)"):
    perf_df = pd.DataFrame({
        'Model': ['ARIMA', 'Naive Baseline'],
        'RMSE': [round(r['arima_rmse'], 2), round(r['naive_rmse'], 2)],
    })
    st.table(perf_df)
    if r['arima_rmse'] < r['naive_rmse']:
        st.success("The ARIMA model outperforms the naive baseline.")
    else:
        st.warning("The naive baseline performed better than ARIMA for this zipcode.")