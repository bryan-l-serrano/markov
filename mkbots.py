#!/usr/bin/env python
import random
import re
import twitter
import time
import reddit_parser

api = twitter.Api(consumer_key = '',
                  consumer_secret = '',
                  access_token_key = '',
                  access_token_secret = '')


common_words = [
'the',
'be',
'to',
'of',
'and',
'a',
'in',
'that',
'have',
'I',
'it',
'for',
'not',
'on',
'with',
'he',
'as',
'you',
'do',
'at',
'this',
'but',
'his',
'by',
'from',
'they',
'we',
'say',
'her',
'she',
'or',
'an',
'will',
'my',
'one',
'all',
'would',
'there',
'their',
'what',
'so',
'up',
'out',
'if',
'about',
'who',
'get',
'which',
'go',
'me',
'when',
'make',
'can',
'like',
'time',
'no',
'just',
'him',
'know',
'get',
'take',
'people',
'into',
'year',
'your',
'good',
'some',
'could',
'them',
'see'
'other',
'than',
'then',
'now',
'look',
'only',
'come',
'its',
'over',
'think',
'also',
'back',
'after',
'use',
'two',
'how',
'our',
'work',
'first',
'well',
'way',
'even',
'new',
'want',
'because',
'any',
'these',
'give',
'day',
'most',
'us'
]

def get_response(sentence):
    keywords = sentence.split()
    final_keywords = []
    for x in range(0,len(keywords)):
        keywords[x] = re.sub(r'\W+', '', keywords[x])
        for y in range(0,len(common_words)):
            if keywords[x] != common_words[y] and y == len(common_words)-1:
                final_keywords.append(keywords[x])
            elif keywords[x] == common_words[y]:
                break
    return final_keywords

def open_text(text):
    data = open(text).read()
    words = [i for i in data.split(' ') if i!='']
    return words

def markov(open_text):

    # returns a dictionary of markov chains where the keys are tuples
    # and the values are a list of strings

    chains = {}

    for x in range(0,len(open_text)):
        if chains.has_key((open_text[x], open_text[x+1])) == False:
            word_list = []
            if x == len(open_text)-2:
                chains.update({(open_text[x], open_text[x+1]): word_list})
                break
            for y in range(x,len(open_text)-1):
                if open_text[y] == open_text[x+1]:
                    word_list.append(open_text[y+1])
            chains.update({(open_text[x], open_text[x+1]): word_list})
    return chains


def new_status(diction):
    final = []
    B = True
    while B == True:
        keys = random.choice(diction.keys())
        if keys[0][0].isupper() == True:
            final.append(keys[0])
            final.append(keys[1])
            B = False

    count = 1
    A =True
    while A == True:
        next_word = diction.get((final[count-1],final[count]))
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
    return ' '.join(final)

def respond(diction, keywords):

    final = []
    B = True
    while B == True:
        keys = random.choice(diction.keys())
        for words in keywords:
            if ((keys[0] == words or keys[1] == words) and keys[0][0].isupper() == True) or keys[0].lower() == words:
                final.append(keys[0])
                final.append(keys[1])
                B = False

    count = 1
    A =True
    while A == True:
        next_word = diction.get((final[count-1],final[count]))
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
    return ' '.join(final)

def post_status(final_string):
    status = api.PostUpdate(final_string)
    print(status.text)

Y = True
while Y == True:
    text = reddit_parser.parse('all')
    open_text = open_text('all')
    diction = markov(open_text)
    to_post = new_status(diction)
    post_status(to_post)
    time.sleep(3600)


