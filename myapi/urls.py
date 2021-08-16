from django.conf.urls import url 
from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
urlpatterns = [
	# viewssssssss
	url(r"^token/$", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    url(r"^token/refresh/$", TokenRefreshView.as_view(), name='token_refresh'),
	url(r"^api-reporters$", views.api_all_reporter, name="api_all_reporter"),
	url(r"^view-api-reporters/(?P<reporter_id>[0-9]+)$", views.api_view_reporter, name="api_view_reporter"),
	url(r"^add-api-reporters$", views.api_add_reporter, name="api_add_reporter"),
	url(r"^update-api-reporters/(?P<reporter_id>[0-9]+)$", views.api_upate_reporter, name="api_upate_reporter"),
	url(r"^delete-api-reporters/(?P<reporter_id>[0-9]+)$", views.api_delete_reporter, name="api_delete_reporter"),
	
	# class
	url(r"^class-reporters$", views.ReporterListView.as_view()),
	url(r"^ts-class-reporters/(?P<reporter_id>[0-9]+)$", views.ReporterAPI.as_view()),

]