from sklearn.svm import SVC
import numpy as np

def classifyBySVM(Train_donors, Train_labels, Test_donors1, Test_labels1, Test_donors2, Test_labels2):
    import numpy as np
    X_train = np.array(Train_donors)
    y_train = np.array(Train_labels)
    X_test1 = np.array(Test_donors1)
    y_test1 = np.array(Test_labels1)
    X_test2 = np.array(Test_donors2)
    y_test2 = np.array(Test_labels2)
    # kernel = 'rbf'
    clf = SVC(kernel='rbf',gamma='auto')
    clf.fit(X_train, y_train)
    score_rbf1 = clf.score(X_test1, y_test1)
    print("the SN of rbf is : %f"%score_rbf1)
    score_rbf2 = clf.score(X_test2, y_test2)
    print("the SP of rbf is : %f"%score_rbf2)
