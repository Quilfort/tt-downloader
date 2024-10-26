# TT Downloader for Android and Termux

This guide explains how to set up Termux to automatically download TT videos when you share a TT URL to Termux.

## Prerequisites

- Termux app installed on your Android device
- Python installed in Termux

## Setup Instructions

1. **Create the termux-url-opener script**

   Open Termux and run the following command:

   ```bash
   mkdir -p ~/bin && nano ~/bin/termux-url-opener
   ```

   This creates the necessary directory and opens a new file in the nano text editor.

2. **Write the script**

   In the nano editor, add the following content:

   When location is `/data/data/com.termux/files/home/tt-downloader/Termux/tt-downloader.py` your script will be:

   ```bash
   #!/data/data/com.termux/files/usr/bin/bash

   python /data/data/com.termux/files/home/tt-downloader/Termux/tt-downloader.py "$1"
   ```

3. **Save and exit**

   Press `Ctrl+X`, then `Y`, then `Enter` to save the file and exit nano.

4. **Make the script executable | Optional**

   You may need to make the termux-url-opener executable, depending on how you set up your Termux.

   Run the following command:

   ```bash
   chmod +x ~/bin/termux-url-opener
   ```

## Usage

After completing the setup:

1. Find a TT video you want to download.
2. Tap the "Share" button.
3. Select Termux from the share menu.
4. Termux will automatically start the download process.

## How it Works

- When you share a TT URL to Termux, it looks for the `termux-url-opener` script in the `~/bin` directory.
- This script then calls your Python downloader with the shared URL as an argument.
- Your Python script handles the actual downloading of the video.

## Troubleshooting

- Ensure that `yt-dlp` is up-to-date. If not, it's possible it won't download or just download a small file
```bash
# Inside Termux
pip install -U yt-dlp
```
- Ensure your Python script (`tt-downloader.py`) is working correctly and can handle URLs passed as command-line arguments.
- Check that the paths in the `termux-url-opener` script are correct, especially if you've moved your Python script.
- If you encounter issues, you may want to add error handling or output messages in the bash script for better feedback.


## Coming Soon

- Share the video directly with a group or contact using Whatsapp.
- Automatically remove the video if the user only wants to share it
- Add other platforms such as YT
