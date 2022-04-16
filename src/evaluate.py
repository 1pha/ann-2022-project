import numpy as np
from sklearn.metrics import roc_auc_score, classification_report


def calculate_result(model, dataset):

    probas = np.array([])
    labels = np.array([])

    for x, y in dataset:

        probas = np.concatenate([probas, model.predict(x).reshape(-1)])
        labels = np.concatenate([labels, y])

    preds = (probas >= 0.5).astype(int)
    return roc_auc_score(labels, probas), classification_report(labels, preds)
