#!/bin/env python3
class Kostka:
    """
    Kostka nam definuje hraci kostku
    pocet_sten=8
    """
    def __init__(self,pocet_sten=6):
        """
        nastaveni
        :param pocet_sten:
        """
        self.__pocet_sten = pocet_sten

    def __str__(self):
        """
        Vraci info o nasi kostce
        :return:
        """
        return str("Kostka s {0} stenami".format(self.kolik_ma_sten()))

    def kolik_ma_sten(self):
        """
        Vrati nam pocet sten ko stky
        :return:
        """
        return(self.__pocet_sten)
    def hod(self):
        """
        Vykona hod kostkou, vrati cislo 1..pocet_sten
        :return:
        """
        import random as _random
        return _random.randint(1, self.__pocet_sten)


class hun:
    """

    """
    def __init__(self, jmeno, zivot, utok, obrana, kostka):
        """
       Hun se nejak jmenuje,
        :param jmeno:
        :param zivot: zivot maximalni
        :param utok: sila mece
        :param obrana:  odolnost stitu
        :param kostka:
        """
        self.jmeno = jmeno
        self.zivot = zivot
        self._max_zivot = zivot
        self._utok = utok
        self._obrana = obrana
        self._kostka = kostka
        self._stav = "Zdravy"
        self.__zprava=""
    def __updatestav(self):
        if self.zivot > self._max_zivot :
            stav="zvlastni"
        elif self.zivot == self._max_zivot:
            stav="Zdravy"
        elif self.zivot <=0:
            stav="Mrtvy"
        else:
            stav="Zraneny"
        self._stav=stav
        return stav
    @property
    def nazivu(self):
        return self.zivot > 0
    def lifestatus(self):
        return str(f"{self.zivot}/{self._max_zivot}")
    def lifebar(self):
        size=20
        type="#"
        full=int(self.zivot * (size / self._max_zivot))
        if (full==0) and (self.zivot>0):
            type="."
            full=1
        return str(f"[{type*full}{' '*(size-full)}]")
    def __hurt(self,damage):
        self.zivot-=damage
        self.__zprava=f"{self.jmeno} je trosku posramocen, dostal zasah za {damage}  a nyni je s zivotem {self.zivot} {self.__updatestav()}"

    def bran_se(self,uder):
        zraneni=(uder - (self._obrana + self._kostka.hod()))

        if zraneni > 0:
            self.__hurt( zraneni)
        else:
            self.__zprava=f"{self.jmeno} je sikovny, a nedostal zadny damage z {uder} moznych "

    def utok(self,souper):
        zasah = self._utok + self._kostka.hod()
        souper.bran_se(zasah)
        self.__nastav_zoravu(f"{self.jmeno} zautocil na {souper.jmeno} a snazi se mu ustedrit {zasah}")
    def __nastav_zoravu(self,zprava):
        self.__zprava=zprava
    def oznam(self):
        return self.__zprava

    def __str__(self):
        return str(f"{self._stav} bojovnik {self.jmeno}")

class mag(hun):
    def __init__(self, jmeno, zivot, utok, obrana, kostka, mana, mutok):
        super().__init__(jmeno,zivot,utok, obrana, kostka)
        self.__mana=mana
        self.__max_mana=mana
        self.__mutok=mutok


class arena:
    def __init__(self, bojovnik1, bojovnik2, kostka):
        self.__bojovnik1=bojovnik1
        self.__bojovnik2=bojovnik2
        self.__kostka=kostka
    def headers(self):
        print("-----------------ARENA--------------")
    def __vycisti(self):
        import sys,subprocess
        if sys.platform.startswith("win"):
            subprocess.call(["cmd.exe","/C","cls"])
        else:
            subprocess.call(["clear"])

    def vykresli(self):
        self.__vycisti()
        self.headers()
        print(f"{self.__bojovnik1.jmeno:<40}{self.__bojovnik2.jmeno}")
        print(f"{self.__bojovnik1.lifebar():<40}{self.__bojovnik2.lifebar()}")
        print(f"{self.__bojovnik1.lifestatus():<40}{self.__bojovnik2.lifestatus()}")
    def __update_header(self):
        self.vykresli()

    def __sleep(self,secs,precision=0):
        import random,time
        if precision>secs:
            precision=secs
        add=-precision+2*(random.randint(0,precision))
        time.sleep(secs+add)
        time.sleep(0.2)


    def __text_dopln(self,jaky):
        print(jaky)
        self.__sleep(0.75)
    def fight(self):
        import sys,subprocess,random,time
        self.__vycisti()
        if random.randint(0,1):
            (self.__bojovnik1, self.__bojovnik2) = (self.__bojovnik2,
                                                    self.__bojovnik1)

        print("Vitejte v arene")
        self.__sleep(3,2)
        print("Dnes se spolu utkaji dva silni souperi ")
        self.__sleep(3,2)

        print(f"V levem rohu {self.__bojovnik1.jmeno}")
        self.__sleep(3,2)
        print(f"V pravem rohu {self.__bojovnik2.jmeno}")
        self.__sleep(3,2)
        print("Zapas mzue zacit!! ")
        self.__sleep(3,2)
        self.vykresli()
        while(self.__bojovnik1.nazivu and self.__bojovnik2.nazivu):
            self.vykresli()
            self.__bojovnik1.utok(self.__bojovnik2)
            self.vykresli()
            self.__text_dopln(self.__bojovnik1.oznam())
            self.__text_dopln(self.__bojovnik2.oznam())
            if self.__bojovnik2.nazivu:
                self.__sleep(3,2)
                self.vykresli()
                self.__bojovnik2.utok(self.__bojovnik1)
                self.vykresli()
                self.__text_dopln(self.__bojovnik2.oznam())
                self.__text_dopln(self.__bojovnik1.oznam())
            print("jeee, to je podivana")
            self.__sleep(3,2)





sestka=Kostka()
hektor=hun("hektor",100,15,5,sestka)
pinda=hun("pinda",80,15,5,sestka)
haha=mag("Hahektor",100,10,5,sestka,50,50)
coloseum=arena(hektor,haha,sestka)
coloseum.fight()

