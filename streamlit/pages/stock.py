import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go


st.write("""
# Technical Graphs


""")
col1=st.sidebar
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://docs.google.com/spreadsheets/d/1AnWdX9wNGMagSbPzDzvMcd_zfCLuJFrDHbtmldv_5Uc/edit?usp=sharing)
""")
island = st.sidebar.selectbox('Main',('Candle Stick','Open','Close'))
doll = st.sidebar.selectbox('Technical',('MACD','RSI','Bollinger'))
uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    input_df = pd.read_csv("streamlit/Alternating Framework.csv")
st.subheader('User Input features')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters .')

df=input_df
df.columns = map(str.lower, df.columns)
try:
    df['plotting']=df.index
except:
    pass

try:
    df['plotting']=df["date"]
except:
    pass
try:
    df['plotting']=df["date/time"]
except:
    pass
try:
    df['plotting']=df["time"]
except:
    pass
try:
    df['plotting']=df["datetime"]
except:
    pass
if island=="Close":
     st.write(" ## Closing price")
     st.plotly_chart(px.line(df,x="plotting",y="close"))
if island=='Open':
     st.write(" ## Opening price")
     st.plotly_chart(px.line(df,x="plotting",y="open"))
if island=='Candle Stick':
     st.write(" ## Candle")
     fig=go.Figure(data=[go.Candlestick(x=df['plotting'],
                open=df['open'],
                high=df['high'],
                low=df['low'],
                close=df['close'])])
     st.plotly_chart(fig)


exp1 = df.close.ewm(span = 12, adjust=False).mean()
exp2 = df.close.ewm(span = 26, adjust=False).mean()

df["macd"] = exp1 - exp2
df['sign'] = df.macd-df.macd.ewm(span = 9, adjust=False).mean()
if doll=="MACD":
     st.write(" ## MACD")
     st.plotly_chart(px.line(df,x="plotting",y="sign"))
rsi_period = 14

# to calculate RSI, we first need to calculate the exponential weighted aveage gain and loss during the period
df['gain'] = (df['close'] - df['open']).apply(lambda x: x if x > 0 else 0)
df['loss'] = (df['close'] - df['open']).apply(lambda x: -x if x < 0 else 0)

# here we use the same formula to calculate Exponential Moving Average
df['ema_gain'] = df['gain'].ewm(span=rsi_period, min_periods=rsi_period).mean()
df['ema_loss'] = df['loss'].ewm(span=rsi_period, min_periods=rsi_period).mean()

# the Relative Strength is the ratio between the exponential avg gain divided by the exponential avg loss
df['rs'] = df['ema_gain'] / df['ema_loss']

# the RSI is calculated based on the Relative Strength using the following formula
df['rsi_14'] = 100 - (100 / (df['rs'] + 1))

if doll=="RSI":
     st.write(" ## RSI")
     st.plotly_chart(px.line(df,x="plotting",y="rsi_14"))
import pandas_ta as ta
my_bbands = ta.bbands(df.close, length=20, std=2.5)

df=df.join(my_bbands)
if doll=="Bollinger":
     st.write(" ## Bollinger bands")
     st.plotly_chart(px.line(df,x="plotting",y=["close","BBL_20_2.5","BBU_20_2.5"]))
