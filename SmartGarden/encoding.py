from base64 import b64encode, decodestring, decodebytes
import asyncio

def decodePicture(name):
    file = '/home/pi/Desktop/smartGarden/SmartGarden/Pictures/' + str(name)+".jpg"
    with open(file, "rb") as imageFile:
        encoded = b64encode(imageFile.read())
        return encoded.decode('utf-8')
    
async def encodePicture(encoded):
    fh = open("imageToSave.jpeg", "wb")
    fh.write(decodebytes(encoded))
    fh.close()


