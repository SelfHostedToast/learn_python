# 8-7 Album

def make_album(artist_name, album_name, song_count=None):
    album = {'artist': artist_name, 'album': album_name}
    if song_count:
        album['song count'] = song_count
    return album

one = make_album('lunchbox', 'new jazz', 23)
two = make_album('800pts', 'fenrir')
three = make_album('redda', 'new world')

print(one)
print(two)
print(three)