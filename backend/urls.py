from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from account.views import CustomTokenObtainPairView  # Import your custom view
from django.conf import settings
from django.conf.urls.static import static
from django.urls import re_path

urlpatterns = [
    path('admin/', admin.site.urls),

    path('account/',include('account.urls')),
    
    path('store/',include('store.urls')),
    path('product/',include('product.urls')),
    path('idea/',include('idea.urls')),
    path('like/',include('like.urls')),
    path('reports/',include('report.urls')),
    path('cart/',include('cart.urls')),


    
    path('api/token/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),  # Use custom view
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)