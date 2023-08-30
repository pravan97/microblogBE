from django.contrib.auth import authenticate
from django.contrib.sites import requests
from django.http import JsonResponse
from django.shortcuts import render
from djoser.serializers import UserSerializer
from djoser.views import TokenCreateView, User
# Create your views here.
from rest_framework import generics, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Post, Comment, Like
from .serializers import PostSerializer, CommentSerializer, LikeSerializer
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ModelViewSet
from django_filters.rest_framework import DjangoFilterBackend


class CurrentUserView(generics.RetrieveAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        return self.request.user


def all_users(request):
    users = User.objects.all().values('id', 'username', 'email')
    return JsonResponse(list(users), safe=False)


class PostListCreateView(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class CommentListCreateView(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

    def get_queryset(self):
        queryset = Comment.objects.all()
        post_id = self.request.query_params.get('post_id')

        if post_id:
            queryset = queryset.filter(post=post_id)

        return queryset

class LikeListCreateView(ModelViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    def get_queryset(self):
        queryset = Like.objects.all()
        post_id = self.request.query_params.get('post_id')

        if post_id:
            queryset = queryset.filter(post=post_id)

        return queryset

    @action(detail=False, methods=['DELETE'])
    def delete_by_post(self, request):
        post_id = self.request.query_params.get('post_id')

        if not post_id:
            return Response({'error': 'post_id parameter is required.'}, status=status.HTTP_400_BAD_REQUEST)

        likes_to_delete = Like.objects.filter(post=post_id)
        likes_to_delete.delete()

        return Response({'message': f'Likes for post {post_id} have been deleted.'}, status=status.HTTP_204_NO_CONTENT)
