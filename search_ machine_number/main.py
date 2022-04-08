import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl


img = cv2.imread('images/1.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#Привести к серому цвету

#изображение(только серый формат), надо поиграть, надо поиграть
img_filter = cv2.bilateralFilter(gray, 11, 15, 15)

#создать контуры изображения
edges = cv2.Canny(img_filter, 30, 200)

#найти контуры
cont = cv2.findContours(edges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

#считать все контуры
cont = imutils.grab_contours(cont)

#поиск квадратных контуров(2 параметр) выбираем последние 8 элементов
cont = sorted(cont, key=cv2.contourArea, reverse=True)[:8]

#поиск номера
pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)#2 параметр надо поиграть
    if len(approx) == 4:# это для номера 4 координаты
        pos = approx
        break

#размер полотна будет gray.shape
mask = np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)#метод рисует контуры, где рисует, 255 это цвет, -1 обводка
bitwise_img = cv2.bitwise_and(img, img, mask=mask)#тут применяю битовые операции

#получаю номер
(x, y) = np.where(mask==255)
(x1, y1) = np.min(x), np.min(y)
(x2, y2) = np.max(x), np.max(y)
crop = gray[x1:x2, y1:y2]


#для чтения информации с номерного знака
text =easyocr.Reader(['en'])
text = text.readtext(crop)#получаю из картинки текст

#вывод текста над номером
res = text[[0][-2]]
final_image =cv2.putText(img, res, (x1 - 200, y2+160), cv2.FONT_HERSHEY_SIMPLEX, 3, (0, 0, 255), 1)
final_image = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)#рисую квадратик


pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))#вывести картинку, конвертнуть что бы правильно отображались цвета()
pl.show()

