import csv
import asyncio

async def writeData(data):
    with open('data.csv', mode='a') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)
        
async def writeFile(name, data):
    with open(name, mode='w') as csv_file:
        csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow(data)
        
async def readFile(name):
    with open(name) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        return list(csv_reader)
    
async def deleteFile(name):
    f = open(name, 'w+')
    f.close()
    return True

async def find_plant(plant_name):
    
    plantData = await readFile('database.csv')
    for row in plantData:
        if plant_name == row[0]:
            return row
        
    return False

# print(asyncio.get_event_loop().run_until_complete(readFile()))

#with open('data.csv') as csv_file:
#    csv_reader = csv.reader(csv_file, delimiter=',')
#    print(list(csv_reader))