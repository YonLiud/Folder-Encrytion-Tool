from encrypt import encrypt
from decrypt import decrypt
import os

import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox

def main():
    # basic tkinter window
    window = tk.Tk()
    window.minsize(200, 200)
    # open window in center of screen
    
    window.title('Folder Encryption Tool')
    
    def encrypt_folder():
        
        window.withdraw()
        
        encwindow = tk.Toplevel()
        encwindow.minsize(500, 300)
        encwindow.geometry("500x300+{}+{}".format(int(window.winfo_screenwidth()/2-250), int(window.winfo_screenheight()/2-150)))
        
        while True:
            folder = filedialog.askdirectory()
            
            if folder == '':
                messagebox.showerror('Error, No folder specified', 'No folder selected, a folder must be selected to encrypt')
                encwindow.destroy()
                window.deiconify()
            else:
                break
        tk.Label(encwindow, text='Selected folder: ' + folder).pack()   
        
        while True:
            option = None
            key = filedialog.askopenfilename(filetypes=[('Key files', '*.key')])
            tk.Label(encwindow, text="Selected key file: " + str(key)).pack()

            if key == '':
                messagebox.showwarning('No key selected', 'No key has been selected')
                newkey = messagebox.askyesno('No key selected', 'No key selected, would you like to create a new key?')
                if newkey == True:
                    messagebox.showinfo('New key', 'A new key will be created')
                    key = None
                    break
            else:
                break
    
        
        try:
            newpath = encrypt(folder, key)
            messagebox.showinfo('Success', 'Folder encrypted successfully in ' + str(newpath))
        except Exception as e:
            messagebox.showerror('Error', 'Error: ' + str(e))
            messagebox.showwarning('Error', 'An error has occured, please try again')
        encwindow.destroy()
        window.deiconify()
            
        

    def decrypt_folder():
        window.withdraw()
        
        decwindow = tk.Toplevel()
        decwindow.minsize(500, 300)
        decwindow.geometry("500x300+{}+{}".format(int(window.winfo_screenwidth()/2-250), int(window.winfo_screenheight()/2-150)))
        
        while True:
            folder = filedialog.askopenfilename(filetypes=[('Encrypted Folder', '*.secured.tar.gz')])
            
            if folder == '':
                messagebox.showerror('Error, No folder specified', 'No folder selected, a folder must be selected to decrypt')
                decwindow.destroy()
                window.deiconify()
            else:
                break
        tk.Label(decwindow, text='Selected folder: ' + folder).pack()   
        
        while True:
            option = None
            key = filedialog.askopenfilename(filetypes=[('Key files', '*.key')])
            tk.Label(decwindow, text="Selected key file: " + str(key)).pack()

            if key == '':
                messagebox.showwarning('No key selected', 'A key must be selected to decrypt')
            else:
                break
        
        
        try:
            newpath = decrypt(folder, key)
            messagebox.showinfo('Success', 'Folder decrypted successfully in ' + str(newpath))
        except Exception as e:
            messagebox.showerror('Error', 'Error: ' + str(e))
            messagebox.showwarning('Error', 'An error has occured, please try again')
        decwindow.destroy()
        window.deiconify()
        
    tk.Button(window, text='Encrypt Folder', command=encrypt_folder).pack()
    tk.Button(window, text='Decrypt Folder', command=decrypt_folder).pack()
    
    tk.Label(window, text='Source at https://github.com/YonLiud/Folder-Encrytion-Tool', fg="grey").pack(side='bottom')
    tk.Label(window, text='Made by Yonchukku Development [https://yonchukku.dev] ', fg='grey').pack(side='bottom')
    window.mainloop()
    
if __name__ == '__main__':
    main()