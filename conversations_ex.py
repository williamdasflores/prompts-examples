import os
from litellm import litellm
from textwrap import dedent
from dotenv import load_dotenv
from pricing_ex import analyze_cost

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
MODEL_NAME = "openai/gpt-4o-mini"


def simulate_conversation():
    conversation = [
        {
            "role": "system",
            "content": dedent("""
               You are a senior software enginneer well versed in Python.
                Your answers are comprehensive and intuitive to follow.
            """)
        }
    ]
    converation_rounds = [
        "What is Python and what make it so popular for development?",
        "How do I create a virtual environment in that language?",
        "What are the top 3 most important libraries for beginners?",
        "Can you show me a simple example of using those libraries?"
    ]
    
    for round_num, user_message in enumerate(converation_rounds, start=1):
        print(f"--- Round {round_num} ---")
        print(f"User message: {user_message}")

        conversation.append({
            "role": "user",
            "content": user_message
        })

        response = litellm.completion(
            model = MODEL_NAME,
            messages=conversation
        )

        assistant_message = response.choices[0].message.content
        print(f"Assistant: {assistant_message}")

        conversation.append({
            "role": "assistant",
            "content": assistant_message
        })

        print(f"--- ROUND {round_num} SUMMARY COSTS ---")
        analyze_cost(response)



def main():
    response = simulate_conversation()

if __name__ == "__main__":
    main()



        