import cv2
import glob
import os

# Set the path to the folder containing the images
image_folder = r'C:\Users\jarsh\Downloads\Compressed\archive_3\PKLotYoloData\NoXML\UFPR04\images'

# Set the output video file path
video_file = r'C:\Users\jarsh\Downloads\Compressed\archive_3\PKLotYoloData\NoXML\UFPR04\images/video.mp4'

# Get the list of image files
image_files = glob.glob(image_folder + '/*.jpg')

# Check if there are any image files
if not image_files:
    print("No image files found in the folder.")
    exit()

# Sort the image files by name (assuming they are named sequentially)
image_files.sort()

# Create a video writer
fourcc = cv2.VideoWriter_fourcc('M','J','P','G')
fps = 10  # frames per second

# Get the size of the first image
width, height = cv2.imread(image_files[0]).shape[:2]

# Create a video writer
video_writer = cv2.VideoWriter(video_file, fourcc, fps, (width, height))

# Check if the video writer is opened successfully
if not video_writer.isOpened():
    print("Error opening video writer.")
    exit()

# Iterate over the image files
for image_file in image_files:
    # Print the image file path
    print("Processing image:", image_file)
    
    # Read the image
    image = cv2.imread(image_file)

    # Check if the image is read successfully
    if image is None:
        print(f"Error reading image: {image_file}")
        continue

    # Write the image to the video
    video_writer.write(image)
    print(f"Image {image_file} written to video.")

# Release the video writer
video_writer.release()

# Check if the video file exists and has a non-zero size
if os.path.isfile(video_file) and os.path.getsize(video_file) > 0:
    print(f"Video saved successfully: {video_file}")
else:
    print("Error saving video.")
