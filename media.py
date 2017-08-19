class Movie():
    """A movie clss.

    a data struct that stores movies title, poter and trailer link

    Attributes:
        title: a string to store the title of the movie
        poster_image_url: a stirng to store the url of the image
        trailer_youtube_url: a string to store the youtube  url of the trailer
        """
    def __init__(self, movie_title,  poster_image, trailer_youtube):
      self.title = movie_title
      self.poster_image_url = poster_image
      self.trailer_youtube_url = trailer_youtube
