from tkinter.scrolledtext import ScrolledText
from PIL import Image
import ImageProcessing
import serialCommunication
import os,time
from tkinter import *
from tkinter import filedialog
from text2png import *
def TkinterClear(root):
    for widget in root.pack_slaves():
        widget.destroy()
def PrintTime(text=False):
    ImageProcessing.process_image('image.png',text)
    serialCommunication.printImage()
def textFileLoad(textoEntrada):
    archivotxt=filedialog.askopenfilename(initialdir = current_dir,title = "Select a text file",filetypes = (("txt files","*.txt"),("all files","*.*")))
    with open(archivotxt, encoding="utf-8") as f:
        textoEntrada.delete("1.0",END)
        textoEntrada.insert(END,f.read())
def TextoAImg(texto,size):
    try:
        fuentesize=int(size)
    except:
        fuentesize=13
    lines=texto.split("\n")
    print("Max: ",max(lines,key=len))
    print("Len: ",len(max(lines,key=len)))
    text2png(texto,current_dir+"\\image.png",width=160,fontfullpath="Pokemon_GB.ttf",fontsize=fuentesize)
def textFile(root):
    TkinterClear(root)
    root.geometry("400x400")
    title=Label(root,text="Text",font=("Pokemon GB",20))
    title.pack(pady=5)
    textoEntrada=ScrolledText(root,height=10,width=50)
    textoEntrada.pack(pady=5)
    textoEntrada.focus_set()
    fuenteLabel=Label(root,text="Enter font size here",font=("Pokemon GB",10))
    fuenteLabel.pack(pady=5)
    fuenteEntry=Entry(root)
    fuenteEntry.pack(pady=5)
    fileBoton=Button(root,text="Load text file",command=lambda:textFileLoad(textoEntrada))
    fileBoton.pack(pady=5)
    enviarTexto=Button(root,text="Print",command=lambda:[TextoAImg(textoEntrada.get("1.0",END),fuenteEntry.get()),PrintTime(True)])
    enviarTexto.pack(pady=5)
    volverBoton=Button(root,text="Return",command=lambda:MainMenu(root))
    volverBoton.pack(pady=5)
def ImgFile(root):
    filearchivo=filedialog.askopenfilename(initialdir = current_dir,title = "Select an image",filetypes = (("png files","*.png"),("jpg files","*.jpg"),("all files","*.*")))
    img = Image.open(filearchivo)
    imgpng=img.save(current_dir+'\\image.png')
    PrintTime()
def MainMenu(root):
    TkinterClear(root)
    title=Label(root,text="GB printing",font=("Pokemon GB",20))
    title.pack(pady=5)
    botonforText=Button(root,text="Print text (experimental)",command=lambda:textFile(root))
    botonforText.pack(pady=5)
    botonforImg=Button(root,text="Print image",command=lambda:ImgFile(root))
    botonforImg.pack(pady=5)
    botonExit=Button(root,text="Exit",command=root.destroy)
    botonExit.pack(pady=5)
current_dir = os.path.dirname(os.path.abspath(__file__))
root=Tk()
root.geometry("300x200")
root.title("GB printer")
MainMenu(root)
root.mainloop()
