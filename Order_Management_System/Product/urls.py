from rest_framework.routers import DefaultRouter
from Product.views import ProductViewsets, OrderViewsets, UsersViewsets

#-- router
router = DefaultRouter()

#--- Urls to the viewset
router.register(r"product", ProductViewsets, basename="Prods")
router.register(r"order", OrderViewsets, basename="orders")
router.register(r"user", UsersViewsets, basename="users")


