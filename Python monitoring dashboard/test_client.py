import socket
from Dashboard_data import *
import json


while True:
    # Create a client socket
    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    # Connect to the server
    clientSocket.connect(("127.0.0.1",9090));

    # Send data to server
    def get_data():
        data_id = ID()
        data_ip = ip()
        data_os = OS()
        data_cpu_cores = cpu_cores()
        data_usage_cpu = cpu_usage()
        data_total_mem = total_memory()
        data_usage_mem = memory_usage()


        x = "{}"
        y = {
            "ID": data_id,
            "IP": data_ip,
            "OS": data_os,
            "CPU_cores": data_cpu_cores,
            "usage_CPU": data_usage_cpu,
            "total_mem": data_total_mem,
            "usage_mem": data_usage_mem,

        }
        z = json.loads(x)
        z.update(y)
        return json.dumps(z)

    # Send data to the server
    clientSocket.send(get_data().encode())
    print("sent")

    # Close connection
    clientSocket.close()
