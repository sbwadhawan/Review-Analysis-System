import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def train():
    columns = ['sentence', 'sentiment']
    df_1 = pd.read_csv('imdb_labelled.txt', sep='\t', header=None)
    df_2 = pd.read_csv('amazon_cells_labelled.txt', sep='\t', header=None)
    df_3 = pd.read_csv('yelp_labelled.txt', sep='\t', header=None)
    df = pd.concat((df_1, df_2, df_3))
    df.columns = columns
    X = df['sentence'].values
    y = df['sentiment'].values

    tfidf = TfidfVectorizer()
    X = tfidf.fit_transform(X)

    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size = 0.25)

    logistic = LogisticRegression()
    logistic.fit(x_train, y_train)

    y_pred = logistic.predict(x_test)
    score = accuracy_score(y_test,y_pred)
    print("Logistic Accuracy",score)

    svm = SVC()
    svm.fit(x_train,y_train)

    y_pred = svm.predict(x_test)
    score = accuracy_score(y_test, y_pred)
    print("SVM Accuracy", score)

    nb = MultinomialNB()
    nb.fit(x_train,y_train)

    y_pred = nb.predict(x_test)
    score = accuracy_score(y_test, y_pred)
    print("Naive Bayes Accuracy", score)

    tree = DecisionTreeClassifier()
    tree.fit(x_train,y_train)

    y_pred = tree.predict(x_test)
    score = accuracy_score(y_test, y_pred)
    print("Decision Tree Accuracy", score)

    return tfidf, logistic, svm, nb, tree

def test(userInput):
    tfidf, log, svm, nb, tree = train()
    review_tfidf = tfidf.transform([userInput])
    y_pred = log.predict(review_tfidf)
    # print(y_pred)
    if y_pred[0] == 0:
        pred = "Negative"
    else:
        pred = "Positive"
    # score = accuracy_score(y_test, y_pred)
    return pred