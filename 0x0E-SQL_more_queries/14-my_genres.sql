-- lists all genres of the show dexter
SELECT tv_genres.name
FROM tv_shows JOIN tv_genres JOIN tv_show_genres
ON tv_show_genres.show_id = tv_shows.id and tv_genres.id = tv_show_genres.genre_id
WHERE tv_shows.title = 'Dexter'
ORDER BY tv_genres.name;
