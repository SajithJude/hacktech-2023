import streamlit as st
import pandas as pd
import statsmodels.formula.api as smf

# load sample data
df = pd.read_csv('sample_data.csv')

# get list of available input parameters from statsmodels.formula.api documentation
input_params = ['formula', 'data', 'subset', 'drop_cols', 'weights', 'missing', 'groups',
                're_formula', 'vc_formula', 're_weights', 'cov_struct', 'use_t', 'ddof']

# create dropdown menu for selecting input parameters
selected_params = st.multiselect('Select input parameters', input_params)

# create dictionary of selected input parameters and their corresponding values
input_dict = {}
for param in selected_params:
    input_dict[param] = st.text_input(param, '')

# run model with selected input parameters and display results
if st.button('Run model'):
    model = smf.mixedlm(**input_dict).fit()
    st.write(model.summary())
