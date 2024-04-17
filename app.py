# # Cell 1: Setup
# import streamlit as st
# from openai import OpenAI
# import os

# # Get your OpenAI API key from environment variables 
# api_key = os.getenv("OPENAI_API_KEY")  # Used in production
# client = OpenAI(api_key = api_key)

# # Cell 2: Title & Description
# st.title('📊 Chart Decision Assistant')
# st.markdown('''
# This app assists you in choosing the most suitable chart for your data analysis.
# Input your data type and the question you are asking about your data.
# ''')

# # Cell 3: Function to generate text using OpenAI
# def analyze_text(data_type, question):
#     if not api_key:
#         st.error("OpenAI API key is not set. Please set it in your environment variables.")
#         return

#     client = OpenAI(api_key = api_key)
#     model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

#     # Instructions for the AI
#     messages = [
#         {"role": "system", "content": "You are an expert in data visualization techniques."}, 
#         {"role": "system", "content": "Suggest the most appropriate type of chart to use for a {data_type} data type when the question is: \n{question}"}
#     ]

#     response = client.chat.completions.create(
#         model = model,
#         messages = messages,
#         temperature = 0  # Lower temperature for less random responses
#     )
#     return response.choices[0].message.content

# Is the irrigation mode (localized, not applicable, gravity, aspersion, pivot, gravity_localized, localized_pivot) used the same for each crop type (Zucchini, Potato, Tomato, Green bean, Coriander and parsley, Cucumber, Mint, Eggplant, Carrot, Onion, Cauliflower, Green cabbage, Celery, Kiwat tomato, Lettuce, Artichoke, Strawberry, Hot pepper, Helda bean, Absinthe, Blueberry, Jerusalem artichoke, Watermelon, Turnip, Pepper, Endive)
# # Cell 5: Streamlit UI for Chart Decision
# data_type = st.selectbox("Select the data type:", ("Categorical", "Numerical", "Ordinal", "Continuous", "Discrete"))
# question_about_data = st.text_area("Enter the question you are asking about this data:")

# if st.button('Decide Chart Type'):
#     with st.spinner('Analyzing your data and question...'):
#         chart_type_suggestion = analyze_text(data_type, question_about_data)
#         st.success(f"The appropriate chart type for your data and question might be: {chart_type_suggestion}")

# Cell 1: Setup (Unchanged)
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
def analyze_text(data_type, question):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    client = OpenAI(api_key=api_key)
    model = "gpt-3.5-turbo"  # Using the GPT-3.5 model

    # Instructions for the AI
    messages = [
        {"role": "system", "content": "You are an expert in data visualization techniques."}, 
        {"role": "system", "content": f"Suggest the most appropriate type of chart to use for a {data_type} data type when the question is: \n{question}"}
    ]

    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=0  # Lower temperature for less random responses
    )
    return response.choices[0].message.content

# Cell 4: Function to generate the image
def generate_image(data_type, question):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return

    response = client.images.generate(
        model="dall-e-3",
        prompt=data_type, question,
        size="1024x1024",
        quality="standard",
        n=1,
    )

    # Assuming the API returns an image URL; adjust based on actual response structure
    return response.data[0].url

# Cell 4: Streamlit UI for Chart Decision (Modified)
data_type = st.selectbox("Select the data type:", ("Categorical", "Numerical", "Ordinal", "Continuous", "Discrete"))
variables = st.text_input("Enter your variables (comma-separated, e.g., Age, Salary, Department):")
question_about_data = st.text_area("Enter the question you are asking about this data:")

if st.button('Decide Chart Type'):
    with st.spinner('Analyzing your data and question...'):
        chart_type_suggestion = analyze_text(data_type, question_about_data)
        st.success(f"The appropriate chart type for your data and question might be: {chart_type_suggestion}")

    with st.spinner('Generating Thumbnail...'):
        thumbnail_url = generate_image(data_type, question_about_data)  # Consider adjusting the prompt for image generation if needed
        st.image(thumbnail_url, caption='Generated Thumbnail')



