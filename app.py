# Import Libraries 
import pandas as pd 
import streamlit as st
import plotly.express as px
import os 

# Provide info about project
# Create streamlit headers
# Requirement - at least one st.header with text
st.title('TripleTen: Project Four')
st.subheader('Car Advertisement Analysis By Brandon Levan')
st.write("Using a car advertisement data set, I've created two plots below that visual how certain attributes impact used car sales. Here is the link to my GitHub Repository That Generates This Web App - [brandon-levan/TripleTen_Sprint_Four_Project](https://github.com/brandon-levan/TripleTen_Sprint_Four_Project)")

# Add divider
st.divider()

# Create variable path to csv 
path = os.path.dirname(__file__)
my_file = path+'/vehicles_us.csv'

# Read in csv
vehicles = pd.read_csv(my_file)
vehicles = vehicles.rename(columns={"price": "Price", "model_year": "Model Year", "model": "Model", "condition": "Condition", "cylinders": "Cylinders", "fuel": "Fuel", "odometer": "Odometer", "transmission": "Transmission", "type": "Type", "paint_color": "Paint Color", "is_4wd": "Is 4WD", "date_posted": "Date Posted", "days_listed": "Days Listed"})

# Requirement - at least one Plotly Express histogram using st.write or st.plotly_chart
# Requirement - at least one checkbox using st.checkbox that changes the behavior of any of the above components
plot_one = st.toggle('Toggle off to hide Histogram of Blah Compared to Blah', value=True)
if plot_one:

    st.header('Test')
    st.subheader("Define a custom colorscale")
    st.write('Here is a chart of blah blah blah')

    # Inst
    genre = st.radio(
    "What's your favorite movie genre",
    ["Cylinders", "Model Year", "Condition"],
    index=0,
    horizontal=True
    )

    fig_one = px.scatter(vehicles, x=genre, y="Price", color = "Condition", symbol="Condition", hover_data=['Model'], title= "Unsorted Input")
    st.plotly_chart(fig_one, theme="streamlit", use_container_width=True)
    # else:
    #     fig_one = px.scatter(vehicles, x="model_year", y="price", color="condition", symbol="condition", hover_data=['model'], title= "Unsorted Input")
    #     st.plotly_chart(fig_one, theme="streamlit", use_container_width=True)

st.divider()

# Requirement - at least one Plotly Express histogram using st.write or st.plotly_chart
# Requirement - at least one checkbox using st.checkbox that changes the behavior of any of the above components
plot_two = st.toggle('Toggle off to hide Scatter Plot of Blah Compared to Blah', value=True)
if plot_two:

    st.header('Test')
    st.subheader("Define a custom colorscale")
    st.write('Here is a chart of blah blah blah')

    fig_two = px.histogram(vehicles, x="Date Posted", color="Type")
    st.plotly_chart(fig_two, theme="streamlit", use_container_width=True)


