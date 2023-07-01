startsumm = 1000
def choice (ch=int(input("Выберите операцию Пополнение 1 Снятие 2 Выход 3   "))):
    if ch == 1:
        def vnesti(s=int(input("Внесите на счет сумму кратную 50 у.е. ")), count=1):
            global startsumm
            if s % 50 == 0 and count < 3:
                a = startsumm + s
                return a
            if s % 50 == 0 and count == 3:
                b = startsumm + s * 1.03
                return b
            return 'Такую сумму внести нельзя'
        print(vnesti())
        return ""
    if ch == 2:
        def snyat(s1=int(input("Снимите со счета сумму кратную 50 у.е. ")), count=3):
            global startsumm
            if s1 % 50 == 0 and count < 3 and s1 < startsumm:
                if s1 * 0.015 > 30 and s1 * 0.015 < 600:
                    startsumm -= s1 * 1.015

                    return startsumm
                if s1 * 0.015 < 30:
                    startsumm -= s1 + 30

                    return startsumm
                if s1 * 0.015 > 600:
                    startsumm -= s1 + 600

                    return startsumm
                return ""

            if s1 % 50 == 0 and count == 3 and s1 < startsumm:
                if s1 * 0.015 > 30 and s1 * 0.015 < 600:
                    startsumm -= s1 * 1.015
                    return startsumm * 1.03
                if s1 * 0.015 < 30:
                    startsumm -= s1 + 30
                    return startsumm * 1.03
                if s1 * 0.015 > 600:
                    startsumm -= s1 + 600
                    return startsumm * 1.03
                return ""
            return "Такую сумму снять нельзя"
        print(snyat())
        return ""
    if ch == 3:
        def exit_():
            return"Выход"
        print(exit_())
        return ""
    return "Такой операции не существует"
print(choice())

