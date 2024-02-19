import customtkinter

def open_new_window():
    new_window = customtkinter.CTkToplevel(janela)
    new_window.title("caracteres especiais")
    new_window.geometry("290x130")
    new_window.resizable(False, False)
    chars = ["е", "а", "с", "г", "р", "о", "в", "н", "м", "т", "я", "ш", "у", "и", "п", "л", "г", "ф", "д", "ж"]

    for i, char in enumerate(chars):

        customtkinter.CTkButton(master=new_window, width=4, height=2, text=char, fg_color="#51087E", border_width=1, command=lambda ch=char: set_text(ch)).place(x=68 + 15 * (i % 10), y=25 * (i // 10))


def set_text(text):
   nick_entry.insert(END, text)

janela = customtkinter.CTk()
janela.title("Mastery Search Tool - MST, @Rifuzada")
janela.geometry("440x270")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")


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

twitter = customtkinter.CTkLabel(janela, text="by @Rifuzada",text_color="#116530",fg_color=("#116530", "#242424"),corner_radius=8)
twitter.place(x=165, y=180)
twitter.bind("<Button-1>", lambda e: open_url(url))

info1 = customtkinter.CTkLabel(janela, text="", fg_color=("#116530", "#242424"), text_color="#116530")
info1.place(x=0, y=0)
