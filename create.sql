create table albums (
  id SERIAL primary key,
  title Varchar(64) not null,
  release_year integer
)

create table collections (
  id SERIAL primary key,
  title Varchar(64) not null,
  release_year integer
)

create table songs (
  id SERIAL primary key,
  title Varchar(64) not null,
  duration_sec integer,
  album_id integer references albums(id)
)

create table collection_songs (
  collection_id integer references collections(id),
  song_id integer references songs(id),
  Constraint cs primary key (collection_id, song_id)
)

create table singers (
  id SERIAL primary key,
  name Varchar(64) not null,
)

create table singers_albums (
  artist_id integer references singers(id),
  album_id integer references albums(id),
  Constraint sa primary key (artist_id, album_id)
)

create table genres (
  id SERIAL primary key,
  title varchar(64) not null,
)

create table genres_singers (
  genre_id integer references genres(id),
  artist_id integer references singers(id),
  Constraint gs primary key (genre_id, artist_id)
)