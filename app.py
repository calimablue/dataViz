import streamlit as st
from openai import OpenAI
import os

# # Get your OpenAI API key from environment variables 
# api_key = os.getenv("OPENAI_API_KEY")  # Used in production
# client = OpenAI(api_key=api_key)

# # Cell 2: Title & Description
# st.title('📊 Chart Decision Assistant')
# st.markdown('''
# This app helps you decide the best type of chart to use for your data visualization needs.
# Input your data type, the question you are asking about the data, and I'll suggest the most appropriate chart type for you.
# ''')

# # Cell 3: Function to decide chart type
# def decide_chart(data_type, question):
#     if not api_key:
#         st.error("OpenAI API key is not set. Please set it in your environment variables.")
#         return "Error: API key not set."

#     # Instructions for the AI (adjust if needed)
#     instructions = f"Based on the provided data types and their associated best practices for visual representation, which chart type would be most appropriate for visualizing data when the question is: '{question}' and the data type is '{data_type}'?"

#     response = client.Completions.create(
#         model="text-davinci-003",  # Specify the model you wish to use
#         prompt=instructions,
#         temperature=0.3,  # A balance between randomness and determinism
#         max_tokens=60  # Limit the response length
#     )
    
#     # Extract the suggested chart type from the response
#     suggestion = response.choices[0].text.strip()
    
#     return suggestion if suggestion else "Unable to suggest a chart type for this question."

# # Cell 4: Streamlit UI for Chart Decision
# data_type_options = {
#     "Categorical": "such as customer type (New, Returning, VIP)",
#     "Numerical (Quantitative Trend)": "such as monthly sales revenue over time ($100, $200, $300)",
#     "Numerical (Quantitative)": "such as number of employees (10, 20, 30)",
#     "Numerical (Discrete)": "such as grades in different subjects (Math: 30, 39, 75)",
#     "Qualitative": "such as customer feedback (Positive, Neutral, Negative)"
# }

# data_type = st.selectbox(
#     "Select the type of your data:",
#     list(data_type_options.keys()),
#     format_func=lambda x: f"{x}: {data_type_options[x]}"
# )

# question_about_data = st.text_area("What question are you asking about this data?")

# if st.button('Decide Chart Type'):
#     with st.spinner('Analyzing your question...'):
#         chart_type = decide_chart(data_type, question_about_data)
#         if "Error:" not in chart_type:
#             st.success(f"The appropriate chart type for your question might be a: {chart_type}")
#         else:
#             st.error(chart_type)



# # Cell 1: Setup
# import streamlit as st
# from openai import OpenAI
# import os

# Get your OpenAI API key from environment variables
api_key = os.getenv("OPENAI_API_KEY")  # Used in production
if api_key:
    client = OpenAI(api_key=api_key)

# Cell 2: Title & Description
st.title('📊 Chart Decision Assistant')
st.write('This app assists you in choosing the most suitable chart for your data analysis.')

# Cell 3: Function to decide chart type using OpenAI
def decide_chart(data_type, question):
    if not api_key:
        st.error("OpenAI API key is not set. Please set it in your environment variables.")
        return "Error: API key not set."

    # Instructions for the AI
    instructions = f"Suggest the most appropriate type of chart to use for a {data_type} data type when the question is: '{question}'."

    response = client.Completions.create(
        model="text-davinci-003",  # You may update this to the latest model available
        prompt=instructions,
        temperature=0.3,  # A balance between randomness and determinism
        max_tokens=60  # Limit the response length
    )
    
    suggestion = response.choices[0].text.strip()
    return suggestion if suggestion else "Unable to suggest a chart type for this question."

# Cell 4: Streamlit UI for Chart Decision
data_type = st.text_input("Enter the data type (e.g., 'Categorical', 'Numerical')")
variables = st.text_input("Enter your variables (comma-separated)")
question_about_data = st.text_area("Enter the question you are asking about the data")

if st.button('Decide Chart Type'):
    with st.spinner('Analyzing your data and question...'):
        chart_type_suggestion = decide_chart(data_type, question_about_data)
        if "Error:" not in chart_type_suggestion:
            st.success(f"The appropriate chart type for your data and question might be: {chart_type_suggestion}")
        else:
            st.error(chart_type_suggestion)

