from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status , viewsets, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from .serializers import UserSerializer, CoordinateSerializers, CoordinateInfoSerializers
from .models import Coordinates
from .permissions import IsSuper, IsOwner
from customUser.models import MyUser



class CoordinateViewSet(viewsets.ModelViewSet) :
    queryset = Coordinates.objects.all()
    serializer_class = CoordinateSerializers
    http_method_names = ['post']

    def create(self, request, *args, **kwargs) :
        obj = super().create(request, *args, **kwargs)
        return obj



@api_view(['GET'])
@permission_classes((IsSuper, IsAuthenticated))
def get_all_coordinates(request) :
    all_ = Coordinates.objects.all()
    ser = CoordinateSerializers(all_, many=True)

    return Response(ser.data, status=status.HTTP_200_OK)

@api_view(['GET'])
@permission_classes((IsSuper, IsAuthenticated))
def get_final_coordinates(request) :
    userNames = MyUser.objects.values_list('user_name', flat=True)
    all_coords = []
    for userName in userNames :
        try :
            coord = Coordinates.objects.filter(person__user_name = userName).latest('created_at')
            all_coords.append(coord)
        except :
            pass
    all_coords = list(dict.fromkeys(all_coords))
    ser = CoordinateInfoSerializers(all_coords, many=True)

    return Response(ser.data, status=status.HTTP_200_OK)



## Creating a new MyUser (Custom User)
@api_view(['POST'])
@permission_classes((AllowAny, ))
def create_user(request) :
    ser = UserSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data, status=status.HTTP_201_CREATED)
    else :
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)

## Taking new token for an active MyUser (Custom User)
class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk
        })