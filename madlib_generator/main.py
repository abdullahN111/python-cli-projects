
with open("story.txt", "r") as f:
    story = f.read()
    
words = set()
word_start = -1

target_start = "<"
target_end = ">"

for i, char in enumerate(story):
    if char == target_start:
        word_start = i
        
    if char == target_end and word_start != -1:
        word = story[word_start: i+1]
        words.add(word)
        word_start = -1
        
answers = {}

for word in words:
    answer = input(f"Enter a word for {word}: ")
    answers[word] = answer
    

for word in words:
    story = story.replace(word, answers[word])
    
print(story)