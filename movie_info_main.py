import media
import fresh_tomatoes
"""Main module of the project."""

#four instances of my favourite movies
a_Space_Odyssey = media.Movie("2001: A Space Odyssey",
                              """http://t0.gstatic.com/images?q=tbn:ANd9GcQdmmLZ7\
                              lXsw1WRy7c5qN3mka2e9ANSpHIG2INi53P6OVS8KyJo""",
                              "https://www.youtube.com/watch?v=XHjIqQBsPjk")
arrival = media.Movie("Arrival",
                      """http://t0.gstatic.com/images?q=tbn:ANd9GcSMztV\
                      icsYXcHHWNkejxIoFcW4H1eKhjSghAVixeAueuPEXmSKN""",
                      "https://www.youtube.com/watch?v=ZLO4X6UI8OY")
fight_club = media.Movie("Fight Club",
                         """https://images-na.ssl-images-amazon.com/images/M/MV5BZGY5Y2RjMmItNDg5Yy00NjUwLThjMTEtNDc2OGUzNTBiYmM1XkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_UX182_CR0,0,182,268_AL_.jpg""",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg")
i_am_legend = media.Movie("I Am Legend",
                          """http://www.gstatic.com/tv/thumb/movieposters/170977/p170977_p_v8_ah.jpg""",
                          "https://www.youtube.com/watch?v=ewpYq9rgg3w")

#create a list of movies as input for the function
movies = [a_Space_Odyssey, arrival, fight_club, i_am_legend]
#the function to display the web
fresh_tomatoes.open_movies_page(movies)
