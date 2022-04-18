import numpy as np
from sklearn.metrics import roc_auc_score, classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme()


def calculate_result(model, dataset, sampling=None):

    probas = np.array([])
    labels = np.array([])

    for x, y in dataset:

        probas = np.concatenate([probas, model.predict(x).reshape(-1)])
        labels = np.concatenate([labels, y])

    preds = (probas >= 0.5).astype(int)

    auc, report = roc_auc_score(labels, probas), classification_report(labels, preds)
    cf = confusion_matrix(labels, preds)
    if sampling is not None:
        print(f"{sampling.upper()}")
    print(f"AUC: {auc:.4f}")
    print(report)
    print(cf)
    return auc, report, cf


def plot_loss_acc(hist, title, save=None):

    fig, loss_ax = plt.subplots(figsize=(12, 7))
    acc_ax = loss_ax.twinx()

    loss_ax.set_title(title, size="xx-large")

    train_loss = loss_ax.plot(
        hist.history["loss"], "b", linestyle="--", linewidth=2, label="Train Loss"
    )
    valid_loss = loss_ax.plot(
        hist.history["val_loss"], "b", linestyle="-", linewidth=2, label="Valid Loss"
    )
    loss_ax.set_xlabel("Epochs", size="x-large")
    loss_ax.set_ylabel("Binary Entropy Loss", size="x-large")
    loss_ax.tick_params(labelsize="large")

    train_acc = acc_ax.plot(
        hist.history["accuracy"], "r", linestyle="--", linewidth=2, label="Train Acc"
    )
    valid_acc = acc_ax.plot(
        hist.history["val_accuracy"], "r", linestyle="-", linewidth=2, label="Valid Acc"
    )
    acc_ax.set_ylabel("Accuracy (%)", size="x-large")
    acc_ax.tick_params(labelsize="large")

    _lns = train_loss + valid_loss + train_acc + valid_acc
    labs = [l.get_label() for l in _lns]
    acc_ax.legend(_lns, labs, loc="upper left")

    # plt.show()
    if save is not None:
        fig.savefig(save + "/loss_acc.png")
    return fig


def plot_loss_auc(hist, title, save=None):

    fig, loss_ax = plt.subplots(figsize=(12, 7))
    acc_ax = loss_ax.twinx()

    loss_ax.set_title(title, size="xx-large")

    train_loss = loss_ax.plot(
        hist.history["loss"], "b", linestyle="--", linewidth=2, label="Train Loss"
    )
    valid_loss = loss_ax.plot(
        hist.history["val_loss"], "b", linestyle="-", linewidth=2, label="Valid Loss"
    )
    loss_ax.set_xlabel("Epochs", size="x-large")
    loss_ax.set_ylabel("Binary Entropy Loss", size="x-large")
    loss_ax.tick_params(labelsize="large")

    train_acc = acc_ax.plot(
        hist.history["auc"], "y", linestyle="--", linewidth=2, label="Train AUC"
    )
    valid_acc = acc_ax.plot(
        hist.history["val_auc"], "y", linestyle="-", linewidth=2, label="Valid AUC"
    )
    acc_ax.set_ylabel("AUROC", size="x-large")
    acc_ax.tick_params(labelsize="large")

    _lns = train_loss + valid_loss + train_acc + valid_acc
    labs = [l.get_label() for l in _lns]
    acc_ax.legend(_lns, labs, loc="upper left")

    # plt.show()
    if save is not None:
        fig.savefig(save + "/loss_auc.png")
    return fig


def plot_auc_acc(hist, title, save=None):

    fig, loss_ax = plt.subplots(figsize=(12, 7))
    acc_ax = loss_ax.twinx()

    loss_ax.set_title(title, size="xx-large")

    train_loss = loss_ax.plot(
        hist.history["auc"], "y", linestyle="--", linewidth=2, label="Train AUC"
    )
    valid_loss = loss_ax.plot(
        hist.history["val_auc"], "y", linestyle="-", linewidth=2, label="Valid AUC"
    )
    loss_ax.set_xlabel("AUC", size="x-large")
    loss_ax.set_ylabel("Binary Entropy Loss", size="x-large")
    loss_ax.tick_params(labelsize="large")

    train_acc = acc_ax.plot(
        hist.history["accuracy"], "r", linestyle="--", linewidth=2, label="Train ACC"
    )
    valid_acc = acc_ax.plot(
        hist.history["val_accuracy"], "r", linestyle="-", linewidth=2, label="Valid ACC"
    )
    acc_ax.set_ylabel("Accuracy (%)", size="x-large")
    acc_ax.tick_params(labelsize="large")

    _lns = train_loss + valid_loss + train_acc + valid_acc
    labs = [l.get_label() for l in _lns]
    acc_ax.legend(_lns, labs, loc="upper left")

    # plt.show()
    if save is not None:
        fig.savefig(save + "/auc_acc.png")
    return fig
