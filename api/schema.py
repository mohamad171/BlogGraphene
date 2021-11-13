import graphene
from graphene_django import DjangoObjectType
from api.models import *


class PostType(DjangoObjectType):
    class Meta:
        model = Post
        fields = ('id','title','author','description')


class CommentType(DjangoObjectType):
    class Meta:
        model = Comment
        fields = ('id','body','author','post')

class PostMutation(graphene.Mutation):
    class Arguments:
        title = graphene.String(required=True)
        description = graphene.String(required=True)
    post = graphene.Field(PostType)
    @classmethod
    def mutate(self,root,info,title,description):
        p = Post()
        p.title = title
        p.description = description
        p.author = info.context.user
        p.save()
        return self.post

class Mutation(graphene.ObjectType):
    insert_post = PostMutation.Field()

class Query(graphene.ObjectType):
    posts = graphene.List(PostType)
    comments = graphene.List(CommentType)

    def resolve_posts(self,info,**kwargs):
        return Post.objects.filter()

    def resolve_comments(self, info, **kwargs):

        return Comment.objects.all()

schema = graphene.Schema(query=Query,mutation=Mutation)