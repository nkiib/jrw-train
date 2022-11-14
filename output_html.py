import os
import datetime as dt
from itertools import zip_longest
import pandas_datareader.data as pdr

def output_html(filename , str1 ,filetype): # 出力処理
    path1 = os.path.dirname(__file__) + "/" 
    file1 = path1 + filename + '.' +filetype
    write1( file1, str1 ) 
    #print(filename)
    #print(path1 + ' に '+ filename + filetype + ' を出力')

def write1( file1, str1 ): # ファイルの編集処理
    with open( file1, 'w', encoding='utf-8' ) as f1: 
        f1.write( str1 ) 
    return 0

def edit_html(trainfo,line,file,delay_in):
    
    now = dt.datetime.today()

    result = pdr.get_quote_yahoo('JPY=X')
    ary_result = result["price"].values
    price = ary_result[0]
    
    #print('test')
    #print(trainfo)
    str1 = '''
    <!DOCTYPE html>
    <html lang=ja>

    <head>
        <meta charset="utf-8">
        <title>{line_code}JR遅延</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="format-detection" content="telephone=no">
        <link rel="stylesheet" href="style.css">
    </head>
    <body>
        <h1>現在の運行状態</h1>
        <h2>{line_code}</h2>

        {date}
        <br>現在のドル円：{rate}
        <h3>現在の遅れ電車まとめ</h3>
        <ul>
        {delay_info}
        </ul>
        <div id="main">
            <table>
                <thead>
                    <tr>
                        <th>路線名</th>
                        <th>列車番号</th>
                        <th>向き</th>
                        <th>種別</th>
                        <th>行先</th>
                        <th>遅れ時間</th>
                        <th>両数</th>
                        <th>現在地</th>
                        <th>現在地</th>
                    </tr>
                </thead>
                <tbody>
                    {table}
                </tbody>
            </table>
        </div>
    </body>
    '''.format(line_code = line,table = trainfo , date = now,delay_info = delay_in,rate = price)

    output_html(file,str1,'html')

def html_directout(direct0,direct1,line,file,delay_in,d0_go,d1_go):
    

    result = pdr.get_quote_yahoo('JPY=X')
    ary_result = result["price"].values
    price = ary_result[0]

    now = dt.datetime.today()
    #print('test')
    #print(trainfo)
    str1 = '''
    <!DOCTYPE html>
    <html lang=ja>

    <head>
        <meta charset="utf-8">
        <title>{line_code}JR遅延</title>
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <meta name="format-detection" content="telephone=no">
        <link rel="stylesheet" href="style.css">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=DotGothic16&display=swap');
        </style>
    </head>
    <body>
        <h1>現在の運行状態</h1>
        <h2>{line_code}</h2>

        {date}
        <br>現在のドル円：1USD = {rate}JPY
        <h3>現在の遅れ電車まとめ</h3>
        <details>
            <summary>遅れ一覧</summary>
                <ul>
                {delay_info}
                </ul>
        </details>
        <h3>現在の走行列車一覧</h3>
        <details open>
        <summary><b>{go0}</b>方面</summary>
            <div id="main">
                <table>
                    <thead>
                        <tr>
                            <th>路線名</th>
                            <th>列車番号</th>
                            <th>向き</th>
                            <th>種別</th>
                            <th>行先</th>
                            <th>遅れ時間</th>
                            <th>両数</th>
                            <th>現在地</th>
                            <th>現在地</th>
                        </tr>
                    </thead>
                    <tbody>
                        {table0}
                    </tbody>
                </table>
            </div>
        </details>
        <hr>
        <details open>
        <summary><b>{go1}</b>方面</summary>
        <div id="main">
            <table>
                <thead>
                    <tr>
                        <th>路線名</th>
                        <th>列車番号</th>
                        <th>向き</th>
                        <th>種別</th>
                        <th>行先</th>
                        <th>遅れ時間</th>
                        <th>両数</th>
                        <th>現在地</th>
                        <th>現在地</th>
                    </tr>
                </thead>
                <tbody>
                    {table1}
                </tbody>
            </table>
        </div>
        </details>
    </body>
    '''.format(line_code = line,table0 = direct0 , table1 = direct1 ,date = now,delay_info = delay_in,go0 = d0_go,go1 = d1_go,rate = price)

    output_html(file,str1,'html')

def direc_fix(direct0 ,direct1 ,line ,file ,delay,d0_for,d1_for):
    out0 = ''
    out1 = ''
    delayout = ''
    d0_go = ''
    d1_go = ''

    for d0,d1,g0,g1,d,ln in zip_longest(direct0,direct1,d0_for,d1_for,delay,line,fillvalue=''):
        out0 += d0
        out1 += d1

        if g0 not in d0_go:
            d0_go += g0 + '・' 
        if g1 not in d1_go:
            d1_go += g1 + '・'
        delayout += d
    d0_go = d0_go[:-1]
    d1_go = d1_go[:-1]
    html_directout(out0,out1,line,file,delayout,d0_go,d1_go)

def html_fix(htmlout,line,file,delay):
    out = ''
    delayout = ''
    for h in htmlout:
        out += h
    for d in delay:
        delayout += d + '\n'
    edit_html(out,line,file,delayout)