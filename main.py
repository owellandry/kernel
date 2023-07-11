import tkinter as tk
from tkinter import messagebox
import subprocess

def create_users():
    seleccion = option_var.get()
    users = []
    passwords = []

    if seleccion == 1:
        users = ["spukM01-", "spukM02-", "spukT01-", "spukT02-", "spukN01-"]
        passwords = ['SpMT1*@1@1$', 'SpMT2$0201*', 'SpTT1E01/23', 'SpTT2E@2/23', 'SpNT1TCD/23']
    elif seleccion == 2:
        users = ["apolM01-", "apolM02-", "apolT01-", "apolT02-", "apolN01-"]
        passwords = ['ApMT1*@1@1$', 'ApMT2$0201*', 'ApTT1E01/23', 'ApTT2E@2/23', 'ApNT1TCD/23']
    elif seleccion == 3:
        users = ["arteM01-", "arteM02-", "arteT01-", "arteT02-", "arteN01-"]
        passwords = ['AtMT1*@1@1$', 'AtMT2$0201*', 'AtTT1E01/23', 'AtTT2E@2/23', 'AtNT1TCD/23']
    elif seleccion == 4:
        users = ["skylab-"]
        passwords = ['campus2023']
    elif seleccion == 5:
        users = ["salyut-"]
        passwords = ['campus2023']
    elif seleccion == 6:
        users = ["campus-"]
        passwords = ['campus2023']
    elif seleccion == 7:
        users = ["ikaros-"]
        passwords = ['campus2023']
    elif seleccion == 8:
        users = ["ulysses-"]
        passwords = ['campus2023']
    else:
        messagebox.showerror("Error", "Opción inválida")
        return

    opcion = pc_entry.get()

    for i in range(len(users)):
        user = users[i] + opcion
        password = passwords[i]

        subprocess.run(["sudo", "useradd", "-m", user])
        subprocess.run(["sudo", "passwd", user], input=(password + '\n' + password).encode())

        subprocess.run(["sudo", "chsh", "-s", "/bin/bash", user])

    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

    subprocess.run(["cd", "Downloads"])
    subprocess.run(["sudo", "apt-get", "install", "gdebi", "-y"])
    subprocess.run(["sudo", "apt-get", "install", "curl", "-y"])
    subprocess.run(["sudo", "apt-get", "install", "htop", "-y"])
    subprocess.run(["sudo", "apt-get", "install", "python3-pip", "-y"])
    subprocess.run(["sudo", "add-apt-repository", "ppa:obsproject/obs-studio", "-y"])
    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "install", "obs-studio", "-y"])
    subprocess.run(["sudo", "wget", "-cO", "-", "'https://code.visualstudio.com/sha/download?build=stable&os=linux-deb-x64'"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "wget", "-cO", "-", "'https://download.typora.io/linux/typora_1.4.1-dev_amd64.deb'"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "wget", "-cO", "-", "'https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb'"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "wget", "'https://download-installer.cdn.mozilla.net/pub/devedition/releases/112.0b9/linux-x86_64/es-ES/firefox-112.0b9.tar.bz2'"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "wget", "-cO", "-", "'https://dl.discordapp.net/apps/linux/0.0.26/discord-0.0.26.deb'"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "gdebi", "google.deb"])
    subprocess.run(["sudo", "gdebi", "visualCode.deb"])
    subprocess.run(["sudo", "gdebi", "typora.deb"])
    subprocess.run(["sudo", "gdebi", "discord.deb"])
    subprocess.run(["sudo", "apt", "install", "git", "gitk", "-y"])

    subprocess.run(["cd", ".."])

    sala = ""
    opcion = sala_entry.get()

    if opcion == 1:
        sala = "spuk *"
    elif opcion == 2:
        sala = "apol *"
    elif opcion == 3:
        sala = "arte *"
    elif opcion == 4:
        sala = "skylab *"
    elif opcion == 5:
        sala = "salyut *"
    elif opcion == 6:
        sala = "campus *"
    elif opcion == 7:
        sala = "ikaros *"
    elif opcion == 8:
        sala = "ulysses *"
    else:
        messagebox.showerror("Error", "Opción inválida")
        return

    lista_usuarios = subprocess.run(["cut", "-d:", "-f1", "/etc/passwd"], capture_output=True, text=True).stdout
    lista_usuarios_ordenada = subprocess.run(["echo", lista_usuarios], capture_output=True, text=True).stdout
    subprocess.run(["curl", "-o-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh"])
    subprocess.run(["curl", "-o-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh", "|", "bash"])
    subprocess.run(["cd"])
    subprocess.run(["source", "~/.bashrc"])

    for usuario in lista_usuarios_ordenada:
        subprocess.run(["sudo", "su", usuario, "-c", "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh"])
        subprocess.run(["sudo", "su", usuario, "-c", "curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh | bash"])
        subprocess.run(["sudo", "su", usuario, "-c", "cd && source ~/.bashrc"])

    subprocess.run(["curl", "-o-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh"])
    subprocess.run(["curl", "-o-", "https://raw.githubusercontent.com/nvm-sh/nvm/v0.35.3/install.sh", "|", "bash"])
    subprocess.run(["source", "~/.bashrc"])

    subprocess.run(["sudo", "wget", "-cO", "-", "'https://downloads.mongodb.com/compass/mongodb-compass_1.36.2_amd64.deb'"],
                   stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    subprocess.run(["sudo", "dpkg", "-i", "compass.deb"])

    subprocess.run(["sudo", "apt", "install", "apache2", "-y"])
    subprocess.run(["sudo", "apt", "install", "php", "libapache2-mod-php", "php-mysql", "-y"])
    subprocess.run(["sudo", "ufw", "allow", "Apache"])
    subprocess.run(["sudo", "ufw", "enable"])
    subprocess.run(["cd", "/var/www/html/"])
    subprocess.run(["sudo", "rm", "-r", "index.html"])

    for usuario in lista_usuarios_ordenada:
        carpeta = usuario.replace("a", "A").replace("s", "S").replace("m", "M").replace("n", "N").replace("i", "I").replace("u", "U").replace("c", "C").replace("t", "T")
        subprocess.run(["sudo", "mkdir", carpeta])
        subprocess.run(["sudo", "chown", f"{usuario}:{usuario}", carpeta])
        subprocess.run(["sudo", "chmod", "u+rwx", carpeta])

    subprocess.run(["sudo", "chmod", "-R", "755", "/var/www/html"])
    subprocess.run(["sudo", "touch", "/etc/apache2/sites-available/your_domain.conf"])
    subprocess.run(["sudo", "echo", "-e", "\"<VirtualHost *:80>\nServerAdmin webmaster@localhost\nServerName html\nServerAlias www.html\nDocumentRoot /var/www/html\nErrorLog ${APACHE_LOG_DIR}/error.log\nCustomLog ${APACHE_LOG_DIR}/access.log combined\n</VirtualHost>\" | sudo tee /etc/apache2/sites-available/your_domain.conf"])
    subprocess.run(["sudo", "a2ensite", "your_domain.conf"])
    subprocess.run(["sudo", "a2dissite", "000-default.conf"])
    subprocess.run(["sudo", "apache2ctl", "configtest"])
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])
    subprocess.run(["sudo", "a2dismod", "mpm_event"])
    subprocess.run(["sudo", "a2enmod", "mpm_prefork"])
    subprocess.run(["sudo", "a2enmod", "php8.1"])
    subprocess.run(["sudo", "systemctl", "restart", "apache2"])

    subprocess.run(["cd"])

    subprocess.run(["sudo", "apt", "install", "mysql-server", "-y"])
    subprocess.run(["sudo", "touch", "script.sql"])
    subprocess.run(["sudo", "echo", "-e", "\"CREATE USER 'campus'@'%' IDENTIFIED WITH mysql_native_password BY 'campus2023'; GRANT ALL PRIVILEGES ON *.* TO 'campus'@'%';\" | sudo tee script.sql"])
    subprocess.run(["sudo", "mysql", "<", "script.sql"])
    subprocess.run(["sudo", "rm", "script.sql"])

    subprocess.run(["cd", "Downloads"])
    subprocess.run(["sudo", "cp", "-rp", "firefox-112.0b9.tar.bz2", "/opt/"])
    subprocess.run(["cd", "/opt/"])
    subprocess.run(["sudo", "tar", "xjf", "firefox-112.0b9.tar.bz2"])
    subprocess.run(["sudo", "rm", "-rf", "firefox-112.0b9.tar.bz2"])
    subprocess.run(["sudo", "chown", "-R", "$USER", "/opt/firefox/"])
    subprocess.run(["sudo", "touch", "~/.local/share/applications/firefox_dev.desktop"])
    subprocess.run(["sudo", "echo", "-e", "\"[Desktop Entry]\nName=Firefox Developer\nGenericName=Firefox Developer Edition\nExec=/opt/firefox/firefox %u\nTerminal=false\nIcon=/opt/firefox/browser/chrome/icons/default/default128.png\nType=Application\nCategories=Application;Network;X-Developer;\nComment=Firefox Developer Edition Web Browser.\nStartupWMClass=Firefox Developer Edition\" | sudo tee ~/.local/share/applications/firefox_dev.desktop"])
    subprocess.run(["sudo", "chmod", "+x", "~/.local/share/applications/firefox_dev.desktop"])
    subprocess.run(["cd"])

    subprocess.run(["sudo", "apt", "update"])
    subprocess.run(["sudo", "apt", "upgrade", "-y"])

# Crear la ventana principal
window = tk.Tk()
window.title("Creación de usuarios")
window.geometry("400x300")

# Etiqueta y entrada para el número de PC
pc_label = tk.Label(window, text="Ingrese el número del PC:")
pc_label.pack()

pc_entry = tk.Entry(window)
pc_entry.pack()

# Etiqueta y opción de selección de la sala
option_label = tk.Label(window, text="Seleccione la sala:")
option_label.pack()

option_var = tk.IntVar()

option_1 = tk.Radiobutton(window, text="Sputnik", variable=option_var, value=1)
option_1.pack()

option_2 = tk.Radiobutton(window, text="Apolo", variable=option_var, value=2)
option_2.pack()

option_3 = tk.Radiobutton(window, text="Artemis", variable=option_var, value=3)
option_3.pack()

option_4 = tk.Radiobutton(window, text="Skylab", variable=option_var, value=4)
option_4.pack()

option_5 = tk.Radiobutton(window, text="Salyut", variable=option_var, value=5)
option_5.pack()

option_6 = tk.Radiobutton(window, text="Campus", variable=option_var, value=6)
option_6.pack()

option_7 = tk.Radiobutton(window, text="Ikaros", variable=option_var, value=7)
option_7.pack()

option_8 = tk.Radiobutton(window, text="Ulysses", variable=option_var, value=8)
option_8.pack()

# Botón para crear los usuarios
create_button = tk.Button(window, text="Crear usuarios", command=create_users)
create_button.pack()

# Ejecutar la ventana principal
window.mainloop()
