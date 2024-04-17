import threading
import time
from queue import PriorityQueue
import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class Producer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        logger.debug("start producer")
        tasks = [
            (1, "Task(priority=0)."),
            (2, "Task(priority=2)."),
            (0, "Task(priority=1)."),
            (6, "Task(priority=4)."),
            (3, "Task(priority=3)."),
            (4, "Task(priority=6)."),
        ]

        for task in tasks:
            self.queue.put(task)
            time.sleep(0.5)

        logger.debug("end producer")


class Consumer(threading.Thread):
    def __init__(self, queue):
        super().__init__()
        self.queue = queue

    def run(self):
        print("Consumer start")
        while True:
            priority, task = self.queue.get()
            if task is None:
                self.queue.task_done()
                break
            logger.debug(f">{task}\t\tsleep({priority * 0.1})")
            time.sleep(priority * 0.1)
            self.queue.task_done()

        print("Consumer end")

def main():
    queue = PriorityQueue()
    producer = Producer(queue)
    consumer = Consumer(queue)

    producer.start()
    consumer.start()

    producer.join()
    queue.put((None, None))
    queue.join()
    consumer.join()


if __name__ == "__main__":
    main()