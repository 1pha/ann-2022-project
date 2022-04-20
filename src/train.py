import tensorflow as tf

from .model import build_googlenet
from .dataset import load_train_dataset
from .optimizers import build_optimizer
from .evaluate import plot_auc_acc, plot_loss_acc, plot_loss_auc

import wandb
from wandb.keras import WandbCallback


def run(config):

    wandb.init(config=config.to_dict(), project="ann-2022", name=config.output_dir[9:])

    model = build_googlenet(config)
    train_ds, valid_ds = load_train_dataset(config)

    steps_per_epoch = len(train_ds)
    optimizer = build_optimizer(config, steps_per_epoch)

    model.compile(
        optimizer=optimizer,
        loss=tf.losses.BinaryCrossentropy(
            label_smoothing=config.label_smoothing, name="bce"
        ),
        metrics=["accuracy", tf.keras.metrics.AUC()],
    )

    callbacks = []
    if config.early_stop:
        callbacks.append(
            tf.keras.callbacks.EarlyStopping(
                monitor="val_loss", patience=config.patience, min_delta=1e-4
            )
        )

    if config.scheduler == "plateau":
        callbacks.append(
            tf.keras.callbacks.ReduceLROnPlateau(
                monitor="val_loss", factor=0.2, patience=8, min_lr=1e-6
            )
        )

    callbacks.append(WandbCallback())

    hist = model.fit(
        train_ds, validation_data=valid_ds, epochs=config.epochs, callbacks=callbacks
    )
    wandb.finish()
