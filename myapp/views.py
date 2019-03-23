from django.shortcuts import render, render_to_response
from django.http import HttpResponse
import requests
import json

# Create your views here.
def index(response):
    url = 'https://swapi.co/api/films'
    response = requests.get(url)
    data = response.json()
    peliculas = {'peliculas':[]}
    for i in data['results']:
        id = i['url'].split('/')[-2]
        peliculas['peliculas'].append({'title':i['title'], 'episode_id':i['episode_id'],
         'release_date':i['release_date'], 'director':i['director'],
         'producer':i['producer'], 'id': str(id)})
    return render_to_response('index.html',peliculas)

def movie(response,movie):
    url = 'https://swapi.co/api/films/' + str(movie)
    response = requests.get(url)
    data = response.json()
    movie = {}
    for k,v in data.items():
        if (k == "species" or k == "vehicles" or  k == "url" or
        k == "edited" or k == "created"):
            pass
        elif k == "characters":
            names = {}
            for n in data["characters"]:
                response = requests.get(n)
                data = response.json()
                names[data["name"]] = n.split('/')[-2]
            movie[k] = names
        else:
            movie[k] = v
    data = {"movie": movie}
    return render_to_response('movie.html', data)

def character(response, character):
    url = 'https://swapi.co/api/people/' + str(character)
    response = requests.get(url)
    data = response.json()
    print(data)
    return render_to_response('character.html', {"character" : data})
