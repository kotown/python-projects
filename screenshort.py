import time
import pyautogui
import os
import tkinter as tk

def screenshot():
    save_location ='C:/Users/Bramwel/OneDrive/Documents/Code/python/screenshot data'
    if not os.path.exists(save_location):
        os.makedirs(save_location)

    name = int(round(time.time() * 1000))
    name = '{}.png'.format(name)
    time.sleep(0)
    img = pyautogui.screenshot(name)
    file_path= os.path.join(save_location, name)
    img.save(file_path)

root=tk.Tk()
root.title("Screenshot app")
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)
frame = tk.Frame(root)
frame.pack()
button=tk.Button(
    frame,
    text="Screenshot",
    command=screenshot
)
button.pack(side=tk.LEFT)

close=tk.Button(
    frame,
    text="QUIT",
    command=quit
)
close.pack(side=tk.LEFT)

root.mainloop()