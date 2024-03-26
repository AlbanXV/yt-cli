from pytube import YouTube
from pytube.cli import on_progress
from termcolor import colored
from utility import *
from convert_mp3 import *

def download_video(url, choice):
    """
    Downloads specific video from a youtube URL.

    args:
        - url (str) : url-string from a youtube link
        - choice (bool) : Boolean value
    
    returns:
        - video_path (str)

    """

    create_dir()

    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        match choice:
            case False:
                stream = yt.streams.get_highest_resolution()
                filename = stream.default_filename
                video_path = os.path.join("downloads", filename)

                print(colored(f"Downloading: {filename}..\n", "yellow"))
                stream.download(output_path="downloads", filename=filename)

                print(colored(f"Successfully downloaded: {filename}", "light_green"))
            
            case True:
                available_streams = yt.streams.filter(progressive=True, file_extension="mp4").order_by('resolution').desc()
                print(colored("Available video qualities:\n", "cyan"))
                for i, j in enumerate(available_streams, 1):
                    print(f"{i}. Quality: {j.resolution}, Type: {j.mime_type}, Size: {format_file_size(j.filesize)}")
                
                quality_choice = int(input("\nEnter number corresponding to desired video quality:")) - 1
                selected_stream = available_streams[quality_choice]

                filename = selected_stream.default_filename
                video_path = os.path.join("downloads", filename)

                print(colored(f"\nDownloading: {filename}..\n", "yellow"))
                selected_stream.download(output_path="downloads", filename=filename)

                print(colored(f"Successfully downloaded: {filename}", "light_green"))

        mp3 = input("\nConvert video(s) to MP3? Y/N:")
        if mp3.lower() == "y":
            clear()
            convert_to_mp3(video_path)

        return video_path
    except Exception as e:
        print(colored(f"Error downloading video from {url}: {str(e)}", "red"))

def download_videos(urls, choice):
    """
    Downloads multiple videos by calling the download_video() function

    args:
        - urls (list) : list containing youtube url-strings
        - choice (bool) : Boolean value
    
    returns:
        - None

    """

    for url in urls:
        video_path = download_video(url, choice)