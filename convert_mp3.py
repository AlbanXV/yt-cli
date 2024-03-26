import os
from moviepy.editor import VideoFileClip
from termcolor import colored
from utility import *

def convert_to_mp3(filename):
    """
    Converts the chosen file to mp3.

    args:
        - filename (str): Name of the downloaded video
    
    returns:
        - mp3_path (str)

    """

    try:
        video = VideoFileClip(filename)
        mp3_filename = os.path.splitext(os.path.basename(filename))[0] + ".mp3"
        mp3_path = os.path.join("downloads", mp3_filename)
        video.audio.write_audiofile(mp3_path)
        video.close()
        print(colored(f"Successfully converted to MP3: {mp3_filename}", "light_green"))
        
        del_vid = input("\nDo you want to delete the MP4 version and keep the MP3? Y/N:")
        if del_vid.lower() == "y":
            delete_video(filename)

        return mp3_path
    except Exception as e:
        print(colored(f"Error converting to MP3: {str(e)}", "red"))