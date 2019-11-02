import csv
import asyncio

async def writeFile(hum, temp):
    
    data = []
    with open('data.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in list(csv_reader)[::-1][0:10000][::-1]:
            if row == []: break
            data.append(row)
            
    data.append([hum,temp])
    with open('data.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in data:
            csv_writer.writerow(row)
    
async def readFile(name):
    
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)[::-1][0:10][::-1]

async def writeCheck(data):
    
    with open('check.csv', mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)
    return

async def checkFile():
    
    with open('check.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)
    
async def deleteFile(name):
    
    f = open(name, 'w+')
    f.close()
    return True

# print(asyncio.get_event_loop().run_until_complete(readFile()))

#with open('data.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    print(list(csv_reader))