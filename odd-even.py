import threading
import time
def even_numbers():
    for i in range(0, 10, 2):
        print(f"Even: {i}")
        time.sleep(2)
def odd_numbers():
    for i in range(1, 10, 2):
        print(f"Odd: {i}")
        time.sleep(3)
even = threading.Thread(target=even_numbers)
odd = threading.Thread(target=odd_numbers)
even.start()
odd.start()