from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, SubmitField
from wtforms.validators import DataRequired

class AddTaskForm(FlaskForm):
    title= StringField("Task",validators=[DataRequired()])
    completed= BooleanField("Completed")
    submit_btn=SubmitField("Add Task")

class UpdateTaskForm(AddTaskForm):
    submit = SubmitField("Edit")