from rest_framework import views, status, permissions
from rest_framework.response import Response
from .serializers import NewsletterSubscriberSerializer
from .models import NewsletterSubscriber

class SubscribeView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = NewsletterSubscriberSerializer(data=request.data)
        if serializer.is_valid():
            subscriber = serializer.save()
            return Response({
                'message': 'Thank you for subscribing to KKEVO STUDIO MEDIA briefings.',
                'email': subscriber.email
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UnsubscribeView(views.APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request, token):
        try:
            subscriber = NewsletterSubscriber.objects.get(unsubscribe_token=token)
            subscriber.is_active = False
            subscriber.save()
            return Response({'message': 'You have been successfully unsubscribed.'})
        except NewsletterSubscriber.DoesNotExist:
            return Response({'error': 'Invalid unsubscribe token.'}, status=status.HTTP_404_NOT_FOUND)
