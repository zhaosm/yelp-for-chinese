# python .\api_main.py -inst .\api_new.csv -forChinese True -key 'Bar,Ba' -filter {'categories':['Japanese'],'price':[2],'rating':['1-5']}
import argparse
from display import main as display

def api_main():
    parser = argparse.ArgumentParser(description='api')
    parser.add_argument('-inst', required = True, dest='filename', action='store', help='Input file name')
    parser.add_argument('-forChinese', required = False, dest='forChinese', action='store', help='Chinese or total')
    parser.add_argument('-key', required = True, dest='keywords', action='store', help='keywords used')
    parser.add_argument('-filter', required = False, dest='filter', action='store', help='filter used')
    args = parser.parse_args()
    display(filename = args.filename, forChinese=args.forChinese, keywords = args.keywords, filter = args.filter)

if __name__ == '__main__':
    api_main()