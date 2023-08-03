import streamlit as st
import pandas as pd
# import matplotlib as plt
import os

file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)


select_file = st.selectbox('select location', file_name_list)

st.write('Hello world')

df = pd.read_csv (select_file)
st.dataframe(df)


el_list = df.columns.tolist()[27:100]
st.selectbox('select element', el_list)

st.multiselect('select location', file_name_list)
