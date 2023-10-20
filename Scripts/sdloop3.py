import requests
from PIL import Image
import base64
import io
import os

url = "http://127.0.0.1:7860"

# Specify the desired width and height
width = 1000  # Replace with your desired width
height = 562  # Replace with your desired height



# Define the output path
output_path = r'D:\AfterEffectsBot\Assets\descaled images'

# Find the minimum available number for the output filename
counter = 1
while os.path.exists(os.path.join(output_path, f'output{counter}.png')):
    counter += 1

# Find the highest numbered prompt file
highest_prompt_counter = 0
highest_prompt_filename = None

prompt_directory = r'D:\Youtube Bot Audio'  # Replace with the correct path to your prompt files directory

for filename in os.listdir(prompt_directory):
    if filename.startswith("Photoprompt") and filename.endswith(".txt"):
        # Extract the prompt counter from the filename
        try:
            prompt_counter = int(filename.split("Photoprompt")[1].split(".")[0])
            if prompt_counter > highest_prompt_counter:
                highest_prompt_counter = prompt_counter
                highest_prompt_filename = filename
        except ValueError:
            pass

# Read the content of the highest numbered prompt file
if highest_prompt_filename:
    with open(os.path.join(prompt_directory, highest_prompt_filename), 'r') as prompt_file:
        prompt_text = prompt_file.read()
else:
    print("No prompt files found.")

# Check if a valid prompt was found
if 'prompt_text' in locals():
    payload = {
        "prompt": prompt_text,
        "steps": 20,
        "width": width,
        "height": height
    }

    try:
        # Send the API request
        response = requests.post(url=f'{url}/sdapi/v1/txt2img', json=payload)
        response.raise_for_status()  # Check for HTTP request errors

        # Parse the JSON response
        r = response.json()

        # Decode the image data
        image_data = base64.b64decode(r['images'][0])

        # Open the image using PIL
        image = Image.open(io.BytesIO(image_data))

        # Generate a unique filename with the counter
        output_filename = os.path.join(output_path, f'output{counter}.png')

        # Save the image with the unique filename
        image.save(output_filename)

        # Print the prompt text and the filename of the generated image
        print(f"Prompt Used: {prompt_text}")
        print(f"Generated Image: {output_filename}")

    except requests.exceptions.RequestException as e:
        print(f"Request error: {e}")
    except KeyError as ke:
        print(f"KeyError: {ke}")
    except Exception as ex:
        print(f"Error: {ex}")
else:
    print("No valid prompt file found.")
