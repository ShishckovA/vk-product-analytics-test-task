import sys
import logging

import concurrent.futures
from concurrent.futures import ThreadPoolExecutor

from task import Task
from counter import Counter

logging.basicConfig(level=logging.INFO, stream=sys.stdout)

new_counter = Counter()
values = [2] * 10
tasks = []

for id_, value in enumerate(values):
    tasks.append(Task(value, id_))
with ThreadPoolExecutor(max_workers=2) as executor:
    future_to_task = {}

    for task in tasks:
        logging.info(f"Submitting task {task.id}")
        future_to_task[executor.submit(task.execute)] = task
        logging.info(f"Task {task.id} submitted")

    for future in concurrent.futures.as_completed(future_to_task):
        task_executed = future_to_task[future]
        logging.info(f"Updating counter with result from task {task_executed.id}")
        new_counter.update(future.result())
        logging.info(f"Updated with {task_executed.id}th task result")

print(new_counter.value)
