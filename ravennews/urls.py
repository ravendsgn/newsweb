from django.urls import path
from .views import index, detail, error_page, contact, category_news

urlpatterns = [
    path('', index, name='index'),
    path('news/<int:news_id>/', detail, name='detail'),
    path('contact/', contact, name='contact'),
    path('404/', error_page, name='error_page'),
    path('category/<int:category_id>/', category_news, name='category_news'),  # New route for category filtering
]
from django.urls import path
from .views import add_comment, delete_comment

urlpatterns += [
    path('news/<int:news_id>/comment/', add_comment, name='add_comment'),
    path('comment/<int:comment_id>/delete/', delete_comment, name='delete_comment'),
]

from django.contrib.auth import views as auth_views
from .views import register, profile

urlpatterns += [
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name='logout'),
    path('profile/', profile, name='profile'),
]


# from django.urls import path
# from . import views  # Import views from the current app

# urlpatterns = [
#     path('', views.index, name='index'),
#     path('detail/', views.detail, name='detail'),
#     path('contact/', views.contact, name='contact'),
#     path('404/', views.error_page, name='error_page'),
#     path('pages/single_page/', views.detail, name='detail'),  # Define a view for this page
# ]
