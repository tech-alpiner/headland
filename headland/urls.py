from django.contrib.auth import views as auth_views
from django.views.generic import RedirectView
from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'headland.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/logout/$', auth_views.logout, kwargs={'next_page': 'home'}, name='auth_logout'),
    url(r'^register/complete/$', RedirectView.as_view(pattern_name='home'), name='registration_complete'),
    url(r'^accounts/', include('registration.backends.simple.urls', namespace='users')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('headland_app.urls')),
]
