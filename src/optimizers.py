import tensorflow as tf
import tensorflow_addons as tfa


def _build_scheduler(config, steps_per_epoch):

    name = config.scheduler
    if name == "cosine":
        scheduler = tf.keras.optimizers.schedules.CosineDecay(
            initial_learning_rate=config.learning_rate,
            decay_steps=config.decay_steps,
            alpha=0.0
        )
    elif name == "cyclic":
        scheduler = tfa.optimizers.CyclicalLearningRate(
            initial_learning_rate=config.learning_rate,
            maximal_learning_rate=config.maximal_learning_rate,
            scale_fn=lambda x: 1 / (2.**(x-1)),
            step_size=2 * steps_per_epoch
        )
    return scheduler


def build_optimizer(config, steps_per_epoch: int = None):

    name = config.optimizer
    if config.scheduler is None or config.scheduler == "plateau":
        if name == "adam":
            optimizer = tf.keras.optimizers.Adam(learning_rate=config.learning_rate, decay=config.weight_decay)
        elif name == "adamw":
            optimizer = tfa.optimizers.AdamW(learning_rate=config.learning_rate, weight_decay=config.weight_decay)

    else:
        scheduler = _build_scheduler(config, steps_per_epoch)
        if name == "adam":
            optimizer = tf.keras.optimizers.Adam(scheduler)
        elif name =="adamw":
            optimizer = tfa.optimizers.AdamW(scheduler)

    return optimizer
