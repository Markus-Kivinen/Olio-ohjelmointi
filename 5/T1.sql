CREATE TABLE IF NOT EXISTS artist(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  followers INTEGER NOT NULL
);

CREATE TABLE IF NOT EXISTS album(
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  artist_id INTEGER NOT NULL,
  tracks INTEGER NOT NULL,
  FOREIGN KEY(artist_id) REFERENCES artist(id)
);

.mode csv
.import --skip 1 t1_artist.csv artist
.import --skip 1 t1_album.csv album
