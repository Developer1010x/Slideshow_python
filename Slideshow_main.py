import io
import os
import sys
import glob
import shutil
import tkinter as tk
from tkinter import *
from PIL import Image
from PIL import ImageTk
import PySimpleGUI as sg
from logging import shutdown
from tkinter import messagebox  
####################################################################################################################################
patta='SlideshowApp_images'
mark1="testImages"
if not os.path.exists(patta):
     messagebox.askokcancel("notice","  The image directory is either missing or could not be located. To keep the  images, a new folder is made.") 
     os.makedirs(patta)
     python = sys.executable
     os.execl(python, python, * sys.argv)
#
jetta=os.getcwd()
filename='SlideshowApp_images'
passat=os.path.join(jetta,filename)
polo=str(passat)
vento=str(passat)+"/*"
patha=str(passat)
#
def delaa():
    rapid=os.getcwd()
    filename='SlideshowApp_images'
    passat=os.path.join(rapid,filename)
    folder=str(passat)
    img_types = (".png", ".jpg", "jpeg", ".tiff", ".bmp")
    flist0 = os.listdir(folder)
    fnames = [f for f in flist0 if os.path.isfile(os.path.join(folder, f)) and f.lower().endswith(img_types)]
    num_files = len(fnames)                
    if num_files == 0:
        sg.popup('No files in folder')
        raise SystemExit()
    del flist0  

    def get_img_data(f, maxsize=(500, 500), first=False):
        img = Image.open(f)
        img.thumbnail((500,500))
        if first:                     
            bio = io.BytesIO()
            img.save(bio, format="PNG"or"JPG"or"JPEG")
            del img
            return bio.getvalue()
        return ImageTk.PhotoImage(img)
    filename = os.path.join(folder, fnames[0])
    image_elem = sg.Image(data=get_img_data(filename, first=True))
    filename_display_elem = sg.Text(filename, size=(90, 3))
    file_num_display_elem = sg.Text('File 1 of {}'.format(num_files), size=(25, 1))
    col = [[filename_display_elem],[image_elem],[sg.Button('Next', size=(4, 2)), sg.Button('Prev', size=(4, 2)), sg.Button('delete', size=(5, 2)), file_num_display_elem]]
    col_files = [[sg.Listbox(values=fnames, change_submits=True, size=(60, 30), key='listbox')],[sg.Button('Next', size=(8, 2)), sg.Button('Prev', size=(8, 2)), sg.Button('delete', size=(8, 2)), file_num_display_elem]] 
    layout = [[ sg.Column(col)]]
    window = sg.Window('Slideshow saved photos', layout, return_keyboard_events=False,location=(0, 0), use_default_focus=True)
    i = 0
    while True:
        event, values = window.read()
        print(event, values)
        if event == sg.WIN_CLOSED:
            break
        elif event in ('Next'):
            i += 1
            if i >= num_files:
                i -= num_files
            filename = os.path.join(folder, fnames[i])
        elif event in ('delete'):
            filename = os.path.join(folder, fnames[i])
            os.remove(filename) 
            i += 1
            python = sys.executable
            os.execl(python, python, * sys.argv)

        elif event in ('Prev'):
            i -= 1
            if i < 0:
                i = num_files + i
            filename = os.path.join(folder, fnames[i])
                   
        else:
            filename = os.path.join(folder, fnames[i])
    
        image_elem.update(data=get_img_data(filename, first=True))
        file_num_display_elem.update('File {} of {}'.format(i+1, num_files))
    window.close()
#
def Alll():
    def parse_folder(path):
        images = glob.glob(f'{path}/*.jpg') + glob.glob(f'{path}/*.png')+glob.glob(f'{path}/*.tiff')+glob.glob(f'{path}/*.raw')
        return images
    
    def load_image(path, window):
        try:
            image = Image.open(path)
            image.thumbnail((400, 400))
            photo_img = ImageTk.PhotoImage(image)
            window["image"].update(data=photo_img)
        except:
            messagebox.askretrycancel("Unable to open {path}!")
            
    def main():
        elements = [
            [sg.Image(key="image")],
            [
                sg.Text("Image File"),
                sg.Input(size=(25, 1), enable_events=True, key="file"),
                sg.FolderBrowse(),
            ],
            [
                sg.Button("Prev",size=(5, 1)),
                sg.Button("Next",size=(5, 1)),
                sg.Button("Save",size=(5, 1)),
                sg.Button("Exit",size=(5, 1)),
                sg.Button("update",size=(6, 1))
            ]
        ]
        window = sg.Window("Image Viewer", elements, size=(550, 500))
        images = []
        location = 0
        while True:
            event, values = window.read()
            if event == "Exit" or event == sg.WIN_CLOSED: 
                if 1+1==2:
                    break
            if event == "file":
                images = parse_folder(values["file"])
                if images:
                    load_image(images[0], window)
            if event == "Next" and images:
                if location == len(images) - 1:
                    location = 0
                else:
                    location += 1
                load_image(images[location], window)
            if event == "Prev" and images:
                if location == 0:
                    location = len(images) - 1
                else:
                    location -= 1
                load_image(images[location], window)
            if event == "Save" and images:
                if True:
                    src_dir = images[location]
                    dst_dir = polo
                    for jpgfile in glob.iglob(os.path.join(src_dir)):
                        shutil.copy(jpgfile, dst_dir) 
                else :
                    break    
            if event == "update":
                python = sys.executable
                os.execl(python, python, * sys.argv)

        window.close()
    if __name__ == "__main__":
        main() 
#
slider = Tk()
slider.title("Slider")
slider.overrideredirect(True)
slider.geometry("{0}x{1}+0+0".format(slider.winfo_screenwidth(), slider.winfo_screenheight()))
slider.config(bg="black")
slider.resizable(1,1)
ab = None
imgq=i = 0
paused = True
chit = []
#
for name in glob.glob(vento):
    val = name
    img= Image.open(val)
    pic_width = img.size[0]
    pic_height = img.size[1]
    real_aspect=pic_width/pic_height
    cal_width=int(real_aspect*900)
    load2=img.resize((cal_width,900))
    render = ImageTk.PhotoImage(load2)
    chit.append(render)
#
if len(chit)==0:   
    messagebox.showinfo("warning","!!! Add images !!!") 
    Alll()
#
def slide_show():
    global ab, imgq, paused
    if not paused:
        imgq = (imgq+1) % len(chit)
        lbl.config(image=chit[imgq])
    ab = slider.after(2000, slide_show)
#
def start():
    global ab, imgq, paused
    paused = False
    if ab:  
        slider.after_cancel(ab)
        ab = None
    slide_show()
#   
def pause():
    global ab, imgq, paused
    paused = True
#
def next():
    global i
    i=i+1
    lbl.configure(image = chit[i])
# 
def pervious():
    global i
    i=i-1
    lbl.configure(image = chit[i])
#
lbl = tk.Label(image=chit[imgq])
lbl.pack()
#
def deelll():
    print()
#
def dela():
    shutil.rmtree(patha)
    os.makedirs(patta)
    python = sys.executable
    os.execl(python, python, * sys.argv)
#
def Close():
    slider.destroy()
#
def UC():
    python = sys.executable
    os.execl(python, python, * sys.argv)
#
def shutdown():
    os.system("sudo shutdown -h now")
#    
menubar = Menu(slider)
file = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Photos Settings', menu = file)
file.add_command(label ='add photos ', command = Alll)
file.add_command(label ='Del Few photos ', command = delaa)
file.add_command(label ='clear all photos ', command = dela)
file.add_command(label ='Force_Updatechange', command = UC)
#
ss = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='Slideshow settings', menu = ss)
ss.add_command(label ='previous', command = pervious )
ss.add_command(label ='pause', command =pause)
ss.add_command(label ='next', command = next)
ss.add_command(label ='start', command = start)
#
Spn = Menu(menubar, tearoff = 0)
menubar.add_cascade(label ='utility', menu = Spn)
Spn.add_command(label ='Quit application', command = Close)
Spn.add_command(label ='shutdown PC ', command = shutdown)
#
slider.config(menu = menubar)
#
mainloop()
####################################################################################################################################