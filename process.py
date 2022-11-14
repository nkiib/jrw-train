import json
import urllib.request
import output_html as oh
import sys

def line_alfa():
    print('A:琵琶湖線・京都線・神戸線\nB:湖西線\nC:草津線\nD:奈良線\nE:嵯峨野線・山陰線\nF:おおさか東線\nG:宝塚線・福知山線\nH:JR東西線・学研都市線\nJ:播但線\nL:舞鶴線\nO:大阪環状線\nP:ゆめ咲線\nQ:大和路線\nR:阪和線・羽衣支線\nS:関西空港線\nT:和歌山線\nU:万葉まほろば線（桜井線）\nV:関西本線\nW:きのくに線')

def end():
    print('入力された値が不正です。')
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
        # 停車中の電車の取り扱い
        try:
            position = dictst[stn[0]]
        except KeyError:
            position = "？？？"
        try:
            posi2 = dictst[stn[1]]
        except KeyError:
            posi2 = "？？？"

        nick_flag = 0
        try:
            nick_name = str(item['nickname'])
            if nick_name != "" and nick_name != 'None':
                nick_flag = 1
        except KeyError:
            nick_name = ""

        change_flag = 0
        try:
            changed = item['typeChange']
            if changed != "":
                change_flag =1
        except:
            changed = ""

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
        trt = TrainType
        delay = str(item['delayMinutes']) + '分'

        print('路線：' + line_name + '\t列車：' + TrainNumber + '\t列車名：' + nick_name +'\t向き：' + Direction + '\t種別：' + TrainType + '\t行先：' +  goto + '\t遅れ：' + delay + '遅れ\t' + car + '\t' + position + ' と ' + posi2) 
        
        #遅延レベルによる色分け
        if item['delayMinutes'] > 60:
            delay ='<td id="delay_over"><b>' + delay + "</b></td>"
            TrainNumber ='<td id="delay_over"><b>' + TrainNumber + "</b></td>"
        elif item['delayMinutes'] > 30:
            delay ='<td id="delay_60"><b>' + delay + "</b></td>"
            TrainNumber = '<td id="delay_60"><b>' + TrainNumber + "</b></td>"
        elif item['delayMinutes'] > 10:
            delay = '<td id="delay_30"><b>' + delay + "</b></td>"
            TrainNumber = '<td id="delay_30"><b>' + TrainNumber + "</b></td>"
        elif item['delayMinutes'] > 5:
            delay = '<td id="delay_10"><b>' + delay + "</b></td>"
            TrainNumber = '<td id="delay_10"><b>' + TrainNumber + "</b></td>"
        elif item['delayMinutes'] > 0:
            delay = '<td id="delay_5"><b>' + delay + '</b></td>'
            TrainNumber = '<td id="delay_5"><b>' + TrainNumber + "</b></td>"
        elif item['delayMinutes'] == 0:
            delay = '<td>' + delay + '</td>'
            TrainNumber = '<td>' + TrainNumber + '</td>'
            
        #種別による色分け
        if '快' in TrainType or '新快' in TrainType or '紀州' in TrainType:
            TrainType = '<span id="blue">' + TrainType 
        elif '特急' in TrainType:
            TrainType = '<span id="red">' + TrainType  

        if nick_flag == 1:
            TrainType += '<br><small>' + nick_name + '</small>'
        if change_flag == 1:
            TrainType += '<br><small>' + changed + '</small>'
        
        #html出力処理
        obje = '\t\n<tr><td>' + line_name + '</td>' + TrainNumber + '<td>' + Direction + '</td><td>' + TrainType + '</td><td>' + goto + '</td>' + delay + '<td>' + car + '</td><td>' + position + '</td><td>' + posi2  + '</td></tr>'
        htmlout.append(obje)
        lineout.append(obje)
        raw_object = '\t\n<tr><td>' + line_name + '</td>' + TrainNumber + '<td>' + Direction + '</td><td>' + TrainType + '</td><td>' + goto + '</td>' + delay + '<td>' + car + '</td><td>' + position + '</td><td>' + posi2  +'</td></tr>'
        
        if item['direction'] == 0:
            d0_for.append(goto)
            direct0.append(raw_object)
        elif item['direction'] == 1:
            d1_for.append(goto)
            direct1.append(raw_object)
        

        #遅れ出力処理
        if item['delayMinutes'] != 0:        
            send_line = trt + goto + '行き:' + delay + '分遅れ' + str(position) + 'と' + str(posi2) + '周辺'
            delay_info.append('<li>' + send_line + '</li>')
            oh.html_fix(lineout,line_name,line_name,delay_info)
            chain = 1
        
    #遅延なし出力
    if chain == 0:
        # print('現在遅れはありませんでしたよぉ。安心して出かけろ。')
        delay_info.append('<li>遅れなし</li>') # 遅れなしの場合のHTMLタグ挿入
        oh.html_fix(lineout,line_name,line_name,delay_info)
        chain = 1

    # oh.html_fix(htmlout,line_name,'al',delay_info)
    oh.direc_fix(direct0,direct1,line_name,'allout',delay_info,d0_for,d1_for)