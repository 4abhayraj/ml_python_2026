secret_word="python"
counter=0
while True:
    word=input("Enter the secret word: ").lower()
    counter=counter+1
    if word==secret_word:
        print("correct word")
        break
    if word==secret_word  or counter>7:
        print("too many attempts")
        break
