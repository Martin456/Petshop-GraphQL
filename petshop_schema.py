import graphene


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))

    def resolve_hello(self, info, name):
        return 'Hello ' + name


class Category(graphene.ObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=True)


class Tag(graphene.ObjectType):
    id = graphene.Int(required=True)
    name = graphene.String(required=True)


class Pet(graphene.ObjectType):
    id = graphene.Int(required=True)
    category = Category()
    name = graphene.String(required=True)
    photoUrls = graphene.List(graphene.String)
    tags = graphene.List(Tag)
    status = graphene.Enum('Status', ['available', 'pending', 'sold'])


