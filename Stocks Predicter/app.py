import streamlit as st
import pandas as pd
import numpy as np
import pickle as pkl
import tradingview_ta as tt
from tradingview_ta import TA_Handler, Interval, Exchange

model = pkl.load(open("model.pkl", "rb"))

st.title("Stock Market Prediction")


st.subheader("Graph of Stock Price")


tesla = TA_Handler(
    symbol="TSLA",
    screener="america",
    exchange="NASDAQ",
    interval=Interval.INTERVAL_1_DAY,
    proxies={'http': 'http://localhost:8501'} # Uncomment to enable proxy (replace the URL).
)
print(tesla.get_analysis().summary)
# Example output: {"RECOMMENDATION": "BUY", "BUY": 8, "NEUTRAL": 6, "SELL": 3}




