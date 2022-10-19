import unittest

def numRep(lista):
    diccionario = {}
    for i in lista:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    return diccionario

class TestNum(unittest.TestCase):
    def test_1(self):
        dict = numRep([0,1,2,3])
        self.assertEqual({0:1,1:1,2:1,3:1}, dict)
    def test_2(self):
        dict = numRep([0,0,1,2,1,3])
        self.assertEqual({0:2, 1:2, 2:1, 3:1}, dict)

if __name__=='__main__':
    unittest.main()
