# Разработать фрагмент программы с использованием библиотеки pyqrcode, позволяющей
# создавать изображение QR-кода на основе переданной в программу текстовой строки.

import pyqrcode

img = pyqrcode.create(input('Введите текст:\t'))
img.svg('your_text.svg')