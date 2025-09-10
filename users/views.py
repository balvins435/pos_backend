from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from .serializers import RegisterSerializer, LoginSerializer
from .permissions import IsAdmin, IsCashier
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    """Generate JWT tokens with custom claims (role included)."""
    refresh = RefreshToken.for_user(user)
    refresh["role"] = user.role   # 👈 Add role claim
    return {
        "refresh": str(refresh),
        "access": str(refresh.access_token),
    }


class RegisterView(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"detail": "Use POST to register a new user."})

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            tokens = get_tokens_for_user(user)
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,   # 👈 Include role
                "refresh": tokens["refresh"],
                "access": tokens["access"],
                "message": "Registration successful"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data["user"]
            tokens = get_tokens_for_user(user)
            return Response({
                "id": user.id,
                "username": user.username,
                "email": user.email,
                "role": user.role,   # 👈 Include role
                "refresh": tokens["refresh"],
                "access": tokens["access"],
                "message": "Login successful"
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AdminOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsAdmin]

    def get(self, request):
        return Response({"message": "Hello Admin"})


class CashierOnlyView(APIView):
    permission_classes = [IsAuthenticated, IsCashier]

    def get(self, request):
        return Response({"message": "Hello Cashier"})