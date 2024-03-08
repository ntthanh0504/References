import numpy as np
from sklearn.linear_model import LogisticRegression

def forward_selection(X_train, y_train, features):
    """Perform forward selection feature selection.

    Args:
        X_train: A Pandas DataFrame containing the training data.
        y_train: A Pandas Series containing the target variable.
        features: A list of all the features.

    Returns:
        A list of the selected features.
    """

    selected_features = []
    while features:
        best_feature = None
        best_score = None

        for feature in features:
            if feature not in selected_features:
                model = LogisticRegression(max_iter=1000)
                model.fit(X_train[selected_features + [feature]], y_train)
                score = model.score(X_train[selected_features + [feature]], y_train)

                if best_score is None or score > best_score:
                    best_feature = feature
                    best_score = score

        if best_feature is None:
            break

        selected_features.append(best_feature)
        features.remove(best_feature)

    return selected_features

def backward_elimination(X_train, y_train, features):
    """Perform backward elimination feature selection.

    Args:
        X_train: A Pandas DataFrame containing the training data.
        y_train: A Pandas Series containing the target variable.
        features: A list of all the features.

    Returns:
        A list of the selected features.
    """

    selected_features = features.copy()
    while selected_features:
        worst_feature = None
        worst_score = None

        for feature in selected_features:
            model = LogisticRegression(max_iter=1000)
            model.fit(X_train.drop([feature], axis=1), y_train)
            score = model.score(X_train.drop([feature], axis=1), y_train)

            if worst_score is None or score < worst_score:
                worst_feature = feature
                worst_score = score

        if worst_feature is None:
            break

        selected_features.remove(worst_feature)

    return selected_features
