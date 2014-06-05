import json
json_data=open('config.json')
data = json.load(json_data)
json_data.close()

num = data[0]
part = data[1]
#print(num)
json_data=open('maxln.json')
data = json.load(json_data)
json_data.close()

for curln in data:
    if num == curln[1]:
        print (""+num+part+curln[3]+curln[2])
