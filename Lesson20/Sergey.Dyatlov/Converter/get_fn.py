#-*- coding: utf-8 -*-
"""
Диалог открытия файла
===============================================
Контрольная работа по курсу 'Введение в Python'
Дятлов Сергей
"""

# Фнкция открывает файлер Windows для выбора файла
# Возвращает текстовое занчение полного пути файла
# Входные параметры:
#	root 	- Корень файловой структуры откуда ничинать просмотр (пока не реализован)
#	msg		- Заголовок окна диалога

def get_fn(msg = u'Выберите файл'):
#		root
	root = None
	
	from win32com.shell import shell
#	import os

	flag = 0xFFFF	# Флаги полноты объектов выбора
					# Сейчас подняты все (методом тыка) надо найти описание

	try:
		pidl = shell.SHBrowseForFolder(0, root, msg, flag)
	except:
		print(u'Ошибка выбора файла')
		return None
	
	path = shell.SHGetPathFromIDList(pidl[0])
	return path


#print "%s" %get_fn()