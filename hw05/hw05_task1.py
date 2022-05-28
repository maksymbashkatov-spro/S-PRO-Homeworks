# Поскольку в ТЗ указано, что нужно запрашивать только имена файлов, а не путь целиком,
# я сделал именно это.
original_file_name = input('Введите имя исходного файла: ')
new_file_name = input('Введите имя нового файла: ')
count = 1

with open(f'test_files\{original_file_name}.txt', 'r') as original_file,\
     open(f'test_files\{new_file_name}.txt', 'w') as new_file:
    for line in original_file:
        new_file.write(f'{count}: {line}')
        count += 1


# Пример работы программы:
# Введите имя исходного файла: test_file1
# Введите имя нового файла: test_file2
