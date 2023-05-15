import math  # for tan function and pi constant
import tkinter as tk

if __name__ == "__main__":
    # initializing the window
    window = tk.Tk()
    window.title("Stronghold Calculator")

    # set window dimensions and disable resizing
    base = 230
    height = 110
    window.geometry(f"{base}x{height}")
    window.resizable(False, False)

    # 75% transparency
    window.attributes('-alpha', 0.75)

    # stay on top of all other windows
    window.attributes('-topmost', True)

    # row 0
    x_label = tk.Label(window, text="X").grid(row=0, column=1)
    z_label = tk.Label(window, text="Z").grid(row=0, column=2)
    f_label = tk.Label(window, text="F").grid(row=0, column=3)

    # row 1
    one_label = tk.Label(window, text=" 1").grid(row=1, column=0)
    x1_entry = tk.Entry(window, width=6)
    x1_entry.grid(row=1, column=1)
    z1_entry = tk.Entry(window, width=6)
    z1_entry.grid(row=1, column=2)
    f1_entry = tk.Entry(window, width=6)
    f1_entry.grid(row=1, column=3)

    # row 2
    two_label = tk.Label(window, text=" 2").grid(row=2, column=0)
    x2_entry = tk.Entry(window, width=6)
    x2_entry.grid(row=2, column=1)
    z2_entry = tk.Entry(window, width=6)
    z2_entry.grid(row=2, column=2)
    f2_entry = tk.Entry(window, width=6)
    f2_entry.grid(row=2, column=3)

    # row 3
    result_label = tk.Label(window, text="Location:").grid(row=3, column=1)

    def get_coords():
        try:
            x1 = float(x1_entry.get())
            z1 = float(z1_entry.get())
            f1 = float(f1_entry.get())
            x2 = float(x2_entry.get())
            z2 = float(z2_entry.get())
            f2 = float(f2_entry.get())

            z = ((z1 * math.tan(-f1 * math.pi / 180)) -
                 (z2 * math.tan(-f2 * math.pi / 180)) - x1 + x2) / (math.tan(
                     -f1 * math.pi / 180) - math.tan(-f2 * math.pi / 180))
            x = (z - z1) * math.tan(-f1 * math.pi / 180) + x1
            result = f"{round(x), round(z)}"
        except:  # noqa
            # excepting all posssible errors because there are too many errors,
            # and regardless of the error type, the program will still run
            # and display "ERROR"
            result = "ERROR"
        finally:
            tk.Label(window, text=result).grid(row=3, column=2)

    calculate_button = tk.Button(window, text="Find",
                                 command=get_coords).grid(row=3, column=3)

    window.mainloop()
