from pytube import YouTube
import os


def create_dir():
    download_dir = "downloads"
    dir_exists = os.path.exists(download_dir)

    if not dir_exists:
        os.makedirs(download_dir)

def download_video(url):
    create_dir()

    try:
        yt = YouTube(url)
        stream = yt.streams.get_highest_resolution()
        filename = stream.default_filename
        video_path = os.path.join("downloads", filename)
        stream.download(output_path="downloads", filename=filename)
        print(f"Successfully downloaded: {filename}")
        return video_path
    except Exception as e:
        print(f"Error downloading video from {url}: {str(e)}")

def download_videos(urls):
    for url in urls:
        video_path = download_video(url)

def convert_to_mp3(file):
    ...

def main():
    links = []

    print("yt-cli: Download youtube video(s)")
    while True:
        url = input("Enter Youtube URL(s) (Press Enter to stop adding URLs):\n")
        if url.strip() == "":
            break
        links.append(url)
    download_videos(links)
    

if __name__ == "__main__":
    main()