from django.conf.urls import url
#from django.contrib import admin
from mysite.views import hello

#urlpatterns = [
#    url(r'^admin/', admin.site.urls),
#]

urlpatterns = [
    url(r'^hello/', hello),
]
