import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
if api_key:
    client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('📊 Chart Decision Assistant')
st.write('This app assists you in choosing the most suitable chart for analyzing your data based on the types of variables you are working with.')

# Cell 3: Function to decide chart type using OpenAI
def decide_chart(variable_types, question):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return "Error: API key not set."

    # Construct the prompt for the AI
    prompt = f"Suggest the most appropriate type of chart to use when analyzing {', '.join(variable_types)} variables. The question I am asking about the data is: '{question}'."

    response = client.Completions.create(
        model="text-davinci-003",  
        prompt=prompt,
        temperature=0.3,  # A balance between randomness and determinism
        max_tokens=100  # Limit the response length
    )
    
    suggestion = response.choices[0].text.strip()
    return suggestion if suggestion else "Unable to suggest a chart type for this question."

# Cell 4: Streamlit UI for Chart Decision
variable_type1 = st.selectbox("Select the first variable type:", ("Categorical", "Numerical", "Ordinal", "Continuous", "Discrete"), index=0)
variable_type2 = st.selectbox("Select the second variable type (optional):", ("None", "Categorical", "Numerical", "Ordinal", "Continuous", "Discrete"), index=0)

question_about_data = st.text_area("Enter the question you are asking about the data")

if st.button('Decide Chart Type'):
    variable_types = [variable_type1]
    if variable_type2 != "None":
        variable_types.append(variable_type2)
        
    with st.spinner('Analyzing your data and question...'):
        chart_type_suggestion = decide_chart(variable_types, question_about_data)
        if "Error:" not in chart_type_suggestion:
            st.success(f"The appropriate chart type for your data and question might be: {chart_type_suggestion}")
        else:
            st.error(chart_type_suggestion)

