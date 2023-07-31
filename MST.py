import requests
from id_champ import get_champions_name
from tkinter import *
import customtkinter
import webbrowser

janela = customtkinter.CTk()
janela.title("Mastery Search Tool - MST, @Rifuzada")
janela.geometry("450x370")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")

def open_url(url):
   webbrowser.open_new_tab(url)

def region_check():
    b = str(region_entry.get())
    if len(b) == 3:
        pass
    elif len(b) == 2:
        pass
    elif len(b)== 1:
        print("A região escolhida está incorreta.")
        info['text']= "A região escolhida está incorreta.\nPor favor coloque a região certa."
        
    elif len(b) == 0:
        info['text'] = "Por favor selecione a região antes de apertar o botao."

    elif len(b) > 3:
        print("A região escolhida está incorreta.")
        info['text']= "A região escolhida está incorreta.\nPor favor coloque a região certa."

        
def nick_check():
    a = str(nick_entry.get())
    if len(a) <= 16:
        info["text"] = "Para pesquisar novamente feche a janela que acabou de abrir e pesquise novamente."
        try:
            if len(a) <= 1:
                info['text'] = "Por favor selecione o nick antes de apertar o botao."
        except:
            info['text'] = "por favor selecione escreva um nick."
    elif len(a) > 16:
        print("O nick escolhido está incorreto.")
        info['text']= "O nick escolhido está incorreto.\nPor favor coloque o nick certo."

        
def pegar_id():
    janela.geometry("450x200")
    nick = ""
    x = "%s" % nick_entry.get()
    nick = x
    nick.upper()
    region = ""
    c = "%s" %region_entry.get()
    region = c
    apikey = ""#Sua api key aqui.
    ids = requests.get(f"https://"+region+".api.riotgames.com/lol/summoner/v4/summoners/by-name/"+nick+"?api_key="+apikey)
    pf2 = ids.json()
    summonerid = pf2["id"]
    mastery = requests.get(f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-summoner/{summonerid}?api_key={apikey}")
    top_5 = mastery.json()
    ids = requests.get(f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/{summonerid}?api_key={apikey}")
    pf = ids.json()
    pf1 = str(pf)

    region1 = str(region)
    a = region1.replace("br1", "BR")
    a = a.replace("kr", "KR")
    a = a.replace("tr1","TR")
    a = a.replace("OC1","OCE")
    a = a.replace("LA2","LAS")
    a = a.replace("EUN1","EUNE")
    a = a.replace("EUW1","EUW")
    a = a.replace("NA1","NA")
    a = a.replace("LA1","LAN")
    a = a.replace("Br1", "BR")
    l = a.replace("jp1", "JP")
    
    def a():
        janela.geometry('310x300')
        try:
            champion_id = top_5[0]["championId"]
            Maestria1 = top_5[0]["championLevel"]
            Pontos1 = top_5[0]["championPoints"]
            Bau1 = top_5[0]["chestGranted"]
            Maestria2 = top_5[1]["championLevel"]
            Champion2 = top_5[1]["championId"]
            Bau2 = top_5[1]["chestGranted"]
            Pontos2 = top_5[1]["championPoints"]
            Champion3 = top_5[2]["championId"]
            Bau3 = top_5[2]["chestGranted"]
            Pontos3 = top_5[2]["championPoints"]
            Maestria3 = top_5[2]["championLevel"]
            if 1 <= int(champion_id) <= 897:
                Bauz = str(Bau1)
                a = Bauz.replace("True", "Sim")
                a = a.replace("False", "Não")
                Baus = str(Bau2)
                b = Baus.replace("False", "Não")
                d = b.replace("True", "Sim")
                Bau = str(Bau3)
                e = Bau.replace("False", "Não")
                f = e.replace("True", "Sim")
            
            for text1 in pf.get("name"):
                text1 = "O perfil pesquisado foi: " + pf["name"] + "\n"
                text2 =f"A Sua maior maestria é com o champion: {get_champions_name(int(champion_id))}\nSua maestria é de nível {Maestria1}.\nCom {Pontos1:_} pontos de maestria.\nJá ganhou baú com este champion? {a}\nSua Segunda maior maestria é com o champion: {get_champions_name(int(Champion2))}\nSua maestria é de nível {Maestria2}.\nCom {Pontos2:_} pontos de maestria.\nJá ganhou baú com este champion? {d}\nSua Terceira maior maestria é com o champion: {get_champions_name(int(Champion3))}\nSua maestira é de nível {Maestria3}\nCom {Pontos3:_} pontos de maestria.\nJá ganhou baú com este champion? {f}\n"                
                texto_maestrias["text"] = text2.replace("_", '.')
                texto_orientacao["text"] = text1
            button.destroy()
            info['text']= '' 
            nick_entry.grid_forget()
            region_entry.grid_forget()
        except:
            texto_maestrias["text"] = "O jogador pesquisado não possui todas as 3 maestrias..."


    texto_orientacao = Label(janela, text="Clique no botão abaixo para exibir as maestrias de "+ pf["name"], font=("Arial", 10), background="#242424", fg="white") 
    texto_orientacao.grid(column=0, row=4)

    regiao = Label(janela, text="A Região selecionada é {0}".format(l),bg = "#242424", fg="white")
    regiao.grid(column=0,row=5)
    button = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Exibir", command=a)
    button.place(relx=0.5, rely=0.5)
    button.grid(column=0, row=6)
    
    region_entry.grid_forget()
    nick_entry.grid_forget()
    botao.destroy()


    texto_maestrias = Label(janela, text="",bg = "#242424",  fg="white")
    texto_maestrias.grid(column=0   , row=7)
    

region_entry = customtkinter.CTkEntry(janela,width=200, height=40, border_width=1, placeholder_text='Ex: br1, na1, kr, tr1, etc...', text_color='silver')
region_entry.grid(row=6, column=0, padx=10, pady=10)
nick_entry = customtkinter.CTkEntry(janela, width=430, height=40, border_width=1, placeholder_text="Escreva um nick", text_color="silver")
nick_entry.grid(row=0, column=0, padx=10, pady=10)

botao = customtkinter.CTkButton(master=janela, text="Buscar Maestrias",fg_color="#51087E",  command=lambda: [nick_check(),region_check(), pegar_id()])
botao.place(relx=0.5, rely=0.5)
botao.grid(column=0, row=12)

url= "https://twitter.com/rifuzada"
twitter = Label(janela, text="by @Rifuzada",background="#242424", fg="#116530")
twitter.grid(column=0, row=26)
twitter.bind("<Button-1>", lambda e:open_url(url))

info = Label(janela, text="",background="#242424", fg="#116530")
info.grid(column=0, row=25)


janela.mainloop()
