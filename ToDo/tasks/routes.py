from flask import Blueprint, redirect, url_for, render_template,flash,abort,request
from flask_login import login_required,current_user
from ToDo import db
from ToDo.tasks.forms import AddTaskForm,UpdateTaskForm
from ToDo.models import Task

task = Blueprint("task", __name__)

@task.route('/tasks')
@login_required
def tasks():
    tasks = current_user.tasks
    return render_template('tasks.html',title='Tasks',tasks=tasks)

@task.route("/tasks/add",methods=['GET','POST'])
@login_required
def add_task():
    form=AddTaskForm()
    if form.validate_on_submit():
        task=Task(title=form.title.data,completed=form.completed.data, user_id=current_user.id )
        db.session.add(task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('task.tasks'))
    return render_template('add_task.html',title='Add Task',form=form)

@task.route("/tasks/<int:taskId>/update", methods=["GET", "POST"])
@login_required
def update_task(taskId):
    form = UpdateTaskForm()
    task = Task.query.get_or_404(taskId)
    if task.author != current_user:
        abort(403)

    if request.method == "GET":
        form.title.data = task.title
        form.completed.data = task.completed

    if form.validate_on_submit():
        task.title = form.title.data
        task.completed = form.completed.data
        db.session.commit()
        flash(f"Task updated successfully", "success")
        return redirect(url_for("task.tasks"))

    return render_template(
        "update_task.html", title="Update Task", task=task, form=form
    )


@task.route("/tasks/<int:taskId>/delete", methods=["GET"])
def delete_task(taskId):
    task = Task.query.get_or_404(taskId)
    if task.author != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()
    flash(f"task {task.title} deleted successfully ", "success")
    return redirect(url_for("task.tasks"))