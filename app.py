import streamlit as st
import requests
import pandas as pd
import numpy as np

'''
# TaxiFareModel Front End
'''

# st.markdown('''
# Remember that there are several ways to output content into your web page...

# Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
# ''')

# '''
# ## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

# 1. Let's ask for:
# - date and time
# - pickup longitude
# - pickup latitude
# - dropoff longitude
# - dropoff latitude
# - passenger count
# '''

# '''
# ## Once we have these, let's call our API in order to retrieve a prediction

# See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

# 🤔 How could we call our API ? Off course... The `requests` package 💡
# '''

import datetime
with st.form(key='my_form'):
    d = st.date_input(
        "Provide Date",
        datetime.date(2024, 1, 1))

    t = st.time_input(
        'Provide Time',
        datetime.time(0, 00))

    # st.write('Your date ', d)
    # st.write('Your time ', t)

    pickup_datetime = str(d) + " " + str(t)

    pickup_latitude = st.number_input("Provide Pickup Latitude")
    # st.write("Your pickup latitude ", pickup_latitude)

    pickup_longitude = st.number_input("Provide Pickup Longtitude")
    # st.write("Your pickup longtitude ", pickup_longitude)

    dropoff_latitude = st.number_input("Provide Dropoff Latitude")
    # st.write("Your dropoff latitude ", dropoff_latitude)

    dropoff_longitude = st.number_input("Provide Dropoff Longtitude")
    # st.write("Your dropoff longtitude ", dropoff_longitude)

    passenger_count = st.number_input('Provide the number of passengers')
    # st.write("The number of passengers is ", passenger_count)

    submit_button = st.form_submit_button(label='Submit')

    url = 'https://taxifare.lewagon.ai/predict'

    if url == 'https://taxifare.lewagon.ai/predict':

    # st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

    # '''

    # 2. Let's build a dictionary containing the parameters for our API...

    # 3. Let's call our API using the `requests` package...

    # 4. Let's retrieve the prediction from the **JSON** returned by the API...

    # ## Finally, we can display the prediction to the user
    # '''
    #2. Let's build a dictionary containing the parameters for our API...
        data = {
            "pickup_latitude": pickup_latitude,
            "pickup_longitude": pickup_longitude,
            "dropoff_latitude": dropoff_latitude,
            "dropoff_longitude": dropoff_longitude,
            "passenger_count": int(passenger_count),
            "pickup_datetime": pickup_datetime
        }

        #3. Let's call our API using the `requests` package...
        r = requests.get(url, params=data)
        pred_fare = r.json()['fare']

        #4. Let's retrieve the prediction from the **JSON** returned by the API...
        st.markdown("Your Predicted Fare is :")
        st.write(pred_fare)

# df = pd.DataFrame(
#     np.random.randn(1000, 2) / [50, 50] + [37.76, -122.4],
#     columns=['lat', 'lon'])

# st.map(df)
