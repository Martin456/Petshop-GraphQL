import graphene
from flask import Flask
from flask_graphql import GraphQLView
from petshop_schema import Query, Mutations


app = Flask(__name__)

schema = graphene.Schema(query=Query, mutation=Mutations)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql',
                 schema=schema, graphiql=True))

if __name__ == "__main__":
    app.run()