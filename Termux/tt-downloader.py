import os
import requests
import sys
import time
import yt_dlp
import random
import string
from urllib.parse import urlparse

def expand_url(url):
    try:
        response = requests.head(url, allow_redirects=True)
        return response.url
    except requests.RequestException:
        return url

def download_video(url, output_path):
    try:
        ydl_opts = {
            'outtmpl': output_path,
            'format': 'best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        current_time = time.time()
        os.utime(output_path, (current_time, current_time))
        
        print(f"Video downloaded successfully: {output_path}")

    except Exception as e:
        print(f"Error downloading video: {str(e)}")

def generate_unique_filename(base_path):
    """Generates a unique filename by appending a random string if the file exists."""
    if not os.path.exists(base_path):
        return base_path

    filename, extension = os.path.splitext(base_path)
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    unique_filename = f"{filename}_{random_string}{extension}"
    return unique_filename

def get_default_filename(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    
    if 'youtube.com' in parsed_url.netloc or 'youtu.be' in parsed_url.netloc:
        filename = "Youtube_video.mp4"
    else:
        if len(path_parts) > 1:
            username = path_parts[1].strip('@')
            filename = f"{username}_{path_parts[-1]}.mp4"
        else:
            filename = 'video.mp4'
    
    downloads_dir = os.path.expanduser("~/storage/downloads")
    return generate_unique_filename(os.path.join(downloads_dir, filename))

def normalize_url(url):
    url = expand_url(url)
    parsed_url = urlparse(url)
    
    if 'youtube.com' in parsed_url.netloc or 'youtu.be' in parsed_url.netloc:
        return url  # Preserve the entire URL for YouTube
    
    # Remove query parameters for non-YouTube URLs
    return url.split('?')[0]

def main():
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter the video URL: ")
    
    url = normalize_url(url)
    output_path = get_default_filename(url)

    parsed_url = urlparse(url)
    if not (parsed_url.scheme and parsed_url.netloc):
        print("Error: Invalid URL. Please provide a valid video URL.")
    else:
        download_video(url, output_path)

if __name__ == "__main__":
    main()