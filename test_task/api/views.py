from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import User, Event
from .serializer import UserSerializer, EventSerializer
from .permissions import IsOwnerIsAdminOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]


class EventViewSet(viewsets.ModelViewSet):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerIsAdminOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(organizer=self.request.user)

    @action(detail=True, methods=["post"], permission_classes=[permissions.IsAuthenticated])
    def join(self, request, pk=None):
        event = self.get_object()
        user = request.user

        if user in event.participants.all():
            event.participants.remove(user)
            return Response({"message": "You left the event"}, status=status.HTTP_200_OK)
        else:
            event.participants.add(user)
            return Response({"message": "You joined the event"}, status=status.HTTP_200_OK)