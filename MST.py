import requests
from id_champ import get_champions_name
from tkinter import *
import customtkinter
import webbrowser
from chars import *

def open_url(url):
    webbrowser.open_new_tab(url)
def voltar1():
    janela.geometry(f"440x240+{x}+{y}")
    buttonvoltar1.place_forget()
    region_entry.place(x=5, y=45 )
    nick_entry.place(x=5, y=0)    
    botaoNovaJanela.place(x=140, y=120)
    twitter.place(x=165, y=180)
    info1.configure(text="")
    info1.place(x=0, y=0)
    botao.place(x=135, y=150)
    

def voltar():
    janela.geometry(f"440x240+{x}+{y}")
    buttonvoltar.place_forget()
    buttonvoltar1.place_forget()
    texto_orientacao.grid_forget()
    regiao.grid_forget()
    texto_maestrias.grid_forget()
    buttonvoltar.place_forget()
    region_entry.place(x=5, y=45)
    nick_entry.place(x=5, y=0)
    botaoNovaJanela.place(x=140, y=120)
    twitter.place(x=165, y=180)
    info1.place(x=0, y=0)
    botao.place(x=135, y=150)

def region_check():
    global region

    region = region_entry.get().strip()
    if len(region) == 0 or len(region) > 3:
        info1.configure(text = "A região escolhida está incorreta.\nPor favor coloque a região certa.")
        buttonvoltar1.place(x=0, y=180)
    elif len(region) == 1:
        info1.configure(text = "A região escolhida está incorreta.\nPor favor coloque a região certa.")
        buttonvoltar1.place(x=0, y=180)
    
def nick_check():
    global nick

    nick = nick_entry.get().strip().lower()
    if len(nick) <= 1:
        info1.configure(text  = "Por favor selecione o nick antes de apertar o botao.")
        buttonvoltar1.place(x=0, y=180)
    elif len(nick) > 16:
        info1.configure(text= "O nick escolhido está incorreto.\nPor favor coloque o nick certo.")

        buttonvoltar1.place(x=0, y=180)

def pegar_id():
    global button
    global regiao
    global texto_orientacao
    global texto_maestrias
    global buttonvoltar

    buttonvoltar.configure(state="disabled")
    buttonvoltar.place_forget()
    region_entry.place_forget()
    nick_entry.place_forget()
    botao.place_forget()
    botaoNovaJanela.place_forget()

    nick = ""
    nick = "%s" % nick_entry.get()#salva a info dada no label nick
    nick = nick.upper()
    nick = nick.replace('#', "/")
    region = ""
    region = "%s" %region_entry.get()#salva a info dada no label region
    apikey = "RGAPI-7c344e50-87fc-4a4b-9ac0-fb6db835fa51"#Api key usada pela riot: https://developer.riotgames.com/
    ids1 = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nick}?api_key={apikey}")#request para conseguir os ids
    ids1 = ids1.json()#transforma o request no json que ele responde
    puuid = ids1["puuid"]#puxa o id que precisa do request ids1
    mastery = requests.get(f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={apikey}")#request para puxar maestrias
    top_3 = mastery.json()
    twitter.place(x=125, y=120)
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
    janela.geometry('350x180')
    def display_masteries():
        buttonvoltar.configure(state="normal")
        janela.geometry('360x240')
        twitter.place(x=130, y=210)
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
            text2 = text2.replace("_", '.')
            texto_orientacao["text"] = text1
            texto_maestrias.configure(text=text2)
            texto_maestrias.grid()
            buttonvoltar.place(x=0, y=160)
            button.grid_forget()
            info1['text'] = ''
        except (KeyError, IndexError) as e:
            texto_maestrias["text"] = "O jogador pesquisado não possui todas as 3 maestrias..."

    texto_orientacao = customtkinter.CTkLabel(janela, text=f"Clique no botão abaixo para exibir as maestrias de {ids1['gameName']}#{ids1['tagLine']}", font=("Arial", 10), fg_color=("white", "#242424"),corner_radius=8) 
    texto_orientacao.grid(column=0, row=4)

    regiao = customtkinter.CTkLabel(janela, text="A Região selecionada é {0}".format(region1), fg_color=("white", "#242424"),corner_radius=8)
    regiao.grid(column=0,row=5)
    button = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Exibir", command=display_masteries)
    button.grid(column=0, row=6)



    texto_maestrias = customtkinter.CTkLabel(janela, text="", fg_color=("white", "#242424"), justify="left",corner_radius=8)
    texto_maestrias.grid(column=0   , row=7)


janela.bind('<Return>', lambda event: [nick_check(), region_check(), pegar_id()])
botao = customtkinter.CTkButton(master=janela, text="Buscar Maestrias", fg_color="#51087E", border_width=3, border_color='#07060d', command=lambda: [nick_check(), region_check(),pegar_id()])
botao.place(x=135, y=150)

buttonvoltar = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Voltar", command=voltar)
buttonvoltar1 = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Voltar", command=voltar1)


janela.mainloop()
