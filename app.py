

# Is the irrigation mode (localized, not applicable, gravity, aspersion, pivot, gravity_localized, localized_pivot) used the same for each crop type (Zucchini, Potato, Tomato, Green bean, Coriander and parsley, Cucumber, Mint, Eggplant, Carrot, Onion, Cauliflower, Green cabbage, Celery, Kiwat tomato, Lettuce, Artichoke, Strawberry, Hot pepper, Helda bean, Absinthe, Blueberry, Jerusalem artichoke, Watermelon, Turnip, Pepper, Endive)

import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
client = OpenAI(api_key=api_key)

# Cell 2: Title & Description (Unchanged)
st.title('📊 Chart Decision Assistant')
st.markdown('''
This app assists you in choosing the most suitable chart for your data analysis.
Input your data type and the question you are asking about your data.
''')

# Cell 3: Function to generate text using OpenAI (Unchanged)
def analyze_text(data_types, question):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI
    messages = [
        {"role": "system", "content": "You are an expert in data visualization techniques."},
        {"role": "system", "content": f"Given data types: {data_types}."},
        {"role": "user", "content": f"What is the best type of chart to use if the question is: {question}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content


# Cell 4: Streamlit UI for Chart Decision (Modified to include variable names and types)
st.markdown("### Input your data variables and their corresponding types")

# Create an empty list to hold variable names and types for display
variable_info_display = []

# Use Streamlit's expander to allow users to input multiple variables
with st.expander("Add your variables and types"):
    for i in range(5):  # Allow up to 5 variables for simplicity; adjust as needed
        col1, col2 = st.columns(2)
        with col1:
            variable_name = st.text_input(f"Variable Name {i+1}", key=f"var_name_{i}")
        with col2:
            data_type = st.selectbox(f"Data Type {i+1}", ("Categorical", "Numerical", "Ordinal", "Continuous", "Discrete"), key=f"data_type_{i}")
        # Collect data for display purposes only if variable name is not empty
        if variable_name:
            variable_info_display.append((variable_name, data_type))

question_about_data = st.text_area("Enter the question you are asking about this data:")

if st.button('Decide Chart Type'):
    if not variable_info_display:  # Check if at least one variable has been entered
        st.error("Please enter at least one variable name and type.")
    else:
        with st.spinner('Analyzing your data and question...'):
            # Construct a single message from variable info for display
            data_types = ', '.join([dtype for _, dtype in variable_info_display])
            chart_type_suggestion = analyze_text(data_types, question_about_data)
            st.success(f"The appropriate chart type for your data and question might be: {chart_type_suggestion}")
