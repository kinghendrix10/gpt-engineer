import os

from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq

# OpenAI API example
openai_model = ChatOpenAI(
    model=os.getenv("MODEL_NAME"),
    temperature=0.1,
    callbacks=[StreamingStdOutCallbackHandler()],
    streaming=True,
)

openai_prompt = (
    "Provide me with only the code for a simple python function that sums two numbers."
)

openai_model.invoke(openai_prompt)

# Claude API example
claude_model = ChatAnthropic(
    model=os.getenv("MODEL_NAME"),
    temperature=0.1,
    callbacks=[StreamingStdOutCallbackHandler()],
    streaming=True,
)

claude_prompt = (
    "Provide me with only the code for a simple python function that sums two numbers."
)

claude_model.invoke(claude_prompt)

# Groq API example
groq_model = ChatGroq(
    model=os.getenv("MODEL_NAME"),
    temperature=0.1,
    callbacks=[StreamingStdOutCallbackHandler()],
    streaming=True,
)

groq_prompt = (
    "Provide me with only the code for a simple python function that sums two numbers."
)

groq_model.invoke(groq_prompt)
