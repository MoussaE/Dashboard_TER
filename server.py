from waitress import serve
from main import server
import socket

host = socket.gethostbyname(socket.gethostname())
print(host)
serve(server,host=host,port=8050)