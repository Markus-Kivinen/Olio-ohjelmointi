--.mode table
SELECT artist.name, SUM(album.tracks) AS total_tracks
FROM album
JOIN artist ON album.artist_id = artist.id
GROUP BY artist.name
ORDER BY artist.name
