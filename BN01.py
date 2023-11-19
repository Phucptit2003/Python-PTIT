import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Đọc dữ liệu từ file CSV và chuyển đổi nó thành một pandas DataFrame
def load_data(file_path):
    df = pd.read_csv(file_path)
    return df

# Tách tập dữ liệu thành hai phần: tập huấn luyện và tập kiểm tra
def split_data(df, test_size=0.2):
    X = df.iloc[:, :-1].values
    y = df.iloc[:, -1].values
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=0)
    return X_train, X_test, y_train, y_test

# Xây dựng cây quyết định
def build_decision_tree(X_train, y_train, criterion='entropy'):
    clf = DecisionTreeClassifier(criterion=criterion)
    clf.fit(X_train, y_train)
    return clf

# Đánh giá cây quyết định bằng cách sử dụng tập kiểm tra
def evaluate_model(clf, X_test, y_test):
    y_pred = clf.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy
