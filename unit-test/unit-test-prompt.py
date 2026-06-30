import os
from litellm import litellm
from dotenv import load_dotenv
from longest_str import find_longest_string
from textwrap import dedent
import inspect

load_dotenv()
os.environ["ANTHROPIC_API_KEY"] = os.getenv("ANTHROPIC_API_KEY")
LLM_MODEL = "anthropic/claude-haiku-4-5-20251001";
MAX_TOKENS_DEFAULT = 2000

def get_completion(
    prompt,
    model=LLM_MODEL,
    max_tokens=MAX_TOKENS_DEFAULT,
    **kwargs
):
    parsed_messages = []

    if type(prompt) is str:
        parsed_messages = [
            {
                "role": "user",
                "content": prompt
            }
        ]
    else:
        parsed_messages = prompt

    response = litellm.completion(
        model = model,
        messages=parsed_messages,
        max_tokens=max_tokens,
        **kwargs
    )
    
    return response

    
def main():
    function_code = inspect.getsource(find_longest_string)
    print("*** --- Function to be tested --- ****")
    print(f"{function_code}")
    print("*** --- ****")

    prompt = dedent(f"""
        ## Instruction
        Write unit test for the following Python function. Write a short comment above each test function
        to clarify the purpose of the test case.
                    
        ## Context
        Python function:
        ```python
            {function_code}
        ```

        ## Constraints
        * Use unit test
        * Create a test class named `TestFindLongestString`
        * Include at least 4 test cases:
            * A standard case with clear longest string
            * A case where the list is empty
            * A case to test tie-breaking behavior
            * A case to test TypeError
        * Do not include edge cases.
        * The output must be ONLY a single, complete block of Python code.
        * Dot not include any explanations or surrounding text.
                    """)
    
    response = get_completion(prompt)
    print(response.choices[0].message.content)

if __name__ == '__main__':
    main()
