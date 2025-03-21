from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

@api_view(['POST'])
def register(request):
    username = request.data.get('username')
    password = request.data.get('password')

    if not username or not password:
        return Response({"error": "Campos obrigatórios!"}, status=400)

    if User.objects.filter(username=username).exists():
        return Response({"error": "Usuário já existe!"}, status=400)

    user = User.objects.create_user(username=username, password=password)
    return Response({"message": "Usuário registrado com sucesso!"}, status=201)

@api_view(['POST'])
def login(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = User.objects.filter(username=username).first()
    if user and user.check_password(password):
        refresh = RefreshToken.for_user(user)
        return Response({"refresh": str(refresh), "access": str(refresh.access_token)})

    return Response({"error": "Credenciais inválidas!"}, status=400)
