import streamlit
import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
streamlit.title('Recipies for Food 🥑 and Yummy Shakes 🥝🍇')

streamlit.header('a basic recipe')
streamlit.text('eggs')
streamlit.text('parmesan cheese')

streamlit.text('avocado!: 🥑')
streamlit.text('lastly, bread: 🍞')

streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')
streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index))
streamlit.dataframe(my_fruit_list)
