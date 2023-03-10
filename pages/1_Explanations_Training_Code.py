import streamlit as st
import pandas as pd
import openai
import os 


openai.api_key =  os.getenv("APIKEY")


with st.expander("How to use"):
            st.markdown("""
    
                #### Upload your dataset in CSV format, 
                #### Type a one line description about the dataset,
                #### Select all the columns in the dataset
                #### Enter a one line description about the Coulumn in each input field and press enter
                #### Click Generate Explanation to understand the best practice and reasons to select columns
                #### Click Generate code to Generate a python Machine learning code to train the model with the selected parameters
                """)

# Read CSV file
uploaded_f = st.file_uploader('Upload CSV', type=['csv'])

if uploaded_f is not None:
# Display column selection checkboxes
    df = pd.read_csv(uploaded_f)
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

if st.button("Generate Explanation :"):

    inpt = "Generate an explanation on which of the following columns to as training parameters for a dataset about " + context + " . " + "Column description :" +  str(column_descriptions)
    st.write(inpt)

    outpt = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=inpt,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
    explan= outpt.choices[0].text.strip()
    st.write(explan)
    st.stop()

if st.button("Generate Code :"):

    inpt_code = "Generate training code in python selecting the best parameters from the following columns of a dataset about " + context + " . " + "Column description :" +  str(column_descriptions)
    st.write(inpt_code)

    outpt = openai.Completion.create(
                                        engine="text-davinci-003",
                                        prompt=inpt_code,
                                        max_tokens=3600,
                                        n=1,
                                        stop=None,
                                        temperature=0.5,
                                        )
    explan_code= outpt.choices[0].text.strip()
    st.code(explan_code)
    st.stop()



