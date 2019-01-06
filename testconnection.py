import json
import socket

def gethosts(data):
    return data["hosts"]


def isOpen(host, port):
    timeout = 1 #timeout for 1 second if port blocked
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.settimeout(timeout)
        s.connect((host, int(port)))
        s.shutdown(2)
        return True
    except:
        return False

def get_status(host, portlist):
    result=[]

    for p in portlist:
        if isOpen(host,p):
            status = 'open'
        else:
            status = 'closed'
        
        result.append ({ 
                "host": host, "port": p, "status": status 
            })
    return result


if __name__ == '__main__':
    filename = 'config.json'
    with open(filename, "r") as f:
        data = json.loads(f.read())

    hostlist = gethosts(data)

    arr = []

    for x in hostlist:
        arr.append(get_status(x['host'], x['ports']))
    print(arr)

  


