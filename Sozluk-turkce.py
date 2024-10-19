None
meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap", 
            "ROFL": "bir şakaya karşılık cevap",
            "SHEESH": "onaylamak",
            "CREEPY": "korkunç",
            "AGGRO": "agresifleşmek/sinirlenmek",
            "LMAO": "gülmekten patlamak",
            "ASAP": "yakın zamanda",
            "GOAT": "tüm zamanların en iyisi",
            "GANG": "arkadaş grubu",
            "NGL": "not gonna lie(cidden yanlış değil ama...)",
            "IDK": "bilmiyorum",
            "IDC": "umrumda değil",
            "JK": "sadece şaka",
            "OMG": "aman tanrım",
            "FR": "for real(gerçekten)",
            }

word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!):")

if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("bu kelime uyuşmuyor")
