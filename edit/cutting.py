import ffmpeg
import os

timestamps = [0, 10, 13, 16, 72, 74, 125, 128, 170, 174, 202, 206, 238, 241, 277, 280, 385, 388, 419, 422, 465, 469, 520, 525, 585, 590, 625, 630, 733]
input_video_path = "source_5.mp4"
output_folder = "output_clips_5/"

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

for i in range(len(timestamps) - 1):
    start_time = timestamps[i]
    end_time = timestamps[i + 1]
    output_path = f"{output_folder}/clip_{i + 1}.mp4"
    
    try:
        (
            ffmpeg
            .input(input_video_path, ss=start_time, to=end_time)
            .output(output_path, vcodec='copy', acodec='copy')  # Correct codec options
            .run()
        )
        print(f"Saved clip {i + 1}: {output_path}")
    except ffmpeg.Error as e:
        print(f"Error processing clip {i + 1}: {e.stderr.decode('utf-8')}")
