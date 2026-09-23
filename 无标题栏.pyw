import tkinter as tk

if __name__ =="__main__":
    root = tk.Tk()
    root.title("无标题栏")
    root.geometry("500x300+100+100")
    root.overrideredirect(True)

    b = tk.Button(root, text="关闭", font=("微软雅黑", 20), command=root.destroy)
    b.pack(pady=20)

    root.mainloop()
