# photo-datetime-offset
This is a python script to offset the datetime of all images within a specified directory. This is specifically for photos taken with a Camp Snap camera that I own, but should work for any photos.

# How Does It Work?
This script will go through all the photos in a specified directory and add an offset to the timestamp of each photo. The offset is determined by the difference in the first photo's timestamp and the timestamp you will specify. This project assumes that all files in the specified directory are photos that require the same offset.

# How To
1. Clone this GitHub repo.
2. Navigate to this repository in console.
3. Run `pipenv install` in console.
4. Run `pipenv run py src/main.py` in console.
5. Copy and Paste/Type in the full path to your folder of photos that need their timestamps offset.
6. Type in the date that you want the first photo in your directory to be timestamped as.
7. Wait until the script finishes, and you should be all set!
