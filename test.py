import tkinter as tk
root=tk.Tk()
root.geometry("500x450+700+280") 
root.title("Let's go gambling!")
button=tk.Button(root,text="Roll",width=10)
button.place(x=210,y=200)
button.grid_location(x=10,y=10)
root.mainloop()