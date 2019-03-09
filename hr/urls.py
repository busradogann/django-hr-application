from django.contrib import admin
from django.urls import path, include

from main.views import *

urlpatterns = [
    path('', JobsList.as_view(), name='job_list'),
    path('<int:pk>', JobDetail.as_view(), name='job_detail'),
    path('manager/create', ManagerJobCreate.as_view(), name='manager_job_create'),
    path('manager/applications', ManagerApplicationList.as_view(), name='manager_application_list'),
    path('manager/applications/<int:pk>', ManagerApplicationDetail.as_view(), name='manager_application_detail'),
    path('signup/', signup, name='signup'),
    path('', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]
