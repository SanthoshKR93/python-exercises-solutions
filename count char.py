def count_char(text,char):
   count=0
   for c in text:
      if c==char:
         count+=1
   return count
text=[]
text=input('enter the text')
char=input('enter the character to b searched for:')
print(str(count_char(text,char)))
