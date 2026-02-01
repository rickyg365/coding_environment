#!/data/data/com.termux/files/usr/bin/env python

import time
import threading

import termuxgui as tg

"""
Idea
Data entry
    Create schema
    C:      input data
    RUD:    Display Data for Edit/Delete
    Function?: perform analysis, send to server, download
"""

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
        btn_click = lambda event, btn: event.type == tg.Event.click and event.value["id"] == btn
        for ev in c.events():
            if btn_click(ev, button):
                count += 1

    # Setup Threads
    watcher = threading.Thread(target=handle, daemon=True)
    watcher.start()

    time.sleep(8)
    print(f"Button pressed {count} times")


    time.sleep(3)










