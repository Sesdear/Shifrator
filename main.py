import tkinter as tk
class Shifrator:
    def __init__(self, key):
        self.key = dict(zip('ABCDEFGHIJKLMNOPQRSTUVWXYZ', key.upper()))
    def process_text(self, text, direction):
        key_mapping = self.key if direction == 'encrypt' else {v: k for k, v in self.key.items()}
        return ''.join(key_mapping.get(char.upper(), char) if char.isalpha() else char for char in text)
    def encrypt(self, text):
        return self.process_text(text, 'encrypt')
    def decrypt(self, text):
        return self.process_text(text, 'decrypt')
class ShifratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Shifrator By HLNikNiky")
        self.root.configure(bg="black")
        self.custom_key, self.cipher = "", None
        self.create_widgets()
    def create_widgets(self):
        text_color, bg_color = "white", "black"
        grid_params = {'padx': 5, 'pady': 5}
        tk.Label(self.root, text="Введите ключ:", bg=bg_color, fg=text_color).grid(row=0, column=0, **grid_params)
        self.entry_key = tk.Entry(self.root, bg=bg_color, fg=text_color)
        self.entry_key.grid(row=0, column=1, **grid_params)
        tk.Button(self.root, text="Запустить ключ", command=lambda: (setattr(self, 'custom_key', self.entry_key.get()), setattr(self, 'cipher', Shifrator(self.custom_key)), self.root.update()), bg=bg_color, fg=text_color).grid(row=0, column=2, **grid_params)
        tk.Label(self.root, text="Введите текст:", bg=bg_color, fg=text_color).grid(row=1, column=0, **grid_params)
        self.entry_text = tk.Entry(self.root, bg=bg_color, fg=text_color)
        self.entry_text.grid(row=1, column=1, **grid_params)
        self.radio_var = tk.StringVar(value="encrypt")
        tk.Radiobutton(self.root, text="Зашифровать", variable=self.radio_var, value="encrypt", bg=bg_color, fg=text_color).grid(row=2, column=0, **grid_params)
        tk.Radiobutton(self.root, text="Дешифровать", variable=self.radio_var, value="decrypt", bg=bg_color, fg=text_color).grid(row=2, column=1, **grid_params)
        tk.Button(self.root, text="Выполнить", command=lambda: self.result_label.config(text=f"Результат: {self.cipher.encrypt(self.entry_text.get()) if self.radio_var.get() == 'encrypt' else self.cipher.decrypt(self.entry_text.get())}"), bg=bg_color, fg=text_color).grid(row=3, column=0, columnspan=2, **grid_params)
        self.result_label = tk.Label(self.root, text="", bg=bg_color, fg=text_color)
        self.result_label.grid(row=4, column=0, columnspan=2, **grid_params)
        self.root.resizable(False, False)
    def set_custom_key(self, key):
        self.custom_key = key
        self.cipher = Shifrator(self.custom_key)
if __name__ == "__main__":
    root = tk.Tk()
    app = ShifratorApp(root)
    root.mainloop()
