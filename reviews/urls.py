from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'create/(?P<product_id>[0-9]+)/$',
        views.CreateReview.as_view(), name='create'),
    url(r'edit/(?P<review_id>[0-9]+)/$',
        views.EditReview.as_view(), name='edit'),
]
