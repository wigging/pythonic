---
title: Update label text in Tkinter
date: February 4, 2023
---

Example of updating a Label's text in Tkinter.

```python
import tkinter as tk
from tkinter import ttk


class MyApp:

    def __init__(self, root):
        self.root = root
        self.counter = tk.IntVar()
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.root.title('My App')
        self.root.geometry('400x200')

    def create_widgets(self):
        frame = ttk.Frame(self.root).pack(pady=10)
        ttk.Button(frame, text='Increment', command=self.increment).pack()
        ttk.Label(frame, textvariable=self.counter).pack()

    def increment(self):
        self.counter.set(self.counter.get() + 1)
        print(f'counter is {self.counter.get()}')


if __name__ == '__main__':
    root = tk.Tk()
    MyApp(root)
    root.mainloop()
```

<p><img src="../images/tkinter-label.png" style="max-width: 400px;" alt="tkinter label"></p>
