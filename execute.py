from stock import get_location, add_stock, reduce_stock
from tasks import create_task, insert_task, get_task, complete_task
from settings import SUPPLY_ACTION, ORDER_ACTION


actions = {SUPPLY_ACTION: add_stock, ORDER_ACTION: reduce_stock}


def process_item(action, order_item):
    location = get_location(order_item)
    task = create_task(action, order_item, location)
    return insert_task(task)


def execute_task(task_id):
    """
    execute task impacts the stock amounts and tasks queue
    """
    task = get_task(task_id)
    actions[task['action']](task['product'])
    complete_task(task_id)
