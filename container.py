from dao.movies_dao import MovieDao
from dao.directors_dao import DirectorDao
from dao.genres_dao import GenreDao
from service.directors_serv import DirectorServise
from service.genres_serv import GenreServise
from service.movies_serv import MovieServise
from setup_db import db

movie_dao = MovieDao(db.session)
movie_service = MovieServise(movie_dao)

genre_dao = GenreDao(db.session)
genre_service = GenreServise(genre_dao)

director_dao = DirectorDao(db.session)
director_service = DirectorServise(director_dao)