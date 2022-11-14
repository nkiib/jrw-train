import process as pro

def sec(a):
    if a == 'B':return('kosei')
    elif a == 'C':return('kusatsu')
    elif a == 'D':return('nara')
    elif a == 'F':return('osakahigashi')
    elif a == 'J':return('bantan')
    elif a == 'L':return('maizuru')
    elif a == 'O':return('osakaloop')
    elif a == 'P':return('yumesaki')
    elif a == 'Q':return('yamatoji')
    elif a == 'R':return('hanwahagoromo')
    elif a == 'S':return('kansaiairport')
    elif a == 'U':return('manyomahoroba')
    elif a == 'V':return('kansai')
    elif a == 'W':return('kinokuni')
    elif a != 'A' and a != 'E' and a != 'G' and a != 'H' and a != 'T':
        return a
    print('更に詳細な区間を数字で選択してください')
    if a == 'A':
        print('0:以下の路線全区間\n1:琵琶湖線・北陸線（近江塩津〜長浜・長浜〜京都）\n2:京都線（京都〜大阪）\n3:神戸線・山陽線（大阪〜姫路〜上郡）\n4:赤穂線')
        sec = input('取得したい区間は？')
        if sec == '0':return a
        elif sec == '1':return 'hokurikubiwako'
        elif sec == '2':return 'kyoto'
        elif sec == '3':return 'kobesanyo'
        elif sec == '4':return 'ako'
        else:pro.end()
    elif a == 'E':
        print('0:以下の路線全区間\n1:嵯峨野線\n2:園部〜福知山\n3:福知山〜居組')
        sec = input('取得したい区間は？')
        if sec == '0':return a
        elif sec == '1':return 'sagano'
        elif sec == '2':return 'sanin1'
        elif sec == '3':return 'sanin2'
        else: pro.end()
    elif a == 'G':
        print('0:以下の路線全区間\n1:大阪〜新三田\n2:新三田〜福知山')
        sec = input('取得したい区間は？')
        if sec == '0':return a
        elif sec == '1':return('takarazuka')
        elif sec == '2':return('fukuchiyama')
        else: pro.end()
    elif a == 'H':
        print('0:以下の路線全区間\n1:東西線\n2:学研都市線')
        sec = input('取得したい区間は？')
        if sec == '0':return a
        elif sec == '1':return('tozai')
        elif sec == '2':return('gakkentoshi')
        else: pro.end()
    elif a == 'T':
        print('0:以下の路線全区間\n1:王寺〜五条\n2:五条〜和歌山')
        sec = input('取得したい区間は？')
        if sec == '0':return a
        elif sec == '1':return('wakayama2')
        elif sec == '2':return('wakayama1')
        else: pro.end()

def sec2():
    line = {'A':'tokaido','B':'kosei','C':'kusatsu','D':'nara','E':'sanin','F':'osakahigashi','G':'fukuchiyama','H':'tozai','J':'bantan','L':'maizuru','O':'osakaloop','P':'yumesaki','Q':'yamatoji','R':'hanwahagoromo','S':'kansaiairport','T':'wakayama','U':'manyomahoroba','V':'kansai','W':'kinokuni'}
    alfa = ['A','B','C','D','E','F','G','H','J','L','O','P','Q','R','S','T','U','V','W']

    for w in alfa:
        print(w + ':' + line[w])
