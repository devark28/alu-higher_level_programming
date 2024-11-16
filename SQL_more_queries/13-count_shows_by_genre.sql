--
SELECT DISTINCT tv_genres.name as genre, (
    SELECT COUNT(*)
    FROM tv_show_genres
    WHERE tv_genres.id = tv_show_genres.genre_id
) AS number_of_shows
FROM tv_genres, tv_show_genres
WHERE tv_genres.id = tv_show_genres.genre_id
ORDER BY number_of_shows DESC;