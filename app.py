import graphene
from flask import Flask
from flask_graphql import GraphQLView
from petshop_schema import Query

app = Flask(__name__)

schema = graphene.Schema(query=Query)

app.add_url_rule('/graphql', view_func=GraphQLView.as_view('graphql', schema=schema, graphiql=True))

# Optional, for adding batch query support (used in Apollo-Client)
# app.add_url_rule('/graphql/batch', view_func=GraphQLView.as_view('graphql', schema=schema, batch=True))


@app.route('/')
def hello_world():
    return 'Hello, World!'