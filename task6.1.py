from time import sleep

class TraficLight:

    def __init__(self):
        self.__color = {"red": 7, "yellow": 2, "green": 7}

    def running(self):
        i = 0
        while i < 50:
            for key in self.__color:
                print(f"New color: {key}.")
                sleep(self.__color.get(key))
            i += 1



svet = TraficLight()
svet.running()
