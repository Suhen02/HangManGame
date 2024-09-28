import random
import hangman_stages
import list_word
print("***** WELL COME TO HANG MAN GAME ****** ")
#name_list=["apple","banana","sea","india","river"]
name=random.choice(list_word.word)
lives=6
prin_word=[]
for i in name:
   prin_word += '_'
print(prin_word)
gameOver=False   
while not gameOver:
    guessed_letter=input("enter the letter : ").lower()
    for i in range (len(name)):
        if name[i]==guessed_letter:
            prin_word[i]=guessed_letter
    print(prin_word) 
    if guessed_letter not in name:
        lives-=1
        if lives == 0:
            gameOver=True
            print("you loose !!")
    if '_' not in prin_word:  
        gameOver=True 
        print("congraters (: you win")
    print(hangman_stages.stages[lives]) 
   
