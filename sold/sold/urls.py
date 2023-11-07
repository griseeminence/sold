from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import CreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('django.contrib.auth.urls')),
    # path(
    #     'auth/registration/',
    #     CreateView.as_view(
    #         template_name='registration/registration_form.html',
    #         form_class=UserCreationForm,
    #         success_url=reverse_lazy('articles:index'),
    #     ),
    #     name='registration',
    # ),
    path('', include('core.urls')),
    path('', include('item.urls')),
    path('', include('dashboard.urls')),
    path('', include('communication.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


if settings.DEBUG:
    import debug_toolbar
    urlpatterns += (path('__debug__/', include(debug_toolbar.urls)),)