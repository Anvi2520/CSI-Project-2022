import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.tree import export_graphviz
from six import StringIO
from IPython.display import Image
import pydotplus
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report, confusion_matrix



def clpred(hospital_id,age,gender,aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,lymphoma,solid_tumor_with_metastasis):
    df = pd.read_csv("dataset.csv")
    values=[hospital_id,age,gender,aids,cirrhosis,diabetes_mellitus,hepatic_failure,immunosuppression,leukemia,lymphoma,solid_tumor_with_metastasis]
    #print(df)
    df = df.dropna(axis=0, how='any')
    #print(df)
    string_to_int = preprocessing.LabelEncoder()
    df = df.apply(string_to_int.fit_transform)
    df.rename(columns={'Success/Fail': 'Success_Fail'}, inplace=True)
    #print(df)
    feature_cols = ['hospital_id','age','gender','aids', 'cirrhosis', 'diabetes_mellitus', 'hepatic_failure',
                'immunosuppression', 'leukemia', 'lymphoma', 'solid_tumor_with_metastasis']
    X = df[feature_cols]
    y = df.Success_Fail
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.15)

    classifier =DecisionTreeClassifier(criterion="entropy", random_state=100)
    classifier.fit(X_train, y_train)
    y_pred= classifier.predict(X_test)

    acc=metrics.accuracy_score(y_test, y_pred)
    print("Accuracy:",acc)
    data_p = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
    print(confusion_matrix(y_test, y_pred))
    print(classification_report(y_test, y_pred))
    '''dot_data = StringIO()
    export_graphviz(classifier, out_file=dot_data, max_depth=7,filled=True, rounded=True,special_characters=True, feature_names=feature_cols, class_names=['0', '1'])
    graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
    graph.write_png('Success_Fail.png')
    Image(graph.create_png())'''
    new_input = [values]
    return classifier.predict(new_input)