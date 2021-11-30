import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist_1 = Artist("David Bowie")
artist_repository.save(artist_1)
artist_2 = Artist("Gary Numan")
artist_repository.save(artist_2)

pdb.set_trace()

