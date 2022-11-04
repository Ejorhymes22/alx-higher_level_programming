-- lists all shows and all genres linked to theat show
SELECT tv_shows.title, tv_genres.name
FROM tv_shows left JOIN tv_show_genres
on tv_shows.id = tv_show_genres.show_id
left JOIN tv_genres
on tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name
