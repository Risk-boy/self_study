S = input()

dict = {'a':'', 'b':'', 'c':'', 'd':'', 'e':'', 'f':'', 
        'g':'', 'h':'', 'i':'', 'j':'', 'k':'', 'l':'',
        'm':'', 'n':'', 'o':'', 'p':'', 'q':'', 'r':'', 's':'',
        't':'', 'u':'', 'v':'', 'w':'', 'x':'', 'y':'',
        'z':'' }

for key in dict:
    dict[key] = S.find(key)

for key in dict:
    print(dict.get(key), end = ' ')        