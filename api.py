import subprocess
import sys
from flask import Flask, jsonify
from flask import request
from tasks import next_tasks
from stock import get_stock
from execute import process_item, execute_task
from settings import ORDER_ACTION, SUPPLY_ACTION

app = Flask("warehouse")


@app.route('/order', methods=['POST'])
def order():
    for order_item in request.json:
        task_id = process_item(ORDER_ACTION, order_item)
    return jsonify(task_id)


@app.route('/supply', methods=['POST'])
def supply():
    for order_item in request.json:
        task_id = process_item(SUPPLY_ACTION, order_item)
    return jsonify(task_id)


@app.route('/tasks/<task_id>/complete', methods=['POST'])
def execute(task_id):
    execute_task(int(task_id))
    return jsonify(200)


@app.route('/next-tasks')
def get_next_tasks():
    return jsonify(next_tasks())


@app.route('/stock')
def stock():
    return jsonify(get_stock())


subprocess.Popen([sys.executable, "robot.py"])
app.run('0.0.0.0', 8001)
