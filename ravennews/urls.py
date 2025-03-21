from django.urls import path
from .views import index,detail, error_page,contact

urlpatterns = [
    path('',index,name='index'),
    path('news/<int:news_id>/',detail,name='detail'),
    path('contact/', contact, name='contact'),
    path('404/',error_page,name='error_page')
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
