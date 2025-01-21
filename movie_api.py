from fastapi import Body, FastAPI

app = FastAPI()

# New Book Collection
MOVIES = [
    {'title': 'Inception', 'director': 'Christopher Nolan', 'genre': 'Sci-Fi'},
    {'title': 'The Dark Knight', 'director': 'Christopher Nolan', 'genre': 'Action'},
    {'title': 'Pulp Fiction', 'director': 'Quentin Tarantino', 'genre': 'Crime'},
    {'title': 'The Godfather', 'director': 'Francis Ford Coppola', 'genre': 'Crime'},
    {'title': 'Interstellar', 'director': 'Christopher Nolan', 'genre': 'Sci-Fi'},
    {'title': 'Parasite', 'director': 'Bong Joon-ho', 'genre': 'Drama'}
]


@app.get("/movies")
async def read_all_movies():
    return MOVIES


@app.get("/movies/{movie_title}")
async def read_movie(movie_title: str):
    for movie in MOVIES:
        if movie.get('title').casefold() == movie_title.casefold():
            return movie


@app.get("/movies/")
async def read_genre_by_query(genre: str):
    movies_to_return = []
    for movie in MOVIES:
        if movie.get('genre').casefold() == genre.casefold():
            movies_to_return.append(movie)
    return movies_to_return


# Get all movies by a specific director using path or query parameters
@app.get("/movies/bydirector/")
async def read_movies_by_director_path(director: str):
    movies_to_return = []
    for movie in MOVIES:
        if movie.get('director').casefold() == director.casefold():
            movies_to_return.append(movie)

    return movies_to_return


@app.get("/movies/{movie_director}/")
async def read_director_genre_by_query(movie_director: str, genre: str):
    movies_to_return = []
    for movie in MOVIES:
        if movie.get('director').casefold() == movie_director.casefold() and \
                movie.get('genre').casefold() == genre.casefold():
            movies_to_return.append(movie)

    return movies_to_return


@app.post("/movies/create_movie")
async def create_movie(new_movie=Body()):
    MOVIES.append(new_movie)


@app.put("/movies/update_movie")
async def update_movie(updated_movie=Body()):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == updated_movie.get('title').casefold():
            MOVIES[i] = updated_movie


@app.delete("/movies/delete_movie/{movie_title}")
async def delete_movie(movie_title: str):
    for i in range(len(MOVIES)):
        if MOVIES[i].get('title').casefold() == movie_title.casefold():
            MOVIES.pop(i)
            break
