from llama_cpp import Llama
llm = Llama(
    model_path="./models/dolphin-2.2.1-mistral-7b.Q2_K.gguf",
    # n_gpu_layers=-1, # Uncomment to use GPU acceleration
    # seed=1337, # Uncomment to set a specific seed
    # n_ctx=2048, # Uncomment to increase the context window
)
output = llm(
    "Q: Donne le nom des planètes du système solaire. A: ",  # Prompt
    # max_tokens=32, # Generate up to 32 tokens, set to None to generate up to the end of the context window
    # Stop generating just before the model would generate a new question
    stop=["Q:", "\n"],
    echo=True  # Echo the prompt back in the output
)  # Generate a completion, can also call create_completion
print(output)
