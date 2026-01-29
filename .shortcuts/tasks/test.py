#!/data/data/com.termux/files/usr/bin/env python

import time
import threading

import termuxgui as tg


with tg.Connection() as c:
    a = tg.Activity(c)

    root = tg.LinearLayout(a)

    title = tg.TextView(a, "Sample Title", root)
    title.settextsize(30)

    content_data = """
This is an example set of data text!


Continued down here...

"""

    content = tg.TextView(a, content_data, root)
    content.setlinearlayoutparams(10)

    button = tg.Button(a, "Click Me!", root)

    # Handle Events
    count = 0
    def handle():
        global count
        for ev in c.events():
            if ev.type == tg.Event.click and ev.value["id"] == button:
                count += 1

    # Setup Threads
    watcher = threading.Thread(target=handle, daemon=True)
    watcher.start()

    time.sleep(8)
    print(f"Button pressed {count} times")


    time.sleep(3)










