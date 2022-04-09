
from . models import Details
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework import generics, permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . Serializers import DetialsSerializer, UserSerializer, RegisterSerializer
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.auth import AuthToken
from django.contrib.auth import login
from knox.views import LoginView as KnoxLoginView
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/drf/details-list/',
		'Detail View':'/drf/details-detail/<str:pk>/',
		'Create':'/drf/details-create/',
		'Update':'/drf/details-update/<str:pk>/',
		'Delete':'/drf/details-delete/<str:pk>/',
		'register':'/drf/register',
        'login':'/drf/login',
        'logout':'/drf/logout',
		'logoutall':'/drf/logoutall',
		}

	return Response(api_urls)

@api_view(['POST'])
def login_api(request):
    serializer = AuthTokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = serializer.validated_data['user']
    _, created, token = AuthToken.objects.create(user)

    return Response({
        'user_info': {
            'id': user.id,
            'username': user.username,
            'email': user.email

            },
        'token': token
    })
     

@api_view(['GET'])
def DetailsList(request):
	details = Details.objects.all().order_by('-id')
	serializer = DetialsSerializer(details, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def DetailsDetail(request, pk):
	details = Details.objects.get(id=pk)
	serializer = DetialsSerializer(details, many=False)
	return Response(serializer.data)

@api_view(['POST'])
def DetailsCreate(request):
	serializer = DetialsSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def DetailsUpdate(request, pk):
	detail = Details.objects.get(id=pk)
	serializer = DetialsSerializer(instance=detail, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def DetailsDelete(request, pk):
	detail = Details.objects.get(id=pk)
	detail.delete()

	return Response('Item succsesfully delete!')


# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })


# Login
class LoginAPI(KnoxLoginView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)