import os

# Set the paths to the folders
image_folder = r'C:\Users\jarsh\Downloads\Compressed\archive_3\PKLotYoloData\HasXML\UFPR05\test\images'
label_folder = r'C:\Users\jarsh\Downloads\Compressed\archive_3\PKLotYoloData\HasXML\UFPR05\test\labels'

# Get the list of image files
image_files = os.listdir(image_folder)

# Get the list of label files
label_files = os.listdir(label_folder)

# Iterate over the label files
for label_file in label_files:
    # Check if the corresponding image file exists
    if label_file.replace('.txt', '.jpg') not in image_files:
        # Delete the extra label file
        os.remove(os.path.join(label_folder, label_file))