import streamlit as st
import plotly.express as px
import backend

#The widget functions are called here
st.title('Weather Forecast for the Next Days')
place = st.text_input('Place: ')
days = st.slider('Forecast Days', min_value=1, max_value=5,
                 help='Select the number of days to forecast')
option = st.selectbox('Select data to view',
                      ('Temperature', 'Sky'))
st.subheader(f'{option} forecast for the next {days} days in {place}')


if place:
    try:
        #Get the data from the API
        filtered_data = backend.get_data(place, days)


        if option == 'Temperature':
            temperatures = [dict['main']['temp'] for dict in filtered_data]
            temperatures = [item/10 for item in temperatures]
            dates = [dict['dt_txt'] for dict in filtered_data]
            #Create the temperature plot
            figure = px.line(x=dates, y=temperatures, labels={'x': 'Dates', 'y':'Temperature (C)'})
            st.plotly_chart(figure)
        elif option == 'Sky':
            images = {'Clear': 'images/clear.png', 'Clouds': 'images/cloud.png', 'Rain': 'images/rain.png',
                      'Snow': 'images/snow.png'}
            sky_conditions = [dict['weather'][0]['main'] for dict in filtered_data]
            #Renders the image of the sky
            image_paths = [images[con] for con in sky_conditions]
            st.image(image_paths, width=115)
    except KeyError:
        st.write('That place does not exist.')