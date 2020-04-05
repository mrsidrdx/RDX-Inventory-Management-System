from django.urls import path
from inventapp import views

urlpatterns = [
    path('saveObject/<str:objectType>/',views.saveObject,name='saveObject'),
    path('updateObject/<str:objectType>/<str:objectId>',views.updateObject,name='updateObject'),
    path('showObjects/<str:objectType>',views.showObjectList, name='showObjects'),
    path('showObjectDetails/<str:objectType>/<str:objectId>',views.showObjectDetail,name='showObjectDetail'),
    path('modelObjects/<str:objectType>',views.modelObjects,name='addEditObjects'),
    path("register/", views.register, name="register"),
    path("login/", views.user_login, name="user_login"),
    path('logout/', views.user_logout, name='logout'),
]
