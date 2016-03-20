import socket
import sys
import serial

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# # Serial port parameters
serial_speed = 9600
serial_port = '/dev/tty.HC-06-DevB' # bluetooth shield hc-06
#connect to bluetooth

conn_bluetooth = serial.Serial(serial_port, serial_speed, timeout=1)


# Bind the socket to the port
server_address = ('localhost', 10000)
print >>sys.stderr, 'starting up on %s port %s' % server_address
sock.bind(server_address)

# Listen for incoming connections
sock.listen(1)

while True:
	# Wait for a connection
	print >>sys.stderr, 'waiting for a connection'
	connection, client_address = sock.accept()

	try:
		print >>sys.stderr, 'connection from', client_address
		# Receive the data in small chunks and retransmit it
		while True:
			data = int(connection.recv(16))
			print >>sys.stderr, 'received "%s"' % data
			if data:
				print >>sys.stderr, 'sending data back to the client'
				options[data](data)
			else:
				print >>sys.stderr, 'no more data from', client_address
				break
            
	finally:
		# Clean up the connection
		connection.close()

def connect():
    if not conn_bluetooth:
    	conn_bluetooth = serial.Serial(serial_port, serial_speed, timeout=1)
    print ("bluetooth conecting...")

def forward(data):
    conn_bluetooth.write(data)

def reverse():
    conn_bluetooth.write(data)

def stop():
    print "n is a prime number\n"

options = {
		0 : stop,
		1 : reverse,
        2 : forward,    
        5 : connect,
}
		
