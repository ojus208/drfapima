from xml.etree.ElementInclude import include
from rest_framework.routers import SimpleRouter
from .views import bookacallview , contactformview
from django.urls import path, include

# router = SimpleRouter()
# router.register("bookacall",bookacallview )
# router.register("contactfrom",contactformview )

urlpatterns = [
    path("bookacall", bookacallview ),
    path("contactform", contactformview)
]