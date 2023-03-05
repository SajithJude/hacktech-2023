import streamlit as st
import pandas as pd
import altair as alt
import openai
import os 


# Set page title
st.set_page_config(page_title='CodeGen', layout='wide')

# Page title and description
st.title('CodeGen')
st.write('A tool By the community for the community to make sustainable innovating easy...')

# Upload file

with st.expander("Visualization tool"):
            uploaded_file = st.file_uploader('Upload CSV', type=['csv'])

            if uploaded_file is not None:
                # Read CSV
                df = pd.read_csv(uploaded_file)

                # Select columns to plot
                st.write('### Select Columns to Plot')
                columns = list(df.columns)
                x_col = st.selectbox('X axis', options=columns)
                y_col = st.selectbox('Y axis', options=columns)

                # Generate scatter plot
                st.write('### Scatter Plot')
                chart = alt.Chart(df).mark_circle().encode(
                    x=x_col,
                    y=y_col,
                    tooltip=columns
                ).interactive()
                st.altair_chart(chart, use_container_width=True)



