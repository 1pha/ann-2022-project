import tensorflow as tf

from .model import build_googlenet
from. dataset import load_train_dataset
from .optimizers import build_optimizer
from .evaluate import plot_auc_acc, plot_loss_acc, plot_loss_auc

def run(config):

    model = build_googlenet(config)
    train_ds, valid_ds = load_train_dataset(config)

    steps_per_epoch = len(train_ds)
    optimizer = build_optimizer(config, steps_per_epoch)

    model.compile(
    optimizer=optimizer,
    loss=tf.losses.BinaryCrossentropy(
        label_smoothing=config.label_smoothing,
        name="bce"
    ),
    metrics=['accuracy', tf.keras.metrics.AUC()]
    )

    callbacks = []
    if config.early_stop:
        callbacks.append(tf.keras.callbacks.EarlyStopping(monitor='val_loss', patience=config.patience))

    if config.scheduler == "plateau":
        callbacks.append(tf.keras.callbacks.ReduceLROnPlateau(monitor="val_loss", factor=.2, patience=config.patience, min_lr=1e-5))

    callbacks.append(
        tf.keras.callbacks.ModelCheckpoint(
            config.output_dir + "/ckpts/{epoch:02d}-{val_auc:.4f}.hdf5",
            monitor="val_loss",
            save_best_only=True,
            save_weights_only=False,
        )
    )

    callbacks.append(
        tf.keras.callbacks.CSVLogger(
            config.output_dir + "/hist.csv",
            separator=",",
            append=True,
        )
    )

    hist = model.fit(
    train_ds,
    validation_data=valid_ds,
    epochs=config.epochs,
    callbacks=callbacks
    )
    config.save(config.output_dir)

    title = f"Batch size {config.batch_size}, {config.optimizer.capitalize()}, {config.scheduler} \n Label Smoothing={config.label_smoothing} Augmentation: {config.use_augmentation}",

    if "auc" not in hist.history.keys():
        hist.history["auc"] = hist.history["auc_1"] 
        hist.history["val_auc"] = hist.history["val_auc_1"] 

    plot_loss_acc(hist, title, config.output_dir);
    plot_loss_auc(hist, title, config.output_dir);
    plot_auc_acc(hist, title, config.output_dir);