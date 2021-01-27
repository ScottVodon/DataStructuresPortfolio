'''
------------------------------------------------------------------------
Movie class utility functions
------------------------------------------------------------------------
Author: Scott Vodon
ID:     181686100
Email:  vodo6100@mylaurier.ca
__updated__ = 2019 M01 14
------------------------------------------------------------------------
'''
from Movie import Movie

def get_movie():
    """
    -------------------------------------------------------
    Creates a Movie object by requesting data from a user.
    Use: movie = get_movie()
    -------------------------------------------------------
    Returns:
        movie - a Movie object based upon the user input (Movie).
    -------------------------------------------------------
    """
    title = input('Title: ')
    year = input('Year of release')
    director = input('Director: ')
    rating = input('Rating: ')
    genres = read_genres()
        
    movie = Movie(title,year,director,rating,genres)
    
    return movie


def read_movie(line):
    """
    -------------------------------------------------------
    Creates and returns a Movie object from a line of formatted string data.
    Use: movie = read_movie(line)
    -------------------------------------------------------
    Parameters:
        line - a vertical bar-delimited line of movie data in the format
          title|year|director|rating|genre codes (str)
    Returns:
        movie - a Movie object based upon the data from line (Movie)
    -------------------------------------------------------
    """

    line.strip()
    data = line.split('|')
    data[4] = data[4].split(',')
    genre_list = []
    
    title = data[0]
    year = int(data[1])
    director = data[2]
    rating = float(data[3])
    
    for i in data[4]:
        genre_list.append(int(i))
        
    genres = genre_list

    movie = Movie(title,year,director,rating,genres)
    
    return movie


def read_movies(fv):
    """
    -------------------------------------------------------
    Reads a file of string data into a list of Movie objects.
    Use: movies = read_movies(fv)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
    Returns:
        movies - a list of Movie objects (list of Movie)
    -------------------------------------------------------
    """
    fv.seek(0)
    movies = []
    
    for line in fv:
        movie = read_movie(line)
        movies.append(movie)

    return movies


def menu():
    """
    -------------------------------------------------------
    Prints all genres in the Movie.GENRES list. Use for input menus.
    Use: menu()
    -------------------------------------------------------
    Returns:
        None
    -------------------------------------------------------
    """
    print('Genres')
    for i in range(0,len(Movie.GENRES)):
        print('{:>2}:  {}'.format(i,Movie.GENRES[i]))

    return


def read_genres():
    """
    -------------------------------------------------------
    Asks a user to select genres from a list of genres and returns
    an integer list of the genres chosen.
    Use: genres = read_genres()
    -------------------------------------------------------
    Returns:
        genres - sorted numeric list of movie genres (list of int)
    -------------------------------------------------------
    """

    menu()
    genres = []
    genre = input('Enter a genre number (ENTER to quit):')
    while genre != '' or len(genres) == 0:
        if not genre.isdigit():
            print('Error: not a positive number')
        else:
            genre = int(genre)
            if genre in genres:
                print('Error: genre already chosen')
            elif genre >= len(Movie.GENRES):
                print('Error: input must be < {}'.format(len(Movie.GENRES)))
            else:
                genres.append(genre)
            
        genre = input('Enter a genre number (ENTER to quit):')
        genres.sort()

    return genres


def write_movies(fv, movies):
    """
    -------------------------------------------------------
    Writes the contents of movies to fv. Overwrites or
    creates a new file of Movie objects converted to strings.
    Use: write_movies(fv, movies)
    -------------------------------------------------------
    Parameters:
        fv - an already open file of movie data (file)
        movies - a list of Movie objects (list of Movie)
    Returns:
        None
    -------------------------------------------------------
    """

    # Your code here

    return


def get_by_year(movies, year):
    """
    -------------------------------------------------------
    Creates a list of Movies from a particular year.
    Use: ymovies = get_by_year(movies, year)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        year - the Movie year to select (int)
    Returns:
        ymovies - Movie objects whose year attribute is 
            year (list of Movie)
    -------------------------------------------------------
    """
    ymovies = []
    for movie in movies:
        if movie.year == year:
            ymovies.append(movie)

    return ymovies


def get_by_rating(movies, rating):
    """
    -------------------------------------------------------
    Creates a list of Movies whose ratings are equal to or higher
    than rating.
    Use: rmovies = get_by_rating(movies, rating)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        rating - the minimum Movie rating to select (float)
    Returns:
        rmovies - Movie objects whose rating attribute is 
            greater than or equal to rating (list of Movie)
    -------------------------------------------------------
    """

    rmovies = []
    for movie in movies:
        if movie.rating == rating:
            rmovies.append(movie)

    return rmovies


def get_by_genre(movies, genre):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include genre.
    Use: gmovies = get_by_genre(movies, genre)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genre - the genre code to look for (int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            genre (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    
    for i in movies:
        if genre in i.genres:
            gmovies.append(i)

    return gmovies


def get_by_genres(movies, genres):
    """
    -------------------------------------------------------
    Creates a list of Movies whose list of genres include all the genre
    codes in genres.
    Use: m = get_by_genres(movies, genres)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
        genres - the genre codes to look for (list of int)
    Returns:
        gmovies - Movie objects whose genre list includes 
            all the genres in genres (list of Movie)
    -------------------------------------------------------
    """

    gmovies = []
    
    for movie in movies:
        flag = True
        for i in genres:
            if i not in movie.genres:
                flag = False
        if flag ==  True:
            gmovies.append(movie)
            
    return gmovies


def genre_counts(movies):
    """
    -------------------------------------------------------
    Counts the number of movies in each genre given in Movie.GENRES.
    Use: counts = genre_counts(movies)
    -------------------------------------------------------
    Parameters:
        movies - a list of Movie objects (list of Movie)
    Returns:
        counts - the number of Movies in each genre in Movie.GENRES.
            The index of each number in counts is the index of
            the matching genre in Movie.GENRES. (list of int)
    -------------------------------------------------------
    """
    counts = []
    for i in range(len(Movie.GENRES)):
        count = 0
        for movie in movies:
            if i in movie.genres:
                count += 1
        counts.append(count)

    return counts
