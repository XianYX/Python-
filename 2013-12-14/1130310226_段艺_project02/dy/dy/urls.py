from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from django.contrib.auth.views import login,logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'dy.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$','addr_book.views.index'),
    url(r'^login/$','addr_book.views.login'),
    url(r'^accounts/login/$','addr_book.views.login'),
    url(r'^register/$','addr_book.views.register'),
    url(r'^logout/$','addr_book.views.logout'),
    url(r'^add/$','addr_book.views.add'),
    url(r'^show/$','addr_book.views.show'),
    url(r'^delete/$','addr_book.views.delete'),
    url(r'^change/$','addr_book.views.change'),
    url(r'^setpasswd/$','addr_book.views.setpasswd'),
    url(r'^setsuccess/$','addr_book.views.setsuccess'),
)
