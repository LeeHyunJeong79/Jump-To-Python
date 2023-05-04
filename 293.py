dic={'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E',
    '..-.':'F','--.':'G','....':'H','..':'I','.---':'J',
    '-.-':'K','.-..':'L','--':'M','-.':'N','---':'O',
    '.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T',
    '..-':'U','...-':'V','.--':'W','-..-':'X','-.--':'Y','--..':'Z'}
def mos(data):
    
    result=[]
    for word in data.split("  "):
        for char in word.split():
            if char in dic:
                result.append(dic[char])
        result.append(" ")
    print(result)#리스트 출력
    return "".join(result)#리스트 합치기 
print(mos('.... .  ... .-.. . . .--. ...  . .- .-. .-.. -.--'))

