import os
from os import system, name
from termcolor import colored

## -- Utility -- ##

def create_dir():
    """
    Creates the "downloads" folder if it doesnt exist.

    args:
        - None
    
    returns:
        - None

    """

    download_dir = "downloads"
    dir_exists = os.path.exists(download_dir)

    if not dir_exists:
        os.makedirs(download_dir)

def delete_video(filename):
    """
    Deletes a specific video-file.

    args:
        - filename (str) : filename of the video
    
    returns:
        - None

    """

    try:
        os.remove(filename)
        print(colored(f"Successfully deleted video: {filename}", "light_green"))

    except Exception as e:
        print(colored(f"Error deleting MP4 file: {str(e)}", "red"))

def format_file_size(size):
    """
    Function to calculate video size in bytes.

    args:
        - size : Size of video
    
    returns:
        - None
    
    """

    if size < 1024:
        return f"{size} bytes"
    elif size < 1024*1024:
        return f"{size / 1024:.2f} KB"
    else:
        return f"{size / (1024*1024):.2f} MB"
    
def clear():
    """
    Function to clear terminal screen prints.

    args:
        - None
    
    returns:
        - None
    
    """
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')