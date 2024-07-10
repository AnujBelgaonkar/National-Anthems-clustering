import nltk
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
from nltk.corpus.reader.wordnet import NOUN, VERB, ADJ, ADV
import re

def removewords(listoftokens, listofWords):
    return [token for token in listoftokens if token not in listofWords]

def pos_tagger(tag):
    if tag.startswith('J'):
        return ADJ
    elif tag.startswith('V'):
        return VERB
    elif tag.startswith('N'):
        return NOUN
    elif tag.startswith('R'):
        return ADV
    else:
        return None
    
def pos_tag_tokens(listoftokens):
    tagged_tokens = nltk.pos_tag(listoftokens)
    tagged_tokens = [(token, pos_tagger(tag)) for token, tag in tagged_tokens]
    return tagged_tokens

def applyLemmetization(listoftokens, lemmatizer):
    lemmatized_tokens = []
    listoftaggedtokens = pos_tag_tokens(listoftokens)
    for token, tag in listoftaggedtokens:
        if tag is None:
            lemmatized_tokens.append(lemmatizer.lemmatize(token))
        else:
            lemmatized_tokens.append(lemmatizer.lemmatize(token, tag))
    return lemmatized_tokens

def remove_special_words(sentence):
    sentence = re.sub(r'https?\S+', '', sentence)  # Remove URLs starting with http or https
    sentence = re.sub(r'www\S+', '', sentence)    # Remove URLs starting with www
    sentence = re.sub(r'[^A-Za-z0-9\s]', '', sentence)  # Remove special characters
    sentence = re.sub(r"\S*@\S*\s?", " ", sentence)    # Remove mentions and emails
    sentence = re.sub("\S*\d\S*"," ", sentence) 
    return sentence

def twoLetters(listOfTokens):
    return [token for token in listOfTokens if len(token) <= 2 or len(token) >= 21]

def processCorpus(corpus, language='english'):
    processed_corpus = []
    stopwords = set(nltk.corpus.stopwords.words(language))
    countries = [line.rstrip('\n') for line in open(r"E:\Projects\National Anthems\lists\countries.txt")]
    nationalities= [line.rstrip('\n') for line in open(r"E:\Projects\National Anthems\lists\nationalities.txt")]
    extra_words = [line.rstrip('\n') for line in open(r"E:\Projects\National Anthems\lists\stopwords_scrapmaker.txt")]
    lemmatizer = WordNetLemmatizer()
    for document in corpus:
        document = document.replace(u'\ufffd', '8')
        document = document.replace(',', '')
        document = document.rstrip('\n')
        document = document.casefold()
        document = remove_special_words(document)
        listoftokens = word_tokenize(document)
        twoletterwords = twoLetters(listoftokens)
        listoftokens = removewords(listoftokens, stopwords)
        listoftokens = removewords(listoftokens, twoletterwords)
        listoftokens = removewords(listoftokens,countries)
        listoftokens = removewords(listoftokens,nationalities)
        listoftokens = removewords(listoftokens,extra_words)
        listoftokens = applyLemmetization(listoftokens, lemmatizer)
        listoftokens = removewords(listoftokens,extra_words)
        processed_corpus.append(" ".join(listoftokens))
    
    return processed_corpus
    



    