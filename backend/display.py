import csv
import json
import ast

def main():
#def main(filename,forChinese=False,keywords='',filter={}):

    filename = request.args.get('filename')
    forChinese = request.args.get('forChinese')
    keywords = request.args.get('key')
    filter = request.args.get('filter')

    data=[]
    with open(filename) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for line in readCSV:
            if line[0]=='img':
                continue
            data.append(line)

    if forChinese:
        data=sorted(data, key=lambda x:x[1],reverse=True)
    else:
        data=sorted(data, key=lambda x:x[2],reverse=True)

    keywords=keywords[1:-1]
    key=keywords.split(',')
    tmp_out=data
    for item in key:
        tmp_data=[]
        for datam in tmp_out:
            if item in datam[5]:
                tmp_data.append(datam)
        tmp_out=tmp_data

    tmp_filter=ast.literal_eval(filter)
    lists=list(tmp_filter.keys())
    matching={'img':0,'rating_Chinese':1,'rating':2,'numReviews':3,'price':4,'name':5,'type':6,'address':7,'business_id':8,'categories':9,'phone':10}
    for item in lists:
        for word in tmp_filter[item]:
            tmp_data=[]
            if item=='categories':
                for datam in tmp_out:
                    if word in datam[matching[item]]:
                        tmp_data.append(datam)
            elif item=='price':
                for datam in tmp_out:
                    if len(datam[matching[item]])==word:
                        tmp_data.append(datam)
            elif item=='rating':
                if forChinese:
                    word=word.split('-')
                    for datam in tmp_out:
                        if int(word[0])<float(datam[matching['rating_Chinese']])<int(word[1]):
                            tmp_data.append(datam)
                else:
                    word=word.split('-')
                    for datam in tmp_out:
                        if int(word[0])<float(datam[matching['rating']])<int(word[1]):
                            tmp_data.append(datam)
            tmp_out=tmp_data

    res=['img','rating_Chinese','rating','numReviews','cost','name','type','address','business_id','categories','phone']

    final_output = []
    for i in range(10):
        for j in range(11):
            tmp_out[i][j]=str(res[j])+':'+tmp_out[i][j]
        final_output.append(ast.literal_eval("{" + str(tmp_out[i]).replace('",', ',').replace(':', '":"').replace('":"//','://').replace("[", "").replace("]", "").replace("'",'"')[:-1] +'", "rank"'+':"'+str(i)+'"}'))

    print(final_output)


if __name__ == "__main__":
    filename='api_database.csv'
    main(filename,forChinese=False,keywords='Bar,Ba',filter={"categories":["Japanese"]})