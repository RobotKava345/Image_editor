from PIL import Image, ImageFilter, ImageEnhance
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMainWindow, QMessageBox, QListWidgetItem
from qt_material import apply_stylesheet
import sys



#with Image.open("silas-schneider-BBoq3MaPNoM-unsplash.jpg") as img:
    #print("Розмір:", img.size)
    #print("Формат:", img.format)
    #print("Тип:", img.mode)

    #black_img = img.convert("L") # перетвор на ЧБ
    #black_img.show()
    #name = img.filename.split(".")[0]
    #black_img.save(name+"_black.jpg")
    #blur_image = img.filter(ImageFilter.BLUR)
    #blur_image.save(name+"_blur.jpg")

    #rotate_img = img.transpose(Image.ROTATE_90)
    #rotate_img.save("rotate.jpg")
    #rotate_img.show()
    #sharpen_image = img.filter(ImageFilter.SHARPEN)
    #sharpen_image.save("sharpen.jpg")

    #bright_obj = ImageEnhance.Brightness(img) #підсилювач яскр
    #bright_img = bright_obj.enhance(2) # підсил яскр до 2
    #bright_img.show()

    #contraster = ImageEnhance.Contrast(img)
    #contrast_img = contraster.enhance(2)
    #contrast_img.show()

    #color_img = ImageEnhance.Color(img).enhance(2) #Насиченість кольору
    #color_img.show()


class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__()
        uic.loadUi('window.ui', self)
        

class ImageEditor(QtWidgets.QMainWindow):
    def __init__(self):
        self.image = None
        self.original = None
        self.save_path = 'edited/'
        self.ui = Ui()
        self.ui.show()
        
    
    def open(self, filename):
        self.image = Image.open(filename)
        self.original = self.image

    def do_black_white(self):
        self.image = self.image.convert("L")

    def do_blur(self):
        self.image = self.image.filter(ImageFilter.BLUR)

    def rotate_90(self):
        self.image = self.image.transpose(Image.ROTATE_90)

    def sharpen(self):
        self.image = self.image.filter(ImageFilter.SHARPEN)


app = QApplication([])
editor = ImageEditor()
apply_stylesheet(app, theme='dark_teal.xml')
app.exec_()