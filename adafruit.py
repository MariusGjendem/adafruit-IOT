import pyfirmata
from Adafruit_IO import Client, Feed, RequestError
import time

run_count = 0
ADAFRUIT_IO_USERNAME = "Resonack"
ADAFRUIT_IO_KEY = "aio_qmUJ99ITqa4l8nV5Rjf66SfShx9X"

aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

board = pyfirmata.Arduino('COM4')

it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin('a:1:i')

try:
 iot = aio.feeds('iot')

except RequestError:
 feed = Feed(name='iot')
 iot = aio.create_feed(feed)

while True:
  print('sending count:', run_count)
  run_count += 1

  potval = analog_input.read()
  aio.send_data('potentiometer', potval)

  data = aio.receive(iot.key)

  print('Data:', data.value)



  time.sleep(3)