import subprocess

# Specify the path to your batch file
batch_file_path = "J:\Stable-diffusion\stable-diffusion-webui\webui-user.bat"  # Replace with the actual path

# Set the working directory to where the batch file is located
working_directory = "J:\Stable-diffusion\stable-diffusion-webui"

try:
    subprocess.Popen(batch_file_path, shell=True, cwd=working_directory)
    print(f"Batch file '{batch_file_path}' has been opened.")
except FileNotFoundError:
    print(f"Batch file not found at '{batch_file_path}'.")
except Exception as e:
    print(f"An error occurred: {e}")
