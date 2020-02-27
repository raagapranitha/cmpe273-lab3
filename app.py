from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolvers as r
from ariadne import MutationType

app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
student = ObjectType('Student')

quer2 = QueryType()
classs=ObjectType('Class')

mutation1 = MutationType()
mutation.set_field('create_Student', r.resolver_createStudent)

mutation2 = MutationType()
mutation.set_field('create_Class', r.resolver_createClass)

query.set_field('student_with_id', r.student_with_id)
query2.set_field('class_with_id', r.class_with_id)


schema = make_executable_schema(type_defs, [student, mutation, query,classs,mutation2,query2])

@app.route('/graphql', methods=['GET'])
def playground():
    return PLAYGROUND_HTML, 200
    
@app.route('/graphql', methods=['POST'])
def graphql_server():
    data = request.get_json()
    success, result = graphql_sync(
    schema,
    data,
    context_value=None,
    debug=app.debug
    )
    status_code = 200 if success else 400
    return jsonify(result), status_code

if __name__=="__main__":
    app.run(Debug=True,port=8080)