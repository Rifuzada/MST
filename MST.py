import requests
from id_champ import get_champions_name
from tkinter import *
import customtkinter
import webbrowser

janela = customtkinter.CTk()
janela.title("Mastery Search Tool - MST, @Rifuzada")
janela.geometry("448x270")
customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("blue")



def open_url(url):
   webbrowser.open_new_tab(url)

def openNewWindow():
    newWindow = customtkinter.CTkToplevel(janela)
    newWindow.title("caracteres especiais")
    newWindow.geometry("290x130")
    newWindow.resizable(False,False)
    botao1 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="е",fg_color="#51087E",border_width=1,  command= lambda:set_text("е"))
    botao1.place(x=68,y=0)

    botao2 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="а",fg_color="#51087E",border_width=1 , command= lambda:set_text("а"))
    botao2.place(x=83,y=0)

    botao3 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="с",fg_color="#51087E", border_width=1 , command= lambda:set_text("с"))
    botao3.place(x=98,y=0)

    botao4 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="г",fg_color="#51087E",border_width=1 ,  command= lambda:set_text("г"))
    botao4.place(x=114,y=0)

    botao5 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="р",fg_color="#51087E",border_width=1 ,  command= lambda:set_text("р"))
    botao5.place(x=125,y=0)

    botao6 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="о",fg_color="#51087E",border_width=1 ,  command= lambda:set_text("о"))
    botao6.place(x=140,y=0)

    botao7 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="в",fg_color="#51087E",border_width=1 ,  command= lambda:set_text("в"))
    botao7.place(x=155,y=0)

    botao8 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="н",fg_color="#51087E",border_width=1 ,  command= lambda:set_text("н"))
    botao8.place(x=170,y=0)

    botao9 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="м",fg_color="#51087E",border_width=1 ,  command= lambda:set_text("м"))
    botao9.place(x=185,y=0)

    botao10 = customtkinter.CTkButton(master=newWindow,width=4, height=2, text="т",fg_color="#51087E", border_width=1 , command= lambda:set_text("т"))
    botao10.place(x=203,y=0)

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
    a = a.lower()
    p = '#'
    if len(a) <= 16:
        try:
            if len(a) <= 1:
                info['text'] = "Por favor selecione o nick antes de apertar o botao."
        except:
            info['text'] = "por favor selecione escreva um nick."
    elif len(a) > 16:
        print("O nick escolhido está incorreto.")
        info['text']= "O nick escolhido está incorreto.\nPor favor coloque o nick certo."

        
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
        janela.geometry('370x150')
        def a():
            janela.geometry('310x300')
            try:
                champion_id = top_3[0]["championId"]
                Maestria1 = top_3[0]["championLevel"]
                Pontos1 = top_3[0]["championPoints"]
                Bau1 = top_3[0]["chestGranted"]
                Maestria2 = top_3[1]["championLevel"]
                Champion2 = top_3[1]["championId"]
                Bau2 = top_3[1]["chestGranted"]
                Pontos2 = top_3[1]["championPoints"]
                Champion3 = top_3[2]["championId"]
                Bau3 = top_3[2]["chestGranted"]
                Pontos3 = top_3[2]["championPoints"]
                Maestria3 = top_3[2]["championLevel"]
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
                
                for text1 in ids1.get("gameName"):
                    text1 = f"O perfil pesquisado foi: {ids1['gameName']}#{ids1['tagLine']}\n"
                    text2 =f"A Sua maior maestria é com o champion: {get_champions_name(int(champion_id))}\nSua maestria é de nível {Maestria1}.\nCom {Pontos1:_} pontos de maestria.\nJá ganhou baú com este champion? {a}\nSua Segunda maior maestria é com o champion: {get_champions_name(int(Champion2))}\nSua maestria é de nível {Maestria2}.\nCom {Pontos2:_} pontos de maestria.\nJá ganhou baú com este champion? {d}\nSua Terceira maior maestria é com o champion: {get_champions_name(int(Champion3))}\nSua maestira é de nível {Maestria3}\nCom {Pontos3:_} pontos de maestria.\nJá ganhou baú com este champion? {f}\n"                
                    texto_maestrias["text"] = text2.replace("_", '.')
                    texto_orientacao["text"] = text1
                button.destroy()
                info['text']= '' 
            except:
                texto_maestrias["text"] = "O jogador pesquisado não possui todas as 3 maestrias..."


        texto_orientacao = Label(janela, text=f"Clique no botão abaixo para exibir as maestrias de {ids1['gameName']}#{ids1['tagLine']}", font=("Arial", 10), background="#242424", fg="white") 
        texto_orientacao.grid(column=0, row=4)

        regiao = Label(janela, text="A Região selecionada é {0}".format(l),bg = "#242424", fg="white")
        regiao.grid(column=0,row=5)
        button = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Exibir", command=a)
        button.place(relx=0.5, rely=0.5)
        button.grid(column=0, row=6)
        
        region_entry.destroy()
        nick_entry.destroy()
        botao.destroy()
        twitter.destroy()
        botaoNovaJanela.destroy()


        texto_maestrias = Label(janela, text="",bg = "#242424",  fg="white")
        texto_maestrias.grid(column=0   , row=7)
        

def set_text(text):
    nick_entry.insert(100,text)
    return


# Entry labels
region_entry = customtkinter.CTkEntry(janela,width=200, height=40, border_width=1, placeholder_text='Ex: br1, na1, kr, tr1, etc...', text_color='silver',justify='center')
region_entry.grid(row=3, column=0, padx=15, pady=5,columnspan=2, sticky=(W))
region_entry.place(x=8,y=50)

nick_entry = customtkinter.CTkEntry(janela, width=430, height=40, border_width=1, placeholder_text="Riot#ID", text_color="silver",justify='center')
nick_entry.grid(row=0, column=0, padx=10, pady=10,columnspan=3,sticky=(N))
nick_entry.place(x=8,y=0)
#Buttons
botaoNovaJanela = customtkinter.CTkButton(master=janela,width=100, height=20,border_width=3,border_color='#07060d', text="caracteres especiais",fg_color="#51087E",  command= lambda:openNewWindow())
botaoNovaJanela.place(x=140, y=120)

botao = customtkinter.CTkButton(master=janela, text="Buscar Maestrias",fg_color="#51087E",border_width=3,border_color='#07060d',  command=lambda: [nick_check(),region_check(), pegar_id()])
botao.place(x=135,y=150)

url= "https://twitter.com/rifuzada"
twitter = Label(janela, text="by @Rifuzada",background="#242424", fg="#116530")
twitter.place(x=165,y=180)
twitter.bind("<Button-1>", lambda e:open_url(url))

info = Label(janela, text="",background="#242424", fg="#116530")
info.grid(column=0, row=25)

janela.mainloop()

