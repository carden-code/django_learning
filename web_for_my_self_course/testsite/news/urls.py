from django.urls import path
from news.views import *

urlpatterns = [
    path('register/', register, name='register'),
    path('login/', user_login, name='login'),

    path('', HomeNews.as_view(), name='home'),
    # path('', index, name='home'),
    path('category/<int:category_id>/', NewsByCategory.as_view(), name='category'),
    # path('category/<int:category_id>/', get_category, name='category'),
    path('news/<int:pk>/', ViewNews.as_view(), name='view_news'),
    path('news/add-news/', CreateNews.as_view(), name='add_news')
]
