Django Signals & Python Classes

Quick Overview

This covers:
✅ Understanding Django Signals.
✅ Creating an iterable Rectangle class.

🛠 Django Signals

1️⃣ Are Signals Synchronous?

Yes! Django signals block execution until they complete. We prove this using a slow signal handler with time.sleep(5).

2️⃣ Do Signals Run in the Same Thread?

Yes! We print thread IDs and confirm that the caller and the signal execute in the same thread.

3️⃣ Do Signals Share the Database Transaction?

Yes! Using transaction.atomic(), we check if the signal runs within the same transaction, proving it does.

📏 Rectangle Class

We build a Rectangle class that:
🔹 Takes length and width as input.
🔹 Supports iteration, yielding {'length': value} first, then {'width': value}.

Example:

rect = Rectangle(10, 5)
for attr in rect:
    print(attr)

🔹 Output:

{'length': 10}
{'width': 5}

🚀 Running the Code

🔹 Django Signals → Requires Django installed, run in a Django environment.
🔹 Rectangle Class → Run as a standalone Python script.

🎯 Conclusion

This assignment clarifies Django signals' behavior and reinforces Python class design. Short, practical, and fun!


