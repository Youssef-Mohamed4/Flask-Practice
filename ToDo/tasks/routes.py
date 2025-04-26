from flask import Blueprint, redirect, url_for, render_template
from flask_login import login_required,current_user
from ToDo import db
from ToDo.tasks.forms import AddTaskForm
from ToDo.models import Task

task = Blueprint("task", __name__)

@task.route('/Tasks')
@login_required
def tasks():
    tasks=current_user.tasks
    return render_template('tasks.html',title='Tasks',tasks=tasks)

@task.route("/Tasks/Add",methods=['GET','POST'])
@login_required
def add_task():
    form=AddTaskForm()
    if form.validate_on_submit():
        task=Task(title=form.task.data,completed=form.completed.data)
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('tasks'))
    return render_template('add_task.html',title='Add Task',form=form)