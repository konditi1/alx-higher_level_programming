--  lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- use only one SELECT statement
-- select the database
USE hbtn_0d_tvshows;
-- list all shows
SELECT s.title, g.genre_id
FROM tv_shows AS s
JOIN tv_show_genres AS g
ON s.id = g.show_id
ORDER BY s.title ASC, g.genre_id ASC;

