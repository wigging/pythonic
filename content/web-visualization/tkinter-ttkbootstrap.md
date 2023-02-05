---
title: Theme ttkbootstrap
date: February 4, 2023
---

Example of a Tkinter app using the ttkbootstrap theme. More information about
the theme is available on GitHub at [israel-dryer/ttkbootstrap](https://github.com/israel-dryer/ttkbootstrap).

```python
import ttkbootstrap as ttk
import matplotlib.pyplot as plt


class MyApp:

    def __init__(self, root):
        self.root = root
        self.configure_window()
        self.create_widgets()

    def configure_window(self):
        self.root.title('Example App')
        self.root.geometry('400x300')
        self.root.resizable(False, False)

    def create_widgets(self):
        ttk.Label(text='Below is Entry widget').pack(pady=10)
        ttk.Entry().pack()
        ttk.Button(text='Hello there', bootstyle='success').pack(pady=10)
        ttk.Button(text='Plot data', command=self.create_plot).pack(pady=20)

    def create_plot(self):
        # Numbers to plot
        numbers = [1, 2, 5, 4, 8, 10, 7]

        # Create plot
        fig, ax = plt.subplots(tight_layout=True)
        ax.plot(numbers)
        ax.set_xlabel('X axis')
        ax.set_ylabel('Y axis')
        ax.grid(color='0.8')
        ax.set_frame_on(False)
        ax.tick_params(color='0.8')

        # Show window containing the plot figure
        plt.show()


if __name__ == '__main__':
    root = ttk.Window(themename='darkly')
    MyApp(root)
    root.mainloop()
```

<p><img src="../img/tkinter-ttkbootstrap.png" style="max-width: 400px;" alt="ttkbootstrap"></p>
