import requests
import time
from settings import WAREHOUSE_URL


while True:
    tasks = requests.get(WAREHOUSE_URL + "/next-tasks")
    for task in tasks.json():
        requests.post(WAREHOUSE_URL + f"/tasks/{str(task['id'])}/complete")
    time.sleep(0.5)
