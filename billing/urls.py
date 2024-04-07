from django.urls import path, include
from rest_framework.routers import SimpleRouter
from . import views

router = SimpleRouter()
router.register(r'products', views.ProductViewset)
router.register(r'bills', views.BillViewSet)
router.register(r'billedproducts', views.BilledProductViewSet, basename='billedproducts')
router.register(r'customers', views.CustomerViewSet, basename='customers')
router.register(r'employees', views.EmployeeViewSet, basename='employees')

urlpatterns = [
    path('logout/', views.logout, name='logout'),
    path('api-auth/', include('rest_framework.urls', namespace = 'restframework'))   
]

urlpatterns += router.urls