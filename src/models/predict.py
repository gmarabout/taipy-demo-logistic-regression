from sklearn.linear_model import LogisticRegression


def train(X, Y):
    X_train, Y_train = X[:50], Y[:50]
    X_test, Y_test = X[50:], Y[50:]
    # Using scikit-learn default
    regression = LogisticRegression(random_state=0).fit(X_train, Y_train)
    print(f"intercept: {regression.intercept_} coefficients: {regression.coef_}")
    print(f"train accuracy: {regression.score(X_train, Y_train)}")
    print(f"test accuracy: {regression.score(X_test, Y_test)}")
    return regression


def predict(x, regression: LogisticRegression):
    return regression.predict(x)
