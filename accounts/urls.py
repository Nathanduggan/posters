
from django.conf.urls import url, include
from accounts.views import logout, login, register, profile, index
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^login/', login, name="login"),
    url(r'^register/', register, name="register"),
    url(r'^profile/', profile, name="profile"),
    url(r'^index/', index, name="index"),
    url(r'^password-reset/', include(url_reset))
]