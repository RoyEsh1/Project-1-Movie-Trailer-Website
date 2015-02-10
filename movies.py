import media
import fresh_tomatoes
 
# Sourcing favourite movies, using an array in advnce to ease the migraiton to the fresh_tomatoes module

FavMovies = []
FavMovies.append(media.Movie("Man on Wire", "", "http://www.impawards.com/2008/posters/man_on_wire_ver2.jpg", "https://www.youtube.com/watch?v=EIawNRm9NWM"))
FavMovies.append(media.Movie("Zero Dark Thirty", "", "http://www.sonypictures.com/movies/zerodarkthirty/assets/images/onesheet.jpg", "https://www.youtube.com/watch?v=LJFra3B9sbA"))
FavMovies.append(media.Movie("Fight Club", "", "http://images.moviefanatic.com/iu/v1391623510/fight-club-poster.jpg", "https://www.youtube.com/watch?v=STl3eifhkm4"))
FavMovies.append(media.Movie("The Godfather", "", "http://upload.wikimedia.org/wikipedia/en/4/4d/Godfather.jpg", "https://www.youtube.com/watch?v=sY1S34973zA"))
FavMovies.append(media.Movie("Taxi Driver", "", "http://ia.media-imdb.com/images/M/MV5BMTQ1Nzg3MDQwN15BMl5BanBnXkFtZTcwNDE2NDU2MQ@@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=44gB58YS53A"))
FavMovies.append(media.Movie("Scarface", "", "http://mtv.mtvnimages.com/shared/media/images/acovers/standard/dra700/a724/a72481m9dv7.jpg", "https://www.youtube.com/watch?v=7pQQHnqBa2E"))

# Building HTML page

fresh_tomatoes.open_movies_page(FavMovies)
