from django.conf.urls.defaults import *

from locations_app.views import *
from recipes_app.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'phillyphoodaccess.views.home', name='home'),
    # url(r'^phillyphoodaccess/', include('phillyphoodaccess.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    ('^$', home),
    ('^recipes', recipe_search),
    ('^recipe_search', recipe_results),
    ('^directions', direction_results),
    ('^search_again', home)
)
