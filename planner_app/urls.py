from django.urls import path
from . import views

urlpatterns=[

path(
'welcome/',
views.welcome
),

path(
'signup/',
views.signup,
name='signup'
),

path(
'login/',
views.user_login,
name='login'
),

path(
'home/',
views.home
),

path(
'success/',
views.success,
name='success'
),

path(
'user_logout/',
views.user_logout
),

path(
'dashboard/',
views.dashboard
),

path(
'timetable/',
views.timetable
),

path(
'add/',
views.add_subject
),

path(
'export/',
views.export_timetable
),

path(
'chat/',
views.chatbot
)

]
