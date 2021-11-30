from db.run_sql import run_sql
from models.album import Album
import repositories.album_repository as album_repository

def save(album):
    sql = "INSERT INTO albums (title, artist_id, genre) VALUES (%s, %s, %s) RETURNING *"
    values = [album.title, album.artist.id, album.genre]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE  FROM albums"
    run_sql(sql)