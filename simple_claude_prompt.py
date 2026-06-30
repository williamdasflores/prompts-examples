import os
from litellm import litellm
from dotenv import load_dotenv

load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
LLM_MODEL = "anthropic/claude-haiku-4-5-20251001";

def prompt():
    response = litellm.completion(
        model = LLM_MODEL,
        messages = [
            {
                "role": "user",
                "content": "List the most 10 principal cities in South America. As a selector, use the human development index. Tell me the source"
            }
        ] 
    )
    return response

def main():
    response = prompt()
    print("--- BEGIN ---\n")
    print(f"{response.choices[0].message.content}")
    print("\n--- END ---")

if __name__ == "__main__":
  main()



