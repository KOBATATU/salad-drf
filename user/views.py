from rest_framework.viewsets import mixins, GenericViewSet
from rest_framework.exceptions import NotFound
from rest_framework.permissions import IsAuthenticated

from user.permissions import IsOwner
from user.models import User
from user.serializers import UserMeSerializer, UserSerializer
# Create your views here.

"""
user/meのエンドポイントに対してアクションを行う
- password変更は別エンドポイント

"""
class UserMeViews(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    GenericViewSet):
    serializer_class = UserMeSerializer
    permission_classes = [IsAuthenticated, IsOwner]
    def get_object(self):
        # リクエストしたユーザーのインスタンスを取得します。
        # self.request.userは、認証されたユーザーのインスタンスです。
        user = self.request.user
        if user.is_authenticated:
            return user
        else:
            raise NotFound('ユーザーが見つかりません。')

class UserView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    GenericViewSet
):
    serializer_class = UserSerializer
    queryset = User.objects.all()