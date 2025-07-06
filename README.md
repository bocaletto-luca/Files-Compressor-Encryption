# Files Compressor with Encryption
#### Author: Luca Bocaletto

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue?style=for-the-badge&logo=gnu)](LICENSE) [![Language: Python](https://img.shields.io/badge/Language-Python-blue?style=for-the-badge&logo=python)](https://www.python.org/) [![Linux-Compatible](https://img.shields.io/badge/Linux-Compatible-blue?style=for-the-badge&logo=linux)](https://www.kernel.org/) [![Status: Complete](https://img.shields.io/badge/Status-Complete-brightgreen?style=for-the-badge)](https://github.com/bocaletto-luca/Directory-Monitor)

----
## Description

This software is designed to help users compress and encrypt their files, making them more secure and reducing the required storage space. Here are the main features offered:

- **Compress files:** Users can select the files they want to compress. The software uses the zlib compression library to reduce the file sizes, using the best available compression level.

- **Encrypt files:** The software allows users to specify an encryption key. It then uses the Fernet cryptography library to encrypt the compressed data. Encryption provides an additional level of security to the files, protecting them from unauthorized access.

- **Extract files:** Users can also use the software to extract files from an encrypted archive. This operation involves decrypting the data and decompressing the files in the archive.

![Screenshot 2023-10-18 125051](https://github.com/elektronoide/7bl-Compressor-Encryption/assets/134635227/90a088c6-4786-47f9-a6f3-5d782186da04)

### Management of Archived File Extension

By default, the software uses the ".7bl" extension for archived files, for example, "archived_data.7bl." However, users have the flexibility to change the file extension as they prefer, creating custom extensions or specifying the file name as they wish. The important thing is that the archive's content will be encrypted and compressed regardless of the file extension.

## User Interface

The software offers a simple and intuitive user interface with all the previously mentioned features.

The software uses Python libraries like tkinter, zlib, and cryptography to handle compression and encryption operations. In case of errors or exceptions, the software displays error messages and details through the status label.

---

**Note**: Ensure that you have installed all the necessary dependencies before running the application.

**Maintainer Update**

My current GitHub account is **@bocaletto-luca**, which is now the official maintainer of all projects previously published under the **@Elektronoide** account. Please direct any issues, pull requests, or stars to **@bocaletto-luca** for future updates.

---

