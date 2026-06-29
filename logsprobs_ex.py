import os
from litellm import litellm
from dotenv import load_dotenv
import math

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
LLM_MODEL = "gpt-4o-mini";

prompt = [
    {
        "role": "user",
        "content": "The capital of Brazil is"
    }
]

response = litellm.completion(
    model = LLM_MODEL,
    logprobs = True,
    top_logprobs = 5,
    messages = prompt
)

top_logprobs = response.choices[0].logprobs.content[0].top_logprobs
chosen_token = response.choices[0].message.content

print(f"Prompt: {prompt[0]['content']}")
print(f"The model chosen the token: {chosen_token}")

for logprob in top_logprobs:
    prob_percentage = math.exp(logprob.logprob) * 100
    print(f" - Token: '{logprob.token}', Prob: {prob_percentage: .4f}%")