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
from django.conf.urls import url, include
from django.contrib import admin
#from django.views.generic import RedirectView
from blog import views as blog_views
from accounts.views import profile, login, logout, register, cancel_subscription, subscriptions_webhook
# Media
from .settings import MEDIA_ROOT

# Heroku requisite
from django.contrib.staticfiles import views as static_views

# Home
from become_your_own_developer.views import home

# Forums
from threads import views as forum_views



urlpatterns = [

    # Admin Site
    url(r'^admin/', admin.site.urls),

    # # In case of empty URL we send eveybody to /blog/
    # url(r'^$', RedirectView.as_view(url='/blog/')),

    # Home
    url(r'^$', home, name='home'),

    # Blog App
    url(r'^blog/$', blog_views.post_list ),
    url(r'^blog/(?P<id>\d+)/$', blog_views.post_detail ),
    url(r'^post/edit/(?P<pk>\d+)/$', blog_views.edit_post, name='edit_post' ),
    url(r'^post/new/$', blog_views.new_post, name='new_post' ),

    # Accounts App
    url(r'^register/$', register, name='register'),
    url(r'^profile/$', profile,name='profile'),
    url(r'^login/$', login, name='login'),
    url(r'^logout/$',logout, name='logout'),

    # Flat Pages
    url(r'^pages/',include('django.contrib.flatpages.urls')),

    # Static folder for Heroku
    url(r'^static/(?P<path>.*)$', static_views.serve),

    # Media
    # url(r'^media/(?P<path>.*)$', static_views.serve,{'document_root':MEDIA_ROOT}),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',{'document_root':MEDIA_ROOT}),

    # Stripe URLs
    url(r'^cancel_subscription/$', cancel_subscription, name='cancel_subscription'),
    url(r'^subscriptions_webhook/$', subscriptions_webhook, name='subscriptions_webhook'),

    # Forum URLs
    url(r'^forum/$', forum_views.forum),
    url(r'^threads/(?P<subject_id>\d+)/$', forum_views.threads, name='threads'),
    url(r'^new_thread/(?P<subject_id>\d+)/$', forum_views.new_thread, name='new_thread'),
    url(r'^thread/(?P<thread_id>\d+)/$', forum_views.thread, name='thread'),
    url(r'^post/new/(?P<thread_id>\d+)/$', forum_views.new_post, name='new_post'),
    url(r'^post/edit/(?P<thread_id>\d+)/$', forum_views.edit_post, name='edit_post'),
    url(r'^post/delete/(?P<thread_id>\d+)/(?P<post_id>\d+)/$', forum_views.delete_post, name='delete_post'),

]


