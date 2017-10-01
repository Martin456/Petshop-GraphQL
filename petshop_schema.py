import graphene
import graphene.types.datetime
import graphene.types.uuid
import uuid

# Test implementation
PETS = []
USERS = []
ORDERS = []


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


class Order(graphene.ObjectType):
    id = graphene.Int()
    petId = graphene.Int()
    quantity = graphene.Int()
    shipDate = graphene.types.datetime.DateTime()
    status = graphene.Enum('Status', ['placed', 'approved', 'delivered'])
    complete = graphene.Boolean(default_value=False)


class User(graphene.ObjectType):
    id = graphene.types.uuid.UUID()
    username = graphene.String()
    firstName = graphene.String()
    lastName = graphene.String()
    email = graphene.String()
    password = graphene.String()
    phone = graphene.String()
    userStatus = graphene.Int()

    def __init__(self, username, firstName, lastName, email, password, phone):
        self.id = uuid.uuid4()
        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.password = password
        self.phone = phone


class Query(graphene.ObjectType):
    users = graphene.List(User)
    pets = graphene.List(Pet)
    store = graphene.List(Order)

    def resolve_users(self, info):
        return USERS

    def resolve_pets(self, info):
        return PETS

    def resolve_store(self, info):
        return ORDERS


class CreateUser(graphene.Mutation):
    class Arguments:
        username = graphene.String()
        firstName = graphene.String(default_value="")
        lastName = graphene.String(default_value="")
        email = graphene.String(default_value="")
        password = graphene.String()
        phone = graphene.String(default_value="")

    ok = graphene.Boolean()
    user = graphene.Field(lambda: User)

    def mutate(self, info, username, firstName, lastName, email, 
               password, phone):
        user = User(username=username, firstName=firstName, lastName=lastName,
                    email=email, password=password, phone=phone)
        USERS.append(user)
        return CreateUser(user=user, ok=True)


class DeleteUser(graphene.Mutation):
    class Arguments:
        id = graphene.types.uuid.UUID()

    ok = graphene.Boolean()

    def mutate(self, info, id):
        matches = (item for item in USERS if item.id == id)
        for item in matches:
            USERS.remove(item)
        return DeleteUser(ok=True)
'''
class CreatePet(graphene.Mutation):
    def mutate(self, info):
        pass


class CreateOrder(graphene.Mutation):
    def mutate(self, info):
        pass
'''
    
class Mutations(graphene.ObjectType):
    create_user = CreateUser.Field()
    delete_user = DeleteUser.Field()
    # create_pet = CreatePet.Field()
    # create_order = CreateOrder.Field()
