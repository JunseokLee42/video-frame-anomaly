import cv2
import glob
import os
import csv
import argparse

def get_duration(file):
    cap = cv2.VideoCapture(file)

    if not cap.isOpened():
        print("can't open: ", file)
        errors.append(file)
    
    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    # width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    # height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = cap.get(cv2.CAP_PROP_FPS)

    if fps > 0:
        duration = length / fps
    else:
        duration = 0

    cap.release()
    return duration

def frames(file):
    cap = cv2.VideoCapture(file)

    if not cap.isOpened():
        print("can't open: ", file)

    length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    cap.release()
    return length

def get_mp4_list(base_directory):
    result = {}
    for root, dirs, _ in os.walk(base_directory):
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            mp4_files = glob.glob(f"{dir_path}/*.mp4") # clips for each action
            result[dir] = mp4_files # action_num: list of clips
    return result

def save_to_csv(file_info, csv_name):
    with open(csv_name, 'w', newline='') as csv_file:
        fieldnames = ['directory', 'file', 'frames', 'duration']
        writer = csv.DictWriter(csv_file, fieldnames = fieldnames)

        writer.writeheader()
        for info in file_info:
            writer.writerow(info)

def main():
    parser = argparse.ArgumentParser(description='Process some video files.')
    parser.add_argument('--base_directory', type=str, required=True, help='Base directory containing video files')
    parser.add_argument('--csv_name', type=str, required=True, help='Name of the output CSV file')

    args = parser.parse_args()
    
    base_directory = args.base_directory
    csv_name = args.csv_name

    global errors
    errors = list()
    mp4_files_dict = get_mp4_list(base_directory)

    file_info = []
    for dir, files in mp4_files_dict.items():
        print(f"Directory: {dir}")
        for file in files:
            print(f"    get information on {file}")
            duration = get_duration(file)
            length = frames(file)
            if duration is not None:
                file_info.append({'directory': dir, 'file': file, 'duration': duration, 'frames': length})
    
    save_to_csv(file_info, csv_name)
    print(f"Video information saved to {csv_name}")

if __name__ == "__main__":
    main()