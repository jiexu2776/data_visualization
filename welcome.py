import streamlit as st
import pandas as pd
import matplotlib as plt


st.write('Hello world')

df = pd.read_csv ('Bastar Craton.csv')
st.dataframe(df)


el_list = df.columns.tolist()[27:100]
st.selectbox('select element', el_list)
