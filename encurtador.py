## ANGEL LEDEBRUM GRANVILLE
## FERNANDO FERRARIN

import os
from math import floor

class Encurtador:
    def __init__(self):
        self.dic = {}
        self.nome_arq = "urls.txt"
        self.__load_dic()
        self.indice = 1000 + len(self.dic)

    def __load_dic(self):
        if(os.path.exists("urls.txt")):
            arq = open(f"{self.nome_arq}","rb")
            arq.read()
            arq.close() 
        else:
            print("\nO arquivo não existe!!")

    def __save_dic(self):
        arq = open(f"{self.nome_arq}","w")
        arq.write(f"{self.dic}")
        arq.close()

    def toBase(self, num, b = 62):
        if b <= 0 or b > 62:
            return 0
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        r = num % b
        res = base[r]
        q = floor(num / b)
        while q:
            r = q % b
            q = floor(q / b)
            res = base[int(r)] + res
        return res

    def to10(self, num, b = 62):
        base = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
        limit = len(num)
        res = 0
        for i in range(limit):
            res = b * res + base.find(num[i])
        return res

    def encurtar(self, url):
        self.tupla = (self.toBase(self.indice), url)
        self.dic = {self.indice: self.tupla}
        self.indice += 1
        self.__save_dic()

    def buscar(self, url):
        vet = self.to10(url)
        return self.dic[vet][1]

    def listar_urls(self):
        print(self.dic)

e = Encurtador()
e.encurtar("https://imed.edu.br/Ensino/ciencia-da-computacao/graduacao/sobre-a-profissao/")
print(e.buscar('g8'))