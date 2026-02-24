import random
word_bank= ['computer', 'python', 'hello', 'apple', 'table', 'house', 'ocean', 'guitar', 'pizza', 'friend', 'water', 'sunshine', 'mountain', 'library', 'phone', 'coffee', 'school', 'flower', 'cloud', 'chair', 'pencil', 'blanket', 'keyboard', 'bottle', 'window', 'mirror', 'paper', 'travel', 'music', 'family', 'garden']
word=random.choice(word_bank)
guessed_word=['_']*len(word)
attempt=10
filled=random.randrange(0,len(word))
# print(filled)
guessed_word[filled]=word[filled]
while attempt > 0:
  print('\nCurrent word: ' + ' '.join(guessed_word))
  guess=input("guess a letter: ").lower()

  if guess in word:
    for i in range(len(word)):
        if word[i]==guess:
            guessed_word[i]=guess
    print("great guess")

  else:
    attempt-=1
    print("wrong guess, attempt left: ", attempt)
    
  if "_" not in guessed_word:
    print('\nCongratulation You guessed the word', word)
    break
if attempt==0 and '_' in guessed_word:
   print("\nYou\'ve run out of attempts! The word was: ", word)

       
