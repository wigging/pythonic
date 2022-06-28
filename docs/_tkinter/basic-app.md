---
title: Basic application
permalink: basicapp
---

This example demonstrates the structure of a basic Tkinter application.

```python
import tkinter as tk
import tkinter.ttk as ttk


class MyApp:

    def __init__(self, root):
        self.root = root
        self.configure_gui()
        self.create_widgets()

    def configure_gui(self):
        self.root.title('Example App')
        self.root.geometry('400x300')
        self.root.resizable(True, False)

    def create_widgets(self):
        ttk.Label(text='This is an example app.').pack(pady='10')
        ttk.Button(text='hello').pack()
        ttk.Button(text='there').pack()


if __name__ == '__main__':
    root = tk.Tk()
    main_app = MyApp(root)
    root.mainloop()
```

![basic tkinter app](/pythonic/images/tkinter-app.png)
