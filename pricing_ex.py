import os
from litellm import litellm
from textwrap import dedent
from dotenv import load_dotenv


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

MODEL_PRICING = {
    "gpt-4o-mini": {
        "input_per_1m": 0.40,
        "output_per_1m": 1.60
    }
}

MODEL_NAME = "openai/gpt-4o-mini"

price_info = MODEL_PRICING[MODEL_NAME.split("/")[-1]]
PRICE_PER_INPUT_TOKEN = price_info["input_per_1m"] / 1_000_000
PRICE_PER_OUTPUT_TOKEN = price_info["output_per_1m"] / 1_000_000

def get_completion(prompt, model):
    print("--- Getting completion from LiteLLM ---")

    response = litellm.completion(
        model=model,
        messages=[
          {
            "role": "system",
            "content": "You are a helpful assistant travelling to Switzerland."
          },
          {
            "role": "user",
            "content": prompt
          }
        ]
    )
    return response


def analyze_cost(response):
  if not response:
    print(f"Cannot analyze of faliled API request")
    return
  
  model_used = None
  raw_model_name = response.model

  if "/" in raw_model_name:
    raw_model_name = raw_model_name.split("/")[-1]
  
  for model in MODEL_PRICING.keys():
    if raw_model_name.startswith(model):
      model_used = model
      break;
    
  price_info = MODEL_PRICING[model_used]

  if not price_info:
    print(f"WARNING: Pricing for model '{model_used}' not found!")
    return
  
  usage_data = response.usage
  input_tokens = usage_data.prompt_tokens
  output_tokens = usage_data.completion_tokens

  price_per_input = price_info["input_per_1m"] / 1_000_000
  price_per_output = price_info["output_per_1m"] / 1_000_000

  input_cost = input_tokens * price_per_input
  output_cost = output_tokens * price_per_output
  total_cost = input_cost + output_cost

  #print(f"\n--- Cost breakdown for model: {model_used} ---")
  #print(f"Model response: {response.choices[0].message.content}")
  print(f"Input tokens: \t{input_tokens}\t | Cost: ${input_cost:.8f}")
  print(f"Output tokens:\t{output_tokens}\t | Cost: ${output_cost:.8f}")
  print(f"Total cost: \t${total_cost:.8f}\n")


def main():
  user_prompt = "What is the business city in Switzerland, and what are the most famous places for visit"
  response = get_completion(user_prompt, MODEL_NAME)
  analyze_cost(response)


if __name__ == "__main__":
  main()

          
