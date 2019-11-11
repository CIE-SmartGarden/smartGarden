import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008
import time
import asyncio

SPI_PORT   = 0
SPI_DEVICE = 0
mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def mapping(val, maxval):
    return 100 - (val/maxval)*100
    
async def moisture():
    values = mcp.read_adc(0)
    return (round(mapping(values, 1023), 2))

asyncio.get_event_loop().run_until_complete(moisture())
