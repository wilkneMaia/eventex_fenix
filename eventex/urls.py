from django.contrib import admin
from django.urls import include, path


import eventex.core.views
import eventex.subscriptions.views
# from eventex.subscriptions.views import subscribe

urlpatterns = [
    path('', eventex.core.views.home),
    path('inscricao/', eventex.subscriptions.views.subscribe),
    path('admin/', admin.site.urls),
]
