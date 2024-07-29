""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info

# Create the main window
root = Tk()
root.title("Pokemon Information")
root.geometry('800x500')
root.resizable(False,False)
root.grid_columnconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)

pkmnInfo = {}
# TODO: Create the frames
def btn_click():
  pkmnName = ent_name.get()
  global pkmnInfo 
  pkmnInfo = get_pokemon_info(pkmnName)
  if not pkmnInfo:
    showError(pkmnName)

frm_top = ttk.Frame(root)
frm_top.grid(row=0,column=0, columnspan=2)  


frm_btm_left = ttk.Frame(root)
frm_btm_left.grid(row=1, column=0, sticky='ew')

frm_btm_right = ttk.Frame(root)
frm_btm_right.grid(row=1, column=1,padx=10 ,sticky='ew')


# TODO: Populate the user input frame with widgets

pokemonName = ttk.Label(frm_top, text='Pokemon Name')
pokemonName.grid(row=0,column=0,padx=10)

ent_name = ttk.Entry(frm_top)
ent_name.grid(row=0,column=1)

btn_get = ttk.Button(frm_top, text='Get Info',command=btn_click)
btn_get.grid(row=0,column=2,padx=10)

pokemonInfo = ttk.Label(frm_btm_left,text='Info')
pokemonInfo.grid(row=0,column=0)

pokemonHeight = ttk.Label(frm_btm_left,text='Height:')
pokemonHeight.grid(row=1,column=1)
pokemonHeight_v = ttk.Label(frm_btm_left, text='Test')
pokemonHeight_v.grid(row=1,column=2)

pokemonHeight = ttk.Label(frm_btm_left,text='Weight:')
pokemonHeight.grid(row=2,column=1)
pokemonHeight = ttk.Label(frm_btm_left,text='Type:')
pokemonHeight.grid(row=3,column=1)

pokemonStats = ttk.Label(frm_btm_right,text='Stats')
pokemonStats.grid(row=0,column=0)
pokemonHP = ttk.Label(frm_btm_right, text='HP: ')
pokemonHP.grid(row=1, column=1)
pokemonAtk = ttk.Label(frm_btm_right, text='Attack: ')
pokemonAtk.grid(row=2, column=1)
pokemonDef = ttk.Label(frm_btm_right, text='Defense: ')
pokemonDef.grid(row=3, column=1)
pokemonSpA = ttk.Label(frm_btm_right, text='Special Attack: ')
pokemonSpA.grid(row=4, column=1)
pokemonSpD = ttk.Label(frm_btm_right, text='Special Defense: ')
pokemonSpD.grid(row=5, column=1)
pokemonSpeed = ttk.Label(frm_btm_right, text='Speed: ')
pokemonSpeed.grid(row=6, column=1)

# TODO: Define button click event handler function

def showError(name):
  messagebox.showerror("Error", f"Unable to fetch information for {name} from the PokeAPI")
  

root.mainloop()