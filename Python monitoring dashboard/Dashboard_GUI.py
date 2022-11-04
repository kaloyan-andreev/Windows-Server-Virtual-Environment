from tkinter import *
import socket
import json
import Database_table as dtb


# Create a stream based socket(i.e, a TCP socket) operating on IPv4 addressing scheme
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Bind and listen
serverSocket.bind(("127.0.0.1", 9090))
serverSocket.listen()


# Create Dashboard GUI app
root = Tk()
root.title("Vlab dashboard")


# Create colunms of the dashboard
label_ID = Label(root, text="ID")
label_IP = Label(root, text="IP")
label_OS = Label(root, text="Operating \n System")
Label_total_CPU_cores = Label(root, text="Total \n CPU cores")
label_Usage_CPU = Label(root, text="CPU \n usage")
label_Total_Mem = Label(root, text="Total \n RAM")
label_Usage_Mem = Label(root, text="RAM \n usage")


# Colunms' grid manager
label_ID.grid(row=0, column=0)
label_IP.grid(row=0, column=1)
label_OS.grid(row=0, column=2)
Label_total_CPU_cores.grid(row=0, column=3)
label_Usage_CPU.grid(row=0, column=4)
label_Total_Mem.grid(row=0, column=5)
label_Usage_Mem.grid(row=0, column=6)


# Create button function
def update_table():
    
    """ COLLECT DATA FROM CLIENTS """
    # Connection 1 data
    id = label1['text']
    ip = label2['text']
    os = label3['text']
    cpu = label4['text']
    ram = label6['text']

    # Connection 2 data
    id = lb1['text']
    ip = lb2['text']
    os = lb3['text']
    cpu = lb4['text']
    ram = lb6['text']

    # Connection 3 data
    id = lbl1['text']
    ip = lbl2['text']
    os = lbl3['text']
    cpu = lbl4['text']
    ram = lbl6['text']

    # Connection 4 data
    id = label_1['text']
    ip = label_2['text']
    os = label_3['text']
    cpu = label_4['text']
    ram = label_6['text']

    # Connection 5 data
    id = lb_1['text']
    ip = lb_2['text']
    os = lb_3['text']
    cpu = lb_4['text']
    ram = lb_6['text']

    # Connection 6 data
    id = lbl_1['text']
    ip = lbl_2['text']
    os = lbl_3['text']
    cpu = lbl_4['text']
    ram = lbl_6['text']


    # Put the collected data into a database
    try:
        dtb.c.execute("INSERT INTO Logs VALUES (:server_id, :server_ip, :os, :total_cpu, :total_ram)",
                        {'server_id': id, 'server_ip': ip, 'os': os, 'total_cpu': cpu, 'total_ram': ram})
        print("Server log was successfully added to the VLAB Database")
        dtb.conn.commit()
        
    except:
        print("Server log already exists!")
        dtb.conn.rollback()
        

#Create update database button
update_but = Button(root, text="Update", padx=60, command=update_table)
update_but.grid(row=8, columnspan=8)


# Create function that cantains the connection methods
def connection():

    # Function that contains the data coming from the client server
    def first_conn():
        global label1
        label1 = Label(root, text=data1["ID"])
        label1.grid(row=1, column=0)

        global label2
        label2 = Label(root, text=data1["IP"])
        label2.grid(row=1, column=1)

        global label3
        label3 = Label(root, text=data1["OS"])
        label3.grid(row=1, column=2)

        global label4
        label4 = Label(root, text=data1["CPU_cores"])
        label4.grid(row=1, column=3)

        label5 = Label(root, text=data1["usage_CPU"])
        label5.grid(row=1, column=4)

        global label6
        label6 = Label(root, text=data1["total_mem"])
        label6.grid(row=1, column=5)

        label7 = Label(root, text=data1["usage_mem"])
        label7.grid(row=1, column=6)

    def second_conn():
        global lb1
        lb1 = Label(root, text=data2["ID"])
        lb1.grid(row=2, column=0)

        global lb2
        lb2 = Label(root, text=data2["IP"])
        lb2.grid(row=2, column=1)

        global lb3
        lb3 = Label(root, text=data2["OS"])
        lb3.grid(row=2, column=2)

        global lb4
        lb4 = Label(root, text=data2["CPU_cores"])
        lb4.grid(row=2, column=3)

        lb5 = Label(root, text=data2["usage_CPU"])
        lb5.grid(row=2, column=4)

        global lb6
        lb6 = Label(root, text=data2["total_mem"])
        lb6.grid(row=2, column=5)

        lb7 = Label(root, text=data2["usage_mem"])
        lb7.grid(row=2, column=6)

    def third_conn():
        global lbl1
        lbl1 = Label(root, text=data3["ID"])
        lbl1.grid(row=3, column=0)

        global lbl2
        lbl2 = Label(root, text=data3["IP"])
        lbl2.grid(row=3, column=1)

        global lbl3
        lbl3 = Label(root, text=data3["OS"])
        lbl3.grid(row=3, column=2)

        global lbl4
        lbl4 = Label(root, text=data3["CPU_cores"])
        lbl4.grid(row=3, column=3)

        lbl5 = Label(root, text=data3["usage_CPU"])
        lbl5.grid(row=3, column=4)

        global lbl6
        lbl6 = Label(root, text=data3["total_mem"])
        lbl6.grid(row=3, column=5)

        lbl7 = Label(root, text=data3["usage_mem"])
        lbl7.grid(row=3, column=6)

    def fourth_conn():
        global label_1
        label_1 = Label(root, text=data4["ID"])
        label_1.grid(row=4, column=0)

        global label_2
        label_2 = Label(root, text=data4["IP"])
        label_2.grid(row=4, column=1)

        global label_3
        label_3 = Label(root, text=data4["OS"])
        label_3.grid(row=4, column=2)

        global label_4
        label_4 = Label(root, text=data4["CPU_cores"])
        label_4.grid(row=4, column=3)

        label_5 = Label(root, text=data4["usage_CPU"])
        label_5.grid(row=4, column=4)

        global label_6
        label_6 = Label(root, text=data4["total_mem"])
        label_6.grid(row=4, column=5)

        label_7 = Label(root, text=data4["usage_mem"])
        label_7.grid(row=4, column=6)

    def fifth_conn():
        global lb_1
        lb_1 = Label(root, text=data5["ID"])
        lb_1.grid(row=5, column=0)

        global lb_2
        lb_2 = Label(root, text=data5["IP"])
        lb_2.grid(row=5, column=1)

        global lb_3
        lb_3 = Label(root, text=data5["OS"])
        lb_3.grid(row=5, column=2)

        global lb_4
        lb_4 = Label(root, text=data5["CPU_cores"])
        lb_4.grid(row=5, column=3)

        lb_5 = Label(root, text=data5["usage_CPU"])
        lb_5.grid(row=5, column=4)

        global lb_6
        lb_6 = Label(root, text=data5["total_mem"])
        lb_6.grid(row=5, column=5)

        lb_7 = Label(root, text=data5["usage_mem"])
        lb_7.grid(row=5, column=6)

    def sixth_conn():
        global lbl_1
        lbl_1 = Label(root, text=data6["ID"])
        lbl_1.grid(row=6, column=0)

        global lbl_2
        lbl_2 = Label(root, text=data6["IP"])
        lbl_2.grid(row=6, column=1)

        global lbl_3
        lbl_3 = Label(root, text=data6["OS"])
        lbl_3.grid(row=6, column=2)

        global lbl_4
        lbl_4 = Label(root, text=data6["CPU_cores"])
        lbl_4.grid(row=6, column=3)

        lbl_5 = Label(root, text=data6["usage_CPU"])
        lbl_5.grid(row=6, column=4)

        global lbl_6
        lbl_6 = Label(root, text=data6["total_mem"])
        lbl_6.grid(row=6, column=5)

        lbl_7 = Label(root, text=data6["usage_mem"])
        lbl_7.grid(row=6, column=6)

    
    # Create a loop that will update the data
    while True:

        """ FIRST CLIENT CONNECTION"""

        # Establishing connection with the client 
        (clientConnected1, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))
        
        # Recieving data from the client
        dataFromClient1 = clientConnected1.recv(1024)
        print(dataFromClient1.decode())

        # Print the data in JSON format
        data1 = json.loads(dataFromClient1.decode())
        first_conn()


        """ SECOND CLIENT CONNECTION"""

        # Establishing connection with first client 
        (clientConnected2, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

        # Recieving data from the client
        dataFromClient2 = clientConnected2.recv(1024)
        print(dataFromClient2.decode())

        # Print the data in JSON format
        data2 = json.loads(dataFromClient2.decode())
        second_conn()


        """ THIRD CLIENT CONNECTION"""

        # Establishing connection with first client 
        (clientConnected3, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

        # Recieving data from the client
        dataFromClient3 = clientConnected3.recv(1024)
        print(dataFromClient3.decode())

        # Print the data in JSON format
        data3 = json.loads(dataFromClient3.decode())
        third_conn()


        """ FOURTH CLIENT CONNECTION"""

        # Establishing connection with first client 
        (clientConnected4, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

        # Recieving data from the client
        dataFromClient4 = clientConnected4.recv(1024)
        print(dataFromClient4.decode())

        # Print the data in JSON format
        data4 = json.loads(dataFromClient4.decode())
        fourth_conn()


        """ FIFTH CLIENT CONNECTION"""

        # Establishing connection with first client 
        (clientConnected5, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

        # Recieving data from the client
        dataFromClient5 = clientConnected5.recv(1024)
        print(dataFromClient5.decode())

        # Print the data in JSON format
        data5 = json.loads(dataFromClient5.decode())
        fifth_conn()


        """ SIXTH CLIENT CONNECTION"""

        # Establishing connection with first client 
        (clientConnected6, clientAddress) = serverSocket.accept()
        print("Accepted a connection request from %s:%s" % (clientAddress[0], clientAddress[1]))

        # Recieving data from the client
        dataFromClient6 = clientConnected6.recv(1024)
        print(dataFromClient6.decode())

        # Print the data in JSON format
        data6 = json.loads(dataFromClient6.decode())
        sixth_conn()


        # Method for updating the data
        root.update()

# Method for updataing the function every 1 second
root.after(1000, connection)

root.mainloop()