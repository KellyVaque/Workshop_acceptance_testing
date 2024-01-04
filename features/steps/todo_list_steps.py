# steps/to_do_steps.py
from behave import given, when, then

to_do_list = []

@given('the to-do list is empty')
def step_given_to_do_list_empty(context):
    global to_do_list
    to_do_list = []

@given('the to-do list contains tasks')
def step_given_to_do_list_with_tasks(context):
    # Implementación para inicializar la lista con tareas
    pass

@then('the output should contain')
def step_then_output_should_contain(context):
    # Implementación para verificar que la salida contiene cierto texto
    pass

@then('the to-do list should be empty')
def step_then_to_do_list_should_be_empty(context):
    # Implementación para verificar que la lista de tareas está vacía
    pass

@when('the user adds a task "{task}"')
def step_when_user_adds_task(context, task):
    global to_do_list
    to_do_list.append({"name": task, "description": "", "status": "Incomplete"})

@then('the to-do list should contain "{task}"')
def step_then_to_do_list_should_contain(context, task):
    global to_do_list
    assert any(t["name"] == task for t in to_do_list), f'Task "{task}" not found in the to-do list'

@given('the to-do list contains tasks:')
def step_given_to_do_list_with_tasks(context):
    global to_do_list
    to_do_list = []
    for row in context.table:
        to_do_list.append({"name": row["Task"], "description": row["Description"], "status": row["Status"]})

@when('the user lists all tasks')
def step_when_user_lists_all_tasks(context):
    global to_do_list
    context.output = "\n".join([f"- {task['name']} - {task['description']} - {task['status']}" for task in to_do_list])

@then('the output should contain:')
def step_then_output_should_contain(context):
    assert context.text.strip() == context.output.strip(), f'Expected output:\n{context.text}\nActual output:\n{context.output}'

@when('the user marks task "{task}" as completed')
def step_when_user_marks_task_as_completed(context, task):
    global to_do_list
    for t in to_do_list:
        if t["name"] == task:
            t["status"] = "Complete"
            break

@then('the to-do list should show task "{task}" as completed')
def step_then_to_do_list_should_show_task_as_completed(context, task):
    global to_do_list
    assert any(t["name"] == task and t["status"] == "Complete" for t in to_do_list), f'Task "{task}" not marked as complete'

@when('the user clears the to-do list')
def step_when_user_clears_to_do_list(context):
    global to_do_list
    to_do_list = []

@when('the user edits task "{task}" with name "{new_name}" and description "{new_description}"')
def step_when_user_edits_task(context, task, new_name, new_description):
    global to_do_list
    task_found = False
    for t in to_do_list:
        if t["name"] == task:
            t["name"] = new_name
            t["description"] = new_description
            task_found = True
            break

    assert task_found, f'Task "{task}" not found in the to-do list or not pending'

@then('the to-do list should show task "{task}" with description "{description}" as pending')
def step_then_to_do_list_should_show_task_as_pending(context, task, description):
    global to_do_list
    matching_tasks = [t for t in to_do_list if t["name"] == task and t["description"] == description and t["status"] == "Pending"]
    assert len(matching_tasks) > 0, f'Task "{task}" not found in the to-do list or not pending'


@when('the user lists incomplete tasks')
def step_when_user_lists_incomplete_tasks(context):
    global to_do_list
    incomplete_tasks = [f"- {task['name']} - {task['description']}" for task in to_do_list if task['status'] == 'Incomplete']
    context.output = "\n".join(["Incomplete Tasks:"] + incomplete_tasks)

@then('the incomplete tasks output should contain:')
def step_then_output_should_contain_incomplete(context):
    assert context.text.strip() == context.output.strip(), f'Expected output:\n{context.text}\nActual output:\n{context.output}'
