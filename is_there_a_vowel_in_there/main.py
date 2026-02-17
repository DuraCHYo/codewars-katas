#https://www.codewars.com/kata/57cff961eca260b71900008f/train/python
def is_vow(inp: list[int]) -> list:
    '''
    Docstring для is_vow
    
    :param inp: Описание
    :type inp: list[int]
    :return: List with result
    :rtype: list
    '''
    # Словарь: код гласной -> её символ
    vowel_codes = {97: 'a', 101: 'e', 105: 'i', 111: 'o', 117: 'u'}
    # Список для результата
    result = []
    
    # Шаг 2: перебираем каждый элемент ВХОДНОГО списка
    for item in inp:
        # Проверяем, является ли элемент кодом гласной
        if item in vowel_codes:  # если да
            # добавляем строку с гласной
            result.append(vowel_codes[item])
        else:                     # если нет
            # добавляем само число
            result.append(item)
            
    return result
if __name__=='__main__':
    a = is_vow([118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ])
    if a == [118, "u",120,121,"u",98,122,"a",120,106,104,116,113,114,113,120,106 ]:
        print(f'DONE\n with {a}')
    else:
        print(f'ERROR\n with {a}')
    # should be [118,117,120,121,117,98,122,97,120,106,104,116,113,114,113,120,106 ]