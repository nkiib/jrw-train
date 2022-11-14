import process as pro
import sec

def main():
    pro.line_alfa()
    choise_line = input('取得したい路線をアルファベットで取得')

    line_name = sec.sec(choise_line)

    if line_name == 'A':
        pro.output('hokurikubiwako')
        pro.output('kyoto')
        pro.output('kobesanyo')
        pro.output('ako')
    elif line_name == 'E':
        pro.output('sagano')
        pro.output('sanin1')
        pro.output('sanin2')
    elif line_name == 'G':
        pro.output('takarazuka')
        pro.output('fukuchiyama')
    elif line_name == 'H':
        pro.output('tozai')
        pro.output('gakkentoshi')
    elif line_name == 'T':
        pro.output('wakayama2')
        pro.output('wakayama2')
    else:
        pro.output(line_name)
    return 0

main()
