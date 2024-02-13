# Import Libraries 
import pandas as pd 
import streamlit as st
import plotly.express as px
import os 

# Provide info about project
st.title('TripleTen: Project Four')
st.subheader('Car Advertisement Analysis By Brandon Levan')
st.write("Using a car advertisement data set, I've created two plots below that visual how certain attributes impact used car sales. [Here is the link to my GitHub Repository That Generates This Web App](https://github.com/brandon-levan/TripleTen_Sprint_Four_Project)")

# Add divider
st.divider()

# Create variable path to csv 
path = os.path.dirname(__file__)
my_file = path+'/vehicles_us.csv'

# Read in csv
vehicles = pd.read_csv(my_file)

# Convert data types 
vehicles['price'] = vehicles['price'].astype(float)
vehicles['model_year'] = vehicles['model_year'].astype('Int64')
vehicles['model'] = vehicles['model'].astype(str)
vehicles['condition'] = vehicles['condition'].astype(str)
vehicles['cylinders'] = vehicles['cylinders'].astype('Int64')
vehicles['fuel'] = vehicles['fuel'].astype(str)
vehicles['odometer'] = vehicles['odometer'].astype(float)
vehicles['transmission'] = vehicles['transmission'].astype(str)
vehicles['type'] = vehicles['type'].astype(str)
vehicles['paint_color'] = vehicles['paint_color'].astype(str)
vehicles['is_4wd'] = vehicles['is_4wd'].astype('Int64')
vehicles['date_posted'] = vehicles['date_posted'].astype('datetime64[ns]')
vehicles['days_listed'] = vehicles['days_listed'].astype('Int64')

# Change column names
vehicles = vehicles.rename(columns={"price": "Price", "model_year": "Model Year", "model": "Model", "condition": "Condition", "cylinders": "Cylinders", "fuel": "Fuel", "odometer": "Odometer", "transmission": "Transmission", "type": "Type", "paint_color": "Paint Color", "is_4wd": "Is 4WD", "date_posted": "Date Posted", "days_listed": "Days Listed"})

# Create header
st.header("How Each Attribute Affects a Car's Selling Price")

# Create toggle that allows user to hide or show the scatter plot. Default toggle to true
plot_one = st.toggle('Toggle off to Hide Scatter Plot', value=True)

# If the toggle is set to true than show the scatter plot
if plot_one:

    # Use radio button to allow users to choose which attribute they want to use as the x-axis to compare against price
    genre = st.radio("Choose Which Attribute You Want to use as the X-Axis"
                    , ["Cylinders", "Model Year", "Condition"]
                    , index=0
                    , horizontal=True
                    )

    # Configure parameters of Scatter Plot
    fig_one = px.scatter(vehicles, x=genre, y="Price", color = "Condition", symbol="Condition", hover_data=['Model'], title= "Scatter plot of " + genre + " vs. Price")
    
    # Plot Scatter Plot
    st.plotly_chart(fig_one, theme="streamlit", use_container_width=True)

# Create toggle that allows user to hide or show the histogram. Default toggle to true
plot_two = st.toggle('Toggle off to Hide Histogram', value=True)

# If the toggle is set to true than show the histogram
if plot_two:

    # Use select box to allow users to choose which attribute they want to use as the color option.
    # Histogram will box count by model year and color option 
    # Took a few attributes just to demonstrate usage of select box feature 
    option = st.selectbox("You'd Like to see Count of Car Sales By Model Year and..."
                         , ('Type', 'Paint Color', 'Transmission', 'Condition')
                         )

    # Configure parameters of Histogram
    fig_two = px.histogram(vehicles, x="Model Year", color= option, title= "Histogram of Model Year vs. " + option)
    
    # Plot Histogram 
    st.plotly_chart(fig_two, theme="streamlit", use_container_width=True)



