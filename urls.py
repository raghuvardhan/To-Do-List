from onlineapp import views
from django.conf.urls import url
from onlineapp import classviews
from django.contrib.auth import views as auth_views

urlpatterns = [
    url(r'^colleges/$', views.college_list, name="colleges"),
    url(r'^colleges/(?P<pk>[0-9]+)/$',views.college_detail,name = "college_detail"),
    url(r'^students/$',views.student_list, name = "students"),
    url(r'^students/(?P<pk>[0-9]+)/$',views.student_detail,name='student_detail'),
    url(r'^colleges/(?P<pk>[0-9]+)/student/$',views.college_student_list,name='college_students_list'),
    url(r'^colleges/([a-z]+)/$',classviews.CollegeViewLocation.as_view(),name = "college_location"),
    url(r'^create/$',classviews.CreateCollegeView.as_view(),name = "create_college"),
    url(r'^colleges/(?P<pk>[0-9]+)/update/$',classviews.UpdateCollegeView.as_view(),name = "update_college"),
    url(r'^colleges/(?P<pk>[0-9]+)/delete/$',classviews.DeleteCollegeView.as_view(),name = "delete_college"),
    url(r'^colleges/(?P<id>[0-9]+)/email/',views.email,name = "send_email"),
    url(r'login/$',auth_views.login,name = "login"),
    url(r'^logout/$',auth_views.logout,name = "logout"),
    url(r'^colleges/(?P<slug>[a-z]+)/$', classviews.StudentViewAcronym.as_view(), name="studets_details_acr"),
]