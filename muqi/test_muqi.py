import pandas as pd
from langchain_community.chat_models import ChatOpenAI
from helper_func_muqi import construct_prompt, invoke_llm

# Replace 'education.csv' with the path to your .csv file
file_path = "education_muqi.csv"

# Step 1: Read the CSV file
education_data = pd.read_csv(file_path)

# Step 2: Initialize the LLM
llm = ChatOpenAI(
    base_url="http://localhost:1234/v1",  # Replace with OpenAI base URL if needed
    api_key="lm-studio",  # API key
    model="gpt-3.5-turbo",  # Specify the model name
    temperature=0.85  # Adjust creativity level
)

# Step 3: Construct the prompt
prompt_messages = construct_prompt(education_data)

# Step 4: Use the LLM to refine and validate the data
response = invoke_llm(llm, prompt_messages)

# Step 5: Print the response
print("LLM's Feedback and Suggestions:")
print(response)
