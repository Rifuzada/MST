import customtkinter
import tkinter as tk
import webbrowser
import os, sys

def open_new_window():
    new_window = customtkinter.CTkToplevel(janela)
    new_window.title("Caracteres especiais - MST")
    new_window.geometry(f"290x130+{x+443}+{y}")
    twitter1 = customtkinter.CTkLabel(new_window, text="by @Rifuzada",text_color="#116530",fg_color=("#116530", "#242424"),corner_radius=8)
    twitter1.place(x=85, y=100)
    new_window.resizable(False, False)
    chars = [
    'а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м',
    'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ',
    'ы', 'ь', 'э', 'ю', 'я'
            ]

    for i, char in enumerate(chars):

        customtkinter.CTkButton(master=new_window, width=4, height=2, text=char,border_color='#07060d', fg_color="#51087E", border_width=4, command=lambda ch=char: set_text(ch)).place(x=48 + 20 * (i % 10), y=25 * (i // 10))


def set_text(text):
   nick_entry.insert(tk.ANCHOR, text)


def open_url(url):
    webbrowser.open_new_tab(url)

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        #PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

janela = customtkinter.CTk()
janela.title("Mastery Search Tool - MST, @Rifuzada")
iconpath = resource_path('m7.ico')
janela.iconbitmap(iconpath)
largura_tela = janela.winfo_screenwidth()
altura_tela = janela.winfo_screenheight()
x = (largura_tela - 440) // 2
y = (altura_tela - 240) // 2
janela.geometry(f"440x240+{x}+{y}")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")
janela.resizable(False, False)

# Entry labels
region_entry = customtkinter.CTkEntry(janela, width=200, height=40, border_width=1, placeholder_text='Ex: br1, na1, kr, tr1, etc...', text_color='silver', justify='center')
region_entry.place(x=5, y=45 )

nick_entry = customtkinter.CTkEntry(janela, width=430, height=40, border_width=1, placeholder_text="Riot#ID", text_color="silver", justify='center')
nick_entry.place(x=5, y=0)

# Botoes
botaoNovaJanela = customtkinter.CTkButton(master=janela, width=100, height=20, border_width=3, border_color='#07060d', text="caracteres especiais", fg_color="#51087E", command=open_new_window)
botaoNovaJanela.place(x=140, y=120)

# Labels
url = "https://twitter.com/rifuzada"

twitter = customtkinter.CTkLabel(janela, text="by @Rifuzada",cursor= "hand2",text_color="#116530",fg_color=("#116530", "#242424"),corner_radius=8)
twitter.place(x=165, y=180)
twitter.bind("<Button-1>", lambda e: open_url(url))

info1 = customtkinter.CTkLabel(janela, text="", fg_color=("#116530", "#242424"), text_color="#116530")
info1.place(x=0, y=0)
