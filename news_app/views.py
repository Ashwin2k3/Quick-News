# 
import requests
from django.conf import settings
from django.shortcuts import render

NEWS_API_URL = 'https://newsapi.org/v2/everything'
# INDIA_NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?sources=google-news-in'

# Use your provided API key for Indian news
INDIA_API_KEY = '7c9628099fbd4d63be8c502113ad9ec7'

# def fetch_news(category=None, is_indian_news=False, is_world_news=False):
#     params = {
#         'apiKey': settings.NEWS_API_KEY,
#         'language': 'en',
#         'sortBy': 'publishedAt',
#         'pageSize': 20,  # Number of articles to fetch (optional)
#     }

#     if is_indian_news:
#         # Fetch Indian news using the provided API key and country code 'in'
#         params['apiKey'] = INDIA_API_KEY
#         params['country'] = 'in'
#         response = requests.get(INDIA_NEWS_API_URL, params=params)
#     elif is_world_news:
#         # Fetch World news using keyword 'world'
#         params['q'] = 'world'
#         response = requests.get(NEWS_API_URL, params=params)
#     else:
#         # Fetch specific category news
#         params['q'] = category
#         response = requests.get(NEWS_API_URL, params=params)
    
#     return response.json().get('articles', [])

# def fetch_news(category=None, is_indian_news=False, is_world_news=False):
#     params = {
#         'apiKey': settings.NEWS_API_KEY,
#         'language': 'en',
#         'sortBy': 'publishedAt',
#         'pageSize': 20,
#     }
    
#     if is_indian_news:
#         params['apiKey'] = INDIA_API_KEY
#         params['country'] = 'in'
#         response = requests.get(INDIA_NEWS_API_URL, params=params)
#     elif is_world_news:
#         params['q'] = 'world'
#         response = requests.get(NEWS_API_URL, params=params)
#     else:
#         params['q'] = category
#         response = requests.get(NEWS_API_URL, params=params)

#     articles = response.json().get('articles', [])
    
#     # Remove duplicates based on URL
#     unique_articles = {}
#     for article in articles:
#         unique_articles[article['url']] = article

#     return list(unique_articles.values())
INDIA_NEWS_API_URL = 'https://newsapi.org/v2/top-headlines?sources=the-times-of-india,the-hindu,google-news-in'

def fetch_news(category=None, is_indian_news=False):
    params = {
        'apiKey': settings.NEWS_API_KEY,
        'language': 'en',
        'sortBy': 'publishedAt',
        'pageSize': 20,
    }
    
    if is_indian_news:
        response = requests.get(INDIA_NEWS_API_URL, params=params)
    else:
        params['q'] = category
        response = requests.get(NEWS_API_URL, params=params)

    articles = response.json().get('articles', [])
    
    # Remove duplicates based on URL
    unique_articles = {}
    for article in articles:
        unique_articles[article['url']] = article

    return list(unique_articles.values())


from django.shortcuts import render

def landing_page(request):
    return render(request, 'landing.html')

def category_selection(request):
    country = request.GET.get('country')
    category = request.GET.get('category')
    
    if country == 'in':
        is_indian_news = True
    else:
        is_indian_news = False

    # Call fetch_news with the selected country and category
    articles = fetch_news(category=category, is_indian_news=is_indian_news)

    context = {
        'articles': articles,
        'selected_country': country,
        'selected_category': category,
    }
    return render(request, 'category.html', context)


def index(request):
    context = {
        'articles': fetch_news(),
        'categories': ['technology', 'politics', 'geopolitics', 'health', 'sports', 'business', 'entertainment'],
    }
    return render(request, 'index.html', context)

def category_news(request, category):
    context = {
        'articles': fetch_news(category),
        'categories': ['technology', 'politics', 'geopolitics', 'health', 'sports', 'business', 'entertainment'],
        'selected_category': category
    }
    return render(request, 'category.html', context)

def category_selection(request):
    country = request.GET.get('country')
    category = request.GET.get('category')

    # Assuming fetch_news is already defined
    articles = fetch_news(category=category, is_indian_news=(country == 'in'))

    context = {
        'articles': articles,
        'selected_country': country,
        'selected_category': category,
    }
    return render(request, 'category.html', context)


def indian_news(request):
    context = {
        'articles': fetch_news(is_indian_news=True),
        'categories': ['technology', 'politics', 'geopolitics', 'health', 'sports', 'business', 'entertainment'],
    }
    return render(request, 'category.html', context)

def world_news(request):
    context = {
        'articles': fetch_news(is_world_news=True),
        'categories': ['technology', 'politics', 'geopolitics', 'health', 'sports', 'business', 'entertainment'],
    }
    return render(request, 'category.html', context)
