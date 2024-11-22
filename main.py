# https://www.pythonguis.com/tutorials/create-gui-tkinter/
import tkinter as tk

def create_window(title = "Bob's Brewery", min_width = 300, min_height = 300, max_width = 3000, max_height = 3000, xpos = 800, ypos = 200, geometry_string = ""):
  window = tk.Tk()
  window.title(title)
  window.minsize(min_width, min_height)
  window.maxsize(max_width,max_height)

  if geometry_string == "":
    geometry_string = str(min_width + 200) + "x" + str(min_height + 200) + "+" + str(xpos) + "+" + str(ypos)

  window.geometry(geometry_string)

  return window


root = create_window()
root.mainloop()