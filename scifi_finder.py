# pybites challenge: https://pybit.es/codechallenge25.html
# API: https://developers.themoviedb.org/3/getting-started

#!/usr/bin/python
import json
import requests
import os
from jinja2 import Environment, PackageLoader

# API key for TMDB
API_KEY = 'Your_API_Key'


def find_movies_with_genre(API_KEY, genre_id):
    # Requesting now_playing
    r = requests.get('https://api.themoviedb.org/3/movie/now_playing?<api_key>&language=en-US&page=1')
    # Turns json into dict
    now_playing = r.json()


    movie_list = []
    for item in now_playing['results']:
        if genre_id in item['genre_ids']:
            movie_list.append(item['original_title'])

    print movie_list

    # Create jinja2 environment
    try:
        env = Environment(loader=PackageLoader('scifi_finder', 'templates'))
        template = env.get_template('newsletter.html')
        rend = template.render(movie_list=movie_list)
        print "Templating successful"
        return rend
    except:
        print "Templating fail"
        return "Templating fail"



find_movies_with_genre(API_KEY, 878)
