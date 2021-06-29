# Выполнил: Лабырин Матвей, ИВТ, 2 курс, 1 подгруппа
# Вариант: 5, 6, 10

# Построить таблицу истинности для:
# 1) (A∨B)∧ ¬C
# 2) ((C∨B)→B)∧(A∧ B)→B
# 3) A∨¬C→¬(B↔A)

#-------------------------
a = bool(1)
b = bool(1)
c = bool(1)
# За максимальную ширину таблицы берётся вариант, когда все переменные false
max = "• false • false • false • false • false • false •"
table_width =len(max)
filler = "•"
print(filler * table_width)
print("•   A   •   B   •   C   •   1   •   2   •   3   •")
# 1, 2 и 3 - номера логических задач
# not(x) or y  - реализация импликации

# 1 строка
print(filler * table_width)
print("• " + str(a) + "  • " + str(b) + "  • " + str(c) + "  • " +
      str((a or b) and not(c)) + " • " + str((not(c or b) or b) and not(a and b) or b) +
      "  • " + str(not(a or not(c)) or not(b==a)) + " •")
# 2 строка
a = bool(0)
print(filler * table_width)
print("• " + str(a) + " • " + str(b) + "  • " + str(c) + "  • " +
      str((a or b) and not(c)) + " • " + str((not(c or b) or b) and not(a and b) or b) +
      "  • " + str(not(a or not(c)) or not(b==a)) + "  •")
# 3 строка
a = bool(1)
b = bool(0)
print(filler * table_width)
print("• " + str(a) + "  • " + str(b) + " • " + str(c) + "  • " +
      str((a or b) and not(c)) + " • " + str((not(c or b) or b) and not(a and b) or b) +
      " • " + str(not(a or not(c)) or not(b==a)) + "  •")
# 4 строка
b = bool(1)
c = bool(0)
print(filler * table_width)
print("• " + str(a) + "  • " + str(b) + "  • " + str(c) + " • " +
      str((a or b) and not(c)) + "  • " + str((not(c or b) or b) and not(a and b) or b) +
      "  • " + str(not(a or not(c)) or not(b==a)) + " •")
# 5 строка
a = bool(0)
b = bool(0)
print(filler * table_width)
print("• " + str(a) + " • " + str(b) + " • " + str(c) + " • " +
      str((a or b) and not(c)) + " • " + str((not(c or b) or b) and not(a and b) or b) +
      "  • " + str(not(a or not(c)) or not(b==a)) + " •")
# 6 строка
a = bool(1)
print(filler * table_width)
print("• " + str(a) + "  • " + str(b) + " • " + str(c) + " • " +
      str((a or b) and not(c)) + "  • " + str((not(c or b) or b) and not(a and b) or b) +
      "  • " + str(not(a or not(c)) or not(b==a)) + "  •")
# 7 строка
a = bool(0)
b = bool(1)
print(filler * table_width)
print("• " + str(a) + " • " + str(b) + "  • " + str(c) + " • " +
      str((a or b) and not(c)) + "  • " + str((not(c or b) or b) and not(a and b) or b) +
      "  • " + str(not(a or not(c)) or not(b==a)) + "  •")
# 8 строка
b = bool(0)
c = bool(1)
print(filler * table_width)
print("• " + str(a) + " • " + str(b) + " • " + str(c) + "  • " +
      str((a or b) and not(c)) + " • " + str((not(c or b) or b) and not(a and b) or b) +
      " • " + str(not(a or not(c)) or not(b==a)) + "  •")
print(filler * table_width)
