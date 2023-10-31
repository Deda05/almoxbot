import pyautogui
import listas


def menu():
    while True:
        datakits = input("digite a data que os kits devem ser lançados (dia/mes/ano hora:minuto:segundo): ")
        while True:
            pyautogui.PAUSE = 2.5
            pyautogui.click(x=462, y=881)
            for i, x in listas.pacientes_turno1.items():
                pyautogui.click(x=63, y=183)
                pyautogui.click(x=118, y=376)
                pyautogui.write(i)
                pyautogui.PAUSE = 1.2
                pyautogui.press('enter')
                pyautogui.PAUSE = 1.7
                pyautogui.doubleClick(x=723, y=314)
                pyautogui.PAUSE = 3.0
                pyautogui.click(x=575, y=369)
                pyautogui.write(x)
                pyautogui.press('enter')
                pyautogui.PAUSE = 1.8
                pyautogui.click(x=1216, y=760)
                pyautogui.write(datakits)
                pyautogui.click(x=1476, y=627)
                pyautogui.PAUSE = 2.0
                pyautogui.click(x=1487, y=793, duration=1.3)
                pyautogui.click(x=639, y=252)
                pyautogui.click(x=850, y=338)
                pyautogui.click(x=884, y=316, button='right')
                pyautogui.moveTo(x=719, y=428)
                pyautogui.scroll(-200)
                pyautogui.click(x=643, y=540)
                pyautogui.press('enter')
                pyautogui.PAUSE = 3.0

            else:
                datakits1 = input(
                    "digite a data que os kits devem ser lançados (dia/mes/ano hora:minuto:segundo): "
                )
                pyautogui.PAUSE = 2.5
                pyautogui.click(x=462, y=881)
                for i, x in listas.pacientes_turno2.items():
                    pyautogui.click(x=63, y=183)
                    pyautogui.click(x=118, y=376)
                    pyautogui.write(i)
                    pyautogui.PAUSE = 1.2
                    pyautogui.press('enter')
                    pyautogui.PAUSE = 1.7
                    pyautogui.doubleClick(x=723, y=314)
                    pyautogui.PAUSE = 3.0
                    pyautogui.click(x=575, y=369)
                    pyautogui.write(x)
                    pyautogui.press('enter')
                    pyautogui.PAUSE = 1.8
                    pyautogui.click(x=1216, y=760)
                    pyautogui.write(datakits1)
                    pyautogui.click(x=1476, y=627)
                    pyautogui.PAUSE = 2.0
                    pyautogui.click(x=1487, y=793, duration=1.3)
                    pyautogui.click(x=639, y=252)
                    pyautogui.click(x=850, y=338)
                    pyautogui.click(x=884, y=316, button='right')
                    pyautogui.moveTo(x=719, y=428)
                    pyautogui.scroll(-200)
                    pyautogui.click(x=643, y=540)
                    pyautogui.press('enter')
                    pyautogui.PAUSE = 3.0
                else:
                    dialisador = "85480"
                    linha = "84667"
                    pyautogui.PAUSE = 2.5
                    pyautogui.click(x=462, y=881)
                    for i, x in listas.pacientes_usoun.items():
                        pyautogui.click(x=63, y=183)
                        pyautogui.click(x=118, y=376)
                        pyautogui.write(i)
                        pyautogui.PAUSE = 1.2
                        pyautogui.press('enter')
                        pyautogui.PAUSE = 1.7
                        pyautogui.doubleClick(x=723, y=314)
                        pyautogui.PAUSE = 3.0
                        pyautogui.click(x=575, y=369)
                        pyautogui.write(x)
                        pyautogui.press('enter')
                        pyautogui.write(dialisador)
                        pyautogui.press('enter')
                        pyautogui.write(linha)
                        pyautogui.press('enter')
                        pyautogui.PAUSE = 1.8
                        pyautogui.click(x=1216, y=760)
                        pyautogui.write(datakits1)
                        pyautogui.click(x=1476, y=627)
                        pyautogui.PAUSE = 2.0
                        pyautogui.click(x=1487, y=793, duration=1.3)
                        pyautogui.click(x=639, y=252)
                        pyautogui.click(x=850, y=338)
                        pyautogui.click(x=884, y=316, button='right')
                        pyautogui.moveTo(x=719, y=428)
                        pyautogui.scroll(-200)
                        pyautogui.click(x=643, y=540)
                        pyautogui.press('enter')
                        pyautogui.PAUSE = 3.0
                    else:
                        break
        else:
            print("Erro inesperado")
            break