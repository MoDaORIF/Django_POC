from django.contrib.auth.models import User

from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from .serializers import UserSerializer
from .serializers import UserSerializer


@api_view(["GET"])
def api_users_list(request, format=None):
    return Response(
        {
            "users": reverse("user-list", request=request, format=format),
        }
    )


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
