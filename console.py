import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("David Bowie")
artist_repository.save(artist_1)
artist_2 = Artist("Gary Numan")
artist_repository.save(artist_2)

album_1 = Album("Station to Station", artist_1, "rock")
album_repository.save(album_1)
album_2 = Album("The Pleasure Principle", artist_2, "synth pop")
album_repository.save(album_2)

artist_repository.select_all()
album_repository.select_all()

result = album_repository.select_by_artist(artist_1)
print(result[0].title)

pdb.set_trace()

