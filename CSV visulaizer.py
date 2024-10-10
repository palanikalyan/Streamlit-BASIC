import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Title
st.title("CSV Data Visualizer")

# File uploader
uploaded_file = st.file_uploader("Upload a CSV file", type="csv")

if uploaded_file is not None:
    # Load the data
    df = pd.read_csv(uploaded_file)
    st.write("### Data Preview", df.head())
    
    # Select columns for plotting
    columns = df.columns.tolist()
    x_col = st.selectbox("Select X-axis", columns)
    y_col = st.selectbox("Select Y-axis", columns)
    
    # Plot data
    if x_col and y_col:
        st.write(f"### Line chart: {x_col} vs {y_col}")
        st.line_chart(df[[x_col, y_col]])
else:
    st.write("Upload a CSV file to see the data and plot.")
