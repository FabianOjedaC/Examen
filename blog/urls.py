from django.conf.urls import include, url
from . import views
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'stock', views.ProductoViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'tienda', views.TiendaViewSet)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^index/$',views.index),
    url(r'^salir/index/$',views.index),
    url(r'^salir/$',views.salir,name="logout"),
    url(r'^registroProducto/$',views.registroProducto,name="registroProducto"),
    url(r'^login/$',views.ingreso,name="login"),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
