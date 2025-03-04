def readability_score(text: str):
    vowels = "aeiouyąęóAEIOUYĄĘÓ"
    
    words = text.split()
    sentences = []
    
    syllables = 0
    sentence = ""

    for word in words:
        sentence += " " + word
        syllables += sum(1 for letter in word if letter in vowels)
        
        if word[-1] == ".":
            sentences.append(sentence.strip())
            sentence = ""

    num_sentences = len(sentences)
    num_words = len(words)
    num_syllables = syllables

    ASL = num_words / num_sentences
    ASW = num_syllables / num_words
    return 206.835 - (1.015 * ASL) - (84.6 * ASW)

print(readability_score("Samochód jedzie bardzo szybko. W lesie rosną wysokie drzewa. Dzisiaj jest piękna pogoda."))
