from flask import Flask, request, redirect

app = Flask(__name__)

tasks = []

@app.route('/')
def index():
    return '''
        <h2>Todo App</h2>
        <form method="POST" action="/add">
            <input name="task" placeholder="Enter task">
            <button>Add</button>
        </form>
        <ul>
            ''' + ''.join(f"<li>{t} <a href='/delete/{i}'>Delete</a></li>" for i, t in enumerate(tasks)) + '''
        </ul>
    '''

@app.route('/add', methods=['POST'])
def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:index>')
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
