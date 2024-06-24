
import os
from tqdm import tqdm
from exif import Image
from datetime import datetime

def run():
    # Get image paths
    photo_directory = input("Please type in the path to your photo directory: ")
    filenames = os.listdir(photo_directory)
    image_paths = [f"{photo_directory}\\{filename}" for filename in filenames if os.path.isfile(f"{photo_directory}\\{filename}")]

    # Get offset
    print("Please enter the correct timestamp for the first photo in the directory.")
    actual_initial_datetime = get_actual_datetime_of_first_photo()
    offset = None

    # Modify photo metadata
    for image_path in tqdm(image_paths, desc="Updating Timestamps"):
        try:
            # Open photo
            with open(image_path, "rb") as image_file:
                image = Image(image_file)

            # Read in the EXIF data from the image
            camp_snap_timestamp = image.datetime_original
            camp_snap_datetime = timestamp_to_datetime(camp_snap_timestamp)

            # Calculate actual datetime
            if offset == None:
                offset = actual_initial_datetime - camp_snap_datetime
            actual_datetime = camp_snap_datetime + offset
            actual_timestamp = actual_datetime.strftime("%Y:%m:%d %H:%M:%S")

            # Update datetime in place
            image.datetime = actual_timestamp
            image.datetime_digitized = actual_timestamp
            image.datetime_original = actual_timestamp
            with open(image_path, "wb") as image_file:
                image_file.write(image.get_file())
        except Exception as error:
            print(f"FAILED TO MODIFY TIMESTAMP FOR {image_path}: {error}")

def get_actual_datetime_of_first_photo():
    year = int(input("Year: "))
    month = int(input("Month: "))
    day = int(input("Day: "))
    hours = int(input("Hours: "))
    minutes = int(input("Minutes: "))
    seconds = int(input("Seconds: "))

    return datetime(year, month, day, hours, minutes, seconds)

# Takes an input of YYYY:MM:DD HH:MM:SS, based on Camp Snap exif data
# Returns integers as (Y, M, D, H, M, S)
def timestamp_to_datetime(timestamp):
    date, time = timestamp.split()
    date = date.split(":")
    time = time.split(":")

    year = int(date[0])
    month = int(date[1])
    day = int(date[2])
    hours = int(time[0])
    minutes = int(time[1])
    seconds = int(time[2])

    return datetime(year, month, day, hours, minutes, seconds)

if __name__ == "__main__":
    run()
