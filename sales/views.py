# from rest_framework import status
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework_simplejwt.tokens import RefreshToken
# from .serializers import RegisterSerializer, LoginSerializer
# from rest_framework.permissions import AllowAny


# class RegisterView(APIView):
#     permission_classes = [AllowAny]

#     def get(self, request):
#         return Response({"detail": "Use POST to register a new user."})

#     def post(self, request):
#         serializer = RegisterSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.save()
#             return Response({
#                 "id": user.id,
#                 "username": user.username,
#                 "email": user.email,
#                 "message": "Registration successful"
#             }, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class LoginView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = LoginSerializer(data=request.data)
#         if serializer.is_valid():
#             user = serializer.validated_data["user"]
#             refresh = RefreshToken.for_user(user)
#             return Response({
#                 "refresh": str(refresh),
#                 "access": str(refresh.access_token),
#                 "user": {
#                     "id": user.id,
#                     "username": user.username,
#                     "email": user.email
#                 },
#                 "message": "Login successful"
#             }, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
