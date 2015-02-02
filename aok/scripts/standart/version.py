#-*- coding:utf-8 -*-
__author__ = 'Detonavomek'


'''
 TO DO add_version
 на вході currentVersion - string, типу '1.0'
 на виході - string, типу '1.0', який на 0.1 змінений від попереднього значення
 Приклади:
 '1.0' -> '1.1'
 '1.5' -> '1.6'
 '1.9' -> '2.0'
 '5.2' -> '5.3'
'''

def add_version(currentVersion):
    return str(float(currentVersion)+0.1)

