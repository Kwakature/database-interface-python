import dep as d
import tkinter as tk
#command test
#print(d.recherche("[requette]", "[ip serv]", "[user name]", "[password]", "[databases]"))

#--------------page principale----------------
def open_main_page(ip_serv, user, mdp, database):
    """Open the main page of the application."""
    root = tk.Tk()
    root.title("Main Page")
    root.geometry("400x300")

    def on_click(requete):
        resultat = d.recherche(requete, ip_serv, user, mdp, database)           #voir l erreur sur le boutton de recherche numero 1
        message.config(text=resultat)
    
    tk.Label(root, text="Recherche").pack()
    
    tout_donnee = tk.Button(root, text="toute depence", command=lambda: on_click("SELECT * FROM depences")) #numero 1 
    tout_donnee.pack()
    
    message = tk.Message(root, text="...")
    message.pack()

    button = tk.Button(root, text="Exit", command=root.quit)
    button.pack(pady=10)

    root.mainloop()

#--------------recuperation des infos de connection----------------
def se_connecter():
    ip = ip_serv.get()
    utilisateur = username_entry.get()
    password = password_entry.get()
    database = database_entry.get()

    login_window.destroy()
    open_main_page(ip, utilisateur, password, database)

#--------------page de connexion----------------
login_window = tk.Tk()
login_window.title("Login")
login_window.geometry("300x250")

tk.Label(login_window, text="IP serv").pack()
ip_serv = tk.Entry(login_window)
ip_serv.pack()

tk.Label(login_window, text="Nom Utilisateur").pack()
username_entry = tk.Entry(login_window)
username_entry.pack()

tk.Label(login_window, text="Mot de Passe").pack()
password_entry = tk.Entry(login_window, show='*')
password_entry.pack()

tk.Label(login_window, text="Base de Données").pack()
database_entry = tk.Entry(login_window)
database_entry.pack()

tk.Button(login_window, text="Se connecter", command=se_connecter).pack()

login_window.mainloop()