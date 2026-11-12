SELECT label,
    n_words,
    cost
FROM passages
ORDER BY cost DESC
LIMIT 5;