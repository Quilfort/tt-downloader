# TT Video Downloader for Android (Termux)

This project provides a lightweight Python script to download TT videos using Termux on Android devices.

## Features

- Download TT videos by providing the video URL (supports various TT URL formats)
- Accept URL as a command-line argument or via user input
- Automatically generate a filename based on the TT username and video ID
- Normalize and expand TT URLs for consistent processing
- Handle short mobile links (vm.tiktok.com) and web links
- Save videos directly to the Downloads folder on your Android device
- Set the correct date and time for downloaded files

## Dependencies

This project relies on the following Python libraries:

- `yt-dlp`: For downloading videos from TT and other platforms
- `requests`: For handling URL redirects and expansions

## Installation and Usage on Android with Termux


1. Install Python and the required tools:
   ```
   pkg install python
   pkg install git
   ```

2. Install the required Python libraries:
   ```
   pip install yt-dlp requests
   ```

3. Clone this repository (or download the script):
   ```
   git clone git@github.com:Quilfort/tt-downloader.git
   cd tt-downloader
   ```

4. Give Termux access to your storage:
   ```
   termux-setup-storage
   ```

5. Run the script in one of two ways:

   a. With a URL as a command-line argument:
      ```
      python tt_downloader.py https://vm.tiktok.com/...
      ```

   b. Without an argument (you'll be prompted to enter the URL):
      ```
      python tt_downloader.py
      ```

6. The script supports various TT URL formats, including:
   - Short mobile links (e.g., https://vm.tiktok.com/...)
   - Web links (e.g., https://www.tiktok.com/@username/video/...)
   - Mobile app links (e.g., https://www.tiktok.com/t/...)

7. The video will be downloaded to your Android device's Downloads folder with a filename based on the TT username and video ID.

## Usage Notes

- The script will automatically handle different TT URL formats, including short links and links with additional parameters.
- The filename will be based on the TT username and video ID, ending with '.mp4'.
- Downloaded videos are saved in the Downloads folder of your Android device.
- The file's date and time will be set to the current date and time when it's downloaded.

## Legal Disclaimer

This tool is for educational purposes only. Ensure you have the right to download and use videos as per TT's terms of service and applicable copyright laws.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest versions of the required libraries installed:
```bash
pip install -U yt-dlp requests
```
2. Check your internet connection.
3. Verify that the TT video URL is correct and the video is publicly accessible.
4. Make sure Termux has permission to access your storage.

For any persistent issues, please open an issue in the project repository.

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is open source and available under the [MIT License](LICENSE).