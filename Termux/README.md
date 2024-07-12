# TikTok Video Downloader for Android (Termux)

This project provides a lightweight Python script to download TikTok videos using Termux on Android devices.

## Features

- Download TikTok videos by providing the video URL
- Automatically generate a default filename based on the TikTok username
- Ensure the output file always has a .mp4 extension
- Normalize TikTok URLs for consistent processing
- Save videos directly to the Downloads folder on your Android device

## Dependencies

This project relies on the following Python library:

- `yt-dlp`: For downloading videos from TikTok and other platforms

## Installation and Usage on Android with Termux

1. Open Termux and update the package list:
   ```
   pkg update
   ```

2. Install Python and the required tools:
   ```
   pkg install python
   pkg install git
   ```

3. Install yt-dlp:
   ```
   pip install yt-dlp
   ```

4. Clone this repository (or download the script):
   ```
   git clone git@github.com:Quilfort/tt-downloader.git
   cd tt-downloader/Termux
   ```

6. Give Termux access to your storage:
   ```
   termux-setup-storage
   ```

7. Run the script:
   ```
   python tt_downloader.py
   ```

8. Follow the prompts to enter the TikTok video URL and optional custom filename.

9. The video will be downloaded to your Android device's Downloads folder.

## Usage Notes

- The script will automatically format the URL to start with 'https://www.' for consistency.
- If you don't provide a custom filename, it will use the TikTok username as the default filename.
- The script ensures that all output filenames end with '.mp4'.
- Downloaded videos are saved in the Downloads folder of your Android device.

## Legal Disclaimer

This tool is for educational purposes only. Ensure you have the right to download and use videos as per TikTok's terms of service and applicable copyright laws.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest version of `yt-dlp` installed:
   ```
   pip install -U yt-dlp
   ```
2. Check your internet connection.
3. Verify that the TikTok video URL is correct and the video is publicly accessible.
4. Make sure Termux has permission to access your storage.

For any persistent issues, please open an issue in the project repository.

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is open source and available under the [MIT License](LICENSE).