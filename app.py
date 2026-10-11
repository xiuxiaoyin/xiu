from flask import Flask, request, jsonify

app = Flask(__name__)
todos = []      #所有待办
next_id = 1     #下一个可用id

@app.route("/todos",methods=["GET"])
def get_todos():
    return jsonify(todos)

app.run(debug=True)