"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
Проверить работу примера, создав экземпляр и вызвав описанный метод.

Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить
соответствующее сообщение и завершать скрипт.
"""
import time


class Trafficlight:
    __color = ""

    def running(self):
        q = ""
        while q != "q":
            Trafficlight.__color = "RED"
            print(Trafficlight.__color)
            time.sleep(7)
            Trafficlight.__color = "YELLOW"
            print(Trafficlight.__color)
            time.sleep(2)
            Trafficlight.__color = "GREEN"
            print(Trafficlight.__color)
            time.sleep(2)
            q = input("Проехали... для повтора нажмите любую клавишу (для завершения нажмите 'q')")


ob = Trafficlight()
ob.running()