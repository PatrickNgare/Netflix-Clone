from django.shortcuts import render
import tmdbsimple as tmdb


tmdb.API_KEY='9c82e3db6480e76674d7cd0897cfd06b'
 
def index(request):
    
   
    populars = tmdb.Movies().popular()['results']
    
    print(populars)
    
   

    return render(request,'temps/index.html',{"populars": populars})

