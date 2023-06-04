import imdb
import requests
movies=imdb.Cinemagoer()

moviename=input("Enter the name of the movie: ")

movieid=movies.search_movie(moviename)[0].movieID
print(f"Movieid is {movieid}")

movie=movies.get_movie(movieid)
print(movie)
genre=movie.get('genre')
print(genre)

vote=movie.get('rating')
print(vote)

vote=movie.get('director')
print(vote)

company=movie.get('production companies')
print(company)

producer=movie.get('producer')
print(producer)

runtime=movie.get('runtimes')
print(runtime)

year=movie.get('year')
print(year)

votes=movie.get('votes')
print(votes)

writer=movie.get('writer')
print(writer)

rank=movie.get('top 250 rank')
print(rank)
plot=movie.get('plot')
print(plot)
coverurl=movie.get('full-size cover url')
print(coverurl)

requests.get(coverurl)
# [u'music department', 'sound crew', 'camera and electrical department', u'distributors', 'rating', 'runtimes', 'costume designer', u'thanks', 'make up', 'year', 'production design', 'miscellaneous crew', 'color info', u'casting department', 'languages', 'votes', 'producer', 'title', 'mpaa', 'assistant director', 'writer', 'production manager', 'casting director', 'visual effects', 'top 250 rank', 'set decoration', 'editor', 'certificates', u'costume department', 'country codes', 'language codes', 'cover url', u'special effects department', 'special effects companies', 'sound mix', 'genres', u'production companies', 'stunt performer', 'miscellaneous companies', 'cinematographer', 'art direction', 'akas', 'aspect ratio', 'director', 'kind', u'art department', 'countries', u'transportation department', 'plot outline', 'plot', 'cast', u'animation department', 'original music', u'editorial department', 'canonical title', 'long imdb title', 'long imdb canonical title', 'smart canonical title', 'smart long imdb canonical title', 'full-size cover url']
