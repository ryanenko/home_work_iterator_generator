##Задание 1

###Доработать класс FlatIterator в коде ниже. 
###Должен получиться итератор, который принимает список списков и возвращает их плоское представление, 
###т.е последовательность состоящую из вложенных элементов. Функция test в коде ниже также должна отработать без ошибок.
       
       

class FlatIterator:
    def __init__(self, lst):        
        self.lst = lst
        self.cursor = -1


    def __iter__(self):
        self.cursor += 1
        self.next_cursor = 0
        return self

    def __next__(self):        
        if self.next_cursor == len(self.lst[self.cursor]) :
            iter(self)
        if self.cursor  == len(self.lst)  :
            raise StopIteration
        self.next_cursor += 1     
        return self.lst[self.cursor][self.next_cursor - 1]     
            
list_of_list_1= [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]]
              
flat_iterator = FlatIterator(list_of_list_1) 
for item in flat_iterator:
    print(item) 
print('='*90)     

def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    print('Все ОК!')


if __name__ == '__main__':

    test_1()   
print('='*90) 
print('='*90) 
print('='*90) 

##Задание 2
###Доработать функцию flat_generator, Должен получиться генератор, 
###который принимает список списков и возвращает их плоское представление. 
###Функция test в коде ниже также должна отработать без ошибок.


import types


def flat_generator(list_of_lists):

    for lists in list_of_lists:
        for items in lists:
            yield items
    

list_of_list_1= [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]]
              
for item in flat_generator(list_of_list_1):
    print(item) 

print('='*90) 


def test_2():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)
    print('Все ОК!')

if __name__ == '__main__':
    test_2()    
