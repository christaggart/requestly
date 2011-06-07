from django.conf.urls.defaults import patterns, include, url
from django.views.generic import ListView, DetailView
from requests.models import Request

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'requestly.views.home', name='home'),
    (r'^accounts/', include('allauth.urls')),
    (r'^requests/$', ListView.as_view(
            model=Request,
            context_object_name="request_list",
            paginate_by=10,
            allow_empty=True,
        )),
    (r'^requests/(?P<pk>\d+)/$', DetailView.as_view(
            model=Request,
            context_object_name="request_object",
        )),
        
	# Generic view to vote on Link objects
    (r'^requests/(?P<pid>\d+)/(?P<direction>up|down|clear)vote/?$',
        vote_on_object, dict(model=Request, template_object_name='request',
            template_name='requests/request_confirm_vote.html',
            allow_xmlhttprequest=True)),

    # url(r'^dataott/', include('dataott.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
