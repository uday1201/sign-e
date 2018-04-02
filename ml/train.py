from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier()

import pickle

feats, labels = pickle.load(open('main.p', 'rb'))

clf.fit(feats, labels)

pickle.dump(clf, open('model.p', 'wb'))
