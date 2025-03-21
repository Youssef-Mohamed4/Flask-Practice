from flask import render_template, redirect, url_for
from ToDo.forms import AddTaskForm
from ToDo import app, db
from ToDo.models import Task

@app.route('/')
@app.route('/Tasks')
def tasks():
    tasks=Task.query.all()
    return render_template('tasks.html',title='Tasks',tasks=tasks)

@app.route("/Add-Task",methods=['GET','POST'])
def add_task():
    form=AddTaskForm()
    if form.validate_on_submit():
        task=Task(title=form.task.data,completed=form.completed.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('add_task.html',title='Add Task',form=form)