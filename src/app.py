from flask import Flask, jsonify, request, json
app = Flask(__name__)

todos = [
    { "label": "My first task", "done": False },
    { "label": "My second task", "done": False }
]

@app.route('/todos', methods=['GET'])
def hello_world():
    # suppose you have some information in a json variable

    # you can convert that variable into a json string like this
    json_text = jsonify(todos)

    # and then you can return it on the response body like this
    return json_text

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.data
    decoded_object = json.loads(request_body)
    todos.append(decoded_object)
    update = jsonify(todos)
    print(request_body, decoded_object)
    return(update)

@app.route('/todos/<int:position>', methods=['DELETE'])
def delete_todo(position):
    del todos[position]
    print("This is the position to delete: ",position)
    borrar = jsonify(todos)
    return(borrar)

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)
