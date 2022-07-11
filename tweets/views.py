from django.shortcuts import render
from django.http import Http404, HttpResponse, Http404,JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    print(args,kwargs)
    return HttpResponse("<h1> Hello World</h1>")

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    
    """
    REST API VIEW
    consome by javascript or swift or java
    return json Data
    """
    data = {
        "id": tweet_id,
       
        #"image_path": obj.image.url
    }
    status = 200
    
    try: 
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = "Not found"
        status = 404
    
    
    return JsonResponse(data, status=status) #json.dump 