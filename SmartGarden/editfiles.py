import csv
import asyncio
        
async def writeFile(name, data):
    with open(name, mode='a') as csv_file:
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

async def find_data(data, file):
    fileData = await readFile(file)
    for row in fileData:
        if data == row[0]:
            return row
    return False
