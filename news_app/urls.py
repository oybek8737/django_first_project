from django.urls import path
from .views import news_list,news_detail,homePageView,ContactPageView,error404PageView,aboutPageView,HomePageView

urlpatterns =[
    path('', HomePageView.as_view(), name='home_page'),
    path("news/all/", news_list, name='all_news_list'),
    path('news/<slug:news>/', news_detail, name='news_detail_page'),
    path('contact-us/', ContactPageView.as_view(), name='contact_page'),
    path('error404/', error404PageView, name='error404_page'),
    path('about/', aboutPageView, name='about_page')
]