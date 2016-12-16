#!python
# log/urls.py
from django.conf.urls import url
from . import views

# We are adding a URL called /home
urlpatterns = [
    url(r'^$', views.home, name='home'),

    url(r'^library/$', views.library, name='library'),
    url(r'^clearlibrary/$', views.clearLibrary, name='clearlibrary'),

    url(r'^cc/$', views.cc, name='cc'),
    url(r'^clearcc/$', views.clearcc, name='clearcc'),

    url(r'^subhansrihostel/$', views.subhansrihostel, name='subhansrihostel'),
    url(r'^clearsubhansrihostel/$', views.clearsubhansrihostel, name='clearsubhansrihostel'),

    url(r'^umiamhostel/$', views.umiamhostel, name='umiamhostel'),
    url(r'^clearumiamhostel/$', views.clearumiamhostel, name='clearumiamhostel'),

    url(r'^csedept/$', views.csedept, name='csedept'),
    url(r'^clearcsedept/$', views.clearcsedept, name='clearcsedept'),

    url(r'^dhansarihostel/$', views.dhansarihostel, name='dhansarihostel'),
    url(r'^cleardhansarihostel/$', views.cleardhansarihostel, name='cleardhansarihostel'),

    url(r'^gymkhana/$', views.gymkhana, name='gymkhana'),
    url(r'^cleargymkhana/$', views.cleargymkhana, name='cleargymkhana'),

    url(r'^student/$', views.student, name='student'),


]
