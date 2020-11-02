import requests
from django.shortcuts import render
from bs4 import BeautifulSoup
from request.compat import quote_plus
from . import models
BASE_URL ='https://mumbai.craigslist.org/search/?query={}'


def home(request):
    return render(request,'base.html')
# Create your views here.

def new_search(request):
    search = request.POST.get('search')
    models.Search.objects.create(search=search)
    final_url = BASE_URL.format(quote_plus(search))
    response=requests.get(final_url)
    data= response.text
    soup = BeautifulSoup(data, features='html.parser')
    post_titles = soup.find_all('a',{'class':'result-title'})
    
    return render(request,'craigslist/new_search.html',{'search':search})
