from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns =[
    url(r'admin/',admin.site.urls),
    # url(r'^accounts/login/$', views.login, name='login'),
    url(r'',include('blog.urls')),
]