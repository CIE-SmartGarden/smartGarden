import csv
import asyncio

async def writeFile(hum, temp):
    with open('data.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([hum,temp])
    
async def readFile(name):
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)

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