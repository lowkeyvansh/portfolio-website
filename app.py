from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    projects = [
        {'name': 'Project 1', 'description': 'Description 1', 'link': '#'},
        {'name': 'Project 2', 'description': 'Description 2', 'link': '#'},
    ]
    return render_template('projects.html', projects=projects)

if __name__ == '__main__':
    app.run(debug=True)
