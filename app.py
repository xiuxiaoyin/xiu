from flask import Flask, request, jsonify

app = Flask(__name__)       #创建一个 Flask 应用实例
app.json.ensure_ascii = False       #显示中文

todos = []      #所有待办
next_id = 1     #下一个可用id


def find_todo(todo_id):
    for todo in todos:      #遍历列表
        if todo["id"] == todo_id:       #如果元素（这里是字典）中“id”值与参数todo_id一致
            return todo
    return None         #todos列表中全没匹配上

#GET/todos
@app.route("/todos", methods=["GET"])
def get_todos():
    return jsonify(todos)       #jsonify()将数据转为json响应（转格式），还会设置响应头 Content-Type: application/json；默认会把非 ASCII 字符（中文）转义

#POST/todos
@app.route("/todos", methods=["POST"])
def create_todo():

    #校验
    request_body = request.get_json()       #得到请求体(json格式)
    if "title" not in request_body:
         return jsonify({"message": "title字段不在字典里"}), 400
    if request_body["title"] is None:
         return jsonify({"message": "title为null"}), 400
    if not isinstance(request_body["title"],str):
        return jsonify({"message": "title不是字符串"}), 400
    if len(request_body["title"].strip()) == 0:
        return jsonify({"message": "title为空串"}), 400
    if len(request_body["title"].strip()) > 100:
        return jsonify({"message": "title超出长度限制"}), 400
        
    #业务逻辑
    global next_id      #要加global，否则会认为是新建的变量（作用域）
    todo_id = next_id
    next_id = next_id + 1
    todo =  {"id":todo_id, "title":request_body["title"], "completed": False}
    todos.append(todo)      #添加创建的待办
    return jsonify(todo),201

#GET/todos/<id>
@app.route("/todos/<int:todo_id>", methods=["GET"])
def get_todo(todo_id):
    todo = find_todo(todo_id)       #找
    if todo is None:
        return jsonify({"message": "todo not found"}), 404      #id不存在
    return jsonify(todo)
   

#PUT/todos/<id>
@app.route("/todos/<int:todo_id>", methods=["PUT"])
def update_todo(todo_id):

    #校验
    request_body = request.get_json()       #得到请求体(json格式)
    if "title" not in request_body:
         return jsonify({"message": "title不在字典里"}), 400
    if request_body["title"] is None:
         return jsonify({"message": "title为null"}), 400
    if not isinstance(request_body["title"],str):
        return jsonify({"message": "title不是字符串"}), 400
    if len(request_body["title"].strip()) == 0:
        return jsonify({"message": "title为空串"}), 400
    if len(request_body["title"].strip()) > 100:
        return jsonify({"message": "title超出长度限制"}), 400
    if not isinstance(request_body.get("completed"), bool):
        return jsonify({"message": "completed 必须是布尔值"}), 400

    #业务逻辑
    todo = find_todo(todo_id)       #找
    if todo is None:
        return jsonify({"message": "todo not found"}), 404      #id不存在
    todo["title"] = request_body["title"]
    todo["completed"] = request_body["completed"]
    return jsonify(todo),200

#DELETE/todos/<id>
@app.route("/todos/<int:todo_id>", methods=["DELETE"])
def delete_todo(todo_id):
    todo = find_todo(todo_id)       #找
    if todo is None:
        return jsonify({"message": "todo not found"}), 404      #id不存在
    todos.remove(todo)
    return "",204
    

if __name__ == "__main__":       # 如果是直接运行这个文件，就启动服务；如果被 import，则不启动
    app.run(debug=True)