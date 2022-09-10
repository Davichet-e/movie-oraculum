import joblib
from numpy import load, take

indices = joblib.load("indices.joblib")
cosine_similarities = load("recommendation_matrix.npy")
imdb_ids = load("imdb_ids.npy", allow_pickle=True)


def recommend_movie(original_title) -> list[str]:
    idx = indices[original_title]

    sim_scores = list(enumerate(cosine_similarities[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:4]

    movie_indices = [i[0] for i in sim_scores]

    return list(take(imdb_ids, movie_indices))
