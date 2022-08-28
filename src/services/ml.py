from numpy import load
from string import punctuation
import pymorphy2
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

stop_words = ['и', 'в', 'во', 'не', 'что', 'он', 'на', 'я', 'с', 'со', 'как', 'а', 'то', 'все', 'она', 'так', 'его',
              'но', 'да',
              'ты', 'к', 'у', 'же', 'вы', 'за', 'бы', 'по', 'только', 'ее', 'мне', 'было', 'вот', 'от', 'меня', 'еще',
              'нет', 'о',
              'из', 'ему', 'теперь', 'когда', 'даже', 'ну', 'вдруг', 'ли', 'если', 'уже', 'или', 'ни', 'быть', 'был',
              'него', 'до',
              'вас', 'нибудь', 'опять', 'уж', 'вам', 'ведь', 'там', 'потом', 'себя', 'ничего', 'ей', 'может', 'они',
              'тут', 'где',
              'есть', 'надо', 'ней', 'для', 'мы', 'тебя', 'их', 'чем', 'была', 'сам', 'чтоб', 'без', 'будто', 'чего',
              'раз', 'тоже',
              'себе', 'под', 'будет', 'ж', 'тогда', 'кто', 'этот', 'того', 'потому', 'этого', 'какой', 'совсем', 'ним',
              'здесь',
              'этом', 'один', 'почти', 'мой', 'тем', 'чтобы', 'нее', 'сейчас', 'были', 'куда', 'зачем', 'всех',
              'никогда', 'можно',
              'при', 'наконец', 'два', 'об', 'другой', 'хоть', 'после', 'над', 'больше', 'тот', 'через', 'эти', 'нас',
              'про',
              'всего', 'них', 'какая', 'много', 'разве', 'три', 'эту', 'моя', 'впрочем', 'хорошо', 'свою', 'этой',
              'перед', 'иногда',
              'лучше', 'чуть', 'том', 'нельзя', 'такой', 'им', 'более', 'всегда', 'конечно', 'всю', 'между']
punctuation = punctuation + '»' + '«'

# Скачаешь своей функцией, load_json - псевдокод
# Важно, чтобы у переменных были именно такие имена, в каждом джейсоне хранится одна переменная
sk_corpus4binary_model = list(load('services/content/sk_corpus_binary.npy'))
sk_corpus = list(load('services/content/sk_corpus_multiclass.npy'))
freq_tokens4binary_model = list(load('services/content/freq_tokens_binary.npy'))
freq_tokens = list(load('services/content/freq_tokens_multiclass.npy'))

from keras.models import load_model

modelB = load_model('services/content/modelB.h5')  # Указываешь путь
modelS = load_model('services/content/modelS.h5')
modelF = load_model('services/content/modelF.h5')


def predictProbas(text, modelB=modelB, modelF=modelF, modelS=modelS, TfidfVectorizer=TfidfVectorizer,
                  corpus_binary=sk_corpus4binary_model, corpus=sk_corpus, freqs_binary=freq_tokens4binary_model,
                  freqs=freq_tokens, punctuation=punctuation, stopwords=stopwords, pymorphy2=pymorphy2):
    keys0 = freqs_binary
    keys1 = freqs
    morph = pymorphy2.MorphAnalyzer()

    def parProba(par, TfidfVectorizer=TfidfVectorizer, keys0=keys0, keys1=keys1, morph=morph, punctuation=punctuation,
                 stopwords=stopwords, corpus_binary=corpus_binary, corpus=corpus, freqs_binary=freqs_binary,
                 freqs=freqs, modelB=modelB, modelF=modelF):
        par0 = [word for word in par.split(' ') if word]
        par0 = [token for token in par0 if token not in punctuation]
        par0 = [word.lower() for word in par0]
        par0 = [token for token in par0 if token.isalpha()]
        par0 = [morph.parse(word)[0].normal_form for word in par0]
        par0 = [word for word in par0 if word not in stop_words]
        par0 = [word for word in par0 if word in keys0]
        sk_corpus0 = corpus_binary + [' '.join(par0)]
        vectorizer = TfidfVectorizer(vocabulary=list(keys0))  # tf-idf преобразование
        X_tfidf = vectorizer.fit_transform(sk_corpus0)
        x0 = X_tfidf.toarray()[-1]
        pred0 = modelB.predict(x0[None, ...])
        if np.argmax(pred0) == 1:
            return 'NoneClass'
        else:
            par1 = [word for word in par.split(' ') if word]
            par1 = [token for token in par1 if token not in punctuation]
            par1 = [word.lower() for word in par1]
            par1 = [token for token in par1 if token.isalpha()]
            par1 = [morph.parse(word)[0].normal_form for word in par1]
            par1 = [word for word in par1 if word not in stop_words]
            par1 = [word for word in par1 if word in keys1]
            sk_corpus1 = corpus + [' '.join(par1)]
            vectorizer = TfidfVectorizer(vocabulary=list(keys1))
            X_tfidf = vectorizer.fit_transform(sk_corpus1)
            x1 = X_tfidf.toarray()[-1]

            s_pred = modelS.predict(x1[None, ...])

            inputX = np.concatenate([x1, s_pred.reshape(39)])

            proba = modelF.predict(inputX[None, ...])
            return proba

    proba_list = list()
    pars_list = list()
    pars = [sen for sen in text.split('\n') if sen]
    for par in pars:
        proba = parProba(par)

        proba_list.append(proba)
        pars_list.append(par)
    return proba_list, pars_list
