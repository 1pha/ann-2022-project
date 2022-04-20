import pathlib
import tensorflow as tf
from tensorflow.keras import layers

AUTO = tf.data.AUTOTUNE


def load_train_dataset(
    config,
    path: str = "./data/train/",
    validation_split: float = 0.2,
    img_height: int = 224,
    img_width: int = 224,
):
    data_dir = pathlib.Path(path)

    train_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="training",
        seed=42,
        image_size=(img_height, img_width),
        batch_size=config.batch_size,
    )
    train_ds = _apply_normalization(train_ds)

    val_ds = tf.keras.preprocessing.image_dataset_from_directory(
        data_dir,
        validation_split=validation_split,
        subset="validation",
        seed=42,
        image_size=(img_height, img_width),
        batch_size=config.batch_size,
    )
    val_ds = _apply_normalization(val_ds)

    if config.use_augmentation:
        train_ds = _apply_augmentation(train_ds)

    return train_ds.prefetch(AUTO), val_ds.prefetch(AUTO)


def load_test_dataset(
    config,
    path: str = "./data/test/",
    img_height: int = 224,
    img_width: int = 224,
):
    from glob import glob
    import pandas as pd
    from keras.preprocessing.image import ImageDataGenerator

    test_pic_list = list(glob(path + "/*"))
    test_df = pd.DataFrame(
        {
            "filename": test_pic_list,
            "predicted": [-1 for i in range(len(test_pic_list))],
        }
    )
    test_datagen = ImageDataGenerator(
        rescale=1.0 / 255,
    )
    test_gen = test_datagen.flow_from_dataframe(
        dataframe=test_df,
        directory=None,
        x_col="filename",
        class_mode=None,
        shuffle=False,
        target_size=(img_height, img_width),
        batch_size=config.batch_size,
    )
    return test_gen, test_df


def _apply_normalization(dataset):

    normalization_layer = tf.keras.layers.experimental.preprocessing.Rescaling(
        1.0 / 255
    )
    normalized_ds = dataset.map(lambda x, y: (normalization_layer(x), y))
    return normalized_ds


def _apply_augmentation(dataset):

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
