import time
import threading
from django.core.signals import request_finished
from django.db import transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

# ============================
# Django Signals Questions
# ============================

# Question 1: Are Django signals executed synchronously?
@receiver(request_finished)
def slow_signal_handler(sender, **kwargs):
    print("Signal handler started.")
    time.sleep(5)  # Simulating slow execution
    print("Signal handler finished.")

print("Before request_finished signal.")
request_finished.send(sender=None)
print("After request_finished signal.")

# Question 2: Do Django signals run in the same thread as the caller?
def get_thread_id():
    return threading.get_ident()

@receiver(request_finished)
def check_signal_thread(sender, **kwargs):
    print(f"Signal executed in thread: {get_thread_id()}")

print(f"Main thread: {get_thread_id()}")
request_finished.send(sender=None)

# Question 3: Do Django signals run in the same database transaction as the caller?
@receiver(post_save, sender=User)
def signal_handler(sender, instance, **kwargs):
    print("Signal handler started.")
    print("Is transaction still active?", transaction.get_connection().in_atomic_block)

with transaction.atomic():
    user = User.objects.create(username="testuser")
    print("User created inside transaction.")
    print("Is transaction still active?", transaction.get_connection().in_atomic_block)

# ============================
# Custom Classes in Python
# ============================

class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width

    def __iter__(self):
        yield {"length": self.length}
        yield {"width": self.width}

# Example usage
rect = Rectangle(10, 5)
for attr in rect:
    print(attr)