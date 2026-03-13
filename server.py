import socket

sock = socket.socket()

sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(('', 9090))
sock.listen(0)
conn, addr = sock.accept()
print(addr)

msg = ''

while True:
	data = conn.recv(1024)
	if not data:
		break
	msg += data.decode()
	conn.send(data)

print(msg)

conn.close()
