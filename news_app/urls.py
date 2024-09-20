# from django.urls import path
# from . import views

# urlpatterns = [
#     # path('', views.index, name='index'),
#     path('', views.landing_page, name='landing_page'),
#     path('category/<str:category>/', views.category_news, name='category_news'),
# ]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('select-category/', views.category_selection, name='category_selection'),
    # Other paths...
]
