"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from . import views_pdf

urlpatterns = [
    path("admin/", admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('pessoas.urls')),
    path('documentos/', include('documentos.urls')),
    path('registros/', include('registros.urls')),

    # PDFs
    path('pdf/pessoa/<int:pk>/',    views_pdf.pdf_pessoa,    name='pdf_pessoa'),
    path('pdf/fato/<int:pk>/',      views_pdf.pdf_fato,      name='pdf_fato'),
    path('pdf/relatorio/<int:pk>/', views_pdf.pdf_relatorio, name='pdf_relatorio'),
    path('pdf/memoria/<int:pk>/',   views_pdf.pdf_memoria,   name='pdf_memoria'),

    # Servir arquivos estáticos e mídia mesmo com DEBUG=False (uso local)
    re_path(r'^static/(?P<path>.*)$',  serve, {'document_root': settings.STATIC_ROOT}),
    re_path(r'^media/(?P<path>.*)$',   serve, {'document_root': settings.MEDIA_ROOT}),
]

