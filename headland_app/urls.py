import views
from django.conf.urls import url
from views import UserProfileDetailView, UserProfileEditView
from django.contrib.auth.decorators import login_required as auth


urlpatterns = [
    
    # url(r'^home/$', views.home, name='home'),
    url(r'^news/$', views.home, name='home'),

    # blog urls
    url(r'^blog/$', views.post_list, name='post_list'),
    url(r'^blog/post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
    url(r'^blog/post/new/$', views.post_new, name='post_new'),
    url(r'^blog/post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^users/(?P<slug>\w+)/$', UserProfileDetailView.as_view(), name="profile"),
    url(r'^edit_profile/$', auth(UserProfileEditView.as_view()), name="edit_profile"),
]