import requests
from id_champ import get_champions_name
from tkinter import *
import customtkinter
from chars import *
from PIL import Image
import io


def voltar1():
    janela.geometry(f"440x240+{x}+{y}")
    buttonvoltar1.place_forget()
    region_label.place(x=8, y=58)
    nick_label.place(x=8, y=0)
    region_combobox.place(x=5, y=75)
    nick_entry.place(x=5, y=15)   
    botaoNovaJanela.place(x=140, y=120)
    twitter.place(x=165, y=180)
    info1.place_forget()
    botao.place(x=135, y=150)
    

def voltar():
    janela.geometry(f"440x240+{x}+{y}")
    buttonvoltar.place_forget()
    info1.place_forget()
    buttonvoltar1.place_forget()
    region_label.place(x=8, y=58)
    nick_label.place(x=8, y=0)
    try:
        for label in image_labels:
            label.place_forget()
    except NameError:
        pass
    texto_orientacao.place_forget()
    regiao.place_forget()
    texto_maestrias.place_forget()
    buttonvoltar.place_forget()
    region_combobox.place(x=5, y=75)
    nick_entry.place(x=5, y=15)
    botaoNovaJanela.place(x=140, y=120)
    twitter.place(x=165, y=180)
    botao.place(x=135, y=150)
    
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
    global texto_orientacao, regiao, texto_maestrias
    buttonvoltar.place_forget()
    nick_label.place_forget()
    region_label.place_forget()
    region_combobox.place_forget()
    nick_entry.place_forget()
    botao.place_forget()
    botaoNovaJanela.place_forget()
    nick = ""
    nick = "%s" % nick_entry.get()#salva a info dada no label nick
    nick = nick.upper()
    nick = nick.replace('#', "/")
    region = ""
    region = "%s" %region_combobox.get()#salva a info dada no label region
    apikey = ""#Api key usada pela riot: https://developer.riotgames.com/
    ids1 = requests.get(f"https://americas.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{nick}?api_key={apikey}")#request para conseguir os ids
    ids1 = ids1.json()#transforma o request no json que ele responde
    puuid = ids1["puuid"]#puxa o id que precisa do request ids1
    mastery = requests.get(f"https://{region}.api.riotgames.com/lol/champion-mastery/v4/champion-masteries/by-puuid/{puuid}?api_key={apikey}")#request para puxar maestrias
    top_3 = mastery.json()
    texto_orientacao = customtkinter.CTkLabel(janela, text=f"Clique no botão abaixo para exibir as maestrias de {ids1['gameName']}#{ids1['tagLine']}", font=("Arial", 13), fg_color=("white", "#242424"),corner_radius=8)
    twitter.place(x=155, y=120)
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
    janela.geometry('420x240')
    def display_masteries():
        global image_label
        global image_labels

        if not top_3:
            info1.place(x=50, y=50)
            texto_orientacao.place_forget()
            button.place_forget()
            regiao.place_forget()
            info1.configure(text= "Nenhuma maestria a ser mostrada.\n verifique a regiao e riot ID selecionados.",text_color="#ff0019",font=("Arial", 20))
            buttonvoltar.place(x=5, y=180)
            buttonvoltar.lift()
            buttonvoltar.configure(state="normal")
            janela.geometry('420x240')
            twitter.place(x=150, y=210)
        else:
            try:
                # Get mastery information
                mastery_info = []
                champions = []
                images = []  # Collect all the images

                # Iterate over the top 3 masteries
                for i in range(min(3, len(top_3))): 
                    mastery = top_3[i]
                    champion_id = mastery["championId"]
                    level = mastery["championLevel"]
                    points = mastery["championPoints"]
                    chest_granted = "Sim" if mastery["chestGranted"] else "Não"
                    mastery_info.append((champion_id, level, points, chest_granted))
                    champions.append(champion_id)

                # Iterate over champions to fetch their images
                for champion_id in champions:
                    # Construct the URL for the champion icon
                    url = f"https://raw.communitydragon.org/latest/plugins/rcp-be-lol-game-data/global/default/v1/champion-icons/{champion_id}.png"
                    
                    # Send a GET request to the URL
                    response = requests.get(url)

                    if response.status_code == 200:
                        # Convert the content to an image
                        image_bytes = response.content
                        image = Image.open(io.BytesIO(image_bytes))
                        images.append(image)  # Collect the image

                # Display the images
                image_labels = []
                for idx, image in enumerate(images):
                    champion_image = customtkinter.CTkImage(light_image=image, size=(30,30))
                    image_label = customtkinter.CTkLabel(janela, image=champion_image, text="")
                    image_label.place(x=360, y=40 + idx * 50)  # Adjust the y-coordinate for each image
                    image_labels.append(image_label)
                # Build text for display
                text1 = f"O perfil pesquisado foi: {ids1['gameName']}#{ids1['tagLine']}\n"
                text2 = ""
                for info in mastery_info:
                    champion_name = get_champions_name(info[0])
                    text2 += f"Sua maestria com {champion_name} é de nível {info[1]} com {info[2]:_} pontos.\nJá ganhou baú? {info[3]}\n\n"
                text2 = text2.replace("_", '.')
                texto_orientacao["text"] = text1
                texto_maestrias.configure(text=text2)
                texto_maestrias.place(x=5,y=50)
                regiao.place(x=120,y=20)
                buttonvoltar.place(x=5, y=180)
                buttonvoltar.lift()
                button.place_forget()
                info1['text'] = ''
            except (KeyError, IndexError) as e:
                texto_maestrias["text"] = "O jogador pesquisado não possui todas as 3 maestrias..."

    
    texto_orientacao.place(x=5, y=0)

    regiao = customtkinter.CTkLabel(janela, text="A Região selecionada é {0}".format(region1), fg_color=("white", "#242424"),corner_radius=8)
    regiao.place(x=120,y=40)
    button = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Exibir", command=display_masteries)
    button.place(x=130, y=70)



    texto_maestrias = customtkinter.CTkLabel(janela, text="", fg_color=("white", "#242424"), justify="left",corner_radius=8)
    texto_maestrias.place(x=9999   , y=7)


janela.bind('<Return>', lambda event: [nick_check(), pegar_id()])
botao = customtkinter.CTkButton(master=janela, text="Buscar Maestrias", fg_color="#51087E", border_width=3, border_color='#07060d', command=lambda: [nick_check(), pegar_id()])
botao.place(x=135, y=150)

buttonvoltar = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Voltar", command=voltar)
buttonvoltar1 = customtkinter.CTkButton(master=janela,fg_color="#51087E", text="Voltar", command=voltar1)


janela.mainloop()
