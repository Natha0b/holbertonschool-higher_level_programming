-- Lists all Comedy shows in the database.
SELECT
	st.title
FROM tv_shows AS st
INNER JOIN tv_show_genres AS sh
      ON st.id = sh.show_id
INNER JOIN tv_genres AS g
      ON g.id = sh.genre_id
WHERE g.name = "Comedy"
ORDER BY st.title ASC;
