import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from PIL import Image


@st.cache_data
def load_data():
    data = pd.read_csv(r"C:\Users\admin\Desktop\innomatics internship\Project_3\resources\auto-mpg.csv")
    return data

df = load_data()


st.sidebar.title("Select visualization")
plot_type = st.sidebar.selectbox("Choose a plot type", ["Histogram", "Boxplot", "Scatter plot"])


st.title("Data Visualization Dashboard")
st.header(":red[Cars] Dataset")
image = Image.open(r"C:\Users\admin\Desktop\innomatics internship\Project_3\resources\car.jpg")

st.image(image, caption='Cars')

if plot_type == "Histogram":
    st.header("Histogram")
    column = st.selectbox("Select a column", df.columns)
    fig, ax = plt.subplots()
    sns.histplot(df[column], kde=False, ax=ax)
    st.pyplot(fig)


if plot_type == "Boxplot":
    st.header("Boxplot")
    column = st.selectbox("Select a column", df.columns)
    fig, ax = plt.subplots()
    sns.boxplot(df[column], ax=ax)
    st.pyplot(fig)


if plot_type == "Scatter plot":
    st.header("Scatter plot")
    x_column = st.selectbox("Select X axis column", df.columns)
    y_column = st.selectbox("Select Y axis column", df.columns)
    fig, ax = plt.subplots()
    sns.scatterplot(x=df[x_column], y=df[y_column], ax=ax)
    st.pyplot(fig)
