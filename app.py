# Cell 1: Setup
import streamlit as st
from openai import OpenAI
import os

# Get your OpenAI API key from environment variables 
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
openai.api_key = api_key

# Cell 2: Title & Description
st.title('📊 Chart Decision Assistant')
st.markdown('''
This app assists you in choosing the most suitable chart for your data analysis.
Input your data type and the question you are asking about your data.
''')

# Cell 3: Function to generate text using OpenAI
def analyze_text(data_type, question):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return
    
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI
    prompt = f"Suggest the most appropriate type of chart to use for a {data_type} data type when the question is: '{question}'."

    response = openai.Completion.create(
        model=model,
        prompt=prompt,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].text.strip()

# Since generating an image is not directly relevant to the chart decision assistant, 
# we'll comment out the image generation function. If needed, it can be added back in.
# Cell 4: Function to generate the image (commented out)
# def generate_image(text):
#     # ...

# Cell 5: Streamlit UI for Chart Decision
data_type = st.selectbox("Select the data type:", ("Categorical", "Numerical", "Ordinal", "Continuous", "Discrete"))
question_about_data = st.text_area("Enter the question you are asking about this data:")

if st.button('Decide Chart Type'):
    with st.spinner('Analyzing your data and question...'):
        chart_type_suggestion = analyze_text(data_type, question_about_data)
        st.success(f"The appropriate chart type for your data and question might be: {chart_type_suggestion}")

# The rest of the image generation UI code is commented out as it's not part of the chart assistant functionality.
# if st.button('Generate Thumbnail'):
#     # ...
