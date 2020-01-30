from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from D_IRIS import views

router = routers.DefaultRouter()
router.register(r'lk_mercado', views.LkMercadoView, 'D_IRIS')
router.register(r'validaftagg', views.ValidaFtAggView, 'D_IRIS')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
