+++
title = "Basic Tkinter application"
date = 2022-11-08
+++

This example demonstrates the structure of a basic Tkinter application.

```python
import tkinter as tk
from tkinter import ttk


class MyApp:

    def __init__(self, root):
        self.root = root
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.root.title('Example App')
        self.root.geometry('400x300')
        self.root.resizable(True, False)

    def create_widgets(self):
        ttk.Label(text='This is an example app.').pack(pady=10)
        ttk.Button(text='hello').pack()
        ttk.Button(text='there').pack()


if __name__ == '__main__':
    root = tk.Tk()
    MyApp(root)
    root.mainloop()
```

<p><img src="/img/tkinter-app.png" style="max-width: 400px;" alt="basic tkinter app"></p>
