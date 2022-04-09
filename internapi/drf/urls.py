from django.urls import path
from . import views
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views
urlpatterns = [
	path('', views.apiOverview, name="api-overview"),
	path('details-list/', views.DetailsList, name="details-list"),
	path('details-detail/<str:pk>/', views.DetailsDetail, name="details-detail"),
	path('details-create/', views.DetailsCreate, name="details-create"),

	path('details-update/<str:pk>/', views.DetailsUpdate, name="detaiils-update"),
	path('details-delete/<str:pk>/', views.DetailsDelete, name="details-delete"),

	path('register/', RegisterAPI.as_view() , name='register'),
	path('login/', LoginAPI.as_view() , name='login'),
	 path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]