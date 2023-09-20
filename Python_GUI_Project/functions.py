import tkinter as tk

def project():
    #text
    def caesar_cipher(text, shift):
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                is_upper = char.isupper()
                char = char.lower()
                encrypted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
                if is_upper:
                    encrypted_char = encrypted_char.upper()
                encrypted_text += encrypted_char
            else:
                encrypted_text += char
        return encrypted_text

    #text encrpytion
    def encrypt_text():
        text = textbox.get("1.0", "end-1c")  # Get the text from the Textbox
        shift = 30  # You can change the shift value as needed
        encrypted_text = caesar_cipher(text, shift)
        display_label.config(text=encrypted_text)  # Update the Label with the encrypted text

    #text decrpytion
    def decrypt_text():
        encrypted_text = textbox.get("1.0", "end-1c")
        shift = 30
        decrypted_text = caesar_cipher(encrypted_text, -shift)
        display_label.config(text=decrypted_text)

    root = tk.Tk()
    root.title("Encryption and Decryption-Python")

    font_ = ("Helvetica", 20)

    textbox = tk.Text(root, font=font_, width=50, height=10)
    textbox.pack(pady=10)

    encrypt_button = tk.Button(root, text="Encrypt Text", command=encrypt_text)
    encrypt_button.pack()

    decrypt_button = tk.Button(root, text="Decrypt Text", command=decrypt_text)
    decrypt_button.pack()

    display_label = tk.Label(root, text="", font=font_, anchor="w", width=50, height=10)
    display_label.pack()
    loop = root.mainloop()
    return loop
