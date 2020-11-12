
from django.urls import path

from . import views
from .views import news,home,contact
from .views import BlogList,BlogDetailView,BlogDetaileView,Blogs,BlogUpdateView
from django.conf.urls import url
from .views import BlogDeleteView
from .views import PublisherDetail


urlpatterns = [
    path('', home, name="home"),
    path('news/', news, name="news"),
    path('contact/', contact, name="contact"),
    path('blog/', BlogList.as_view(), name="blogs"), 
    path('blog/<pk>/', BlogDetailView.as_view()), 
    path('blogs/<slug:slug>/', BlogDetaileView.as_view()),
    path('blogs/', Blogs.as_view(), name="bloggy"), #slug = slug field
    path('create/', views.BlogCreateView.as_view(model="Blog", success_url="/blog/")),
    path('<pk>/update', BlogUpdateView.as_view()), 
    path('<pk>/delete/', BlogDeleteView.as_view()), 
    path('home/', views.welcome),
    path('register', views.register),
    path('login', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    url(r'^myblog/$', views.BlogByUserListView.as_view(), name='my-blog'),
    path('<pk>/interest/', PublisherDetail.as_view(), name='interest'),
]       