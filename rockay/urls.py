
from .views import RegionViewSet, LocationViewSet, FoodViewSet, Travel_typeViewSet, RouteViewSet, LivingViewSet, ContactViewSet
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'region/', RegionViewSet, basename='region')
router.register(r'location/', LocationViewSet, basename='location')
router.register(r'food/', FoodViewSet, basename='food')
router.register(r'travel/', Travel_typeViewSet, basename='traveltype')
router.register(r'route/', RouteViewSet, basename='route')
router.register(r'living/', LivingViewSet, basename='living')
router.register(r'contact/', ContactViewSet, basename='contact')

urlpatterns = router.urls

# router = routers.SimpleRouter()
# router.register(r'users', UserViewSet)
# router.register(r'accounts', AccountViewSet)

# urlpatterns = [
#     path('forgot-password/', ForgotPasswordFormView.as_view()),
# ]

urlpatterns += router.urls
