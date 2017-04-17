# blog's urls.py , 
# You should define blog's urls.py in '/main urls.py'
# - from djang.conf.urls import include. url
# - urlpatterns = [ url(r'^blog/', include(blog.view ))]
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list),
    url(r'^(?P<id>\d+)/$', views.post_detail)
]
