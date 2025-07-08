import tkinter as tk
from tkinter import messagebox

def proses_login():
    """
    Mengambil input dari user, memvalidasinya, 
    dan menampilkan pesan sesuai hasilnya.
    """
    username = entry_username.get()
    password = entry_password.get()

    # username dan password 
    if username == "Gilang" and password == "Teles123":
        messagebox.showinfo("Login Berhasil", f"Anjaii si {username}!")
    else:
        messagebox.showerror("Login Gagal", "Username atau Password salah.")

def toggle_password_visibility():
    """
    Mengubah visibilitas karakter password antara '*' dan teks sebenarnya.
    """
    if entry_password.cget('show') == '*':
        entry_password.config(show='')
        show_button.config(text='Hide')
    else:
        entry_password.config(show='*')
        show_button.config(text='Show')

# jendela utama aplikasi
window = tk.Tk()
window.title("Halaman Login")
window.geometry("350x200") 
window.resizable(False, False) 
# Frame widget 
main_frame = tk.Frame(window, padx=20, pady=20)
main_frame.pack(expand=True)

# Label dan Entry Username
label_username = tk.Label(main_frame, text="Username:")
label_username.pack(pady=(0, 5))

entry_username = tk.Entry(main_frame, width=30)
entry_username.pack()

# Label dan Entry Password
password_frame = tk.Frame(main_frame)
password_frame.pack(pady=(10, 5), fill='x') 

label_password = tk.Label(password_frame, text="Password:")
label_password.grid(row=0, column=0, sticky='w') 

entry_password = tk.Entry(password_frame, width=25, show="*") 
entry_password.grid(row=1, column=0, padx=(0, 5), sticky='ew') 
show_button = tk.Button(
    password_frame,
    text="Show",
    command=toggle_password_visibility,
    width=5
)
show_button.grid(row=1, column=1, sticky='e') 

# Tombol Login
button_login = tk.Button(
    main_frame,
    text="Login",
    command=proses_login,
    width=15,
    height=10
)
button_login.pack(pady=20)

# Menjalankan aplikasi
window.mainloop()