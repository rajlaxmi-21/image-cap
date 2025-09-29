from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
import torch
from PIL import Image

model = VisionEncoderDecoderModel.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
processor = ViTImageProcessor.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer = AutoTokenizer.from_pretrained("nlpconnect/vit-gpt2-image-captioning")
tokenizer.pad_token = tokenizer.eos_token

device = torch.device("cpu")
model.to(device)

def generate_caption(image):
    # image = Image.open(image_path)
    pixel_values = processor(images=image, return_tensors="pt").pixel_values.to(device)
  
    attention_mask = torch.ones(pixel_values.shape[:2], dtype=torch.long).to(device)
    output_ids = model.generate(pixel_values, max_length=16, attention_mask=attention_mask)
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

