import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Frank Sinatra")
artist_repository.save(artist_1)
artist_2 = Artist("Gary Numan")
artist_repository.save(artist_2)

album_1 = Album("My Way", artist_1, "swing")
album_repository.save(album_1)
album_2 = Album("The Pleasure Principle", artist_2, "synth pop")
album_repository.save(album_2)

artist_repository.select_all()
album_repository.select_all()

result = album_repository.select_by_artist(artist_1)
print(result[0].title)

artist_repository.update(artist_1)
album_repository.update(album_1)


album_repository.delete(album_2)
artist_repository.delete(artist_2)

pdb.set_trace()

