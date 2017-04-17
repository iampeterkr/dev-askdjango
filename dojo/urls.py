# doso's urls.py

from django.conf.urls import url
from . import views
from . import views_cvb


urlpatterns = [
    url(r'^sum/(?P<numbers>[\d/]+)/$' , views.mysum),
    url(r'^hello/(?P<name>[ㄱ-힣/]+)/(?P<age>[\d/]+)/$' , views.hello),
    url(r'^list1/$' , views.post_list1),
    url(r'^list2/$' , views.post_list2),
    url(r'^list3/$' , views.post_list3),
    url(r'^exceldown/$', views.excel_download),
    url(r'^cvb/list1/$', views_cvb.post_list1),
    url(r'^cvb/list2/$', views_cvb.post_list2),
    url(r'^cvb/list3/$', views_cvb.post_list3),
    url(r'^cvb/exceldown/$' , views_cvb.ExcelDownloadView) ,

]


