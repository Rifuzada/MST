import requests
from id_champ import get_champions_name
from tkinter import *
import customtkinter
import webbrowser

def open_url(url):
    webbrowser.open_new_tab(url)

def open_new_window():
    new_window = customtkinter.CTkToplevel(janela)
    new_window.title("caracteres especiais")
    new_window.geometry("290x130")
    new_window.resizable(False, False)
    chars = ["е", "а", "с", "г", "р", "о", "в", "н", "м", "т", "я", "ш", "у", "и", "п", "л", "г", "ф", "д", "ж"]

    for i, char in enumerate(chars):

        customtkinter.CTkButton(master=new_window, width=4, height=2, text=char, fg_color="#51087E", border_width=1, command=lambda ch=char: set_text(ch)).place(x=68 + 15 * (i % 10), y=25 * (i // 10))


def region_check():
    region = region_entry.get().strip()
    if len(region) == 0 or len(region) > 3:
        info1['text'] = "A região escolhida está incorreta.\nPor favor coloque a região certa."
        region_entry.destroy()
        nick_entry.destroy()
        botao.destroy()
        botaoNovaJanela.destroy()
    elif len(region) == 1:
        info1['text'] = "A região escolhida está incorreta.\nPor favor coloque a região certa."
        region_entry.destroy()
        nick_entry.destroy()
        botao.destroy()
        botaoNovaJanela.destroy()

def nick_check():
    nick = nick_entry.get().strip().lower()
    if len(nick) <= 1:
        info1['text'] = "Por favor selecione o nick antes de apertar o botao."
        region_entry.destroy()
        nick_entry.destroy()
        botao.destroy()
        botaoNovaJanela.destroy()
    elif len(nick) > 16:
        info1['text'] = "O nick escolhido está incorreto.\nPor favor coloque o nick certo."
        region_entry.destroy()
        nick_entry.destroy()
        botao.destroy()
        botaoNovaJanela.destroy()

def pegar_id():
        nick = ""
        nick = "%s" % nick_entry.get()#salva a info dada no label nick
        nick = nick.upper()
        nick = nick.replace('#', "/")
        region = ""
        region = "%s" %region_entry.get()#salva a info dada no label region
        apikey = ""#Api key usada pela riot: https://developer.riotgames.com/
        ids1 = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nick}?api_key={apikey}")#request para conseguir os ids
        ids1 = ids1.json()#transforma o request no json que ele responde
        puuid = ids1["puuid"]#puxa o id que precisa do request ids1
        mastery = requests.get(f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={apikey}")#request para puxar maestrias
        top_3 = mastery.json()

        region_mapping = {
            "br1": "BR",
            "kr": "KR",
            "tr1": "TR",
            "OC1": "OCE",
            "LA2": "LAS",
            "EUN1": "EUNE",
            "EUW1": "EUW",
            "NA1": "NA",
            "LA1": "LAN",
            "jp1": "JP"
        }

        region1 = region
        for code, abbreviation in region_mapping.items():
            region1 = region1.replace(code, abbreviation)
        janela.geometry('370x150')
        def display_masteries():
            janela.geometry('330x190')
            try:
                # Get mastery information
                mastery_info = []
                for i in range(min(3, len(top_3))):  # Ensure we don't exceed the length of top_3
                    mastery = top_3[i]
                    champion_id = mastery["championId"]
                    level = mastery["championLevel"]
                    points = mastery["championPoints"]
                    chest_granted = "Sim" if mastery["chestGranted"] else "Não"
                    mastery_info.append((champion_id, level, points, chest_granted))
                
                # Build text for display
                text1 = f"O perfil pesquisado foi: {ids1['gameName']}#{ids1['tagLine']}\n"
                text2 = ""
                for info in mastery_info:
                    champion_name = get_champions_name(info[0])
                    text2 += f"Sua maestria com {champion_name} é de nível {info[1]} com {info[2]:_} pontos.\nJá ganhou baú? {info[3]}\n"
                texto_maestrias["text"] = text2.replace("_", '.')
                texto_orientacao["text"] = text1
                button.destroy()
                info1['text'] = ''
            except (KeyError, IndexError) as e:
                texto_maestrias["text"] = "O jogador pesquisado não possui todas as 3 maestrias..."




        texto_orientacao = Label(janela, text=f"Clique no botão abaixo para exibir as maestrias de {ids1['gameName']}#{ids1['tagLine']}", font=("Arial", 10), background="#242424", fg="white") 
        texto_orientacao.grid(column=0, row=4)

        regiao = Label(janela, text="A Região selecionada é {0}".format(region1),bg = "#242424", fg="white")
        regiao.grid(column=0,row=5)
        button = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Exibir", command=display_masteries)
        button.place(relx=0.5, rely=0.5)
        button.grid(column=0, row=6)
        twitter.place(x=165, y=140)
        
        region_entry.destroy()
        nick_entry.destroy()
        botao.destroy()
        botaoNovaJanela.destroy()


        texto_maestrias = Label(janela, text="",bg = "#242424",  fg="white", justify="left")
        texto_maestrias.grid(column=0   , row=7)

def set_text(text):
    nick_entry.insert(END, text)

janela = customtkinter.CTk()
janela.title("Mastery Search Tool - MST, @Rifuzada")
janela.geometry("448x270")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

janela.bind('<Return>', lambda event: [nick_check(), region_check(), pegar_id()])

# Entry labels
region_entry = customtkinter.CTkEntry(janela, width=200, height=40, border_width=1, placeholder_text='Ex: br1, na1, kr, tr1, etc...', text_color='silver', justify='center')
region_entry.grid(row=3, column=0, padx=15, pady=5, columnspan=2, sticky=(W))
region_entry.place(x=8, y=50)

nick_entry = customtkinter.CTkEntry(janela, width=430, height=40, border_width=1, placeholder_text="Riot#ID", text_color="silver", justify='center')
nick_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=3, sticky=(N))
nick_entry.place(x=8, y=0)

# Buttons
botaoNovaJanela = customtkinter.CTkButton(master=janela, width=100, height=20, border_width=3, border_color='#07060d', text="caracteres especiais", fg_color="#51087E", command=open_new_window)
botaoNovaJanela.place(x=140, y=120)

botao = customtkinter.CTkButton(master=janela, text="Buscar Maestrias", fg_color="#51087E", border_width=3, border_color='#07060d', command=lambda: [nick_check(), region_check(), pegar_id()])
botao.place(x=135, y=150)

url = "https://twitter.com/rifuzada"
twitter = Label(janela, text="by @Rifuzada", background="#242424", fg="#116530")
twitter.place(x=165, y=180)
twitter.bind("<Button-1>", lambda e: open_url(url))

info1 = Label(janela, text="", background="#242424", fg="#116530")
info1.grid(column=0, row=25)

janela.mainloop()
