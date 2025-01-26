import tkinter as tk

# Fonction de conversion de Fahrenheit à Celsius
def fahrenheit_to_celsius():
    try:
        # Récupérer la valeur saisie et la convertir en float
        fahrenheit = float(ent_temperature.get())
        celsius = (fahrenheit - 32) * 5 / 9  # Formule de conversion
        
        # Déterminer le style du résultat en fonction de la température
        if celsius < 0:
            color = "green"
            emoji = "🥶"
        elif celsius > 35:
            color = "red"
            emoji = "🔥"
        else:
            color = "blue"
            emoji = "🌤️"
        
        # Afficher les étapes du calcul
        calculation = f"Calcul : {fahrenheit}°F - 32 = {fahrenheit - 32} → " \
                      f"({fahrenheit - 32}) * 5 / 9 = {round(celsius, 2)}"
        lbl_calculation.config(text=calculation)
        
        # Afficher le résultat final
        lbl_result.config(text=f"{round(celsius, 2)}°C {emoji}", fg=color)
    except ValueError:
        # Gérer les erreurs si l'entrée n'est pas valide
        lbl_calculation.config(text="Erreur : veuillez entrer un nombre valide.")
        lbl_result.config(text="", fg="black")

# Création de la fenêtre principale
window = tk.Tk()
window.title("Convertisseur de Température")
window.geometry("400x300")  # Définir une taille fixe pour la fenêtre
window.configure(bg="#87CEEB")  # Couleur bleu ciel pour le fond

# Créer un cadre pour l'entrée
frm_entry = tk.Frame(master=window, bg="#87CEEB")

# Widget d'entrée pour la température en Fahrenheit
ent_temperature = tk.Entry(master=frm_entry, width=10, font=("Arial", 14))
lbl_temp = tk.Label(master=frm_entry, text="°F", font=("Arial", 14), bg="#87CEEB")

# Disposer les widgets d'entrée
ent_temperature.grid(row=0, column=0, padx=5, pady=10)
lbl_temp.grid(row=0, column=1, padx=5)

# Bouton pour lancer la conversion
btn_convert = tk.Button(master=window, text="Convertir", command=fahrenheit_to_celsius, font=("Arial", 12), bg="white", width=10)

# Label pour afficher le calcul détaillé
lbl_calculation = tk.Label(master=window, text="", font=("Arial", 10), bg="#87CEEB", wraplength=350)

# Label pour afficher le résultat final
lbl_result = tk.Label(master=window, text="", font=("Arial", 16), bg="#87CEEB")

# Disposition des widgets dans la fenêtre
frm_entry.pack(pady=20)
btn_convert.pack(pady=10)
lbl_calculation.pack(pady=10)
lbl_result.pack(pady=20)

# Lancer la boucle principale
window.mainloop()
