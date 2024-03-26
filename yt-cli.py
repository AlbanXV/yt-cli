from termcolor import colored
from utility import *
from get_video import *

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
    clear()
    download_videos(links, choice)

def main():

    print(colored("\n---------- yt-cli: Download youtube video(s) ----------", "cyan"))
    choice = input("\nChoose mode: \n1 : Download in highest quality\n2 : Download manually (choose quality)\nInput: ").lower()
    quality = False

    match choice:
        case "1":
            clear()
            yt_cli(quality)
        case "2":
            clear()
            quality = True
            yt_cli(quality)
    

if __name__ == "__main__":
    main()