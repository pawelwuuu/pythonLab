# models/svm_model.py
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.calibration import CalibratedClassifierCV

def train_svm_model(X, y, kernel='linear', test_size=0.2):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=42)
    
    base_svm = SVC(kernel=kernel, probability=False)
    model = CalibratedClassifierCV(base_svm, method='sigmoid', cv=3)
    model.fit(X_train, y_train)
    
    y_pred = model.predict(X_test)
    y_proba = model.predict_proba(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    
    full_proba = model.predict_proba(X)
    
    return model, accuracy, full_proba