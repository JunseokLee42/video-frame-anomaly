# Video File Processor

This project is a Python script for processing video files in a specified directory. It extracts information on the videos, such as their duration and the number of frames, and saves this information to a CSV file.

## Requirements

- Python 3.x
- OpenCV (`cv2`)

## Dataset

You can download MVfouls dataset [here](https://github.com/SoccerNet/sn-mvfoul).

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/JunseokLee42/videoprocessor.git
    cd videoprocessor
    ```

2. Install the required Python packages:
    ```sh
    pip install opencv-python
    ```

## Usage

To use this script, you need to specify the base directory containing your video files and the name of the output CSV file.

### Command Line Arguments

- `--base_directory`: The base directory containing the video files.
- `--csv_name`: The name of the output CSV file.

### Example

```sh
python video_anomaly.py --base_directory /path/to/videos --csv_name output.csv
