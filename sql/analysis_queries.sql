-- 1. Top 10 hráčů podle bodů
SELECT Player, Team, Points
FROM draft2014
ORDER BY CAST(Points AS UNSIGNED) DESC
LIMIT 10;

-- 2. Draftová pozice vs. body
SELECT
  CAST(REPLACE(Position, '#', '') AS UNSIGNED) AS DraftPosition,
  Player,
  Points
FROM draft2014
WHERE Points IS NOT NULL AND Points != ''
ORDER BY DraftPosition;

-- 3. Efektivita hráčů – body na zápas
SELECT Player, GP, Points,
  ROUND(CAST(Points AS DECIMAL)/NULLIF(GP, 0), 2) AS PtsPerGame
FROM draft2014
WHERE GP > 0
ORDER BY PtsPerGame DESC
LIMIT 10;

-- 4. Týmy – součet bodů všech hráčů z draftu
SELECT Team, SUM(CAST(Points AS UNSIGNED)) AS TotalPoints
FROM draft2014
GROUP BY Team
ORDER BY TotalPoints DESC
LIMIT 10;

-- 5. David Pastrňák – pozice v žebříčku bodování
SELECT COUNT(*) + 1 AS Rank
FROM draft2014
WHERE CAST(Points AS UNSIGNED) > (
  SELECT CAST(Points AS UNSIGNED)
  FROM draft2014
  WHERE Player LIKE '%Pastrnak%'
);

-- 6. Obránci podle bodů
SELECT Player, Team, Points
FROM draft2014
WHERE Player LIKE '%(D)%'
ORDER BY CAST(Points AS UNSIGNED) DESC;
