import os
import yt_dlp
from urllib.parse import urlparse

def download_tiktok_video(url, output_path):
    try:
        ydl_opts = {
            'outtmpl': output_path,
            'format': 'best',
        }
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        
        print(f"Video downloaded successfully: {output_path}")

    except Exception as e:
        print(f"Error downloading video: {str(e)}")

def get_default_filename(url):
    parsed_url = urlparse(url)
    path_parts = parsed_url.path.split('/')
    if len(path_parts) > 1:
        return path_parts[1].strip('@') + '.mp4'
    return 'video.mp4'

def ensure_mp4_extension(filename):
    if not filename.lower().endswith('.mp4'):
        return filename + '.mp4'
    return filename

def normalize_url(url):
    if not url.startswith('http'):
        url = 'https://' + url
    if not url.startswith('https://www.'):
        url = url.replace('https://', 'https://www.')
    return url

def main():
    url = input("Enter the TikTok video URL: ")
    url = normalize_url(url)
    default_filename = get_default_filename(url)
    output = input(f"Enter the output file name (default: {default_filename}): ") or default_filename
    output = ensure_mp4_extension(output)

    # Use the downloads directory in the user's home folder
    output_path = os.path.expanduser(f"~/storage/downloads/{output}")

    # Validate URL
    parsed_url = urlparse(url)
    if not (parsed_url.scheme and parsed_url.netloc):
        print("Error: Invalid URL. Please provide a valid TikTok video URL.")
    else:
        download_tiktok_video(url, output_path)

if __name__ == "__main__":
    main()