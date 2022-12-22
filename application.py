from numpy import *
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tkinter import *
from PIL import ImageTk, Image  
from tkinter import filedialog 
from tkinter.ttk import * 



def wrt(st,fname):
    file = open(fname,"w+")
    file.write(st)
    file.close() 



def red(fname):    
    file = open(fname,"r")
    f=file.read()
    file.close() 
    return f
 

def open_img():
   try: 
      x = openfilename()
      wrt(x,"upload");print(x);
      img =Image.open(x)
   except:
      x = 'error.png'
      print(x);
      img =Image.open(x)
   img = img.resize((325, 200), Image.ANTIALIAS) 
   img = ImageTk.PhotoImage(img) 
   panel = Label(root, image = img) 
   panel.image = img 
   panel.place(x=750, y=250)
    
    
    
def openfilename(): 
   filename = filedialog.askopenfilename(title ='UPLOAD IMAGE') 
   return filename 



def callback():  
  cell="\n IMAGE FILE NOT UPLOADED..."  
  try:
    model = load_model('a95e30model.h5')
    #model.summary()
    test_image=image.load_img(red("upload"),target_size=(50,50,3))
    #imgplot = plt.imshow(test_image)
    #plt.show()
    test_image=image.img_to_array(test_image)
    test_image=expand_dims(test_image,axis=0)
    result = model.predict(test_image)
    cell="PARASITIZED" if result[0][1]==1 else "UNINFECTED"
    output.set("\n "+cell+" CELL DETECTED !\n");print(cell)
  except:
    output.set(cell);print("EXCEPTION")
    
    
    
root = Tk() 
root.title("Sahaj") 
output=StringVar();
root.attributes('-fullscreen',True)

#root.geometry("1920x1080")
#root['bg'] = "magenta"

background = Image.open("cover2.png")
background = background.resize((1920,1080),Image.ANTIALIAS)
background = ImageTk.PhotoImage(background)
Label(root,image = background).place(x=0, y=0)

root.resizable(width = True, height = True) 

img =Image.open("input1.png")
img = img.resize((325, 200), Image.ANTIALIAS) 
img = ImageTk.PhotoImage(img) 
panel = Label(root, image = img) 
panel.image = img 
panel.place(x=750, y=250)

#upload = PhotoImage(file = r"upload1.png")
upload =Image.open("upload1.png")
upload = upload.resize((325, 200), Image.ANTIALIAS) 
upload = ImageTk.PhotoImage(upload)
Button(root, text = "upload",image = upload,
             command = open_img).place(x=350, y=250)


Label(root, text="\n                  OUTPUT\n",
           width=25,
           font=("Comic Sans Ms 93", 20)).place(x=750, y=600)
Label(root, text="",textvariable = output,
                    font=("Comic Sans Ms 93", 20)).place(x=750, y=600)


#detect = PhotoImage(file = r"detect.png")
detect =Image.open("detect1.png")
detect = detect.resize((325, 200), Image.ANTIALIAS) 
detect = ImageTk.PhotoImage(detect)
Button(root, text="detect",image = detect,
                            command = callback).place(x=350,y=600)


#close = PhotoImage(file = r"close1.png")
close =Image.open("close.png")
close = close.resize((100, 100), Image.ANTIALIAS) 
close = ImageTk.PhotoImage(close)
Button(root, text = "close",image = close,
                            command = root.destroy).place(x=0,y=0) 


root.mainloop()