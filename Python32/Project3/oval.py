import tkinter


class Simple_ovals:
   def __init__(self):
      self._root_window=tkinter.Tk()

      self._canvas=tkinter.Canvas(
         master=self._root_window, height=400,
         width=400, padx=10, pady=10,
         sticky=tkinter.N+tkinter.S+tkinter.E+tkinter.W)

      

      
