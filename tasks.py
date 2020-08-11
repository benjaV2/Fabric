
tasks = {}
cur_id = 0


def create_task(action, product, location):
    return {"action": action, "product": product, "location": location, "complete": False}


def insert_task(task):
    global cur_id
    tasks[cur_id] = task
    cur_id += 1
    return cur_id-1


def get_task(task_id):
    return tasks[task_id]


def complete_task(task_id):
    tasks[task_id]['complete'] = True


def next_tasks():
    pending_tasks = [{'id': k, **v} for k, v in tasks.items() if v["complete"] is False]
    for task in pending_tasks:
        task.pop('complete')
    return pending_tasks


if __name__ == "__main__":
    task1 = create_task("put", "bread", "[5,6]")
    insert_task(task1)
    task2 = create_task("put", "milk", "[4,2]")
    insert_task(task2)
    task3 = create_task("sup", "bread", "[5,6]")
    insert_task(task3)
    print(next_tasks())
