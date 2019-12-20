alph = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

if __name__ == "__main__":
    mode = input('Режим (1 - шифрование; 2 - рашифровывание; 3 - дешифровывание): ')

def readText():
    a = input('Выберете способ ввода текста:\n1)Напечатать вручную\n2)Из файла\n')
    while a!='1' and a!='2':
        a = input('Выберете способ ввода текста:\n1)Напечатать вручную\n2)Из файла\n')
    if a == '1':
        text = input()
    else:
        a = open('Текст.txt')
        text = a.read()
    print(text + '\n')
    return text

def editText():
    text = readText()
    text = text.lower()
    for char in text:
        if alph.find(char) == -1:
            text = text.replace(char,'')
    print(text + '\n')
    return text


if mode == '1':
    ot = editText()
    key = input('Введите ключ: ')
    if len(key) != len(ot):
        l = len(key)
        for i in range(len(ot)-len(key)):
            key+=key[i%l]
    ct = ''
    for i in range(len(ot)):
        ct += alph[ (alph.index(ot[i]) + alph.index(key[i]))%len(alph) ]
    print('---')
    print(ot)
    print(key)
    print(ct)

if mode == '2':
    ct = editText()
    key = input('Введите ключ: ')
    if len(key) != len(ct):
        l = len(key)
        for i in range(len(ct)-len(key)):
            key+=key[i%l]
    dt = ''
    for i in range(len(ct)):
        dt += alph[ (alph.index(ct[i]) - alph.index(key[i]))%len(alph) ]
    print('---')
    print(ct)
    print(key)
    print(dt)

if mode == '3':
    ct = editText()
    ci = 0
    ct2 = ''
    inds = []
    for x in range(2,len(alph)):
        for i in range(0, len(ct), x):
            ct2 += ct[i]
        ct22 = "".join(set(ct2))
        for i in range(len(ct22)):
            ci += ct2.count(ct22[i])*(ct2.count(ct22[i])-1) / float(len(ct2)*(len(ct2)-1))
        if ci > 0.05:
            inds.append([ci,x])
        print(ci)
        print(ct2)
        ct2=''
        ci = 0
    print(inds)
    texts = []
    txt = ''
    for x in range(0,inds[0][1]):
        for i in range(x,len(ct),inds[0][1]):
            txt += ct[i]
        texts.append(txt)
        txt = ''
    del inds
    inds = []
    for T in texts:
        #print(T)
        counts = []
        counts.append([T.count('о'),'о'])
        for i in range(len(alph)):
            if alph[i] != 'о':
                counts.append([T.count(alph[i]),alph[i]])
        inds.append((alph.index(max(counts)[1]) - alph.index(counts[0][1]))%32)
    print(inds)
    keyWord = ''
    for num in inds:
        keyWord += alph[num]
    print(keyWord)

        

