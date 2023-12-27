from django.urls import path
from . import views

app_name = "web"

urlpatterns = [
    #account
    path("signin/", views.MyObtainTokenPairView.as_view(), name="token_obtain_pair"),
    path("register/", views.RegisterView.as_view(), name="auth_register"),
    #api
    path('leads/', views.LeadViewSet.as_view({'get': 'list','post': 'create'}), name='lead-list'),
    path('leads/<int:pk>/', views.LeadViewSet.as_view({'delete':'destroy','put':'update'}), name='lead-delete'),
    path('deals/', views.DealViewSet.as_view({'get': 'list','post': 'create'}), name='deal-list'),
    path('deals/<int:pk>/', views.DealViewSet.as_view({'delete': 'destroy','patch': 'update_status','put':'update'}), name='deal-detail'),
    path('deal/pipeline/<int:pk>/', views.DealWithPipelineStatus.as_view(), name='deal-detail-with-pipeline'),
    


    
   
]