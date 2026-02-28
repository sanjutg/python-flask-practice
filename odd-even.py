# import threading
# import time
# event_even = threading.Event()
# event_odd = threading.Event()
# def even_numbers():
#     for i in range(0, 10, 2):
#         print(f"Even: {i}")
#         event_even.set()
#         event_odd.wait()
#         event_odd.clear()
# def odd_numbers():
#     for i in range(1, 10, 2):
#         print(f"Odd: {i}")
#         event_even.set()
#         event_odd.wait()
#         event_odd.clear()
# def run():
#     thread_even = threading.Thread(target=even_numbers)
#     thread_odd = threading.Thread(target=odd_numbers)
#     thread_even.start()
#     thread_odd.start()
#     thread_even.join()
#     thread_odd.join()

import threading
event_even = threading.Event()
event_odd = threading.Event()
def even_numbers():
    for i in range(0, 10, 2):
        event_even.wait()
        print(f"Even: {i}")
        event_even.clear()
        event_odd.set()
def odd_numbers():
    for i in range(1, 10, 2):
        event_odd.wait()
        print(f"Odd: {i}")
        event_odd.clear()
        event_even.set()
def run():
    thread_even = threading.Thread(target=even_numbers)
    thread_odd = threading.Thread(target=odd_numbers)
    event_even.set()  # Start with even
    thread_even.start()
    thread_odd.start()
    thread_even.join()
    thread_odd.join()
run()