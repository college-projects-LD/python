import pypokedex
import PIL.Image, PIL.ImageTk
import tkinter as tk
import urllib3
from io import BytesIO


window = tk.Tk()
window.title("Landon's Pokedex")
window.geometry("500x500")
window.configure(padx=10, pady=10)

title_l = tk.Label(window, text="Landon's Pokedex")
title_l.configure(font=("Helvetica", 35))
title_l.pack(padx=10, pady=10)


pokemonImage = tk.Label(window) # create a label for the image
pokemonImage.pack(padx=10, pady=10) # pack the image

pokemonInfo = tk.Label(window) # create a label for the info
pokemonInfo.configure(font=("Helvetica", 20)) # set the font
pokemonInfo.pack(padx=10, pady=10) # pack the info

pokemonTypes = tk.Label(window) # create a label for the info
pokemonTypes.configure(font=("Helvetica", 20)) # set the font
pokemonTypes.pack(padx=10, pady=10) # pack the info


def getPokemon():
    # get the pokemon from the pokedex
    pokemon = pypokedex.get(name = text_id_name.get(1.0, "end-1c"))
    # get the image from the pokedex useing the urllib3 library
    http = urllib3.PoolManager()
    response = http.request('GET', pokemon.sprites.front.get('default'))
    image = PIL.Image.open(BytesIO(response.data))

    # set the image to the label
    image = PIL.ImageTk.PhotoImage(image)
    pokemonImage.configure(image=image)
    pokemonImage.image = image



    # set the info to the label
    

    pokemonInfo.configure(text=f"{pokemon.dex} - {pokemon.name}".title()) 
    pokemonTypes.configure(text=" - ".join([type for type in pokemon.types]).title()) 



label_id_name = tk.Label(window, text="Pokemon ID OR NAME:")
label_id_name.configure(font=("Helvetica", 20))
label_id_name.pack(padx=10, pady=10)

text_id_name =tk.Text(window, height=1,)
text_id_name.configure(font=("Helvetica", 20))
text_id_name.pack(padx=10, pady=10)

btn_load = tk.Button(window, text="Load Pokemon", command=getPokemon)
btn_load.configure(font=("Helvetica", 20))
btn_load.pack(padx=10, pady=10)



window.mainloop()






