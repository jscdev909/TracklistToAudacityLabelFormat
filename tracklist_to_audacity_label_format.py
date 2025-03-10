# Track List to Audacity Track List Formatter
# Formats a given text file containing a track list to adhere to Audacity's label format
# Each line of the track list text file is expected to follow this format: "H:MM:SS <song-name> - <artist>"


import sys
from pathlib import Path
import os


def print_usage() -> None:
    current_file_name = __file__.split('\\')[-1]
    print(f"Usage: {current_file_name} <track-list-file>")


def parse_and_test_args() -> str:

    if len(sys.argv) == 1:
        print("[ERROR] No track list file provided, cannot continue. Exiting...")
        print_usage()
        exit(1)
    elif len(sys.argv) > 2:
        print("[ERROR] Too many arguments given! Exiting...")
        print_usage()
        exit(2)

    track_list_file = sys.argv[1]

    # Make sure the file we were given actually exists
    if not Path(track_list_file).is_file():
        print("[ERROR] Track list file provided is not valid, cannot continue. Exiting...")
        exit(3)

    return track_list_file


def main() -> None:

    track_list_file = parse_and_test_args()

    with open(track_list_file, 'r') as tlf:
        track_list = list(map(str.strip, tlf))

    output_file = os.path.join(os.getcwd(), "output.txt")

    with open(output_file, 'w') as of:
        for i, track in enumerate(track_list):
            time = track.split(' ')[0]
            song_name = " ".join(track.split(' - ')[0].split(' ')[1:])
            artist = track.split(' - ')[-1]

            # Skip if track is in an invalid format
            if not time or not song_name or not artist:
                print(f"[WARNING] Track {i} is in an invalid format. Skipping...")
                continue

            total_seconds = int(time.split(':')[-1])
            total_seconds += int(time.split(':')[1]) * 60
            total_seconds += int(time.split(':')[0]) * 60 * 60
            total_seconds_str = str(total_seconds) + '.000000'

            of.write(f"{total_seconds_str}\t{total_seconds_str}\t{artist} - {song_name}\n")

    print("Tracklist reformatting complete!")
    print(f"Output file: {output_file}")


if __name__ == '__main__':
    main()
