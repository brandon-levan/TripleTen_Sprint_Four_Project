# Import Libraries 
import pandas as pd 
import streamlit as st
import plotly.express as px
import os 

st.header('This is a header with a divider', divider='rainbow')
st.header('_Streamlit_ is :blue[cool] :sunglasses:')


path = os.path.dirname(__file__)
my_file = path+'/vehicles_us.csv'

vehicles = pd.read_csv(my_file)

st.table(vehicles.head(20))






# df = px.data.gapminder()

# fig = px.scatter(
#     df.query("year==2007"),
#     x="gdpPercap",
#     y="lifeExp",
#     size="pop",
#     color="continent",
#     hover_name="country",
#     log_x=True,
#     size_max=60,
# )

# tab1, tab2 = st.tabs(["Streamlit theme (default)", "Plotly native theme"])
# with tab1:
#     # Use the Streamlit theme.
#     # This is the default. So you can also omit the theme argument.
#     st.plotly_chart(fig, theme="streamlit", use_container_width=True)
# with tab2:
#     # Use the native Plotly theme.
#     st.plotly_chart(fig, theme=None, use_container_width=True)

agree = st.checkbox('I agree')
if agree:
    st.write('Great!')