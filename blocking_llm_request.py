import os
from litellm import litellm
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
LLM_MODEL = "gpt-4o-mini";

response = litellm.completion(
    model = LLM_MODEL,
    messages = [
        {
            "role": "user",
            "content": "What is the most relevant skills for principal\n" +
             " architecture?. List the top 5 kills. Just list!"
    
        }
    ]
)

print(response.choices[0].message.content)


prompt_tokens = response.usage.prompt_tokens
completion_tokens = response.usage.completion_tokens
total_tokens = response.usage.total_tokens

print(f"Prompt Tokens: {prompt_tokens}")
print(f"Completion Tokens: {completion_tokens}")
print(f"Total Tokens: {total_tokens}")
