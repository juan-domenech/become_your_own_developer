"""become_your_own_developer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import RedirectView
from blog import views as blog_views
from accounts.views import profile, login, logout

urlpatterns = [
    # Admin Site
    url(r'^admin/', admin.site.urls),
    # In case of empty URL we send eveybody to /blog/
    url(r'^$', RedirectView.as_view(url='/blog/')),
    # Blog App
    url(r'^blog/$', blog_views.post_list ),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail ),
    # Accounts App
    #url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile,name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$',logout, name='logout'),

]


