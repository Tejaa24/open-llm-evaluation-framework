from transformers import pipeline

print("Loading TinyLlama...")

generator = pipeline(
    "text-generation",
    model="TinyLlama/TinyLlama-1.1B-Chat-v1.0"
)

prompt = "What is 15 + 27?"

result = generator(
    prompt,
    max_new_tokens=20
)

print(result[0]["generated_text"])