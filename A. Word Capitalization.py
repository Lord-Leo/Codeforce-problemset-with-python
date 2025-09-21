word = input()
new_word=word[0].upper()+word[1:]       #i want just the 1st index to change
new_word1 = word[:-1]+word[-1].upper()  #now just the last index
print(new_word,new_word1)

#more like string slicing
#if i want to change some certain index char what to do
#result
word = input()
index = list(map(int, input().split()))
for i in index:
    word = word[:i]+word[i].upper()+word[i+1:]
print(word)