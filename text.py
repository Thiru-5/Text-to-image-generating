import requests
import base64
from PIL import Image
from io import BytesIO

# Replace 'your_api_key' with your actual Gemini AI API key
API_KEY = 'AIzaSyDJfI12-lpr5jq9OHoyEgN5VXDjWx2kJtg'
API_URL = 'https://aistudio.google.com/app/apikey'  # Replace with actual API endpoint

def generate_image(prompt):
    headers = {
        'Authorization': f'Bearer {API_KEY}',
        'Content-Type': 'application/json'
    }
    
    data = {
        'prompt': prompt,
        'num_images': 1,  # Number of images to generate
        'size': '512x512'  # Desired image size
    }
    
    response = requests.post(API_URL, headers=headers, json=data)
    
    if response.status_code == 200:
        response_data = response.json()
        image_data = response_data.get('images')[0]  # Assuming the response contains an 'images' list
        return image_data
    else:
        print(f"Error: {response.status_code} - {response.text}")
        return None

def save_image(image_data, filename):
    # Decode base64 image data
    image_bytes = base64.b64decode(image_data)
    image = Image.open(BytesIO(image_bytes))
    image.save(filename)
    print(f"Image saved as {filename}")

if __name__ == "__main__":
    prompt = input("Enter the text prompt for image generation: ")
    
    print("Generating image...")
    image_data = generate_image(prompt)
    
    if image_data:
        save_image(image_data, "generated_image.png")
