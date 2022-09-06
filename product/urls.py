from product.views import TestView

from django.urls import path

# The API URLs are now determined automatically by the router.
urlpatterns = [
    path('v1/test/', TestView.as_view(), name='test'),
]