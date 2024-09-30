import os
import whisper
import pandas as pd

# Define paths
save_dir = '/mnt/Data/vivek/Aria/User_1/extracted_data/'
mp4_video = '/mnt/logicNAS/Exchange/Aria/User_8_Assembly1.mp4'

# Ensure the save directory exists
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# Load Whisper model
model = whisper.load_model("base")

# Transcribe the audio from the MP4 with timestamps
result = model.transcribe(mp4_video, verbose=True)

# Initialize an empty string to accumulate transcript with timestamps
transcript_with_timestamps = ""

# Initialize a list to store CSV data (start time, end time, and text)
csv_data = []

# Iterate through each segment to get the text and timestamps
for segment in result['segments']:
    start_time = segment['start']
    end_time = segment['end']
    text = segment['text']

    # Format the transcript with timestamps
    transcript_with_timestamps += f"[{start_time:.2f} - {end_time:.2f}] {text}\n"

    # Append data to the list for CSV
    csv_data.append([start_time, end_time, text])

# Print the transcript with timestamps
print(transcript_with_timestamps)

# Save the transcript with timestamps as a text file
transcript_file_with_timestamps = os.path.join(save_dir, 'audio_transcript_with_timestamps.txt')
with open(transcript_file_with_timestamps, 'w') as f:
    f.write(transcript_with_timestamps)

print(f"Transcript with timestamps saved to {transcript_file_with_timestamps}")

# Convert the CSV data into a Pandas DataFrame
df = pd.DataFrame(csv_data, columns=["Start Time", "End Time", "Text"])

# Save the DataFrame as a CSV file
csv_file_path = os.path.join(save_dir, 'audio_transcript_with_timestamps.csv')
df.to_csv(csv_file_path, index=False)

print(f"Transcript with timestamps saved as CSV to {csv_file_path}")
