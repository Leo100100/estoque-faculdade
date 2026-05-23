import customtkinter as ctk

ctk.set_appearance_mode("light")

app = ctk.CTk()
app.geometry("400x300")

label = ctk.CTkLabel(app, text="Teste")
label.pack(pady=20)

app.mainloop()
