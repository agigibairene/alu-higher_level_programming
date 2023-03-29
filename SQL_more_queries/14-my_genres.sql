--  use the hbtn_0d_tvshows database to lists all genres of the show Dexter.
SELECT name
FROM tv_show_genres AS tv_show_g
INNER JOIN tv_shows AS tv_shows
ON tvg.show_id = tv_shows.id
INNER JOIN tv_genres AS tv_genre
ON tv_genre.id = tv_show_g.genre_id
WHERE tv.title = "Dexter"
ORDER BY name ASC;
