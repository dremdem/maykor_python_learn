#-*- coding: utf-8 -*-
"""
Конвертер НСИ точек измерения подстанции
в файл НСИ ИК БЛиК
===============================================
Контрольная работа по курсу 'Введение в Python'
Дятлов Сергей
"""

# Функция формирования строки выходной таблицы
def makerow(row, ti_ps, blik):
	pol = ['' for c in range(0,66)]
#	print len(pol), pol
	pol[0] = row - 1
	pol[1] = ti_ps.range(row,1).value[:3]
	pol[2] = ti_ps.range(row,1).value[:6]	# ?уточнить
	pol[3] = ti_ps.range(row,11).value
	pol[4] = ti_ps.range(row,7).value
	pol[5] = ti_ps.range(row,8).value
	pol[6] = ti_ps.range(row,5).value
	pol[7] = ti_ps.range(row,6).value
	pol[8] = ti_ps.range(row,4).value
#	pol[9:15] = ' '
	pol[16] = ti_ps.range(row,10).value
	pol[17] = ti_ps.range(row,9).value
#	pol[18:21] = ' '
	pol[22] = ti_ps.range(row,3).value
	pol[23] = ti_ps.range(row,1).value
	pol[24] = ti_ps.range(row,28).value
	pol[25] = ti_ps.range(row,27).value
	pol[26] = ''							# ?уточнить
	pol[27] = ''							# ?уточнить
	pol[28] = ''							# ?уточнить
	pol[29] = ''							# ?уточнить
	pol[30] = ''							# ?уточнить
	pol[31] = ti_ps.range(row,29).value
	pol[32] = ''							# ?уточнить
	pol[33] = ti_ps.range(row,26).value
#	pol[34:35] = ''
	pol[36] = ti_ps.range(row,19).value
	pol[37] = ti_ps.range(row,22).value
	pol[38] = ti_ps.range(row,24).value
#	pol[39:44] = ''
	pol[45] = ti_ps.range(row,13).value
	pol[46] = ti_ps.range(row,14).value
#	pol[47:48] = ''
	pol[49] = ti_ps.range(row,17).value
	pol[50] = ti_ps.range(row,23).value
#	pol[51:52] = ''
#	print len(pol), pol
	pol[53] = ti_ps.range(row,16).value
	pol[54] = ''
	pol[55] = ti_ps.range(row,20).value
#	pol[56:62] = ''
	pol[63] = ti_ps.range(row,25).value
	pol[64] = ti_ps.range(row,12).value
#	pol[65:66] = ''
	blik.range(row+2,1).value = pol

##########################################

#import openpyxl
#from openpyxl import Workbook
import os
import shutil
import xlwings as xw
from get_fn import get_fn

# Должна открываться экранная форма с кнопками выбора файлов
# и старта конвертера.
# Времени разобраться с QT не хватило. Пока стоит заглушка 
# Оставлено на последующую доработку

print (u'\t\tФорма диалога пока в стадии разработки')
print (u'\t\tПриношу извинения за временные неудобства')
print (u'\t\t*****************************************')
#print (u'\n\t\tВыберите исходный файл ведомости НСИ')

try:
	fpath = get_fn(u'Выберите файл исходной ведомости НСИ')
	print (u'\n\t\tВыбран файл ведомости НСИ:\n')
	print "%s" %fpath
except:
	print(u'\n\t\tИсходный файл не выбран')
else:
	
#	Выделяем имя папки и имя файла
	parts = fpath.split('\\')
	fnam = parts[-1]
	fold = fpath[:-len(fnam)]
	
#	Формируем имя выходного файла
	ofpath = fold+'Blik_NSI_'+fnam

#	Проверяем, лежит ли в рабочей папке шаблон заголовка, 
#	если нет - запрашиваем путь к нему
	pfpath = fold+'Header_for_Blik.xlsx'
	
	if not os.path.isfile(pfpath):
		try:
			pfpath = get_fn(u'Укажите файл заголовка БЛиК')
			print (u'\n\t\tВыбран файл заголовка БЛиК:\n')
			print "%s" %pfpath
		except:
			print(u'\n\t\tФайл заголовка БЛиК не выбран')
			pfpath = ''
#	Проблема! Не останавливается по исключению. Надо разлбраться			

#	Копируем заголовок в выходной файл
	shutil.copyfile(pfpath, ofpath)

# 	Открываем исходный файл и рабочие листы
	try:
		ib = xw.Book(fpath)
		ti_ps = ib.sheets[u'ТИ_ПС']	# на русские имена ругается, но работает
#		tp = ib.sheets[u'ТП']	# на русские имена ругается, но работает
	except:
		pass

#	Открываем выходной файл и рабочий лист
	try:
		ob = xw.Book(ofpath)
		blik = ob.sheets[u'Лист1']
	except:
		pass

	for row in range(2,100000):
		val = ti_ps.range(row,1).value
#		print row, val
		if val == None: break
		makerow(row, ti_ps, blik)
			 
	print u'\n Работа завершена\n Обработано точек измерения: ', row-2
 
#wb = Workbook()
#ws = wb.active

# Заголовок
#ws.append(['Path', 'File_Name', 'Size (Bytes)'])
#row = []
#for fn in cat:
#	catsiz[fn] = os.path.getsize(path+'\\'+fn)
#	row = [path, fn, catsiz[fn]]
	#print (row)
#	ws.append(row)

#print (catsiz.values())

#last_cel = 'C'+ str(len(cat) +1)
#print (last_cel)

#wb.save("f_catalog.xlsx")

#ws.auto_filter.ref = 'A1:' + last_cel
#ws.auto_filter.add_sort_condition("C2:" + last_cel)
	
#wb.save("f_catalog.xlsx")

#app = Application().start("Excel.exe")

#	send_mail('sergey.dyatlov@maykor.com', 'Test e-mail', 'This is test message')
	
#except:
	#print(u'Ошибка отправки почты')

