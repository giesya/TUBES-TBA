import tkinter as tk

class TokenRecognizer:
    def __init__(self):
        self.subjek = ["Gisa", "Kyla", "Caca", "Dila", "Nasa"]  # subjek
        self.predikat = ["makan", "masak", "mengerjakan", "pergi", "tidur"]  # predikat
        self.objek = ["nasi", "buah", "tugas", "museum", "kamar"]  # objek
        self.keterangan = ["di", "ke", "kemarin", "besok", "tadi"]  # keterangan

    def recognize(self, word):
        if word in self.subjek:
            return "S"
        elif word in self.predikat:
            return "P"
        elif word in self.objek:
            return "O"
        elif word in self.keterangan:
            return "K"
        else:
            return None  # Return None jika kata tersebut tidak dikenali

class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.stack = []  # inisialisasi tumpukan kosong untuk menyimpan parse tree

    def parse(self, sentence):
        tokens = sentence.split()
        self.stack = []  # mengosongkan stack sebelum mem-parsing kalimat baru
        for token in tokens:
            token_type = self.tokenizer.recognize(token)
            if token_type == "S":
                self.stack.append("S")
            elif token_type == "P":
                if self.stack and self.stack[-1] == "S":
                    self.stack.append("P")
                else:
                    return False  # return False if the parse fails
            elif token_type == "O":
                if self.stack and self.stack[-1] == "P":
                    self.stack.append("O")
                else:
                    return False  # return False jika parse gagal
            elif token_type == "K":
                if self.stack and self.stack[-1] in ["P", "O"]:
                    self.stack.append("K")
                else:
                    return False  # return False jika parse gagal
        return self.stack == ["S", "P", "O", "K"] or self.stack == ["S", "P", "K"] or self.stack == ["S", "P", "O"] or self.stack == ["S", "P"]

class GUI:
    def __init__(self, master):
        self.master = master
        self.master.title("TokenNizer - Kelompok")
        self.tokenizer = TokenRecognizer()
        self.parser = Parser(self.tokenizer)

        self.sentence_label = tk.Label(master, text="Masukkan Kalimat:")
        self.sentence_label.pack()

        self.sentence_entry = tk.Entry(master, width=50)
        self.sentence_entry.pack()

        self.parse_button = tk.Button(master, text="Parse", command=self.parse_sentence)
        self.parse_button.pack()

        self.result_label = tk.Label(master, text="")
        self.result_label.pack()

    def parse_sentence(self):
        sentence = self.sentence_entry.get()
        if self.parser.parse(sentence):
            self.result_label.config(text="Kalimat valid!")
        else:
            self.result_label.config(text="Maaf, kalimat tidak valid!")

root = tk.Tk()
gui = GUI(root)
root.mainloop()
