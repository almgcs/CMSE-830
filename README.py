# CMSE-830
import streamlit as st
import seaborn as sns
import pandas as pd
import plotly.express as px

st.write("""
# Iris Dataset
How can the sepals and petals help distinguish Iris species from one another?
""")

df_iris = sns.load_dataset("iris")

fig = px.scatter_3d(df_iris, x='sepal_length', y='sepal_width', z='petal_width',
              color='petal_length', size='petal_length', size_max=18,
              symbol='species', opacity=0.7)

fig.update_layout(margin=dict(l=0, r=0, b=0, t=0))

st.plotly_chart(fig, use_container_width=False, sharing="streamlit")
