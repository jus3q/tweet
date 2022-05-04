from django.shortcuts import render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Tweet

# Create your views here.
def home_view(request, *args, **kwargs):
    # return HttpResponse("hi")
    return render(request, 'pages/home.html', context={}, status=200)

def tweet_detail_view(request, tweet_id, *args, **kwargs):
    ''' rest api view return json data, consume by java...'''
    data = {
        'id':tweet_id,
        # 'content':obj.content,
        # 'image_path': obj.image.url,
    }
    status = 200
    try:
        obj = Tweet.objects.get(id=tweet_id)
        data['content'] = obj.content
    except:
        data['message'] = 'not found'
        status = 404
    # return HttpResponse(f"hi {tweet_id} - {obj.content}")
    
    return JsonResponse(data, status=status)