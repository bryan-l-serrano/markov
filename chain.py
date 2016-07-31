import random

def markov(text):
    data = open(text).read()

    words = [ i for i in data.split(' ') if i!='']
    chains = {}
    final = []

    for x in range(0,len(words)):
        if chains.has_key((words[x], words[x+1])) == False:
            word_list = []
            if x == len(words)-2:
                chains.update({(words[x], words[x+1]): word_list})
                break
            for y in range(x,len(words)-1):
                if words[y] == words[x+1]:
                    word_list.append(words[y+1])
            chains.update({(words[x], words[x+1]): word_list})

    B = True
    while B == True:
        number = random.randrange(0,len(words))
        if words[number][0].isupper() == True:
            final.append(words[number])
            final.append(words[number+1])
            B = False

    count = 1
    A =True
    while A == True:
        next_word = chains.get((final[count-1],final[count]))
        if len(next_word) == 0:
            A = False
            break
        number = random.randrange(0,len(next_word))
        final.append(next_word[number])
        count += 1
        test = ''.join(final)
        last = test[len(test) - 1] 
        if last == "." or last == '"' or last == '?' or last == '!' or last == ' ' or last == "'":
            A = False
    print ' '.join(final)
