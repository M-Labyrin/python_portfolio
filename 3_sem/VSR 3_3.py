# Написать программу, выводящую на экран последовательно символыанглийского
# и кириллического алфавита с использованием кодов из таблицы unicode-символов.

engl_alphabet = [chr(i) for i in range(ord('a'), ord('z') + 1)]
russ_alphabet = [chr(i) for i in range(ord('а'), ord('я') + 1)]
print(*engl_alphabet)
print(*russ_alphabet)
