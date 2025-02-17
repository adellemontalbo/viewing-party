# ------------- WAVE 1 --------------------

def create_movie(title, genre, rating):
    new_movie = {"title": title, "genre": genre, "rating": rating}
    if title is None or genre is None or rating is None:
        new_movie = None
    return new_movie

def add_to_watched(user_data, movie):
    user_data["watched"].append(movie)
    return user_data 

def add_to_watchlist(user_data, movie):
    user_data["watchlist"].append(movie)
    return user_data 

def watch_movie(user_data, title):
    for movie in user_data["watchlist"]:
        if movie["title"] == title:
            user_data["watched"].append(movie)
            user_data["watchlist"].remove(movie)
    return user_data

# -----------------------------------------
# ------------- WAVE 2 --------------------
# -----------------------------------------

def get_watched_avg_rating(user_data):
    number_of_movies = 0
    average_ratings = 0.0
    if len(user_data["watched"]) == 0:
        average_ratings = 0.0
        return average_ratings
    for movie in user_data["watched"]:
        number_of_movies += 1
        average_ratings += float(movie["rating"])
    average_ratings = average_ratings/number_of_movies
    return average_ratings
        
def get_most_watched_genre(user_data):
# to include multiple genres that have high count
    genre_dict = {}
    most_frequent_genre = ""
    if len(user_data["watched"]) == 0:
        return None
    for movie in user_data["watched"]:
        if movie["genre"] not in genre_dict:
            genre_dict[movie["genre"]] = 1
        elif movie["genre"] in genre_dict:
            genre_dict[movie["genre"]] += 1
    most_frequent_genre = [key for key, value in genre_dict.items()\
         if value == max(genre_dict.values())]
    return ' '.join(most_frequent_genre)


# -----------------------------------------
# ------------- WAVE 3 --------------------
# -----------------------------------------

def get_user_watched_movies(user_data):
    user_watched_movies = []
    for movie in user_data["watched"]:
        user_watched_movies.append(movie)
    return user_watched_movies

def get_friends_watched_movies(user_data):
    friends_watched_movies = []
    for friend in user_data["friends"]:
        for film in friend["watched"]:
            if film not in friends_watched_movies:
                friends_watched_movies.append(film)
    return friends_watched_movies

def get_unique_watched(user_data):
    user_watched_movies = get_user_watched_movies(user_data)
    friends_watched_movies = get_friends_watched_movies(user_data)
    unique_movies = []
    for item in user_watched_movies:
        if item not in friends_watched_movies:
            unique_movies.append(item)
    return unique_movies

def get_friends_unique_watched(user_data):
    user_watched_movies = get_user_watched_movies(user_data)
    friends_watched_movies = get_friends_watched_movies(user_data)
    unique_movies = []
    for movie in friends_watched_movies:
        if movie not in user_watched_movies:
            unique_movies.append(movie)
    return unique_movies

        
# -----------------------------------------
# ------------- WAVE 4 --------------------
# -----------------------------------------

def get_available_recs(user_data):
    movie_recs = []
    friends_watched_user_no = get_friends_unique_watched(user_data)
    for movie in friends_watched_user_no:
        if movie["host"] in user_data["subscriptions"]:
            movie_recs.append(movie)
    return movie_recs

# -----------------------------------------
# ------------- WAVE 5 --------------------
# -----------------------------------------
def get_new_rec_by_genre(user_data):
    new_recs = []
    user_most_watched_genre = get_most_watched_genre(user_data)
    friends_watched_user_no = get_friends_unique_watched(user_data)
    for movie in friends_watched_user_no:
        if movie["genre"] == user_most_watched_genre:
            new_recs.append(movie)
    return new_recs

def get_rec_from_favorites(user_data):
    favorite_recs = []
    movies_user_watched_friends_no = get_unique_watched(user_data)
    for movie in movies_user_watched_friends_no:
        if movie in user_data["favorites"]:
            favorite_recs.append(movie)
    return favorite_recs



