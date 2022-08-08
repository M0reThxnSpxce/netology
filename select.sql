SELECT title, release_year FROM albums WHERE release_year = '2018'
SELECT title, duration_sec FROM songs order by duration_sec DESC limit 1
SELECT title, duration_sec FROM songs WHERE duration_sec >= '210'
SELECT title FROM collections WHERE release_year >= '2018' AND release_year <= '2020'
SELECT name FROM singers WHERE NOT name like '%% %%'
SELECT title FROM songs WHERE title like '%%My%%'