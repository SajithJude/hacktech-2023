import streamlit as st
import pandas as pd

# Read CSV file
uploaded_f = st.file_uploader('Upload CSV', type=['csv'])

if uploaded_f is not None:
# Display column selection checkboxes
    df = pd.read_csv(uploaded_file)
    selected_columns = st.multiselect('Select columns', df.columns)

    # Create dictionary of selected column descriptions
    column_descriptions = {}
    context= st.text_input("Enter the context of the data :")
    for col in selected_columns:
        description = st.text_input(f'{col} Describe the data in relation to the context')
        column_descriptions[col] = description

    # Store selected columns as variables with their respective descriptions
    for col, description in column_descriptions.items():
        exec(f"{col} = '{description}'")

    # Display selected column names and descriptions
    for col, description in column_descriptions.items():
        st.write(f"{col}: {description}")
    
    st.stop()

