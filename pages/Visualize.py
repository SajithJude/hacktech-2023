import streamlit as st

modelhere = st.session_state['modelols']

st.write(modelhere.summary())
dependent_variable = str(modelhere.model.endog_names)
independent_variables = str(modelhere.model.exog_names[1:])
coefficients = str(modelhere.params)
r_squared = str(modelhere.rsquared)

prompt = "Generate a mathematical equation for where the OLS results are " + " Dependent variable :" + dependent_variable + " " + " Independent variables: " + " "+ independent_variables  + " " + " Coefficients :" + " " + coefficients + " " + " R-squared :"+ " " + r_squared
st.write(prompt)

# import pandas as pd
# import altair as alt

# # Set page title
# st.set_page_config(page_title='CSV Scatter Plot', layout='wide')

# # Page title and description
# st.title('CSV Scatter Plot')
# st.write('Upload a CSV file, select columns to plot, and generate a scatter plot.')

# # Upload file
# uploaded_file = st.file_uploader('Upload CSV', type=['csv'])

# if uploaded_file is not None:
#     # Read CSV
#     df = pd.read_csv(uploaded_file)

#     # Select columns to plot
#     st.write('### Select Columns to Plot')
#     columns = list(df.columns)
#     x_col = st.selectbox('X axis', options=columns)
#     y_col = st.selectbox('Y axis', options=columns)

#     # Generate scatter plot
#     st.write('### Scatter Plot')
#     chart = alt.Chart(df).mark_circle().encode(
#         x=x_col,
#         y=y_col,
#         tooltip=columns
#     ).interactive()
#     st.altair_chart(chart, use_container_width=True)



