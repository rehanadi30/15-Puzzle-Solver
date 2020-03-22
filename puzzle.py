# Nama/NIM : Rehan Adi Satrya/13518061
# Keterangan : Tugas Kecil 3 Strategi Algoritma

import timeit

class Puzzle:
    #Default constructor
    def __init__(self):
        self.data = []

    #Getter-----------------------------------------------------------------------------------
    def posisi(self, dataDicari):
        temp = 0
        for i in range (0,16):
            temp += 1
            if (self.data[i] == dataDicari):
                break
        return temp

    def dimanaYangKosong(self):
        return self.posisi(0)
    
    def cariX(self):
        if ((self.dimanaYangKosong() == 2) or (self.dimanaYangKosong() == 4) or (self.dimanaYangKosong() == 5) or (self.dimanaYangKosong() == 7) or (self.dimanaYangKosong() == 10) or (self.dimanaYangKosong() == 12) or (self.dimanaYangKosong() == 13) or (self.dimanaYangKosong() == 15)):
            X = 1
        else:
            X = 0
        return X

    def kurang(self, i):
        temp = 0
        if (i != 16):
            for j in range(1,i):
                if (self.posisi(j) > self.posisi(i)):
                    temp += 1
        else: #Khusus buat i=16
            for j in range(1,i):
                if (self.posisi(j) > self.posisi(0)):
                    temp += 1
        return temp

    def sumKurang(self):
        temp = 0
        for i in range(1,17):
            temp += self.kurang(i)
        return temp

    def isSolvable(self):
        return ((self.sumKurang() + self.cariX())%2 == 0)

    def calculateCost(self):
        temp = 0
        for i in range (0,15):
            if (self.data[i] != (i+1)):
                temp += 1
        if (self.data[15] != 0):
            temp += 1
        return temp

    #Setter-------------------------------------------------------------------------------------
    def setData(self, a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p):
        self.data = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p]

    def tukarUbin(self, a, b):
        temp = 0
        posisiA = self.posisi(a) - 1
        posisiB = self.posisi(b) - 1
        temp = self.data[posisiA]
        self.data[posisiA] = self.data[posisiB]
        self.data[posisiB] = temp

    def swipeAtas(self):
        posisiBawahnya = self.posisi(0) - 1 + 4
        self.tukarUbin(0, self.data[posisiBawahnya])
    
    def swipeBawah(self):
        posisiAtasnya = self.posisi(0) - 1 - 4
        self.tukarUbin(0, self.data[posisiAtasnya])

    def swipeKiri(self):
        posisiKanannya = self.posisi(0) - 1 + 1
        self.tukarUbin(0, self.data[posisiKanannya])

    def swipeKanan(self):
        posisiKirinya = self.posisi(0) - 1 - 1
        self.tukarUbin(0, self.data[posisiKirinya])

    #Method----------------------------------------------------------------------------------------------------------------------
    def printPuzzle(self):
        for i in range (0, 16, 4):
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
        print(" ")

class Node:
        def __init__(self, puzzle=[], level=0):
            self.parent = puzzle
            self.level = level
            self.nextNode = None

        def nextNode(self, nextNode):
            self.nextNode = nextNode

def Solve(puzzle):
    puzzle.printPuzzle()
    for i in range (1,17):
        print(str(i) + " = " + str(puzzle.kurang(i)))
    print(puzzle.isSolvable())
    print("SumKurang + X = " + str(puzzle.sumKurang() + puzzle.cariX()))
    if (puzzle.isSolvable() == False):
        print("Puzzle tidak dapat diselesaikan!!!")
    else:
        print("Puzzle bisa diselesaikan")

def bacaPuzzleDariTXT(text_file_name, puzzle):
    f=open(text_file_name,"r")
    lines=f.read().splitlines()
    input=[]
    for x in lines :
        temp=x.split(  )
        temp1= list(map(int, temp))
        input.append(temp1)
    f.close()
    puzzle.data = input[0] + input[1] + input[2] + input[3]
    

def main1():
    dummy = Puzzle()
    dummy.setData(1,2,3,4,5,6,0,8,9,10,7,11,13,14,15,12)
    dummy.printPuzzle()
    #dummy.swipeAtas()
    dummy.printPuzzle()
    print(str(dummy.posisi(12)))
    print(str(dummy.dimanaYangKosong()))
    print("X : " + str(dummy.cariX()))
    print("SumKurang : " + str(dummy.sumKurang()))
    print("Cost : " + str(dummy.calculateCost()))
    print(dummy.isSolvable())
    print("\n\n")

    for i in range (1,17):
        print(str(i) + " : " + str(dummy.kurang(i)))

def main2():
    dummy = Puzzle()
    bacaPuzzleDariTXT("input.txt", dummy)
    Solve(dummy)

main2()
print("Waktu eksekusi :" + str(timeit.timeit(main1, number=0)))