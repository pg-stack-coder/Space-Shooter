import socket as sc,pickle as pi ,threading as th
s=sc.socket(sc.AF_INET,sc.SOCK_STREAM)
port=4576
host='192.168.102.236'
def get(client):
    while True:
        obj=pi.loads(client.recv(2048))
        print(obj)
        client.sendall(pi.dumps('hello speedy'))
        break
try:
    s.bind((host,port))
    print('connected')
except:
    print('could not connect')
s.listen()

while True:
    client,addr=s.accept()
    print('connected to:',addr)
    th.Thread(target=get,args=(client,)).start()