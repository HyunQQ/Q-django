from django.conf.urls import include,url
from django.contrib import admin
from django.urls import path
from django.contrib.auth import views

# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]
urlpatterns =[
    path('admin/',admin.site.urls),
    path('accounts/login/', views.LoginView.as_view(), name='login', kwargs={'template_name':'login.html'}),
    path('accounts/logout/', views.LogoutView.as_view(), name='logout', kwargs={'next_page': '/'}),
    path('',include('blog.urls')),
]