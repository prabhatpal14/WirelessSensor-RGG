from django.conf.urls import url

from plot import views

urlpatterns = [
    url(r'^plot', views.plot_graph),
    url(r'^algo', views.smallest_last_order),
    url(r'^$', views.plot_graph),
]