from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import UserActivitySerializer
from user_activity.models import User


@api_view(['GET'])
def user_activities_list_view(request):
    queryset = User.objects.all()
    serializer = UserActivitySerializer(instance=queryset, many=True)
    return Response({"ok": True, "members": serializer.data})
