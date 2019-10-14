from django.urls import path

from . import views


urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    #path('login_action', views.login_action, name='login_action'),
    path('manage', views.manage, name='manage'),
    path('guest', views.guest, name='guest'),
    path('search_event', views.search_event, name='search_event'),
    path('search_guest', views.search_guest, name='search_guest'),
    path('qiandao/<int:event_id>', views.qiandao, name='qiandao'),
    path('qiandao_action/<int:event_id>', views.qiandao_action, name='qiandao_action'),
    path('logout', views.logout, name='logout'),

]
