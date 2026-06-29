import os
from litellm import litellm
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

LLM_MODEL = "gpt-4o-mini";
MAX_TOKENS = 100

response = litellm.completion(
    model = LLM_MODEL,
    stream = True,
    messages = [
        {
            "role": "user",
            "content": "You are a java specialist tutoring a junior developer.Explain the difference between concurrency and parallelism in Java."
        }
    ]
)


for chunk in response:
    if chunk.choices[0].delta.content:
        chunk_content = chunk.choices[0].delta.content
        print(chunk_content, end="", flush=True)

