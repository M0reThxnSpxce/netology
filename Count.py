from sqlalchemy import create_engine

engine = create_engine(
    'postgresql://postgres:root@localhost:5432/postgres')

connection = engine.connect()

# количество исполнителей в каждом жанре;
count_performers = connection.execute('''
    SELECT T.title, count(GP.artist_id)
    FROM genres T
    JOIN  genres_singers GP ON T.id = GP.genre_id
    GROUP BY T.title
    ''').fetchall()

print(f'Количество исполнителей в каждом жанре: {count_performers}')

# количество треков, вошедших в альбомы 2019-2020 годов;
count_treck_19_20 = connection.execute('''
    SELECT a.title, a.release_year, count(s.id)
    FROM albums a
    JOIN songs s ON a.id = s.album_id
    WHERE a.release_year >= 2019 AND a.release_year <= 2020
    GROUP BY a.title, a.release_year
    ''').fetchall()

print(f'Количество треков, вошедших в альбомы 2019-2020 годов;: {count_treck_19_20}')

# средняя продолжительность треков по каждому альбому;
duration_track_average = connection.execute('''
    SELECT  a.title, round(AVG(s.duration_sec), 2)
    FROM albums a
    JOIN songs s ON a.id = s.album_id
    GROUP BY a.title
    ''').fetchall()

print(f'Cредняя продолжительность треков по каждому альбому: {duration_track_average}')

# все исполнители, которые не выпустили альбомы в 2020 году;
performers_album_not_in_20 = connection.execute('''
    SELECT p.name, a.release_year
    FROM singers p
    JOIN singers_albums ap ON p.id = ap.artist_id
    JOIN albums a ON ap.album_id = a.id
    WHERE a.release_year != 2020
    ''').fetchall()

print(f'Все исполнители, которые не выпустили альбомы в 2020 году: {performers_album_not_in_20}')

# названия сборников, в которых присутствует конкретный исполнитель (выберите сами);
Name_in_collection = connection.execute('''
    SELECT DISTINCT c.title
    FROM collections c
    JOIN collection_songs sc ON c.id = sc.collection_id
    JOIN songs s ON sc.song_id = s.id
    JOIN albums a ON s.album_id = a.id
    JOIN singers_albums ap ON a.id = ap.album_id
    JOIN singers p ON ap.artist_id = p.id
    WHERE p.name LIKE 'ATB'
    ''').fetchall()

print(f'Названия сборников, в которых присутствует конкретный исполнитель ("artist_7"): {Name_in_collection}')

# название альбомов, в которых присутствуют исполнители более 1 жанра;
album_many_styles = connection.execute('''
     SELECT a.title
     FROM albums a
     JOIN singers_albums ap ON a.id = ap.album_id
     JOIN singers p ON ap.artist_id = p.id
     JOIN genres_singers gp ON p.id = gp.artist_id
     GROUP BY p.name, a.title
     HAVING count(gp.genre_id) > 1
    ''').fetchall()

print(f'Название альбомов, в которых присутствуют исполнители более 1 жанра: {album_many_styles}')

# наименование треков, которые не входят в сборники;
lonely_track = connection.execute('''
    SELECT s.title
    FROM songs s
    LEFT JOIN collection_songs sc ON s.id = sc.song_id
    where sc.song_id IS NULL
    ''').fetchall()

print(f'Наименование треков, которые не входят в сборники: {lonely_track}')

# исполнителя(-ей), написавшего самый короткий по продолжительности трек
# (теоретически таких треков может быть несколько);
the_shortest_track = connection.execute('''
    SELECT p.name, s.duration_sec
    FROM singers p
    JOIN singers_albums ap ON p.id = ap.artist_id
    JOIN albums a ON ap.album_id = a.id
    JOIN songs s ON a.id = s.album_id
    WHERE s.duration_sec IN (SELECT MIN(duration_sec) FROM Songs)
    ''').fetchall()

print(f'Исполнителя(-ей), написавшего самый короткий по продолжительности трек : {the_shortest_track}')

# название альбомов, содержащих наименьшее количество треков.
the_shortest_album = connection.execute('''
    SELECT a.title, count(s.id)
    FROM albums a
    JOIN Songs s  ON a.id = s.album_id
    GROUP BY a.title 
    HAVING count(s.id) in (
        SELECT count(s.id)
        FROM albums a
        JOIN songs s  ON a.id = s.album_id
        GROUP BY a.title
        ORDER BY count(s.id)\
        LIMIT 1)
    ''').fetchall()

print(f'Название альбомов, содержащих наименьшее количество треков : {the_shortest_album}')