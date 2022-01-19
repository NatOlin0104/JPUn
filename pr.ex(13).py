# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 19:53:52 2021

@author: HP
"""

def ex_1_1(filename):
    
    str_1 = (input("enter elements(file must contain numbers) in \" \" :")).split()
    fh = None
    try:
        fh = open(filename,'w', encoding='utf-8')
        
        # запись в файл
        for elem in str_1:
            print(elem, file=fh)
    except Exception as e:
        print("error with your file:", e)
    finally:
        if fh:
            fh.close()
            
    pass

def ex_1_2(filename):
    
    fh = None 
    try:
        with open(filename, encoding='utf-8') as fh:
            # чтение из файла
            file_line = fh.readlines()
            with open(filename, 'a', encoding='utf-8') as fh:
                summ = min_elem = 0
                # поиск минимального числа и общей суммы
                for elem in file_line:
                    elem = float(elem)
                    summ += elem
                    if min_elem != 0:
                        if elem < min_elem:
                            min_elem = elem
                    else:
                        min_elem = elem
                
                # округление суммы до формата 2 знака после запятой
                summ = round(summ, 2) 
                # запись элементов в файл
                print(str(summ), file=fh)
                print(str(min_elem), file=fh)
        
    except Exception as e:
        print("error with your file:", e)
    finally:
        if fh:
            fh.close()
            
    pass
            
def ex_1_3(filename):
    fh = None 
    try:
        with open(filename, encoding='utf-8') as fh:
            # чтение из файла
            file_line = fh.readlines()
            with open(filename, 'a', encoding='utf-8') as fh:
                summ = min_elem = 0
                
                for i in range(len(file_line)):
                    try:
                        # поиск минимального числа и общей суммы
                        elem = float(file_line[i])
                        summ += elem
                        if min_elem != 0:
                            if elem < min_elem:
                                min_elem = elem
                        else:
                            min_elem = elem 
                    # пропуск элементов не являющихся числами
                    except Exception:
                        i += 1
                # проверка изменения значения суммы
                # (т.к. она является основным показателем содержания чисел)
                if summ != 0:
                    # округление суммы до формата 2 знака после запятой
                    summ = round(summ, 2)
                    #запись элементов в файл
                    print(str(summ), file=fh)
                    print(str(min_elem), file=fh)
                else:
                    print("your file don't contain numbers!")
                    
    except Exception as e:
        print("error with your file:", e)
    finally:
        if fh:
            fh.close()
    
    pass

def ex_1_4(filename):
    
    fh = None
    try:
        fh = open(filename, encoding='utf-8')
        # создаем список гласных букв, знаков и счетчики букв
        vowels = ("А", "Е", "Я", "О", "У", "Ю", "Ы", "И", "Э", "Ё")
        signs = ("!", "?", ".", ",", "-", ":", ";", "\"", "(", ")")
        summ_v = summ_c = 0
        for line in fh:
            # считываем построчно из файла и разбиваем на слова
            print(line)
            line = line.split()
            # выделяем первые буквы слов для проверки
            for i in range(len(line)):
                word = list(line[i])
                letter = str(word[0])
                letter = letter.upper()
                # увеличиваем счетчики гласных и согласных букв соответственно
                if letter in vowels:
                    summ_v += 1
                # дополнительная проверка на знаки препинания
                elif letter not in signs:
                    summ_c += 1
        # сравниваем величины счетчиков          
        if summ_c > summ_v:
            print("\nwords begging with a consonant a lot of w.b.w a vowel!:")
        elif summ_c == summ_v:
            print("\nthe same number of words beginning with a consonant ana a vowel!:")
        else:
            print("\nwords begging with a vowel a lot of w.b.w a consonant!:")
        # выводим их значения
        print("con. = ", summ_c, "; vow. = ", summ_v)
        
    except Exception as er:
        print("error with your file:", er)
    finally:
        if fh:
            fh.close()
            
    pass

def ex_1_5(filename):
    
    fh = None
    try:
        fh = open(filename, encoding='utf-8')
        line = fh.readline().split()
        parties = [["Партия №1", 1], ["Партия №2", 2],
                   ["Партия №3", 3], ["Партия №4", 4],
                   ["Партия №5", 5], ["Испорченный бланк", -1]]
        try:
            for i in range(len(line)):
                elem = int(line[i])
                print(elem)
                for par in parties:
                    summ = 0
                    par.append(summ)
                    for num in range(len(par)):
                        num = par[1]
                        if elem == num:
                            summ += 1
                            par[summ] = summ
                    print(par)
        
        except Exception:
            elem = -1
            i += 1
    except Exception as er:
        print("error with your file:", er)
    finally:
        if fh:
            fh.close()
            
    pass

filename = input("enter the name of your file:")
#ex_1_1(filename)
#ex_1_2(filename)
#ex_1_3(filename)
#ex_1_4(filename)
ex_1_5(filename)