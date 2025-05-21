--.mode table
SELECT artist.name as artist, artist.followers, album.name as album, album.tracks FROM artist JOIN album ON album.artist_id = artist.id ORDER BY artist.name ASC, artist.followers ASC, album.name ASC, album.tracks ASC;
