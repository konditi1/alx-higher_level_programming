-- lists all shows and all genres linked to that show from hbtn_0d_tvshows
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
SELECT tv_shows.title AS 'title', tv_genres.name AS 'name'
FROM tv_shows LEFT OUTER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
LEFT OUTER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
ORDER BY title, name;