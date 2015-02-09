import media
import fresh_tomatoes

#an object for each movie is created
trance = media.Movie('Trance',
                     'An art auctioneer who has become mixed up with a group of criminals partners with a hypnotherapist in order to recover a lost painting.',
                     'http://ia.media-imdb.com/images/M/MV5BMjMzNjU1MTg5NF5BMl5BanBnXkFtZTcwMTExMTcwOQ@@._V1_SX214_AL_.jpg',
                     'https://www.youtube.com/watch?v=cQ-qYX9Oz1c',
                     'James McAvoy, Rosario Dawson, Vincent Cassel',
                     '27 March 2013 (UK)')

inception = media.Movie('Inception',
                        'A thief who steals corporate secrets through use of dream-sharing technology is given the inverse task of planting an idea into the mind of a CEO.',
                        'http://ia.media-imdb.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SX214_AL_.jpg',
                        'https://www.youtube.com/watch?v=8hP9D6kZseM',
                        'Leonardo DiCaprio, Joseph Gordon-Levitt, Ellen Page',
                        '16 July 2010 (USA)')

gravity = media.Movie('Gravity',
                      'A medical engineer and an astronaut work together to survive after a catastrophe destroys their shuttle and leaves them adrift in orbit.',
                      'http://ia.media-imdb.com/images/M/MV5BNjE5MzYwMzYxMF5BMl5BanBnXkFtZTcwOTk4MTk0OQ@@._V1_SY317_CR0,0,214,317_AL_.jpg',
                      'https://www.youtube.com/watch?v=OiTiKOy59o4',
                      'Sandra Bullock, George Clooney, Ed Harris',
                      '4 October 2013 (USA)')

the_avengers = media.Movie('The Avengers',
                           'Earth\'s mightiest heroes must come together and learn to fight as a team if they are to stop the mischievous Loki and his alien army from enslaving humanity.',
                           'http://ia.media-imdb.com/images/M/MV5BMTk2NTI1MTU4N15BMl5BanBnXkFtZTcwODg0OTY0Nw@@._V1_SY317_CR0,0,214,317_AL_.jpg',
                           'https://www.youtube.com/watch?v=1hPpG4s3-O4',
                           'Robert Downey Jr., Chris Evans, Scarlett Johansson',
                           '4 May 2012 (USA)')

the_maze_runner = media.Movie('The Maze Runner',
                              'Thomas is deposited in a community of boys after his memory is erased, soon learning they\'re all trapped in a maze that will require him to join forces with fellow "runners" for a shot at escape.',
                              'http://ia.media-imdb.com/images/M/MV5BMjUyNTA3MTAyM15BMl5BanBnXkFtZTgwOTEyMTkyMjE@._V1_SX214_AL_.jpg',
                              'https://www.youtube.com/watch?v=64-iSYVmMVY',
                              'Dylan O\'Brien, Kaya Scodelario, Will Poulter',
                              '19 September 2014 (USA)')

eight_mile = media.Movie('8 Mile',
                     'A young rapper, struggling with every aspect of his life, wants to make the most of what could be his final opportunity but his problems around gives him doubts.',
                     'http://ia.media-imdb.com/images/M/MV5BMTU2MTgyOTk3MF5BMl5BanBnXkFtZTYwOTg2NTI5._V1_SX214_AL_.jpg',
                     'https://www.youtube.com/watch?v=axGVrfwm9L4',
                     'Eminem, Brittany Murphy, Kim Basinger',
                     '8 November 2002 (USA)')

#movies are put in an array so they can be usen in open_movies_page function
movies = [trance, inception, gravity, the_avengers, the_maze_runner, eight_mile]
fresh_tomatoes.open_movies_page(movies)
