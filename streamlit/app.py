import yfinance as yf
import streamlit as st
import plotly.express as px
import pandas as pd

ticker=st.sidebar.text_input("Which Ticker","GOOGL")
st.write("""
# FAC Web Dev Task By Aarnav Gupta 

Use navigation bar to go to other pages

Shown are the stock closing price and volume of """+ticker)



#get data on this ticker
tickerData = yf.Ticker(ticker)

tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-5-31')



# Plot!
st.plotly_chart(px.line(tickerDf,y="Close"), use_container_width=True)
st.write(ticker+" Close vs Time")
st.plotly_chart(px.line(tickerDf,y="Volume"), use_container_width=True)
st.write(ticker+" Trade Volume vs Time")

