-- lists the number of records with the same score in hte table
SELECT score, COUNT(*) 'number'
FROM second_table
GROUP BY score
ORDER BY 'number' DESC;
