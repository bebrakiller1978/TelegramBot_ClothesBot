import json

link1 = 'https://www.farfetch.com/ru/shopping/women/levis-1950s-701-item-16542555.aspx?storeid=9462'
link2 = 'https://www.asos.com/ru/calvin-klein-jeans-plus/chernye-dzhinsy-skinni-s-zavyshennoj-taliej-calvin-klein-jeans-plus/prd/24060103?clr=chernyj-dzhinsovyj&colourWayId=60535749&SearchQuery=%D0%B4%D0%B6%D0%B8%D0%BD%D1%81%D1%8B+calvin+klein&SearchRedirect=true'
link3 = 'https://www.asos.com/ru/armani-exchange/vybelennye-zauzhennye-dzhinsy-armani-exchange-j14/prd/200783995?clr=vybelennyj-sine-goluboj&colourWayId=200784004&SearchQuery=%D0%B4%D0%B6%D0%B8%D0%BD%D1%81%D1%8B+armani'
link4 = 'https://www.farfetch.com/ru/shopping/women/gucci--item-15395384.aspx?storeid=9359'
link5 = 'https://www.yoox.com/ru/42847859FT/item#dept=men&cod10=42847859FT&sizeId=5'

ListOfGeans=[]

geans1 = {'brand':'Levi\'s','color':'Чёрный','size':{'male':{'evro':'S','USA':'31','rus':'46'}, 'female':{'evro':'M','USA':'29','rus':'44'} },'cost':{'rub':19916,'dollar':255},'type':'Прямой крой','link':link1}
ListOfGeans.append(geans1)
geans2 = {'brand':'Calvin Klein','color':'Чёрный','size':{'male':{'evro':'4XL','USA':'42','rus':'58'}, 'female':{'evro':'3XL','USA':'36','rus':'56'} },'cost':{'rub':8490,'dollar':109},'type':'Skinny','link':link2}
ListOfGeans.append(geans2)
geans3 = {'brand':'Armani','color':'Синий','size':{'male':{'evro':'L','USA':'34','rus':'50'}, 'female':{'evro':'L','USA':'31','rus':'48'} },'cost':{'rub':12000,'dollar':154},'type':'Skinny','link':link3}
ListOfGeans.append(geans3)
geans4 = {'brand':'Gucci','color':'Синий', 'size':{'male':{'evro':'','USA':'','rus':''}, 'female':{'evro':'XS','USA':'25','rus':'40'} },'cost':{'rub':68000,'dollar':870},'type':'Расклешенные','link':link4}
ListOfGeans.append(geans4)
geans5 = {'brand':'Tommy Jeans','color':'Синий', 'size':{'male':{'evro':'S','USA':'31','rus':'46'}, 'female':{'evro':'M','USA':'29','rus':'44'} },'cost':{'rub':8900,'dollar':114},'type':'Обычный крой','link':link5}
ListOfGeans.append(geans5)

jsonString = json.dumps(ListOfGeans)
jsonFile = open("data.json", "w")
jsonFile.write(jsonString)
jsonFile.close() 


