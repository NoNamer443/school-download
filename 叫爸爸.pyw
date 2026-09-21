import tkinter as tk
from tkinter.messagebox import showinfo

f = ("Consolas", 40)


def change1(event: None | tk.Event = None) -> None:
    var1.set("爸爸")
    var2.set("不叫")


def change2(event: None | tk.Event = None) -> None:
    var1.set("不叫")
    var2.set("爸爸")


def hit() -> None:
    showinfo("正确", "乖儿子")
    w.destroy()


def try_to_close() -> None:
    showinfo("嘿", "你以为呢")


# 不加点注释就浑身难受
if __name__ == "__main__":
    w = tk.Tk()
    w.title("简单问题")
    w.geometry("500x300")
    w.resizable(False, False)
    w.protocol("WM_DELETE_WINDOW", try_to_close)

    l = tk.Label(w, text="叫爸爸", font=f)

    frame = tk.Frame(w)

    var1 = tk.StringVar()
    b1 = tk.Button(frame, textvariable=var1, font=f, command=hit)

    var2 = tk.StringVar()
    b2 = tk.Button(frame, textvariable=var2, font=f, command=hit)

    l.pack(pady=20)
    frame.pack(pady=20)
    b1.pack(side="left", padx=50)
    b2.pack(side="right", padx=50)

    b1.bind("<Enter>", change1)
    b2.bind("<Enter>", change2)

    var1.set("爸爸")

    var2.set("不叫")

    w.mainloop()
