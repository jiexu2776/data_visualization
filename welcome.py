import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure



file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)


select_file = st.selectbox('select location', file_name_list)

st.write('Hello world')

df = pd.read_csv (select_file)
st.dataframe(df)


el_list = df.columns.tolist()[27:100]
x_data = st.selectbox('select x element', el_list)
y_data = st.selectbox('select y element', el_list)



st.multiselect('select location', file_name_list, file_name_list[0])


x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title='simple line example',
    x_axis_label=x_data,
    y_axis_label=y_data)


genre = st.radio(
    "What\'s your factor for standard deviation",
    ('1sd', '2sd', '3sd'))

if genre == '1sd':
  p.line(df[x_data], df[y_data].mean()-df[y_data].std(), line_width=2)
  p.line(df[x_data], df[y_data].mean()+df[y_data].std(), line_width=2)
  st.write('You selected 1sd')
if genre == '2sd':
  p.line(df[x_data], df[y_data].mean()-2*df[y_data].std(), line_width=2)
  p.line(df[x_data], df[y_data].mean()+2*df[y_data].std(), line_width=2)
  st.write('You selected 2sd')
else:
  p.line(df[x_data], df[y_data].mean()-3*df[y_data].std(), line_width=2)
  p.line(df[x_data], df[y_data].mean()+3*df[y_data].std(), line_width=2)
  st.write('You selected 3sd')  



p.circle(df[x_data], df[y_data], color="navy", size = 15, legend_label='Trend', line_width=2)
p.line(df[x_data], df[y_data].mean(), line_width=2)



st.bokeh_chart(p, use_container_width=True)
