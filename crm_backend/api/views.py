from rest_framework.permissions import AllowAny,IsAuthenticated
from .serializers import UserTokenObtainPairSerializer, RegisterSerializer , LeadSerializer , DealSerializer
from django.contrib.auth.models import User
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework_simplejwt.views import TokenObtainPairView
from . models import Lead,Deal,Pipeline
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters
from rest_framework.decorators import action   
from rest_framework import generics


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = [AllowAny]
    serializer_class = UserTokenObtainPairSerializer  

class RegisterView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer 

   
class LeadViewSet(viewsets.ModelViewSet):   
    serializer_class = LeadSerializer
    permission_classes = [IsAuthenticated]
    queryset = Lead.objects.all() 

    def list(self, request):
        user_id = request.query_params.get('user_id') 
        leads = Lead.objects.filter(owner=user_id)
        serializer = LeadSerializer(leads, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['owner'] = request.user  
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=204)
    
class DealViewSet(viewsets.ModelViewSet):
    serializer_class = DealSerializer
    permission_classes =[IsAuthenticated]
    queryset = Deal.objects.all()

    def list(self,request):
        user_id = request.query_params.get('user_id')
        deals = Deal.objects.filter(owner=user_id)
        serializer = LeadSerializer(deals, many=True)
        return Response(serializer.data)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data['owner'] = request.user  
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=201, headers=headers)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=True, methods=['patch'])
    def update_status(self, request, pk=None):
        deal = self.get_object()
        won = request.data.get('won')
        lost = request.data.get('lost')

        if won is not None:
            deal.won = won
        if lost is not None:
            deal.lost = lost

        deal.save()

        serializer = self.get_serializer(deal)
        return Response(serializer.data, status=status.HTTP_200_OK)
    


class DealWithPipelineStatus(generics.RetrieveUpdateAPIView):
    serializer_class = DealSerializer 
    permission_classes = [IsAuthenticated] 
    queryset = Deal.objects.all()  

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        all_pipeline_stages = Pipeline.objects.all()
        selected_stages = instance.pipeline_status.all()
        selected_stages_titles = [stage.title for stage in selected_stages]

        pipeline_status = [
            {
                'title': stage.title,
                'selected': stage.title in selected_stages_titles  
            }
            for stage in all_pipeline_stages
        ]

        return Response({
            "deal": serializer.data,
            "pipeline_status": pipeline_status
        })
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        selected_stage_title = request.data.get('stage_title')  
        if selected_stage_title:
            pipeline_stage = Pipeline.objects.get(title=selected_stage_title)

            if pipeline_stage in instance.pipeline_status.all():
                instance.pipeline_status.remove(pipeline_stage)
            else:
                instance.pipeline_status.add(pipeline_stage)

            instance.save()
            serializer = self.get_serializer(instance)
            return Response(serializer.data)
        return Response(status=400)