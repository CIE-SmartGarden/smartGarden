from base64 import b64encode, decodestring, decodebytes
import asyncio

async def decodePicture(name):
    file = str(name)+".jpeg"
    with open(file, "rb") as imageFile:
        encoded = b64encode(imageFile.read())
        return encoded
    
async def encodePicture(encoded):
    fh = open("imageToSave.jpeg", "wb")
    fh.write(decodebytes(encoded))
    fh.close()
