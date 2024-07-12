import os
import requests
import sys
import time
import yt_dlp

from urllib.parse import urlparse

def expand_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.url
    except requests.RequestException:
        return url

def download_tt_video(url, output_path):
    try:
        ydl_opts = {
            'outtmpl': output_path,
            'format': 'best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        # Set the file's modification time to the current time
        current_time = time.time()
        os.utime(output_path, (current_time, current_time))
        
        print(f"Video downloaded successfully: {output_path}")

    except Exception as e:
        print(f"Error downloading video: {str(e)}")

def get_default_filename(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    if len(path_parts) > 1:
        username = path_parts[1].strip('@')
        return f"{username}_{path_parts[-1]}.mp4"
    return 'video.mp4'

def normalize_url(url):
    # Expand short URLs
    url = expand_url(url)
    
    # Remove query parameters
    url = url.split('?')[0]
    
    if not url.startswith('http'):
        url = 'https://' + url
    if not url.startswith('https://www.'):
        url = url.replace('https://', 'https://www.')
    return url

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the TT video URL: ")
    
    url = normalize_url(url)
    filename = get_default_filename(url)

    # Use the downloads directory in the user's home folder
    output_path = os.path.expanduser(f"~/storage/downloads/{filename}")

    # Validate URL
    parsed_url = urlparse(url)
    if not (parsed_url.scheme and parsed_url.netloc):
        print("Error: Invalid URL. Please provide a valid TT video URL.")
    else:
        download_tt_video(url, output_path)

if __name__ == "__main__":
    main()