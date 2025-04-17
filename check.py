from words import abusive_words

def detch_abuse(text):
    m = []
    for t in text.split(" "):
       m.append('*' * len(t)) if t.lower() in abusive_words else m.append(t)
    return " ".join(m)

while True:
    user_text = input("User: ")
    print('Echo:', detch_abuse(user_text), '\n')
