from transformers import GPT2Tokenizer, GPT2LMHeadModel

# Load the pre-trained model and tokenizer
tokenizer = GPT2Tokenizer.from_pretrained('gpt2')
model = GPT2LMHeadModel.from_pretrained('gpt2')

# Generate text
prompt = "Once upon a time"
input_ids = tokenizer.encode(prompt, return_tensors='pt')
sample_outputs = model.generate(input_ids, max_length=100, do_sample=True, top_k=50, top_p=0.95, temperature=0.7)
generated_text = tokenizer.decode(sample_outputs[0], skip_special_tokens=True)
print(generated_text)

