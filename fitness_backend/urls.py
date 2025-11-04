from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

# Root/home view
def home(request):
    return JsonResponse({"message": "Fitness Tracker API is running!"})

urlpatterns = [
    path('', home, name='home'),  # <-- add this so / returns a response
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  # your register/login endpoints
]
