# Name Software: Files Compressor with Encryption
# Author: Luca Bocaletto
# Description: This software provides the ability to compress, encrypt, and extract files.
# It allows users to select files to archive or extract, specify an encryption key, and generate encrypted archives.
# It is a useful tool for protecting and compressing sensitive data.
# Import necessary modules
import tkinter as tk
from tkinter import ttk
from cryptography.fernet import Fernet
import zlib
import os
import traceback
from tkinter import filedialog
from cryptography.fernet import InvalidToken

# Define the main application class
class SevenBLCompressor:
    def __init__(self, window):
        self.window = window
        self.window.title("Files Compressor with Encryption")  # Set the window title
        self.window.configure(bg="#f5f5f5")  # Set the background color of the window

        # Create and position user interface elements
        self.create_ui_elements()

    def create_ui_elements(self):
        self.file_label = tk.Label(self.window, text="7bl Compressor with Encryption", font=("Helvetica", 20))
        self.file_label.pack()
        # Labels, lists, input fields, and buttons
        self.file_label = tk.Label(self.window, text="File to archive/extract:")
        self.file_label.pack()

        self.file_listbox = tk.Listbox(self.window, selectmode=tk.MULTIPLE, width=50)
        self.file_listbox.pack()

        self.browse_input_button = tk.Button(self.window, text="Browse", command=self.browse_input_files)
        self.browse_input_button.pack()

        self.output_label = tk.Label(self.window, text="Archived/extracted file:")
        self.output_label.pack()

        self.output_entry = tk.Entry(self.window, width=50)
        self.output_entry.pack()

        self.browse_output_button = tk.Button(self.window, text="Browse", command=self.browse_output_directory)
        self.browse_output_button.pack()

        self.key_label = tk.Label(self.window, text="Encryption key:")
        self.key_label.pack()

        self.key_entry = tk.Entry(self.window, width=50)
        self.key_entry.pack()

        self.generate_key_button = tk.Button(self.window, text="Generate Random Key", command=self.generate_and_set_key)
        self.generate_key_button.pack()

        self.progress_bar = ttk.Progressbar(self.window, orient="horizontal", length=200, mode="determinate")
        self.progress_bar.pack()

        self.create_archive_button = tk.Button(self.window, text="Create Archive", command=self.on_create_archive_button_click)
        self.create_archive_button.pack()

        self.extract_archive_button = tk.Button(self.window, text="Extract from Archive", command=self.on_extract_archive_button_click)
        self.extract_archive_button.pack()

        self.result_label = tk.Label(self.window, text="")
        self.result_label.pack()

        # Customize button colors
        self.create_archive_button.config(bg="#4CAF50", fg="white")
        self.extract_archive_button.config(bg="#4CAF50", fg="white")

    # Handle selection of files to archive/extract
    def browse_input_files(self):
        file_paths = filedialog.askopenfilenames()
        if file_paths:
            self.file_listbox.delete(0, tk.END)
            for file_path in file_paths:
                self.file_listbox.insert(tk.END, file_path)

    # Handle selection of the output directory
    def browse_output_directory(self):
        directory_path = filedialog.askdirectory()
        if directory_path:
            self.output_entry.delete(0, tk.END)
            self.output_entry.insert(0, directory_path)

    # Generate a random key and display it in the interface
    def generate_key(self):
        return Fernet.generate_key()

    def generate_and_set_key(self):
        key = self.generate_key()
        self.key_entry.delete(0, tk.END)
        self.key_entry.insert(0, key.decode())

    # Compress and encrypt a file
    def compress_and_encrypt_file(self, input_file, output_file, key):
        try:
            with open(input_file, 'rb') as infile:
                data = infile.read()
                compressed_data = zlib.compress(data, level=zlib.Z_BEST_COMPRESSION)
                encrypted_data = self.encrypt_data(compressed_data, key)

            with open(output_file, 'wb') as outfile:
                outfile.write(encrypted_data)
            self.update_progress_bar(100)  # Completed
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Error during compression and encryption.")
            self.update_progress_bar(0)  # Error

    # Decompress and decrypt a file
    def decrypt_and_decompress_file(self, input_file, output_file, key):
        try:
            with open(input_file, 'rb') as infile:
                encrypted_data = infile.read()
                decrypted_data = self.decrypt_data(encrypted_data, key)
                decompressed_data = zlib.decompress(decrypted_data)

            with open(output_file, 'wb') as outfile:
                outfile.write(decompressed_data)
            self.update_progress_bar(100)  # Completed
        except InvalidToken:
            self.result_label.config(text="Incorrect encryption key.")
            self.update_progress_bar(0)  # Error
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Error during decompression and decryption.")
            self.update_progress_bar(0)  # Error

    # Create an archive containing the selected files
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
            self.update_status_message(f"Archive {archive_file} created!")
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Error during archive creation.")
            self.update_progress_bar(0)  # Error

    # Extract files from the archive
    def extract_files_from_archive(self, archive_file, output_dir, key):
        try:
            with open(archive_file, 'rb') as infile:
                archive_data = eval(infile.read().decode())

            total_files = len(archive_data)
            for i, (filename, encrypted_data) in enumerate(archive_data.items()):
                self.update_status_message(f"Extracting file {i+1}/{total_files}...")
                decrypted_data = self.decrypt_data(encrypted_data, key)
                decompressed_data = zlib.decompress(decrypted_data)
                output_file = os.path.join(output_dir, filename)
                with open(output_file, 'wb') as outfile:
                    outfile.write(decompressed_data)
                self.update_progress_bar((i + 1) / total_files * 100)

            self.update_status_message("Files extracted from the archive!")
        except InvalidToken:
            self.result_label.config(text="Incorrect encryption key.")
            self.update_progress_bar(0)  # Error
        except Exception as e:
            traceback.print_exc()
            self.result_label.config(text="Error during extraction from the archive.")
            self.update_progress_bar(0)  # Error

    # Encrypt data using a key
    def encrypt_data(self, data, key):
        fernet = Fernet(key)
        return fernet.encrypt(data)

    # Decrypt data using a key
    def decrypt_data(self, data, key):
        fernet = Fernet(key)
        return fernet.decrypt(data)

    # Update the progress bar
    def update_progress_bar(self, value):
        self.progress_bar["value"] = value
        self.window.update_idletasks()

    # Update the status label
    def update_status_message(self, message):
        self.result_label.config(text=message)
        self.window.update_idletasks()

    # Handle the click on the "Create Archive" button
    def on_create_archive_button_click(self):
        input_files = self.file_listbox.get(0, tk.END)
        output_dir = self.output_entry.get()
        key = self.key_entry.get().encode()

        if not input_files:
            self.result_label.config(text="Select at least one file to archive.")
            return

        if not output_dir:
            self.result_label.config(text="Select a destination directory.")
            return

        if not key:
            self.result_label.config(text="Enter an encryption key.")
            return

        for input_file in input_files:
            if not os.path.isfile(input_file):
                self.result_label.config(text=f"The file {input_file} does not exist.")
                return

        try:
            archive_file = os.path.join(output_dir, "archived_data.7bl")
            self.update_status_message("Compressing and encrypting files...")
            self.create_archive(archive_file, input_files, key)
        except Exception as e:
            return

        self.update_progress_bar(0)  # Reset the progress bar
        self.update_status_message("Archive created!")

    # Handle the click on the "Extract from Archive" button
    def on_extract_archive_button_click(self):
        archive_file = self.file_listbox.get(0)  # Assuming only one file is selected
        output_dir = self.output_entry.get()
        key = self.key_entry.get().encode()

        if not archive_file:
            self.result_label.config(text="Select an archive to extract from.")
            return

        if not output_dir:
            self.result_label.config(text="Select a destination directory.")
            return

        if not key:
            self.result_label.config(text="Enter an encryption key.")
            return

        if not os.path.isfile(archive_file):
            self.result_label.config(text=f"The archive {archive_file} does not exist.")
            return

        if not os.path.exists(output_dir):
            os.mkdir(output_dir)

        try:
            self.update_status_message("Extracting from the archive...")
            self.extract_files_from_archive(archive_file, output_dir, key)
        except Exception as e:
            return

        self.update_progress_bar(0)  # Reset the progress bar
        self.update_status_message("Files extracted from the archive!")

# Entry point of the application
if __name__ == "__main__":
    window = tk.Tk()  # Create the main window
    app = SevenBLCompressor(window)  # Create an instance of the application
    window.mainloop()  # Start the main graphical interface loop
