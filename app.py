from ariadne import graphql_sync, make_executable_schema, load_schema_from_path, ObjectType, QueryType
from ariadne.constants import PLAYGROUND_HTML
from flask import Flask, request, jsonify
import resolvers as r
from ariadne import MutationType

app = Flask(__name__)

type_defs = load_schema_from_path('schema.graphql')

query = QueryType()
student = ObjectType('Student')

queryClass = QueryType()
classs = ObjectType('Classs')


mutation = MutationType()
mutation.set_field('create_Student', r.resolver_createStudent)

mutationClass = MutationType()
mutationClass.set_field('create_Class', r.resolver_createClass)

mutationAddStudentToClass =MutationType()
mutationAddStudentToClass.set_field('add_Student_to_Class',r.resolver_add_student_to_class)


query.set_field('student_with_id', r.student_with_id)
queryClass.set_field('class_with_id', r.class_with_id)


schema = make_executable_schema(type_defs, [student, mutation, query,classs,mutationClass,queryClass,mutationAddStudentToClass])

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