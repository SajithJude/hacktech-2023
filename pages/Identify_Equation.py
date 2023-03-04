import streamlit as st
import pandas as pd
import statsmodels.formula.api as smf

st.write('Upload a CSV file, select columns to plot, and generate a scatter plot.')

# Upload file
uploaded_file = st.file_uploader('Upload CSV', type=['csv'])

# get list of available input parameters from statsmodels.formula.api documentation
# input_params = ['formula', 'data', 'subset', 'drop_cols', 'weights', 'missing', 'groups',
#                 're_formula', 'vc_formula', 're_weights', 'cov_struct', 'use_t', 'ddof']

# create dropdown menu for selecting input parameters
# selected_params = st.multiselect('Select input parameters', input_params)



if uploaded_file is not None:
    # Read CSV
    df = pd.read_csv(uploaded_file)
    selected_params = st.multiselect('Select input parameters', df.columns.tolist())
    st.write(selected_params)
    formu = st.text_input(" Input formula ")
    if formu:
        dat = df[selected_params]
        model = smf.ols(formula=formu,data=df).fit()
        st.write(model.summary())
    else:
        st.write("enter the forumla and press enter")
    # # Select columns to plot
    # st.write('### Select Columns to Plot')
    # columns = list(df.columns)
    # x_col = st.selectbox('X axis', options=columns)
    # y_col = st.selectbox('Y axis', options=columns)
# create dictionary of selected input parameters and their corresponding values
# input_dict = {}
# for param in selected_params:
#     input_dict[param] = st.text_input(param, '')

# # run model with selected input parameters and display results
# if st.button('Run model'):
#     model = smf.mixedlm(**input_dict).fit()
#     st.write(model.summary())
