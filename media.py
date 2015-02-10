class Movie:
    
    """ Movie Class: defining movie properities, such as .title, .poster and .trailer """
    
    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.story = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer
