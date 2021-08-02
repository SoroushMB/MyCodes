import pyautogui
import tkinter as tk

root = tk.TK()

canvas1 = tk.Canvas(root, width = 300, height = 300)
canvas1.pack()

def takeScreenshot ():

    myScreenshot = pyautogui.screenshot()
    myScreenshot.save('screenshot2.png')
    print("ScreenshotHasBeenSavedToYourCurrentDirectory")

myButton = tk.Button(text='TakeScreenshot', command=takeScreenshot,
bg='green',fg='white',font= 10)
canvas1.creat.window(150, 150, window=myButton)

root.mainloop()
