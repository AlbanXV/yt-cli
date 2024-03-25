import os
from pytube import YouTube
from pytube.cli import on_progress
from moviepy.editor import VideoFileClip
from termcolor import colored, cprint


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


def yt_cli(choice):
    """
    The terminal client to enter youtube URL(s).

    args:
        - choice (bool) : Boolean value
    
    returns:
        - None
    
    """

    links = []
    counter = 0
    while True:
        print(colored("\nEnter Youtube URL(s) (Press Enter to stop adding URLs):\n", "cyan"))
        url = input()
        if url.strip() == "":
            break
        links.append(url)
        counter += 1
        print(colored(f"URL link(s) added: {counter}"))
    download_videos(links, choice)

def main():

    print(colored("\n---------- yt-cli: Download youtube video(s) ----------", "cyan"))

    choice = input("\nChoose mode: \n1 : Download in highest quality\n2 : Download manually (choose quality)\nInput: ").lower()
    quality = False

    match choice:
        case "1":
            yt_cli(quality)
        case "2":
            quality = True
            yt_cli(quality)
    

if __name__ == "__main__":
    main()