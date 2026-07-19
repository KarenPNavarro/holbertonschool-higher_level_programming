-- My genres
SELECT tv_genres.name
FROM tv_genres, tv_show_genres, tv_shows
WHERE tv_genres.id = tv_show_genres.genre_id
AND tv_shows.id = tv_show_genres.show_id
AND tv_shows.title = 'Dexter'
ORDER BY tv_genres.name ASC;
