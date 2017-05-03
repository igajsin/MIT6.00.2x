#!/usr/bin/python3

def pick(songs):
    if songs == []:
        return []
    else:
        return min(((idx, val) for (idx, val) in enumerate(songs)), key=lambda x: list(x)[1][2])

def song_playlist(songs, max_size):
    songs = songs[:]
    if songs == []:
        return []
    else:
        first_song = songs[0][0]
        first_song_size = songs[0][2]
        if first_song_size <= max_size:
            result = [songs[0][0]]
            max_size -= songs[0][2]
            del songs[0]
            while len(songs) > 0:
                idx, song = pick(songs)
                song_size = song[2]
                if song_size < max_size:
                    result.append(song[0])
                    max_size -= song_size
                    del songs[idx]
                else:
                    break
            return result
        return []
