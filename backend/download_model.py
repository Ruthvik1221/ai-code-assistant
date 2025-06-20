from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

model_name = "codellama/CodeLlama-7b-hf"
model = AutoModelForCausalLM.from_pretrained(model_name, torch_dtype=torch.float16)
tokenizer = AutoTokenizer.from_pretrained(model_name)

model.save_pretrained("./codellama-7b-model")
tokenizer.save_pretrained("./codellama-7b-model")

