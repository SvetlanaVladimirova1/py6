# Создайте несколько переменных заканчивающихся и не оканчивающихся на «s».
# ✔ Напишите функцию, которая при запуске заменяет содержимое переменных
# оканчивающихся на s (кроме переменной из одной буквы s) на None.
# ✔ Значения не удаляются, а помещаются в одноимённые переменные без s на конце.

a = "ffs"
b = "maks"
c = "ggg"
def s():
    for i in a.split():
        if a[0] != "s" and a[-1] == "s":
            return None
        return a
print(s())
def s1():
    for i in b.split():
        if b[0] != "s" and b[-1] == "s":
            return None
        return b
print(s1())
def s2():
    for i in c.split():
        if c[0] != "s" and c[-1] == "s":
            return None
        return c
print(s2())
print(a, b, c)
a = map(lambda x: x.replace("s", ""), a)
b = map(lambda x: x.replace("s", ""), b)
c = map(lambda x: x.replace("s", ""), c)
print(*a, *b, *c)
