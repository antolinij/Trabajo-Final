import socket
import sys
import serial

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.HC-06-DevB' # bluetooth shield hc-06, ls /dev/tty.*
#connect to bluetooth
conn_bluetooth = serial.Serial(serial_port, serial_speed, timeout=1)

# Bind the socket to the port
server_address = ('localhost', 10000)
print (server_address)
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	#print >>sys.stderr, 'waiting for a connection'
	print ("esperando conecciones...")
	connection, client_address = sock.accept()
	#conn_bluetooth.write('0'.encode('ascii'))

	try:
		#print >>sys.stderr, 'connection from', client_address
		# Receive the data in small chunks and retransmit it
		while True:
			data = connection.recv(16)
			data = data.decode('utf-8')
			print ("recibido...")
			print (data)
			if data == '5':
				print ("conectado..")
				break
			elif data == '1':
				print ("marcha atras")
				conn_bluetooth.write('1'.encode('ascii'))
				#conn_bluetooth.write(data.encode('ascii'))
				break
			elif data == '2':
				print ("marcha adelante")
				conn_bluetooth.write('2'.encode('ascii'))
				#conn_bluetooth.write(data.encode('ascii'))
				break
			elif data == '0':
				print ("detenido")
				conn_bluetooth.write('0'.encode('ascii'))
				#conn_bluetooth.write(data.encode('ascii'))
				break
			else:
				print ("no mas info...")
				break
            
	finally:
		# Clean up the connection
		connection.close()

		
