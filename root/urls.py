from django.conf.urls import url
import solver.views as views

urlpatterns = [
	url(r'^$', views.home, name='Home'),
	url(r'^(?P<input_sudoku>[0-9]{81})', views.solution, name='Solution'),
]
