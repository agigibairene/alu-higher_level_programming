-- displays the top 3 of cities temperature during July and August ordered by highest temperature
SELECT `city`, AVG(`value`) AS `avg` FROM `temperatures` 
WHERE `month` = 7 OR `month` = 8 GROUP BY `city`
ORDER BY `avg` DESC LIMIT 3;
