import serial
import time



try:
	
	print("Listening on /dev/ttyACM0... Press CTRL+C to exit")
	
	ser = serial.Serial(port='/dev/ttyACM0', baudrate=115200, timeout=1)

	while True:
	
		msg = ser.readline()
		smsg = msg.decode('utf-8').strip()
		
		if len(smsg) > 0:
		
			print('RX:{}'.format(smsg))
			
			response = input('Enter Response = ')
			response = response + '\r\n'
			ser.write(str.encode(response))			
			print('Response sent...')
			
		time.sleep(1)

except KeyboardInterrupt:

	if ser.is_open:
		ser.close()
	
	print("Program terminated!")