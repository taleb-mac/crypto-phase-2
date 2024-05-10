import tkinter as tk
import tkinter.scrolledtext as tkst
import socket
import threading

BUF_SIZE = 4096*1000
HOST = "localhost"
PORT = 9999

class ServerApp():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chat Server")
        self.window.config(bg="lightgrey")
        self.window.resizable(False, False)
        
        self.chat_label = tk.Label(self.window, text="Chat:")
        self.chat_label.config(font=("Arial", 12), bg='lightgrey')
        self.chat_label.pack(padx=20, pady=5)
        
        self.chat_window = tkst.ScrolledText(self.window)
        self.chat_window.config(font=("Arial", 12), state="disabled" )
        self.chat_window.pack(padx= 20, pady=5)
        
        # Initialize server
        threading.Thread(target=self.server).start()
        
        self.window.mainloop()
        
    def server(self):
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind((HOST, PORT))
        server_socket.listen(1)

        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, f'Server is listening...\n')
        self.chat_window.config(state='disabled')
        
        client_socket, client_address = server_socket.accept()
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, f'Connection established with {client_address}\n')
        self.chat_window.config(state='disabled')

        while True:
            data = client_socket.recv(BUF_SIZE)
            if data:
                self.chat_window.config(state='normal')
                self.chat_window.insert(tk.END, f'Client: {data.decode()}\n')
                self.chat_window.config(state='disabled')
                client_socket.sendall(data)

if __name__ == "__main__":
    ServerApp()
