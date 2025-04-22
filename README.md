# Files Compressor with Encryption

**Author:** Luca Bocaletto

![Screenshot 2023-10-18 125051](https://github.com/elektronoide/7bl-Compressor-Encryption/assets/134635227/90a088c6-4786-47f9-a6f3-5d782186da04)

## Description

This software is designed to help users compress and encrypt their files, making them more secure and reducing the required storage space. Here are the main features offered:

- **Compress files:** Users can select the files they want to compress. The software uses the zlib compression library to reduce the file sizes, using the best available compression level.

- **Encrypt files:** The software allows users to specify an encryption key. It then uses the Fernet cryptography library to encrypt the compressed data. Encryption provides an additional level of security to the files, protecting them from unauthorized access.

- **Extract files:** Users can also use the software to extract files from an encrypted archive. This operation involves decrypting the data and decompressing the files in the archive.

### Management of Archived File Extension

By default, the software uses the ".7bl" extension for archived files, for example, "archived_data.7bl." However, users have the flexibility to change the file extension as they prefer, creating custom extensions or specifying the file name as they wish. The important thing is that the archive's content will be encrypted and compressed regardless of the file extension.

## User Interface

The software offers a simple and intuitive user interface with all the previously mentioned features.

The software uses Python libraries like tkinter, zlib, and cryptography to handle compression and encryption operations. In case of errors or exceptions, the software displays error messages and details through the status label.

In conclusion, "7bl Compressor with Encryption" is a versatile tool for protecting sensitive data and managing files, with a user-friendly interface that allows users to compress, encrypt, and extract their files effectively and securely. Users have complete control over the management of archived file extensions.

# Nome Software: 7bl Compressore con Crittografia

**Autore:** Luca Bocaletto

![Screenshot 2023-10-18 125134](https://github.com/elektronoide/7bl-Compressor-Encryption/assets/134635227/89101817-f4b8-4a22-9e30-5c37ab5007c3)

## Descrizione

Questo software è progettato per aiutare gli utenti a comprimere e crittografare i loro file, rendendoli più sicuri e riducendo lo spazio di archiviazione necessario. Ecco le principali funzionalità offerte:

- **Comprimere file:** Gli utenti possono selezionare i file che desiderano comprimere. Il software utilizza la libreria di compressione zlib per ridurre le dimensioni dei file, utilizzando il miglior livello di compressione disponibile.

- **Crittografare file:** Il software consente agli utenti di specificare una chiave di crittografia. Utilizza quindi la libreria di crittografia Fernet per crittografare i dati compressi. La crittografia offre un ulteriore livello di sicurezza ai file, proteggendoli da accessi non autorizzati.

- **Estrarre file:** Gli utenti possono anche utilizzare il software per estrarre file da un archivio crittografato. Questa operazione coinvolge la decrittografia dei dati e la decompressione dei file nell'archivio.

### Gestione dell'estensione del file archiviato

Di default, il software utilizza l'estensione ".7bl" per i file archiviati, ad esempio, "archived_data.7bl". Tuttavia, gli utenti hanno la flessibilità di modificare l'estensione del file archiviato a loro piacimento, creando estensioni personalizzate o specificando il nome del file come preferiscono. L'importante è che il contenuto dell'archivio sarà crittografato e compresso indipendentemente dall'estensione del file.

## Interfaccia Utente

Il software offre un'interfaccia utente semplice ed intuitiva con tutte le funzionalità precedentemente menzionate.

Il software utilizza librerie Python come tkinter, zlib e cryptography per gestire le operazioni di compressione e crittografia. In caso di errori o eccezioni, il software visualizza messaggi di errore e dettagli tramite l'etichetta di stato.

In conclusione, "7bl Compressore con Crittografia" è uno strumento versatile per la protezione dei dati sensibili e la gestione dei file, con una semplice interfaccia utente che consente agli utenti di comprimere, crittografare ed estrarre i loro file in modo efficace e sicuro. Gli utenti hanno il controllo completo sulla gestione delle estensioni dei file archiviati.
