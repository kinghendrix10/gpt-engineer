import os

from openai import OpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

# OpenAI API example
client = OpenAI(
    base_url=os.getenv("OPENAI_API_BASE"), api_key=os.getenv("OPENAI_API_KEY")
)

response = client.chat.completions.create(
    model=os.getenv("MODEL_NAME"),
    messages=[
        {
            "role": "user",
            "content": "Provide me with only the code for a simple python function that sums two numbers.",
        },
    ],
    temperature=0.7,
    max_tokens=200,
)

print("OpenAI Response:", response.choices[0].message.content)

# Claude API example
claude_client = ChatAnthropic(
    model=os.getenv("MODEL_NAME"),
    temperature=0.7,
    api_key=os.getenv("ANTHROPIC_API_KEY"),
)

claude_response = claude_client.invoke(
    "Provide me with only the code for a simple python function that sums two numbers."
)

print("Claude Response:", claude_response)

# Groq API example
groq_client = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    temperature=0.7,
    api_key=os.getenv("GROQ_API_KEY"),
)

groq_response = groq_client.invoke(
    "Provide me with only the code for a simple python function that sums two numbers."
)

print("Groq Response:", groq_response)
