import streamlit as st
import pandas as pd
import numpy as np

st.title("My First Streamlit App 🎈")
st.write("This is a quick example to show how easy it is to build an interactive app.")

num_points = st.slider("Select number of data points:", min_value=10, max_value=100, value=50)

st.subheader("Interactive Line Chart")
chart_data = pd.DataFrame(
    np.random.randn(num_points, 3),
    columns=["Series A", "Series B", "Series C"]
)

st.line_chart(chart_data)
