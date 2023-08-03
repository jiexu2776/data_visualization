import streamlit as st
import pandas as pd
import os
from bokeh.plotting import figure



file_name_list = []
for i in os.listdir():
  if i.endswith('csv'):
    file_name_list.append(i)




st.write('Hello world')

df = pd.read_csv (select_file)
st.dataframe(df)


el_list = df.columns.tolist()[27:100]
x_data = st.selectbox('select x element', el_list)
y_data = st.selectbox('select y element', el_list)



datafiles = st.multiselect('select location', file_name_list, file_name_list[0])

col1, col2 = st.columns(2)

with col1:
  ele = st.selectbox('element to display', el_list)
  database = []
  for i in datafiles:
    df = pd.read_csv(i)
    database.append(df)
    st.dataframe(database[ele])
    
with col2:
  p = figure(
      title='simple line example',
      x_axis_label=x_data,
      y_axis_label=y_data)
  
  genre = st.radio(
      "What\'s your factor for standard deviation",
      ('1sd', '2sd', '3sd'))
  colors = ['red', 'navy', 'black', 'pink', 'purple']
  for i, color in zip(datafiles, colors):
    df = pd.read_csv(i)
    p.circle(df[x_data], df[y_data], color=color, size = 15, legend_label=i[:-4], line_width=2)
    p.line(df[x_data], df[y_data].mean(), color=color, line_width=2)
    
    if genre == '1sd':
      p.line(df[x_data], df[y_data].mean()-df[y_data].std(),color=color, line_width=2)
      p.line(df[x_data], df[y_data].mean()+df[y_data].std(), color=color,line_width=2)
      st.write('You selected 1sd')
    if genre == '2sd':
      p.line(df[x_data], df[y_data].mean()-2*df[y_data].std(), color=color,line_width=2)
      p.line(df[x_data], df[y_data].mean()+2*df[y_data].std(), color=color,line_width=2)
      st.write('You selected 2sd')
    if genre == '3sd':
      p.line(df[x_data], df[y_data].mean()-3*df[y_data].std(), color=color,line_width=2)
      p.line(df[x_data], df[y_data].mean()+3*df[y_data].std(), color=color,line_width=2)
      st.write('You selected 3sd')  
  
  st.bokeh_chart(p, use_container_width=True)



