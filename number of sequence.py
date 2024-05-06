def count_sentences(text):
    sentences = text.split('. ') 
    return len(sentences)
text = "This is a sample sentence. It contains punctuation."
print("Number of sentences:", count_sentences(text))
