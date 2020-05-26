'''
Created on Sep 12, 2018

@author: connor
'''
from collections import defaultdict

def fill_dict(file_name):
    tracks_dict = defaultdict(list)
    current_playlist = "No Name Given"
    tracks_f = open(file_name)
    for text in tracks_f:
        text = text.strip()
        if text.startswith("https://open.spotify.com"):
            tracks_dict[text[31:]].append(current_playlist)
        else:
            current_playlist = text
    return tracks_dict

def print_dups(tracks):
    print("Duplicate Tracks:")
    for track in tracks:
        if len(tracks[track]) > 1:
            print(track + " Appears in " + str(tracks[track]) + " WebLink: https://open.spotify.com/track/"+track)
    print("End of Duplicate Tracks")

if __name__ == "__main__":
    #format for track_list is one line for playlist name, one line for each track, next playlist name...
    tracks_file = "track_list"
    tracks_dict = fill_dict(tracks_file)
    print_dups(tracks_dict)
