"""mbou URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls.static import static
from mbou import views, settings
from django.views.static import serve

urlpatterns = [
    url(r'^admin/', admin.site.urls, name = "admin"),
    url(r'^index/', views.index, name = "index"),
    url(r'^base/', views.base, name = "base"),
    url(r'^news/(?P<id>\d+)/?$', views.news, name = "news"),
    url(r'^news/add/$', views.news_add, name = "add_news"),
    url(r'^schedule/edit/$', views.schedule_edit, name = "edit_schedule"),
    url(r'^schedule/show/(?P<sform_no>\d+)/?$', views.schedule_show, name = "schedule_show"),
    url(r'^lessons/edit/$', views.lesson_edit, name = "edit_lesson"),
    url(r'^lessons/show/$', views.lessons_show, name = "lessons_show"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
