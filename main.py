import streamlit as st
import plotly.express as px

st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days to forecast')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} forecast for the next {days} days in {place}')


dates = ['2022-22-10', '2022-23-10', '2022-24-10', '2022-25-10']
temp = [10, 15, 12, 8]

figure = px.line(x=dates, y=temp, labels={'x': 'Dates', 'y':'Temperature (C)'})
st.plotly_chart(figure)