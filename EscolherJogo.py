import tkinter as tk
from tkinter import *
import os
import shutil
from gtts import gTTS
from playsound import playsound


tinicial = tk.Tk()
tinicial.geometry("800x500+200+100")
tinicial.title("Escolher Pes 06 - SIS")
tinicial.resizable(width=False, height=False)
tinicial['bg'] = '#49A'
tinicial.iconphoto(True, PhotoImage(file='./arquivos/pes2.png'))
image=PhotoImage(file='./arquivos/pes.png')

caminhoinicial = './conversas'
files = os.listdir(caminhoinicial)

files_mp3 =[caminhoinicial + '\\' + f for f in files if f[-3:]== 'mp3']

for f in files_mp3:
    os.remove(f)


os.startfile(r'E:\PES6\MOTIONJOY\MotioninJoy\ds3\DS3_Tool.exe')
Konamicaminho = r"C:\Users\Marciel\Documents\KONAMI\Pro Evolution Soccer 6\save\folder1"
Optionbr = r"E:\PES6\PC PES 6 BR\Option"
OptionVbr = r"E:\PES6\PES6_VBR Patch_2021\Option"
sisteminha = os.path.abspath(os.path.dirname(__file__))

def pesvbr():
	files = os.listdir(Konamicaminho)
	filesarquivo =[Konamicaminho + '\\' + f for f in files]
	for f in filesarquivo:
		os.remove(f)
	for root, dirs, arquivos in os.walk(OptionVbr):
		for f in arquivos:
			caminho = os.path.join(root, f)
			shutil.copy(caminho, Konamicaminho)
	os.chdir(sisteminha)
	pesvbr = gTTS("Jogue o PES VBR", lang="pt")
	pesvbr.save("./conversas/pesvbr.mp3")
	pesvbr = "./conversas/pesvbr.mp3"
	playsound(pesvbr)
	os.chdir("E:\PES6\PES6_VBR Patch_2021")
	os.startfile(r'E:\PES6\PES6_VBR Patch_2021\PES6_VBR_Patch_2021.exe')
	btnoptpesbr['state'] = tk.DISABLED
	btnoptpesvbr['state'] = tk.NORMAL
	btnpessair['state'] = tk.DISABLED
	#os._exit(1)

def pesbr():
	#files = os.listdir(Optionbr)
	files = os.listdir(Konamicaminho)
	filesarquivo =[Konamicaminho + '\\' + f for f in files]
	for f in filesarquivo:
		os.remove(f)
	for root, dirs, arquivos in os.walk(Optionbr):
		for f in arquivos:
			caminho = os.path.join(root, f)
			shutil.copy(caminho, Konamicaminho)
			os.chdir(sisteminha)
			pesbr = gTTS("Jogue o PES BR", lang="pt")
			pesbr.save("./conversas/pesbr.mp3")
			pesbr = "./conversas/pesbr.mp3"
			playsound(pesbr)
			os.chdir("E:\PES6\PC PES 6 BR")
			os.startfile(r'E:\PES6\PC PES 6 BR\PES6.exe')
			btnoptpesbr['state'] = tk.NORMAL
			btnoptpesvbr['state'] = tk.DISABLED
			btnpessair['state'] = tk.DISABLED
			#os._exit(1)

def optpesbr():
	files = os.listdir(Optionbr)
	filesarquivo =[Optionbr + '\\' + f for f in files]
	for f in filesarquivo:
		os.remove(f)
	for root, dirs, arquivos in os.walk(Konamicaminho):
		for f in arquivos:
			optcaminho = os.path.join(root, f)
			shutil.copy(optcaminho, Optionbr)
			os.chdir(sisteminha)
			salpesbr = gTTS("Salvo o PES BR", lang="pt")
			salpesbr.save("./conversas/salpesbr.mp3")
			salpesbr = "./conversas/salpesbr.mp3"
			playsound(salpesbr)
			btnpessair['state'] = tk.NORMAL
			#btnpesvbr['state'] = tk.DISABLED
				

def optpesvbr():
	files = os.listdir(OptionVbr)
	filesarquivo =[OptionVbr + '\\' + f for f in files]
	for f in filesarquivo:
		os.remove(f)
	for root, dirs, arquivos in os.walk(Konamicaminho):
		for f in arquivos:
			optcaminho = os.path.join(root, f)
			shutil.copy(optcaminho, OptionVbr)
			os.chdir(sisteminha)
			salpesvbr = gTTS("Salvo o PES VBR", lang="pt")
			salpesvbr.save("./conversas/salpesvbr.mp3")
			salpesvbr = "./conversas/salpesvbr.mp3"
			playsound(salpesvbr)
			btnpessair['state'] = tk.NORMAL
			#btnpesbr['state'] = tk.DISABLED


	#print (filesarquivo)
	#print("Pes BR")

def saindo():
	files = os.listdir(Konamicaminho)
	filesarquivo =[Konamicaminho + '\\' + f for f in files]
	for f in filesarquivo:
		os.remove(f)
	os._exit(1)

def abrirsentings():
	os.startfile(r'E:\PES6\PES6_VBR Patch_2021\\settings.exe')
def abrirsentingsbr():
	os.startfile(r'E:\PES6\PC PES 6 BR\\settings.exe')




campointervalo = tk.Label(tinicial, width=800,height=500,image=image, bd=3,fg='black',bg = 'white', font=('arial',10,'bold'))
campointervalo.grid(rowspan=16,columnspan =5)


btnpesbr =tk.Button(tinicial, width=10,height=1,bd=8,underline=7,bg="Goldenrod",text="Pes 06 BR",command=pesbr,font=('Times',18,'bold'))
btnpesbr.place(relx=0.45,rely=0.6)
#campointervalo.insert(0,7)

btnoptpesbr =tk.Button(tinicial, width=13,height=1,bd=8,underline=7,bg="Goldenrod",text="OPT Pes 06 BR",command=optpesbr,font=('Times',18,'bold'))
btnoptpesbr.place(relx=0.7,rely=0.6)
btnoptpesbr['state'] = tk.DISABLED

btnpesvbr =tk.Button(tinicial, width=10,height=1,bd=8,bg="Goldenrod",underline=7,text="Pes 06 VBR",command=pesvbr,font=('Times',18,'bold'))
btnpesvbr.place(relx=0.45,rely=0.4)

btnoptpesvbr =tk.Button(tinicial, width=13,height=1,bd=8,bg="Goldenrod",underline=7,text="OPT Pes 06 VBR",command=optpesvbr,font=('Times',18,'bold'))
btnoptpesvbr.place(relx=0.7,rely=0.4)
btnoptpesvbr['state'] = tk.DISABLED

btnpessair =tk.Button(tinicial, width=10,height=1,bd=8,bg="Goldenrod",underline=0,text="Sair",command=saindo, font=('Times',18,'bold'))
btnpessair.place(relx=0.45,rely=0.8)

btnconfig =tk.Button(tinicial, width=5,height=1,bd=8,bg="Goldenrod",underline=0,text="C. VBR",command=abrirsentings, font=('Times',18,'bold'))
btnconfig.place(relx=0.70,rely=0.8)

btnconfig =tk.Button(tinicial, width=5,height=1,bd=8,bg="Goldenrod",underline=0,text="C. BR",command=abrirsentingsbr, font=('Times',18,'bold'))
btnconfig.place(relx=0.84,rely=0.8)

voz = gTTS("Olá. Aqui você define se joga PES 6 VBR ou PES 6 BR ", lang="pt")
voz.save("./conversas/voz.mp3")
falar = "./conversas/voz.mp3"
playsound(falar)

tinicial.mainloop()

