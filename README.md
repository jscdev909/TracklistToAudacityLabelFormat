# Tracklist To Audacity Label Format Converter

A simple script which converts a text file containing audio track listings into a text file that adheres to Audacity's proprietary format for importing labels.

## Background
Certain long-duration audio files (such as DJ sets) will often need to be divided into parts for easier listening and organization. For these types of audio files, a text tracklist of start and end timecodes is usually provided. However, using this tracklist to cut the audio file into chunks manually can be time-consuming and inefficient.

Audacity provides a means to cut an audio track into segments using its label feature. Labels in audacity can be managed in its dedicated Label Editor window, and sets of labels can be imported from files that match a proprietary label format.

## About
This script aims to convert a typical tracklist you would find with DJ sets and mixed albums into a text file that Audacity can use to place labels to divide up the recording.

The script currently takes one runtime argument, which is the path to a file with a valid tracklist. For a tracklist to be considered valid by the program, each track should be listed on a separate line in the file and adhere to the following format: "H:MM:SS <song-name> - <artist>".

A sample tracklist, sample_track_list.txt, has been provided in the repository for reference as an example of a valid tracklist. Please copy this same format when making your own tracklist to provide to this program.

