from flask import Flask, request, jsonify
from utils import generate_sql_query, execute_sql_query

app = Flask(__name__)

@app.route('/query', methods=['POST'])
def handle_command():
    data = request.json
    command = data['command']
    query = generate_sql_query(command)
    result = execute_sql_query(query)
    return jsonify({'data': result})

if __name__ == '__main__':
    app.run(debug=True, port=5000)