from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns =[
    url(r'admin/',admin.site.urls),
    url(r'^accounts/login/$', views.LoginView.as_view(), name='login', kwargs={'template_name':'login.html'}),
    url(r'^accounts/logout/$', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    url(r'',include('blog.urls')),
]