from django.conf.urls import url
from testproject import views

#set the namespace
app_name = 'testproject'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]

