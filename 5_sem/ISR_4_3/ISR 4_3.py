# Реализовать модификацию изображения генерируемого QR-кода: раскрасить фрагменты
# изображения в несколько случайно определяемых цветов.

import pyqrcode
import random

data = pyqrcode.create(input('Введите текст:\n'))
data.png('code.png', scale=6, module_color=[random.randrange(256), random.randrange(256), random.randrange(256)])
