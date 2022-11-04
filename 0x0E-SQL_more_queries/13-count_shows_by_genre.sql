-- lists all genres from database tv show and displays
-- displays the number of shows linked to each
SELECT tv_genres.name 'genre', count(*) 'number_of_shows'
FROM tv_show_genres JOIN tv_genres
ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_show_genres.genre_id
ORDER BY number_of_shows DESC;
