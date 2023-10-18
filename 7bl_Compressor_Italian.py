# Nome Software: 7bl Compressore con Crittografia
# Autore: Bocaletto Luca
# Descrizione: Questo software offre la possibilità di comprimere, crittografare ed estrarre file. 
# Consente agli utenti di selezionare file da archiviare o da cui estrarre, specificare una chiave di crittografia,
# e generare archivi crittografati. È uno strumento utile per proteggere e comprimere i dati sensibili.
# Importa i moduli necessari
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
import zlib
import os
import traceback
from tkinter import filedialog
from cryptography.fernet import InvalidToken

# Definizione della classe principale dell'applicazione
class SevenBLCompressor:
    def __init__(self, window):
        self.window = window
        self.window.title("7bl Compressore con Crittografia")  # Imposta il titolo della finestra
        self.window.configure(bg="#f5f5f5")  # Imposta il colore di sfondo della finestra

        # Creazione e posizionamento degli elementi dell'interfaccia utente
        self.create_ui_elements()

    def create_ui_elements(self):
        self.file_label = tk.Label(self.window, text="7bl Compressore con Crittografia", font=("Helvetica", 20))
        self.file_label.pack()
        # Etichette, liste, campi di input, e pulsanti
        self.file_label = tk.Label(self.window, text="File da archiviare/estraire:")
        self.file_label.pack()

        self.file_listbox = tk.Listbox(self.window, selectmode=tk.MULTIPLE, width=50)
        self.file_listbox.pack()

        self.browse_input_button = tk.Button(self.window, text="Sfoglia", command=self.browse_input_files)
        self.browse_input_button.pack()

        self.output_label = tk.Label(self.window, text="File archiviato/estratto:")
        self.output_label.pack()

        self.output_entry = tk.Entry(self.window, width=50)
        self.output_entry.pack()

        self.browse_output_button = tk.Button(self.window, text="Sfoglia", command=self.browse_output_directory)
        self.browse_output_button.pack()

        self.key_label = tk.Label(self.window, text="Chiave di crittografia:")
        self.key_label.pack()

        self.key_entry = tk.Entry(self.window, width=50)
        self.key_entry.pack()

        self.generate_key_button = tk.Button(self.window, text="Genera Chiave Casuale", command=self.generate_and_set_key)
        self.generate_key_button.pack()

        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack()

        self.create_archive_button = tk.Button(self.window, text="Crea Archivio", command=self.on_create_archive_button_click)
        self.create_archive_button.pack()

        self.extract_archive_button = tk.Button(self.window, text="Estrai dall'Archivio", command=self.on_extract_archive_button_click)
        self.extract_archive_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Personalizzazione dei colori dei pulsanti
        self.create_archive_button.config(bg="#4CAF50", fg="white")
        self.extract_archive_button.config(bg="#4CAF50", fg="white")

    # Gestisce la selezione di file da archiviare/estraire
    def browse_input_files(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.file_listbox.delete(0, tk.END)
            for file_path in file_paths:
                self.file_listbox.insert(tk.END, file_path)

    # Gestisce la selezione della cartella di destinazione
    def browse_output_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory_path)

    # Genera una chiave casuale e la visualizza nell'interfaccia
    def generate_key(self):
        return Fernet.generate_key()

    def generate_and_set_key(self):
        key = self.generate_key()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key.decode())

    # Comprime e crittografa un file
    def compress_and_encrypt_file(self, input_file, output_file, key):
        try:
            with open(input_file, 'rb') as infile:
                data = infile.read()
                compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)
                encrypted_data = self.encrypt_data(compressed_data, key)

            with open(output_file, 'wb') as outfile:
                outfile.write(encrypted_data)
            self.update_progress_bar(100)  # Completato
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Errore durante la compressione e la crittografia.")
            self.update_progress_bar(0)  # Errore

    # Decompatta e decrittografa un file
    def decrypt_and_decompress_file(self, input_file, output_file, key):
        try:
            with open(input_file, 'rb') as infile:
                encrypted_data = infile.read()
                decrypted_data = self.decrypt_data(encrypted_data, key)
                decompressed_data = zlib.decompress(decrypted_data)

            with open(output_file, 'wb') as outfile:
                outfile.write(decompressed_data)
            self.update_progress_bar(100)  # Completato
        except InvalidToken:
            self.result_label.config(text="Chiave di crittografia errata.")
            self.update_progress_bar(0)  # Errore
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Errore durante la decompressione e la decrittografia.")
            self.update_progress_bar(0)  # Errore

    # Crea un archivio contenente i file selezionati
    def create_archive(self, archive_file, files, key):
        archive_data = {}
        try:
            for file in files:
                with open(file, 'rb') as infile:
                    data = infile.read()
                    compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)
                    encrypted_data = self.encrypt_data(compressed_data, key)
                    archive_data[os.path.basename(file)] = encrypted_data

            with open(archive_file, 'wb') as outfile:
                outfile.write(str(archive_data).encode())
            self.update_status_message(f"Archivio {archive_file} creato!")
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Errore durante la creazione dell'archivio.")
            self.update_progress_bar(0)  # Errore

    # Estrae i file dall'archivio
    def extract_files_from_archive(self, archive_file, output_dir, key):
        try:
            with open(archive_file, 'rb') as infile:
                archive_data = eval(infile.read().decode())

            total_files = len(archive_data)
            for i, (filename, encrypted_data) in enumerate(archive_data.items()):
                self.update_status_message(f"Estrazione file {i+1}/{total_files}...")
                decrypted_data = self.decrypt_data(encrypted_data, key)
                decompressed_data = zlib.decompress(decrypted_data)
                output_file = os.path.join(output_dir, filename)
                with open(output_file, 'wb') as outfile:
                    outfile.write(decompressed_data)
                self.update_progress_bar((i + 1) / total_files * 100)

            self.update_status_message("File estratti dall'archivio!")
        except InvalidToken:
            self.result_label.config(text="Chiave di crittografia errata.")
            self.update_progress_bar(0)  # Errore
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Errore durante l'estrazione dall'archivio.")
            self.update_progress_bar(0)  # Errore

    # Crittografa i dati utilizzando una chiave
    def encrypt_data(self, data, key):
        fernet = Fernet(key)
        return fernet.encrypt(data)

    # Decrittografa i dati utilizzando una chiave
    def decrypt_data(self, data, key):
        fernet = Fernet(key)
        return fernet.decrypt(data)

    # Aggiorna la barra di avanzamento
    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.window.update_idletasks()

    # Aggiorna l'etichetta di stato
    def update_status_message(self, message):
        self.result_label.config(text=message)
        self.window.update_idletasks()

    # Gestisce il clic sul pulsante "Crea Archivio"
    def on_create_archive_button_click(self):
        input_files = self.file_listbox.get(0, tk.END)
        output_dir = self.output_entry.get()
        key = self.key_entry.get().encode()

        if not input_files:
            self.result_label.config(text="Seleziona almeno un file da archiviare.")
            return

        if not output_dir:
            self.result_label.config(text="Seleziona una directory di destinazione.")
            return

        if not key:
            self.result_label.config(text="Inserisci una chiave di crittografia.")
            return

        for input_file in input_files:
            if not os.path.isfile(input_file):
                self.result_label.config(text=f"Il file {input_file} non esiste.")
                return

        try:
            archive_file = os.path.join(output_dir, "archived_data.7bl")
            self.update_status_message("Comprimendo e cifrando i file...")
            self.create_archive(archive_file, input_files, key)
        except Exception as e:
            return

        self.update_progress_bar(0)  # Reimposta la barra di avanzamento
        self.update_status_message("Archivio creato!")

    # Gestisce il clic sul pulsante "Estrai dall'Archivio"
    def on_extract_archive_button_click(self):
        archive_file = self.file_listbox.get(0)  # Si assume che sia selezionato solo un file
        output_dir = self.output_entry.get()
        key = self.key_entry.get().encode()

        if not archive_file:
            self.result_label.config(text="Seleziona un archivio da cui estrarre.")
            return

        if not output_dir:
            self.result_label.config(text="Seleziona una directory di destinazione.")
            return

        if not key:
            self.result_label.config(text="Inserisci una chiave di crittografia.")
            return

        if not os.path.isfile(archive_file):
            self.result_label.config(text=f"L'archivio {archive_file} non esiste.")
            return

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        try:
            self.update_status_message("Estrazione dall'archivio...")
            self.extract_files_from_archive(archive_file, output_dir, key)
        except Exception as e:
            return

        self.update_progress_bar(0)  # Reimposta la barra di avanzamento
        self.update_status_message("File estratti dall'archivio!")

# Punto di ingresso dell'applicazione
if __name__ == "__main__":
    window = tk.Tk()  # Crea una finestra principale
    app = SevenBLCompressor(window)  # Crea un'istanza dell'applicazione
    window.mainloop()  # Avvia il ciclo principale dell'interfaccia grafica
