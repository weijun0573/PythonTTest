import os
##import seaborn as sns
##import matplotlib.pyplot as plt
##import numpy as np


#read pos file

f_positive=open('Pos_all.txt','r',encoding='utf-8')

#read line by line, since each line is a comment, then we will know how many comments in total

comments_positive=f_positive.readlines()
f_positive.close()

#print how many comments in total

print('There are total %s positive comments.' % len(comments_positive))

#create a list to save word length of each comments
#create a list to save letter length of each comments

wordlength_positive=[]
letterlength_positive=[]

for c in comments_positive:
    wordlength_positive.append(len(c.lower().split()))
    letterlength_positive.append(len(c))


#check first lenth of the first comment

print('In the first comment, there are %s words and %s letters.' % (wordlength_positive[0],letterlength_positive[1]))


#look all possible word number and letter number in all positive comments
print(wordlength_positive[:10])
set_wl_positive=set(wordlength_positive)
set_ll_positive=set(letterlength_positive)

order_set_wl_positive=list(set_wl_positive)
order_set_wl_positive.sort()
#print(order_set_wl_positive)


#count appearence of number
#data saved as the following format in the list: word length, appearence
wl_frequency=[]

#count appearence of number
for wl in order_set_wl_positive:
    ap=wordlength_positive.count(wl)
    wl_frequency.append([ap,wl])

#for wl in wl_frequency[:5]:
#    print('There are %s comments with word length equal to %s.' % (wl[0],wl[1]))

#sort results by appearence of word length
#you can also do reverse sorting
#wl_frequency.sort()
wl_frequency.sort(reverse=True)

for wl in wl_frequency[:50]:
    print('There are %s positive comments with word length equal to %s.' % (wl[0],wl[1]))




##sns.histplot(np.array(wordlength_positive),binwidth=10)
##plt.xlim((10,500))
##plt.show()


print('*****************************The following are negative comments************************')


#read pos file

f_negative=open('neg_all.txt','r',encoding='utf-8')

#read line by line, since each line is a comment, then we will know how many comments in total

comments_negative=f_negative.readlines()

f_negative.close()

#print how many comments in total

print('There are total %s negative comments.' % len(comments_negative))

#create a list to save word length of each comments
#create a list to save letter length of each comments

wordlength_negative=[]
letterlength_negative=[]

for c in comments_negative:
    wordlength_negative.append(len(c.split()))
    letterlength_negative.append(len(c))


#check first lenth of the first comment

print('In the first comment, there are %s words and %s letters.' % (wordlength_negative[0],letterlength_negative[1]))


#look all possible word number and letter number in all negative comments
print(wordlength_negative[:10])
set_wl_negative=set(wordlength_negative)
set_ll_negative=set(letterlength_negative)

order_set_wl_negative=list(set_wl_negative)
order_set_wl_negative.sort()
#print(order_set_wl_negative)


#count appearence of number
#data saved as the following format in the list: word length, appearence
wl_frequency_neg=[]

#count appearence of number
for wl in order_set_wl_negative:
    ap=wordlength_negative.count(wl)
    wl_frequency_neg.append([ap,wl])

#for wl in wl_frequency[:5]:
#    print('There are %s comments with word length equal to %s.' % (wl[0],wl[1]))

#sort results by appearence of word length
#you can also do reverse sorting
#wl_frequency.sort()
wl_frequency_neg.sort(reverse=True)

for wl in wl_frequency_neg[:50]:
    print('There are %s negative comments with word length equal to %s.' % (wl[0],wl[1]))


##sns.histplot(np.array(wordlength_positive),binwidth=10,color='green')
##sns.histplot(np.array(wordlength_negative),binwidth=10,color='red')
##plt.xlim((10,500))
##plt.show()




print('\n\n\n\n\n\n\n')



#read pos file

f_positive=open('Pos_all.txt','r',encoding='utf-8')

#read whole text

txt_positive=f_positive.read()
f_positive.close()

#print total word number in all positive comments

txt_positive=txt_positive.lower()
words_positive=txt_positive.split()
print('There are total %s words in all positive comments.' % len(words_positive))


#look all possible word in all positive comments
set_word_positive=set(words_positive)

print('There are total %s unrepeated words in positive comments' % len(set_word_positive))


#count appearence of number
#data saved as the following format in the list: word length, appearence
word_frequency=[]

#count appearence of number

x=0
for word in ['good','exciting','like','happy','love','positive','bad','hate','not','unfortunately','negative']:
    ap=words_positive.count(word)
    word_frequency.append([ap,word])

#for wl in wl_frequency[:5]:
#    print('There are %s comments with word length equal to %s.' % (wl[0],wl[1]))

#sort results by appearence of word length
#you can also do reverse sorting
#wl_frequency.sort()



for word in word_frequency:
    print('There are %s "%s" in positive comments.' % (word[0],word[1]))


print('*****************************The following are negative comments************************')


#open negative comment file

f_negative=open('neg_all.txt','r',encoding='utf-8')

#read whole text

txt_negative=f_negative.read()
f_negative.close()

#print total word number in all negative comments

txt_negative=txt_negative.lower()
words_negative=txt_negative.split()
print('There are total %s words in all negative comments.' % len(words_negative))


#look all possible word in all negative comments
set_word_negative=set(words_negative)

print('There are total %s unrepeated words in negative comments' % len(set_word_negative))


#count appearence of number
#data saved as the following format in the list: word length, appearence
word_frequency_neg=[]

#count appearence of number

x=0
for word in ['good','exciting','like','happy','love','positive','bad','hate','not','unfortunately','negative']:
    ap=words_negative.count(word)
    word_frequency_neg.append([ap,word])

#for wl in wl_frequency[:5]:
#    print('There are %s comments with word length equal to %s.' % (wl[0],wl[1]))

#sort results by appearence of word length
#you can also do reverse sorting
#wl_frequency.sort()



for word in word_frequency_neg:
    print('There are %s "%s" in negative comments.' % (word[0],word[1]))










    
    
