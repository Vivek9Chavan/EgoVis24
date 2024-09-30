import os
import cv2  # OpenCV to process video frames
import pandas as pd
import torch
from tqdm import tqdm  # Progress bar for frame processing

# Load DINOv2 model (for future use in 'dinov2' reduction mode)
dinov2_vits14_reg = torch.hub.load('facebookresearch/dinov2', 'dinov2_vits14_reg')

# Define paths
mp4_video = '/mnt/logicNAS/Exchange/Aria/User_8_Assembly1.mp4'
save_dir = '/mnt/Data/vivek/Aria/User_1/extracted_data/frames/'
save_dir_stamped = '/mnt/Data/vivek/Aria/User_1/extracted_data/frames_stamped/'
transcript_file_path = '/mnt/Data/vivek/Aria/User_1/extracted_data/audio_transcript_with_timestamps.csv'

frame_save_ratio = 0.1  # Reduce number of frames to 10%
frame_reduction_mode = 'uniform'  # 'uniform' or 'dinov2'

# Ensure directories exist
os.makedirs(save_dir, exist_ok=True)
os.makedirs(save_dir_stamped, exist_ok=True)

# Load the video
cap = cv2.VideoCapture(mp4_video)
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap.get(cv2.CAP_PROP_FPS)

# Calculate step size for frame reduction based on uniform ratio
frame_step = int(1 / frame_save_ratio)

# Load the transcript CSV with timestamps
transcript_df = pd.read_csv(transcript_file_path)

# Initialize frame counter
frame_counter = 0
saved_frame_counter = 0

# Process the video frames
with tqdm(total=total_frames) as pbar:
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # For uniform frame reduction
        if frame_reduction_mode == 'uniform':
            if frame_counter % frame_step == 0:
                # Save the frame to save_dir
                frame_filename = f'frame_{saved_frame_counter:06d}.jpg'
                cv2.imwrite(os.path.join(save_dir, frame_filename), frame)

                # Try to sync this frame with transcript timestamps
                current_time_sec = frame_counter / fps

                # Check if the current frame falls within a transcript timestamp range
                for idx, row in transcript_df.iterrows():
                    if row['Start Time'] <= current_time_sec <= row['End Time']:
                        # Create subfolder for this transcript range
                        task_folder = os.path.join(save_dir_stamped, f'{row["Start Time"]:.2f}_{row["End Time"]:.2f}')
                        os.makedirs(task_folder, exist_ok=True)

                        # Save the frame to the timestamped folder
                        stamped_frame_path = os.path.join(task_folder, frame_filename)
                        cv2.imwrite(stamped_frame_path, frame)

                        # Optionally: save text from transcript to a file in this folder
                        transcript_text = row['Text']
                        with open(os.path.join(task_folder, 'transcript.txt'), 'w') as f:
                            f.write(transcript_text)

                # Increment saved frame counter
                saved_frame_counter += 1

        # (Optional) For DINOv2 frame reduction mode, add logic here using the DINO model to select frames intelligently.

        # Increment total frame counter
        frame_counter += 1
        pbar.update(1)

# Release video capture
cap.release()

print(f"Frame extraction completed. {saved_frame_counter} frames saved.")
