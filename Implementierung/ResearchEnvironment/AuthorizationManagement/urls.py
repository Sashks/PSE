from django.urls import path
from django.conf.urls import url

from AuthorizationManagement import views
from django.urls.conf import re_path

urlpatterns = [
    path('', views.homeView, name='home'),

    
    
    #this section should be commented for now, so that we can work with the /admin interface from django; 
    #that means views.foo should not be used for now
    
    
    
    re_path(r'^profile/(?P<pk>\d+)$', views.ProfilView.as_view(), name = 'profile'),
#     re_path(r'^profile/handle_(?P<requestID>\w+)/$', views.foo),
#     re_path(r'^profile/resources/$', views.index),
#     re_path(r'^profile/resources/add_new_resource/$', views.index),
#     re_path(r'^profile/resources/(?P<resourceID>\w+)_send_deletion_request/$', views.foo),
#     re_path(r'^profile/resources/(?P<resorceID>\w+)_edit_users_permissions/$', views.foo),
#     re_path(r'^profile/resources/(?P<resourceID>\w+)_edit_users_permissions/reason_for_change/$', views.foo),
#        
#     re_path(r'^login/$', views.index),
#        
#     re_path(r'^manage_users/$', views.index),
#     re_path(r'^manage_users/block_user/$', views.index),
#     re_path(r'^manage_users/delete_user/$', views.index),
#     re_path(r'^manage_users/(?P<userID>\w+)_permissions_for_resources/$', views.foo),
#     re_path(r'^manage_users/(?P<userID>\w+)_permissions_for_resources/reason_for_change/$', views.foo),
#        
#     re_path(r'^manage_resources/$', views.index),
#     re_path(r'^manage_resources/delete_resource/$', views.index),
#     re_path(r'^manage_resources/(?P<resourceID>\w+)_permissions_for_users/$', views.foo),
#     re_path(r'^manage_resources/(?P<resourceID>\w+)_permissions_for_users/reason_for_change/$', views.foo),
#        
      re_path(r'^search-resources/$', views.search_form, name='search-resources'),
      re_path(r'^search/$', views.search, name='search'),
      re_path(r'^search/(?P<pk>\d+)$', views.ResourceDetailView.as_view(), name='resource-info')
      
      
#     path(r'^?P<pk>\w+)_info/$', views.Details.as_view(), name='details'), *in process*
#     re_path(r'^resources_overview/(?P<resourceID>\w+)_send_request/$', views.foo),
#        
#     re_path(r'^(?P<resourceID>\w+)/$', views.foo),
      
     
    
]