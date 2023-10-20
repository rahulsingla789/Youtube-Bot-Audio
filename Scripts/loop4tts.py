import os
from scipy.io.wavfile import write as write_wav
from bark.api import semantic_to_waveform
from bark import generate_audio, SAMPLE_RATE
from IPython.display import Audio
import nltk
import numpy as np

nltk.download('punkt')

os.environ["CUDA_VISIBLE_DEVICES"] = "1"

from bark.generation import (generate_text_semantic, preload_models)

preload_models()



# Define the script with the content replaced
script = f"""{youtube_content}""".replace("\n", " ").strip()

sentences = nltk.sent_tokenize(script)

SPEAKER = "v2/en_speaker_9"
silence = np.zeros(int(0.25 * SAMPLE_RATE))  # quarter second of silence

pieces = []
for sentence in sentences:
    audio_array = generate_audio(sentence, history_prompt=SPEAKER)
    pieces += [audio_array, silence.copy()]

# Concatenate audio pieces
concatenated_audio = np.concatenate(pieces)






# Define the base filename for WAV files along with the desired path
output_directory = "D:\AfterEffectsBot\Assets\\audios"
base_filename = "youtube_audio"

# Initialize a counter
counter = 1

# Generate a unique filename by appending the counter
wav_filename = os.path.join(output_directory, f"{base_filename}{counter}.wav")

# Check if the file exists
while os.path.exists(wav_filename):
    # Use a unique filename for each WAV file
    counter += 1
    wav_filename = os.path.join(output_directory, f"{base_filename}{counter}.wav")

# Use the unique filename to create the WAV file
write_wav(wav_filename, SAMPLE_RATE, concatenated_audio)

# Display the audio
Audio(concatenated_audio, rate=SAMPLE_RATE)

# Print the filename to confirm where the WAV file has been saved
print(f"WAV file has been saved as {wav_filename}.")
