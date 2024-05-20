import streamlit as st
import pandas as pd
import numpy as np



st.write("""
# Fundamental Analysis


""")
col1=st.sidebar
st.sidebar.header('User Input Features')

st.sidebar.markdown("""
[Example CSV input file](https://docs.google.com/spreadsheets/d/1cOPONCbGayUIClZyjN3GfTg9GCCV4k0GLXRMKdoimE8/edit?usp=sharing)
""")


uploaded_file = st.sidebar.file_uploader("Upload your input CSV file", type=["csv"])
if uploaded_file is not None:
    input_df = pd.read_csv(uploaded_file)
else:
    input_df = pd.read_csv("streamlit/Sample.csv")
   # def user_input_features():
    #    island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
     #   sex = st.sidebar.selectbox('Sex',('male','female'))
      #  bill_length_mm = st.sidebar.slider('Bill length (mm)', 32.1,59.6,43.9)
       # bill_depth_mm = st.sidebar.slider('Bill depth (mm)', 13.1,21.5,17.2)
        #flipper_length_mm = st.sidebar.slider('Flipper length (mm)', 172.0,231.0,201.0)
       # body_mass_g = st.sidebar.slider('Body mass (g)', 2700.0,6300.0,4207.0)
        #data = {'island': island,
         #       'bill_length_mm': bill_length_mm,
 #               'bill_depth_mm': bill_depth_mm,
  #              'flipper_length_mm': flipper_length_mm,
   #             'body_mass_g': body_mass_g,
    #            'sex': sex}
     #   features = pd.DataFrame(data, index=[0])
      #  return features
  #  input_df = user_input_features()




st.subheader('User Input features')

if uploaded_file is not None:
    st.write(input_df)
else:
    st.write('Awaiting CSV file to be uploaded. Currently using example input parameters .')
    

df=input_df
st.subheader('Profitability Ratios')
st.write("EBITDA  : " + str(df["Total Revenue"][0] - df["Other Income"][0]-df["Total Expense"][0]+df["Finance Cost"][0]+df["Depreciation"][0]))
st.write("EBITDA Margin : " + str(int(df["Total Revenue"][0] - df["Other Income"][0]-df["Total Expense"][0]+df["Finance Cost"][0]+df["Depreciation"][0])/int(df["Total Revenue"][0] - df["Other Income"][0])))
st.write("PAT Margin : "+str(df["PAT"][0]/df["Total Revenue"][0]))
st.write("RoE :"+str(df["Net Profit"][0]/df["Shareholder Equity"][0]))
st.write("Asset Turnover : "+str(df["Net Sales"][0]/df["Total Assets"][0]))
st.write("Financial Leverage : "+str(df["Total Assets"][0]/df["Shareholder Equity"][0]))
st.write("PAT Margin : "+str(df["PAT"][0]/df["Total Revenue"][0]))

st.subheader('Leverage Ratios')
st.write("Interest Coverage Ratio : "+str((df["Total Revenue"][0] - df["Other Income"][0]-df["Total Expense"][0]+df["Finance Cost"][0])/df["Interest Payment"][0]))
st.write("Debt to equity Ratio : "+str(df["Total Debt"][0]/df["Total Equity"][0]))
st.write("Debt to Asset Ratio : "+str(df["Total Debt"][0]/df["Total Assets"][0]))
st.write("Financial Leverage : "+str(df["Total Assets"][0]/df["Shareholder Equity"][0]))

st.subheader('Operating Ratios')
st.write("Fixed Assets Turnover : "+str(df["Operating Revenues"][0]/df["Total Assets"][0]))
st.write("Working Capital Turnover : "+str(df["Operating Revenues"][0]/(df["Total Assets"][0]-df["Total Liabilities"][0])))
st.write("Total Assets Turnover : "+str(df["Operating Revenues"][0]/df["Total Assets"][0]))

st.subheader('Valuation Ratios')
st.write("P/S : "+str(df["Share price"][0]*df['Number of Shares'][0]/df["Total Revenue"][0]))
st.write("P/BV : "+str(df["Share price"][0]/((df["Share price"][0]+df['Reserves'][0])/df["Number of Shares"][0])))
st.write("P/E : "+str(df["Share price"][0]*df['Number of Shares'][0]/df["PAT"][0]))
