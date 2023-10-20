if os.path.exists(filename):
    # Read the content from the generated filename
    with open(filename, "r", encoding="utf-8") as file:
        youtube_content = file.read().strip()
        
        
        print(filename +" This txt file is now set as script")

# Increment the counter for the next run
counter += 1

    # Generate the filename for the next run
filename = f"{base_filename}{counter}.txt"

# Print a message when all existing files have been processed
print("All existing YouTube script files have been processed.")
print(filename +" This Txt file will be set as script the next time")