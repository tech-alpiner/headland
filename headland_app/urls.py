from django.conf.urls import url
import views

urlpatterns = [
    
    # url(r'^home/$', views.home, name='home'),
    url(r'^$', views.home, name='home'),

    # blog urls
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^contact/$', views.contact, name='contact'),
]