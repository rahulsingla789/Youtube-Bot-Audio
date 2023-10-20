import os
import re  # Import the 're' module for regular expressions

# Define the base filename
base_filename = "youtube"

# Initialize a counter
counter = 1

# Generate a filename by appending the counter
while True:
    filename = f"{base_filename}{counter}.txt"
    if not os.path.exists(filename):
        break
    counter += 1

# Assuming you have the response from OpenAI stored in a variable 'response'
youtube_script = response['choices'][0]['message']['content']

# Define a regular expression pattern to match text within square brackets
pattern = r'\[.*?\]'

# Use the re.sub() function to remove text within square brackets
cleaned_youtube_script = re.sub(pattern, '', youtube_script)

# Write the cleaned content to the generated filename
with open(filename, "w", encoding="utf-8") as file:
    file.write(cleaned_youtube_script)

# Print the filename to confirm where the content has been written
print(f"YouTube script has been written to {filename}.")
