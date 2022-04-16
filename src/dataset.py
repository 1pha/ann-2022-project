import pathlib
import tensorflow as tf
from tensorflow.keras import layers

AUTO = tf.data.AUTOTUNE


def load_train_dataset(
    path: str = "./data/train/",
    validation_split: float = 0.2,
    img_height: int = 224,
    img_width: int = 224,
    batch_size: int = 16,
    randaugment_n: int = 3,
    randaugment_m: int = 2,
):
    data_dir = pathlib.Path(path)

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="training",
        seed=42,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )
    train_ds = _apply_normalization(train_ds)
    train_ds = _apply_augmentation(train_ds, n=randaugment_n, m=randaugment_m)

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="validation",
        seed=42,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )
    val_ds = _apply_normalization(val_ds)
    val_ds = _apply_augmentation(val_ds, n=randaugment_n, m=randaugment_m)

    return train_ds.prefetch(AUTO), val_ds.prefetch(AUTO)


def _apply_normalization(dataset):

    normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(
        1.0 / 255
    )
    normalized_ds = dataset.map(lambda x, y: (normalization_layer(x), y))
    return normalized_ds


def _apply_augmentation(dataset, n=3, m=2, seed: int = 42):

    simple_aug = tf.keras.Sequential(
        [
            layers.RandomFlip(),
            layers.RandomRotation(factor=0.02),
            layers.RandomZoom(height_factor=0.2, width_factor=0.2),
        ]
    )

    augmentation_ds = dataset.map(
        lambda x, y: (simple_aug(x), y), num_parallel_calls=AUTO
    )
    return augmentation_ds


if __name__ == "__main__":

    train_ds, val_ds = load_train_dataset()
