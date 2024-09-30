import os
import pandas as pd
from hugchat import hugchat
from hugchat.login import Login

# Define directories and file paths
save_dir = '/mnt/Data/vivek/Aria/User_1/extracted_data/'
transcript_file_path = os.path.join(save_dir, 'audio_transcript_with_timestamps.csv')
csv_output_path = os.path.join(save_dir, 'video_task_summary.csv')

# Log in to HuggingChat using your credentials
sign = Login("vivek.chavan@rwth-aachen.de", "temp_AI_hackathon123")
cookies = sign.login()
sign.saveCookiesToDir()

# Initialize the chatbot with the cookies
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())
id = chatbot.new_conversation()
chatbot.change_conversation(id)

# Read the CSV file into a DataFrame
df = pd.read_csv(transcript_file_path)

# Convert the DataFrame into a list of dictionaries to send as structured input
csv_data_list = df.to_dict(orient='records')

# Prepare the input for the LLM, describing the task and the CSV data
base_question = (
        "You are a powerful LLM. I have a CSV file containing audio transcript data with timestamps from a video "
        "where an industrial task is being performed. The columns are 'Start Time', 'End Time', and 'Text'. "
        "From this transcript, identify the tools or objects mentioned in the conversation. Also, based on the transcript, "
        "determine the type of task that is being performed, such as 'Assembly', 'Disassembly', 'Object Inspection', etc. "
        "Please return the output as a CSV format with two columns: 'Objects/Tools Used' and 'Task Type'."
        "Here's the transcript data: \n\n" + str(csv_data_list)
)

# Get the chatbot's response to the formatted question
response = chatbot.chat(base_question)

# Print the entire response for debugging
print("Chatbot Response:", response)

# Extract the actual text from the response, assuming it's in the 'content' attribute of the response object
response_text = response.content if hasattr(response, 'content') else str(response)

# Print the raw response text for inspection
print("Raw Response Text:", response_text)

# Try to manually extract the CSV data
try:
    # Assuming the response is structured with the two columns we requested
    response_lines = response_text.split('\n')  # Split response into lines

    # Create lists to store the extracted objects/tools and task types
    objects_tools = []
    task_types = []

    # Process the lines to extract the content
    for line in response_lines:
        if ',' in line:  # Check if the line contains CSV data (has commas)
            parts = line.split(',')
            objects_tools.append(parts[0].strip())  # First part: Objects/Tools
            task_types.append(parts[1].strip())    # Second part: Task Type

    # Create a DataFrame for the CSV content
    df_output = pd.DataFrame({
        'Objects/Tools Used': objects_tools,
        'Task Type': task_types,
        'Raw Response': response_text  # Optionally include the raw response for reference
    })

    # Save the DataFrame as a CSV file
    df_output.to_csv(csv_output_path, index=False)

    print(f"CSV summary saved to {csv_output_path}")
except Exception as e:
    print(f"Error processing response: {e}")
