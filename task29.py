from sklearn.metrics.pairwise import cosine_similarity

ratings = [
    [5,3,0],
    [4,0,0],
    [1,1,0]
]

similarity = cosine_similarity(ratings)

print(similarity)