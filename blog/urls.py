from djzen.urls import zen_url

urlpatterns = [
  zen_url('about', views.about_page),
 ]
