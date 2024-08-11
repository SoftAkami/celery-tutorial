from task_queue.app import app
import time
from datetime import datetime

@app.task(bind=True, track_started=True)
def counter(self, t: int):
    print(f"Running my counter")
    print(self.request)
    self.update_state(meta={"test": 1})
    for i in range(t):
        print(i)
        time.sleep(10)
    return datetime.now()