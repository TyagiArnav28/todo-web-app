from flask import Flask, render_template, request, jsonify, redirect, url_for
import json
import os
from datetime import datetime

app = Flask(__name__)

# File to store todos
TODOS_FILE = 'todos.json'

def load_todos():
    """Load todos from JSON file"""
    if os.path.exists(TODOS_FILE):
        try:
            with open(TODOS_FILE, 'r') as file:
                return json.load(file)
        except json.JSONDecodeError:
            return []
    return []

def save_todos(todos):
    """Save todos to JSON file"""
    with open(TODOS_FILE, 'w') as file:
        json.dump(todos, file, indent=4)

@app.route('/')
def index():
    """Main page - display all todos"""
    todos = load_todos()
    return render_template('index.html', todos=todos)

@app.route('/add', methods=['POST'])
def add_todo():
    """Add a new todo"""
    task = request.form.get('task', '').strip()
    
    if task:
        todos = load_todos()
        new_todo = {
            'id': len(todos) + 1 if todos else 1,
            'task': task,
            'completed': False,
            'created_at': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        todos.append(new_todo)
        save_todos(todos)
    
    return redirect(url_for('index'))

@app.route('/complete/<int:todo_id>', methods=['POST'])
def complete_todo(todo_id):
    """Toggle todo completion status"""
    todos = load_todos()
    
    for todo in todos:
        if todo['id'] == todo_id:
            todo['completed'] = not todo['completed']
            break
    
    save_todos(todos)
    return redirect(url_for('index'))

@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    """Delete a todo"""
    todos = load_todos()
    todos = [todo for todo in todos if todo['id'] != todo_id]
    
    # Reassign IDs to keep them sequential
    for i, todo in enumerate(todos):
        todo['id'] = i + 1
    
    save_todos(todos)
    return redirect(url_for('index'))

@app.route('/clear-completed', methods=['POST'])
def clear_completed():
    """Remove all completed todos"""
    todos = load_todos()
    todos = [todo for todo in todos if not todo['completed']]
    
    # Reassign IDs
    for i, todo in enumerate(todos):
        todo['id'] = i + 1
    
    save_todos(todos)
    return redirect(url_for('index'))

@app.route('/api/todos', methods=['GET'])
def get_todos_api():
    """API endpoint to get all todos (for future mobile app integration)"""
    todos = load_todos()
    return jsonify(todos)

if __name__ == '__main__':
    app.run(debug=True, port=5000)