from django.conf.urls import url 
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from . import base_class_view
from . import user_views
# from .views import post_list, post_create, post_detail, 

urlpatterns = [
	# ________view (	viết theo dạng HÀM )
	url(r"^$", views.index, name="index"),
	url(r"^add-reporter$", views.add_reporter, name="add_reporter"),
	url(r"^add-article$", views.add_article, name="add_article"),
	url(r"^list-reporters",views.list_reporters,name="list_reporters"),
	# url(r'^gioi-thieu$', 'blog', name='gioi_thieu'),

	# ______class_base_view
	# b2: vào urls myapp để thêm đường dẫn
	# cach 1:
	# path("reporter/<int:reporter_id>", views.view_detail_reporter, name ="view_detail_reporter")
	# cach 2:
	url(r"^reporter/(?P<reporter_id>[0-9]+)$",views.view_detail_reporter, name ="view_detail_reporter"),
	url(r"^all-reporter$",base_class_view.ReportListView.as_view(), name="all_reporters"), #list_view (class_base)
	url(r"^view-reporter/(?P<pk>[0-9]+)$",base_class_view.ReportDetailView.as_view(), name="view_reporter"),
	url(r"^insert-reporter/$",base_class_view.ReporterCreateView.as_view(), name="insert_reporter"),
	url(r"^edit-reporter/(?P<pk>[0-9]+)$",base_class_view.ReporterUpdateView.as_view(), name="edit_reporter"),
	url(r"^remove-reporter/(?P<pk>[0-9]+)$",base_class_view.ReporterDeleteView.as_view(), name="remove_reporter"),
	
	# User
	url(r"^register$",user_views.register_user, name="register_user"),
	url(r"^login$",user_views.login_user, name="login_user"),
	url(r"^logout$",auth_views.LogoutView.as_view(next_page="/"), name="logout_user"),


]