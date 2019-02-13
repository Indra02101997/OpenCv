from textblob import TextBlob
text="I am brilliant"
obj=TextBlob(text)
sent=obj.sentiment.polarity
print (sent)
