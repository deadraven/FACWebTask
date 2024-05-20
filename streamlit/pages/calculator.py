import streamlit as st
import plotly.express as px
import numpy as np
col1 = st.sidebar
col2, col3 = st.columns((10000,0.01))
col1.header('Input Options FV')

#island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))
PMT = st.sidebar.selectbox('PMT made at time of year',('begining','end'))
N= st.sidebar.slider('Time', 0.0,20.1,10.0)
i= st.sidebar.slider('Interest', -20.1,20.1,0.1)
Amount = st.sidebar.text_input('Amount', 1000)
dep = st.sidebar.text_input('Yearly_deposit', 50.0)
col1.header('Input Options PV')

#island = st.sidebar.selectbox('Island',('Biscoe','Dream','Torgersen'))

N2= st.sidebar.slider('Time', 0.0,20.1,10.2)
i1= st.sidebar.slider('Interest', -20.1,20.1,0.2)
Cashflow = st.sidebar.text_input('CashFlow', 1000)
init = st.sidebar.text_input('Initial Investment', 50.1)

if(PMT=="begining"):
    l=1
def joke(N):
    return  float(dep)/i*100*(pow(1+i/100,N+l)-1)+float(Amount)*pow(1+i/100,N)
def joker(N):
    return  float(Cashflow)/(pow(1+i1/100,N))-float(init)






col2.write("# Future value")
col3.write("# Present value")
col2.write("")
col2.write("### Future value calculated :"+str(joke(N)))
d=np.linspace(0,N,1000)
F=joke(d)
col2.plotly_chart(px.line(x=d,y=(F)),use_container_width=True)
col3.write("### Present value calculated :"+str(joker(N2)))
d=np.linspace(0,N2,1000)
F=joker(d)
col3.plotly_chart(px.line(x=d,y=(F)),use_container_width=True)
