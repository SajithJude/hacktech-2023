import streamlit as st
import pandas as pd
import altair as alt

# Set page title
st.set_page_config(page_title='CSV Plotting', layout='wide')

# Page title and description
st.title('CSV Plotting')
st.write('Upload a CSV file and select columns to visualize.')

# Upload file
uploaded_file = st.file_uploader('Upload CSV', type=['csv'])

if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Select columns to visualize
    st.write('### Select Columns to Visualize')
    columns = list(df.columns)
    x_col = st.selectbox('X axis', options=columns)
    y_cols = st.multiselect('Y axis', options=columns)

    # Select visualization type
    st.write('### Select Visualization Type')
    scatter_plot = st.checkbox('Scatter Plot', value=True)
    line_plot = st.checkbox('Line Plot')
    bar_graph = st.checkbox('Bar Graph')

    # Generate plots
    if scatter_plot or line_plot or bar_graph:
        for plot_type in ['scatter', 'line', 'bar']:
            if (plot_type == 'scatter' and scatter_plot) or \
               (plot_type == 'line' and line_plot) or \
               (plot_type == 'bar' and bar_graph):
                st.write(f'### {plot_type.capitalize()} Plot')
                chart = alt.Chart(df).mark_circle() if plot_type == 'scatter' else \
                        alt.Chart(df).mark_line() if plot_type == 'line' else \
                        alt.Chart(df).mark_bar()
                chart = chart.encode(
                    x=x_col,
                    y=alt.Y(y_cols),
                    tooltip=columns
                ).interactive()
                st.altair_chart(chart, use_container_width=True)
