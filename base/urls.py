from django.contrib import admin
from django.urls import path, include

from base.views import base_views, customer_subscription_views, webhook_views

urlpatterns = [
    path('', base_views.homepage, name='home'),
    path('checkout/', base_views.checkout, name='checkout'),
    # path("logout", views.logout_request, name= "logout_request"),
	# path("login", views.login_request, name= "logout_request"),
	# path("register", views.register, name="register"),
	path("create-sub", customer_subscription_views.create_sub, name="create sub"),
	path("complete", customer_subscription_views.complete, name="complete"),
    path('webhook/', webhook_views.my_webhook_view, name='webhook')
]