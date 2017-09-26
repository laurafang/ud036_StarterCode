import webbrowser

# This python file is to write a movie class in media.py. To do this, think about what the properties of a movie are that need to be encapsulated in a movie object such as movie titles, box art, poster images, and movie trailer URLs. Look at what open_movies_page() does with a list of movie objects for hints on how to design your movie class.


# Parent class for moive
class Movie():
    # initial 
	def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube):
		#instance variables : movie_title, movie_storyline, poster_image, trailer_youtube
		self.title = movie_title
		self.storyline = movie_storyline
		self.poster_image_url = poster_image
		self.trailer_youtube_url = trailer_youtube
    # display
	def show_trailer(self):
	    webbrowser.open(self.trailer_youtube_url)
