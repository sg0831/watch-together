from django.contrib import admin
from django.urls import path, include

# 미디어 파일 저장 관련
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
	path("account/", include("account.urls") ),
	path("posts/", include("posting.urls") ),
] + static( settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
