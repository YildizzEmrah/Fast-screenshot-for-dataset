
from tkinter import *
import time
import tkinter
from PIL import ImageTk, Image
import pyautogui as pg
import time

win = Tk()

win.geometry("350x120")

def screenshot():
      #bing mapsda gerek yok yoruma alınabilir.
   pg.click(button='left')
   for a in range(5):
      # Kaç defa yön tuşuna basılmasını istiyorsanız.
       for x in range(20):
           #Yön tuşlarından hangisi seçmek isterseniz.
            pg.press('right')
          #Maps yüklenmeme durumu var hemen hareket ettirirken ( Maps yüklenmesi için beklenilecek süre internete ve bilgisayara bağlı düşürülebilir ya da yorum satırına alınabilir.)  
       time.sleep(2.5)
       random = int(time.time())
        # Orjinal alınan screenshot yolu.
       filename = "F:/Bing Dataset/" + str(random) + ".jpg"
       ss = pg.screenshot(filename)
       # ss.show()
       im = Image.open(filename)

         # Ekranda nasıl bir yerin ss ini almak istiyorsanız ona göre ayarlayın. (1920 x 1080 'in neredeyse tam ortasından 1024x1024 olarak alır.)
       cropped = im.crop((448,28,1472,1052))
         #Croplanmış halinin yolu.
       cropped.save('F:/Bing Dataset/Crop Dataset/' + str(random)+".jpg")

   win.deiconify()


def hide_window():
   win.withdraw()
   win.after(1000, screenshot)

button = Button(win, text="Start process", font=('Aerial 11 bold'), background="black", foreground="white",command=hide_window)
win.title('Image capture for Dataset')
button.pack(pady=20)

win.mainloop()
