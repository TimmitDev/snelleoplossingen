from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

# Defineer App met de standaard naam __name__
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    oplossing = db.Column(db.String)

# Main Page (route)
@app.route('/')
def index():
    # Laat alle oplossingen zien
    todo_list = Todo.query.all()
    return render_template('main.html', todo_list=todo_list)

@app.route('/add', methods=["POST"])
def add():
    # Nieuwe oplossing toevoegen
    title = request.form.get("title")
    oplossing = request.form.get("oplossing")
    new_todo= Todo(title=title, oplossing=oplossing)
    db.session.add(new_todo)
    db.session.commit()
    return redirect(url_for("index"))

@app.route("/verwijder/<int:todo_id>")
def delete(todo_id):
    # Verwijder een oplossing
    todo = Todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))

# Door deze command kan de server starten en start de database
if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)