import pathlib
import tensorflow as tf


def load_train_dataset(
    path: str = "./data/train/",
    validation_split: float = 0.2,
    img_height: int = 224,
    img_width: int = 224,
    batch_size: int = 16,
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

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="validation",
        seed=42,
        image_size=(img_height, img_width),
        batch_size=batch_size,
    )
    val_ds = _apply_normalization(val_ds)

    return train_ds, val_ds

def _apply_normalization(dataset):

    normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(1./255)
    normalized_ds = dataset.map(lambda x, y: (normalization_layer(x), y))
    return normalized_ds

if __name__=="__main__":

    train_ds, val_ds = load_train_dataset()