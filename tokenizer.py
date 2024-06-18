# Menentukan kelas Token Recognizer untuk mengenali jenis kata yang diberikan
class TokenRecognizer:
    def __init__(self):
        # Inisialisasi daftar kata untuk setiap bagian pengucapan
        self.subjek = ["Gisa", "Kila", "Caca", "Dia", "Mereka"]  # subjek
        self.predikat = ["makan", "memasak", "mengerjakan", "pergi", "tidur"]  # predikat
        self.objek = ["nasi", "buah", "tugas", "museum", "kamar"]  # objek
        self.keterangan = ["di", "ke", "kemarin", "besok", "tadi"]  # keterangan

    # Metode untuk mengenali jenis kata yang diberikan
    def recognize(self, word):
        # Cek apakah kata tersebut subjek/bukan
        if word in self.subjek:
            return "S"  
        # Cek apakah kata tersebut predikat/bukan
        elif word in self.predikat:
            return "P"  
        # Cek apakah kata tersebut objek/bukan
        elif word in self.objek:
            return "O"  
        # Cek apakah kata tersebut keterangan/bukan
        elif word in self.keterangan:
            return "K"  
        else:
            return None  # Return None jika kata tersebut tidak dikenali


# Buat sebuah contoh dari Token Recognizer
tokenizer = TokenRecognizer()


# Tentukan kelas Parse untuk mengurai kalimat
class Parser:
    def __init__(self, tokenizer):
        # Inisialisasi parser dengan tokenizer
        self.tokenizer = tokenizer
        self.stack = []  # inisialisasi tumpukan kosong untuk menyimpan parse tree

    # Metode untuk parse kalimat
    def parse(self, sentence):
        # Pisahkan kalimat menjadi beberapa kata (token)
        tokens = sentence.split()
        for token in tokens:
            # Mengenali jenis token
            token_type = self.tokenizer.recognize(token)
            # Cek jenis token dan push ke stack yang sesuai
            if token_type == "S":
                self.stack.append("S")
            elif token_type == "P":
                if self.stack[-1] == "S":
                    self.stack.append("P")
                else:
                    return False  # return False if the parse fails
            elif token_type == "O":
                if self.stack[-1] == "P":
                    self.stack.append("O")
                else:
                    return False  # return False jika parse gagal
            elif token_type == "K":
                if self.stack[-1] in ["P", "O"]:
                    self.stack.append("K")
                else:
                    return False  # return False jika parse gagal
        # Cek apakah parse berhasil
        return self.stack == ["S", "P", "O", "K"] or self.stack == ["S", "P", "K"] or self.stack == ["S", "P", "O"] or self.stack == ["S", "P"]


# Buat sebuah contoh dari Parser dengan tokenizer
parser = Parser(tokenizer)


# Testing Code
sentence = "Caca pergi ke museum"
if parser.parse(sentence):
    print(sentence, ": kalimat tidak valid")  # print "kalimat tidak valid" jika parse gagal
else:
    print(sentence, ": kalimat valid")  # print "kalimat valid" jika parse berhasil