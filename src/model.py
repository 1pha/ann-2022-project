import re
import tensorflow as tf
from tensorflow.keras import layers, utils


def _set_regularizer(regularizer=None, _lambda=1e-2):

    if regularizer is None:
        return None

    elif regularizer == "l2":
        return tf.keras.regularizers.L2(l2=_lambda)

    elif regularizer == "l1":
        return tf.keras.regularizers.L1(l1=_lambda)

    else:
        raise


def inception_module(prev, c1, c2, c3, c4, regularizer=None):
    """
    prev: previous layer
    c1, c2, c3, c4 are channels/number of filters for 4 parallel paths
    c1: channels for path 1
    c2: a tuple of two channels for path 2
    c3: a tuple of two channels for path 3
    c4: channels for path 1
    """

    # Path 1: 1x1 convolution, c1 channels
    p1 = layers.Conv2D(
        filters=c1,
        kernel_size=(1, 1),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(prev)

    # Path 2: 1x1 convolution with channel c2[0], 3x3 convolution with channel c2[1]
    p2 = layers.Conv2D(
        filters=c2[0],
        kernel_size=(1, 1),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(prev)
    p2 = layers.Conv2D(
        c2[1],
        kernel_size=(3, 3),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
        padding="same",
    )(p2)

    # Path 3: 1x1 convolution with channel c3[0], 5x5 convolution with channel c3[1]
    p3 = layers.Conv2D(
        filters=c3[0],
        kernel_size=(1, 1),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(prev)
    p3 = layers.Conv2D(
        filters=c3[1],
        kernel_size=(5, 5),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
        padding="same",
    )(p3)

    # Path 4: maxpooling layer with 3x3 pool size and stride of 1, 1x1 convolution with c4 channels
    p4 = layers.MaxPool2D(pool_size=(3, 3), strides=1, padding="same")(prev)
    p4 = layers.Conv2D(
        filters=c4,
        kernel_size=(1, 1),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(p4)

    # Concatenate the outputs of all 4 paths
    output = layers.Concatenate()([p1, p2, p3, p4])

    return output


input = layers.Input(shape=[224, 224, 3], name="Input")
output = inception_module(input, 6, (6, 6), (6, 6), 6)

inception = tf.keras.Model(input, output)


def build_googlenet(config):

    ## GoogLeNet

    # Input and stem block
    # Input shape: 224,224,3
    # 7x7 convolution, 3x3 maxpool, 3x3 convolution, 3x3 maxpool

    regularizer = _set_regularizer(config.regularizer, config.reg_lambda)

    input = layers.Input(shape=[224, 224, 3])
    x = layers.Conv2D(
        filters=64,
        kernel_size=(7, 7),
        strides=2,
        padding="same",
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(input)
    x = layers.MaxPool2D(pool_size=(3, 3), strides=2, padding="same")(x)
    x = layers.Conv2D(
        filters=64,
        kernel_size=(1, 1),
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(x)
    x = layers.Conv2D(
        filters=192,
        kernel_size=(3, 3),
        padding="same",
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="relu",
    )(x)
    x = layers.MaxPool2D(pool_size=(3, 3), strides=2, padding="same")(x)

    ### Two inception modules and maxpool
    x = inception_module(x, 64, (96, 128), (16, 32), 32, regularizer=regularizer)
    x = inception_module(x, 128, (128, 192), (32, 96), 64, regularizer=regularizer)
    x = layers.MaxPool2D(pool_size=(3, 3), strides=2, padding="same")(x)

    ### Five inception modules and maxpool
    x = inception_module(x, 192, (96, 208), (16, 48), 64, regularizer=regularizer)
    x = inception_module(x, 160, (112, 224), (24, 64), 64, regularizer=regularizer)
    x = inception_module(x, 128, (128, 256), (24, 64), 64, regularizer=regularizer)
    x = inception_module(x, 112, (144, 288), (32, 64), 64, regularizer=regularizer)
    x = inception_module(x, 256, (160, 320), (32, 128), 128, regularizer=regularizer)
    x = layers.MaxPool2D(pool_size=(3, 3), strides=2, padding="same")(x)

    ### Two Inception modules and average pooling layer
    x = inception_module(x, 256, (160, 320), (32, 128), 128, regularizer=regularizer)
    x = inception_module(x, 384, (192, 384), (48, 128), 128, regularizer=regularizer)
    x = layers.AveragePooling2D(pool_size=(7, 7))(x)
    x = layers.Flatten(name="Flatten")(x)

    ### Dropout & classification head
    x = layers.Dropout(0.4)(x)
    output = layers.Dense(
        units=1,
        kernel_regularizer=regularizer,
        bias_regularizer=regularizer,
        activation="sigmoid",
    )(x)

    googlenet = tf.keras.Model(input, output)
    return googlenet


if __name__ == "__main__":

    model = build_googlenet()
    print(model.summary())
