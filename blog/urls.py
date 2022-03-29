from django.conf.urls import url
from .views import index, add_posts, delete_posts, update_posts, login

urlpatterns = [
	url(r'^$', login, name='login'),
	url(r'^index$', index, name='index'),
	url(r'^add_posts$', add_posts, name='add-posts'),
	url(r'^delete_posts/(?P<posts_id>\d+)$', delete_posts, name='delete-posts'),
	url(r'^update_posts/(?P<posts_id>\d+)$', update_posts, name='update-posts'),
]