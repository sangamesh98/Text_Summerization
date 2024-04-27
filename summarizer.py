import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest


text = """ """
def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    #print(stopwords)
    nlp=spacy.load('en_core_web_sm')
    doc=nlp(rawdocs)
    #print(doc)
    tokens=[token.text for token in doc]    
    #print(tokens)
    word_freq={}
    for word in doc:
        if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
                if word.text not in word_freq.keys():
                    word_freq[word.text]=1
                else:
                    word_freq[word.text]+=1

    #print(word_freq)

    max_freq = max(word_freq.values())
    #print(max_freq)

    for word in word_freq.keys():
        word_freq[word]= word_freq[word]/max_freq
    #print(word_freq)
    sent_tokens= [sent for sent in doc.sents]
    #print(sent_tokens)

    sent_scores={}
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                        sent_scores[sent]= word_freq[word.text]
                else:
                        sent_scores[sent]+= word_freq[word.text]
    #print(sent_scores)

    select_len = int(len(sent_tokens) * 0.3)
    #print(select_len)

    summary = nlargest(select_len, sent_scores, key= sent_scores.get)
    #print(summary)


    final_summary = [word.text for word in summary]
    summary= ' '.join(final_summary)
    #print(summary)
    #print("length of original text", len(text.split(' ')))
    #print("length of summary text", len(summary.split(' ')))
    # return summary,doc,len(rawdocs.split(' ')), len(summary.split(' '))


    return summary


if __name__ == '__main__':
     print(summarizer('''

This study presents two types of Kidney cancer detection one is with the help of images and another one is with the help of blood test samples value. Kidney disease is a condition caused by renal disease of the kidneys. In the present study, Kidney cancer is one of the critical diseases for patient diagnosis and classification. Early detection and good treatment can avoid or decrease the growth of cancer disease into the final stage where dialysis or renal transplantation is the only way of saving the life of the patient. Another way is with machine learning models with this model the disease at an early stage can be detected, which is one of the important tasks in today's world. This research proposed kidney image detection through deep learning models like Convolutional Neural Networks (CNNs), and blood sample dataset values through Artificial Neural Network (ANN) models that can be helpful for the early diagnosis of cancer. The existing studies have mainly used only simple CNN models and have done another classification of kidney images. This research consists of CNN with more convolution layers for classifying images of cancer kidneys and normal kidneys and ANN is used for kidney cancer prediction using dataset values. This research will be helpful for early and accurate diagnosis of kidney cancer to save the lives of many patients. Lastly, there is an application page that contains a code in the backend that predicts whether a person is suffering from kidney cancer or not.
'''))
     print(en_core_web_sm)