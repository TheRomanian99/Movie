import webbrowser

#this creates the Movie class which is used to create instances for each of the movies
class Movie():
    def __init__(self, movie_title, movie_storyline, poster_image, youtube_trailer, movie_stars, release_date):
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = youtube_trailer
        self.stars = movie_stars
        self.release_date = release_date
