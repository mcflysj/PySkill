# 帮助纠正文本单词拼写错误
# pip install textblob
from textblob import *
# Fixing Paragraph Spells
def fix_paragraph_words(paragraph):
    sentence = TextBlob(paragraph)
    correction = sentence.correct()
    print(correction)
# Fixing Words Spells
def fix_word_spell(word):
    word = Word(word)
    correction = word.correct()
    print(correction)
fix_paragraph_words("This is sammple tet!!")
fix_word_spell("maangoo")