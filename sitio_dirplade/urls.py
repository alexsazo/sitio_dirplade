from django.conf.urls import patterns, include, url

#Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

#Url de la app ciclo_calidad
urlpatterns = patterns('ciclo_calidad',
    url(r'^$', 'vista_inicio', name ='inicio'),
	url(r'^menu/$', 'vista_inicio', name ='inicio'),
	url(r'^ayuda/$', 'ayuda', name ='ayuda'),
)


urlpatterns += patterns('',
	#Inicio sesion y admin
	#url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
	url(r'^admin/', include(admin.site.urls)),	
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),    
)



#Url en modo debug para servir archivos estaticos

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )