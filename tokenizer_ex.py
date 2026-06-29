import tiktoken


LLM_MODEL = "gpt-4o-mini";
encoding = tiktoken.encoding_for_model(LLM_MODEL)

text = "Generative AI is great!"
tokensID = encoding.encode(text)
print("Tokens ID", tokensID)

decodedTokens = [encoding.decode([token]) for token in tokensID]
print("Decoded Tokens", decodedTokens)