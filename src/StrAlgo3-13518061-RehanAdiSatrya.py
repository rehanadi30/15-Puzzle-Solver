# Nama/NIM : Rehan Adi Satrya/13518061
# Keterangan : Tugas Kecil 3 Strategi Algoritma

import time
from copy import deepcopy

class Puzzle:
    #Default constructor
    def __init__(self, data=[]):
        self.data = data

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
        if ((self.sumKurang() + self.cariX())%2 == 0):
            return True
        else:
            return False

    def calculateCost(self):
        temp = 0
        for i in range (0,15):
            if (self.data[i] != (i+1)):
                temp += 1
        if (self.data[15] != 0):
            temp += 1
        return temp

    def isSame(self, puzzle):
        temp = True
        for i in range (0,16):
            if (self.data[i] != puzzle.data[i]):
                temp = False
        return temp
    def UbinAtas(self):
        if (self.posisi(0) <= 4):
            return -999
        else:
            return self.data[self.posisi(0) - 5]
    
    def UbinBawah(self):
        if (self.posisi(0) >= 13):
            return -999
        else:
            return self.data[self.posisi(0) + 3]
    
    def UbinKiri(self):
        if ((self.posisi(0) % 4) == 1):
            return -999
        else:
            return self.data[self.posisi(0)-2]

    def UbinKanan(self):
        if ((self.posisi(0) % 4) == 0):
            return -999
        else:
            return self.data[self.posisi(0)]

    #Method----------------------------------------------------------------------------------------------------------------------
    def printPuzzle(self):
        for i in range (0, 16, 4):
            if (self.data[i] == 0):
                print(" " + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
            elif(self.data[i+1] == 0):
                print(str(self.data[i]) + "\t" + " " + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
            elif(self.data[i+2] == 0):
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + " " + "\t" + str(self.data[i + 3]))
            elif(self.data[i+3] == 0):
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + " ")
            else:
                print(str(self.data[i]) + "\t" + str(self.data[i + 1]) + "\t" + str(self.data[i + 2]) + "\t" + str(self.data[i + 3]))
        print(" ")

class ListOfPuzzles:
    #Default Constructor
    def __init__(self):
        self.data = []

    def describeList(self):
        lengthLList = len(self.data)
        i = 0
        for items in self.data:
            if (i == 0):
                print("Matriks Awal")
                i += 1
                items.printPuzzle()
            else:
                print("Step ke-" + str(i))
                i += 1
                items.printPuzzle()

    def cheapestPuzzle(self):
        result = self.data[0]
        lengthList = len(self.data)
        for i in range(0,lengthList):
            if (self.data[i].calculateCost() < result.calculateCost()):
                result = self.data[i]
        return result

def Solve(puzzle):
    #KAMUS LOKAL
    jumlahNode = 0
    livingNode = ListOfPuzzles()
    solusi = ListOfPuzzles()

    #ALGORITMA
    if (puzzle.isSolvable() == False):
        print("Puzzle tidak dapat diselesaikan!!!")
    else:
        livingNode.data.append(puzzle)
        while (not (len(livingNode.data) == 0)):
            temp = livingNode.cheapestPuzzle()
            solusi.data.append(temp)
            if (not alreadySolved(temp)):
                tempUp = deepcopy(temp)
                swipe(tempUp, 1)

                tempRight = deepcopy(temp)
                swipe(tempRight, 3)

                tempDown = deepcopy(temp)
                swipe(tempDown, 2)

                tempLeft = deepcopy(temp)
                swipe(tempLeft, 0)
                
                if ((not temp.isSame(tempUp))):
                    livingNode.data.append(tempUp)
                    jumlahNode += 1
                if ((not temp.isSame(tempDown))):
                    livingNode.data.append(tempDown)
                    jumlahNode += 1
                if ((not temp.isSame(tempLeft))):
                    livingNode.data.append(tempLeft)
                    jumlahNode += 1
                if ((not temp.isSame(tempRight))):
                    livingNode.data.append(tempRight)
                    jumlahNode += 1
                livingNode.data.remove(temp)
            else:
                break

        if (not (len(livingNode.data) == 0)):
            print("Step terbaiknya adalah: \n")
            solusi.describeList()
            print("FOUND!! HOREEEEEEE")
            print("Jumlah Node dibangkitkan: " + str(jumlahNode))
        else:
            print("NOT FOUND :(")
             
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

def swipe(puzzle, kode):
    res = puzzle
    if (kode == 0): #Kiri
        res = tukarUbin(puzzle,0,puzzle.UbinKiri())
    elif (kode == 1): #Atas
        res = tukarUbin(puzzle,0,puzzle.UbinAtas())
    elif (kode == 2): #Bawah
        res = tukarUbin(puzzle,0,puzzle.UbinBawah())
    elif (kode == 3): #Kanan
        res = tukarUbin(puzzle,0,puzzle.UbinKanan())
    return res

def tukarUbin(puzzle, a, b):
    temp = puzzle
    if (b != -999):
        temp1 = 0
        posisiA = puzzle.posisi(a) - 1
        posisiB = puzzle.posisi(b) - 1
        temp1 = temp.data[posisiA]
        temp.data[posisiA] = temp.data[posisiB]
        temp.data[posisiB] = temp1
    return temp

def alreadySolved(puzzle):
    return(puzzle.sumKurang() == 0)

def main():
    InitialPuzzle = Puzzle()
    bacaPuzzleDariTXT("input.txt", InitialPuzzle)
    InitialPuzzle.printPuzzle()
    print("FUNGSI KURANG")
    for i in range (1,16):
        print("Ubin ke-" + str(i) + " = " + str(InitialPuzzle.kurang(i)))
    print(" ")
    print("SumKurang + X = " + str(InitialPuzzle.sumKurang() + InitialPuzzle.cariX()))
    print(" ")
    Solve(InitialPuzzle)

#Mainloop
start_time = time.time()
main()
print("--- %s ms ---" % ((time.time() - start_time)*1000))