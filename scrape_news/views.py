from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from .scraping import get_news


def home(request):
    return render(request, 'scrape_news/scraping_news.html')

def scrape_news(request):
    if request.method == 'POST':
        url = request.POST['url']
        data = get_news(url)
        return JsonResponse({'data':data})
    else:
       return JsonResponse({'error':'Error'})