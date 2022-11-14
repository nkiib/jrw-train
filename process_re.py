import json
import urllib.request
import output_html as oh

def line_alfa():
    print('A:琵琶湖線・京都線・神戸線\nB:湖西線\nC:草津線\nD:奈良線\nE:嵯峨野線・山陰線\nF:おおさか東線\nG:宝塚線・福知山線\nH:JR東西線・学研都市線\nJ:播但線\nL:舞鶴線\nO:大阪環状線\nP:ゆめ咲線\nQ:大和路線\nR:阪和線・羽衣支線\nS:関西空港線\nT:和歌山線\nU:万葉まほろば線（桜井線）\nV:関西本線\nW:きのくに線')

def end():
    print('入力された値が不正です。')
    import sys
    sys.exit()

htmlout = []
delay_info = []
direct0 = []
direct1 = []
d0_for = []
d1_for = []
def output(line_name):
    lineout = []
    #路線入力の取得とデータの取得
    line_name_json = line_name + '.json'
    url = 'https://www.train-guide.westjr.co.jp/api/v3/' + line_name_json
    url_st = url.replace('.json','_st.json')
    res = urllib.request.urlopen(url)
    res_st = urllib.request.urlopen(url_st)
    data = json.loads(res.read().decode('utf-8'))
    data_st = json.loads(res_st.read().decode('utf-8'))

    dictst = {}
    chain = 0
    #データと駅名の照会
    for station in data_st['stations']:
        dictst[station['info']['code']] = station['info']['name']
    
    #処理ループ
    for item in data['trains']:
        #データと駅名の照会
        stn = item['pos'].split('_')
        try:
            position = dictst[stn[0]]
        except KeyError:
            position = "？？？"
        try:
            posi2 = dictst[stn[1]]
        except KeyError:
            posi2 = "？？？"

        #閑散路線でのエラー回避
        try:
            goto = item['dest']['text']
        except:
            goto = item['dest']
        try:
            car = str(item['numberOfCars']) + '両'
        except:
            car = '不明'

        #変数代入
        TrainNumber = str(item['no'])
        Direction = str(item['direction'])
        TrainType = item['displayType']
        delay = str(item['delayMinutes']) + '分'

        #遅延レベルによる色分け
        if item['delayMinutes'] > 60:
            delay ='<span id="violet"><b>' + delay + "</b></span>"
            TrainNumber ='<span id="violet"><b>' + TrainNumber + "</b></span>"
        elif item['delayMinutes'] > 30:
            delay ='<span id="red"><b>' + delay + "</b></span>"
            TrainNumber = '<span id="red"><b>' + TrainNumber + "</b></span>"
        elif item['delayMinutes'] > 10:
            delay = '<span id="orange"><b>' + delay + "</b></span>"
            TrainNumber = '<span id="orange"><b>' + TrainNumber + "</b></span>"
        elif item['delayMinutes'] > 0:
            delay = '<span id="blue"><b>' + delay + '</b></span>'
            TrainNumber = '<span id="blue"><b>' + TrainNumber + "</b></span>"
            
        #種別による色分け
        if '快' in TrainType or '新快' in TrainType or '紀州' in TrainType:
            TrainType = '<span id="blue">' + TrainType + '</span>'
        elif '特急' in TrainType:
            TrainType = '<span id="red">' + TrainType + '</span>'
        #html出力処理
        obje = '\t\n<tr><td>' + line_name + '</td><td>' + TrainNumber + '</td><td>' + Direction + '</td><td>' + TrainType + '</td><td>' + goto + '</td><td>' + delay + '</td><td>' + car + '</td><td>' + position + '</td><td>' + posi2 + '</tr>'
        htmlout.append(obje)
        lineout.append(obje)
        if item['direction'] == 0:
            d0 = '\t\n<tr><td>' + line_name + '</td><td>' + TrainNumber + '</td><td>' + Direction + '</td><td>' + TrainType + '</td><td>' + goto + '</td><td>' + delay + '</td><td>' + car + '</td><td>' + position + '</td><td>' + posi2 + '</tr>'
            d0_for.append(goto)
            direct0.append(d0)
        elif item['direction'] == 1:
            d1 = '\t\n<tr><td>' + line_name + '</td><td>' + TrainNumber + '</td><td>' + Direction + '</td><td>' + TrainType + '</td><td>' + goto + '</td><td>' + delay + '</td><td>' + car + '</td><td>' + position + '</td><td>' + posi2 + '</tr>'
            d1_for.append(goto)
            direct1.append(d1)
        print(htmlout)

        #遅れ出力処理
        if item['delayMinutes'] != 0:        
            send_line = str(item['displayType']) + str(item['dest']['text']) + '行き:' + str(item['delayMinutes']) + '分遅れ' + str(position) + 'と' + str(posi2) + '周辺'
            delay_info.append('<li>' + send_line + '</li>')
            oh.html_fix(lineout,line_name,line_name,delay_info)
            chain = 1
        
    #遅延なし出力
    if chain == 0:
        print('現在遅れはありませんでしたよぉ。安心して出かけろ。')
        delay_info.append('<li>遅れなし</li>')
        oh.html_fix(lineout,line_name,line_name,delay_info)
        chain = 1

    # oh.html_fix(htmlout,line_name,'al',delay_info)
    oh.direc_fix(direct0,direct1,line_name,'allout',delay_info,d0_for,d1_for)