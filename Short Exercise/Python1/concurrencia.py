import threading
import time
import random

def cashier(name, atm):
    print(f"{name} is in a transaction at {atm}")
    duration = random.randint(1, 5)
    time.sleep(duration)
    print(f"{name} finished.")

data = [
    ("Maria", "New York ATM"),
    ("Juan", "Brazil ATM"),
    ("Lexa", "Zurich ATM")
]

threads = []

for person in data:
    thread = threading.Thread(target=cashier, args=person)
    threads.append(thread)
    thread.start()

for t in threads:
    t.join()

