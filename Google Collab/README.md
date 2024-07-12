# TikTok Video Downloader

This project provides a Python script to download TikTok videos using a command-line interface. It works both in Google Colab and on local machines.

## Features

- Download TikTok videos by providing the video URL
- Automatically generate a default filename based on the TikTok username
- Ensure the output file always has a .mp4 extension
- Normalize TikTok URLs for consistent processing

## Dependencies

This project relies on the following Python libraries:

- `yt-dlp`: For downloading videos from TikTok and other platforms
- `google.colab` (only for Google Colab usage): For file downloads in the Colab environment

## Installation and Usage

### Google Colab

1. Open a new Google Colab notebook.

2. In a code cell, install the required dependency:

   ```python
   !pip install -U yt-dlp
   ```

3. In a new code cell, copy and paste the entire script provided in the project.

4. Run the cell. You will be prompted to enter a TikTok video URL and an optional custom filename.

5. The video will be downloaded and automatically saved to your local machine.

### Local Machine

1. Ensure you have Python 3.6 or later installed on your system.

2. Install the required dependency:

   ```
   pip install yt-dlp
   ```

3. Save the script as `tiktok_downloader.py` (or any preferred name) on your local machine.

4. Remove or comment out the following line from the script, as it's only needed for Google Colab:

   ```python
   # from google.colab import files
   ```

5. Also, remove or comment out this line inside the `download_tiktok_video` function:

   ```python
   # files.download(output_path)
   ```

6. Run the script using Python:

   ```
   python tiktok_downloader.py
   ```

7. Follow the prompts to enter the TikTok video URL and optional custom filename.

8. The video will be downloaded to the same directory as the script.

## Usage Notes

- The script will automatically format the URL to start with 'https://www.' for consistency.
- If you don't provide a custom filename, it will use the TikTok username as the default filename.
- The script ensures that all output filenames end with '.mp4'.

## Legal Disclaimer

This tool is for educational purposes only. Ensure you have the right to download and use videos as per TikTok's terms of service and applicable copyright laws.

## Troubleshooting

If you encounter any issues:

1. Ensure you have the latest version of `yt-dlp` installed.
2. Check your internet connection.
3. Verify that the TikTok video URL is correct and the video is publicly accessible.
4. If using Google Colab, make sure you're using an up-to-date version of Colab.

For any persistent issues, please open an issue in the project repository.

## Contributing

Contributions to improve the script or documentation are welcome. Please feel free to submit a pull request or open an issue for any bugs or feature requests.

## License

This project is open source and available under the [MIT License](LICENSE).