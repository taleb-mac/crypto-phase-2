import tkinter as tk
import tkinter.scrolledtext as tkst
import socket
import threading

BUF_SIZE = 4096*1000
HOST = "localhost"
PORT = 9999

class ClientApp():
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Chat Client")
        self.window.config(bg="lightgrey")
        self.window.resizable(False, False)
        
        self.chat_label = tk.Label(self.window, text="Chat:")
        self.chat_label.config(font=("Arial", 12), bg='lightgrey')
        self.chat_label.pack(padx=20, pady=5)
        
        self.chat_window = tkst.ScrolledText(self.window)
        self.chat_window.insert(tk.END, f'Connection Established\n')
        self.chat_window.config(font=("Arial", 12), state="disabled" )
        self.chat_window.pack(padx= 20, pady=5)
        
        self.message_label = tk.Label(self.window, text="Message:")
        self.message_label.config(font=("Arial", 12), bg='lightgrey' )
        self.message_label.pack(padx= 20, pady=5, side=tk.LEFT)
        
        self.message_entry = tk.Entry(self.window)
        self.message_entry.config(font=("Arial", 12), width=50)
        self.message_entry.pack(padx= 20, pady=5, side=tk.LEFT)
        
        self.send_button = tk.Button(self.window, width=12, text="Send", bg="white", activebackground="lightgrey")
        self.send_button.config(font=("Arial", 12), command=self.message)
        self.send_button.pack(padx= 20, pady=5)
        
        # Initialize client
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client_socket.connect((HOST, PORT))
        threading.Thread(target=self.receive).start()
        
        self.window.mainloop()
        
    def message(self):
        message = self.message_entry.get()
        self.message_entry.delete(0, tk.END)
        self.chat_window.config(state='normal')
        self.chat_window.insert(tk.END, f'Me: {message}\n')
        self.client_socket.sendall(message.encode())
        
    def receive(self):
        while True:
            data = self.client_socket.recv(BUF_SIZE)
            if data:
                self.chat_window.config(state='normal')
                self.chat_window.insert(tk.END, f'Server: {data.decode()}\n')
                self.chat_window.config(state='disabled')

if __name__ == "__main__":
    ClientApp()
