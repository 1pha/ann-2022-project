import tensorflow as tf

from src.dataset import load_test_dataset
from src import Configuration, build_googlenet


def probs2label(probs):
    if probs > 0.5:
        label = 1
    else:
        label = 0
    return label


def inference(config):

    tf.random.set_seed(config.seed)

    test_ds, test_df = load_test_dataset(config)
    model = build_googlenet(config)
    model_path = "./_models/LR-0.001_BSZ-32_AUG-True_REG-None_LS-0.3_SCH-None/ckpts/65-AUC0.9832-ACC0.9532.hdf5"
    model.load_weights(model_path)

    pred = model.predict(test_ds)

    test_df["predicted"] = list(map(lambda x: probs2label(x), pred))
    test_df["filename"] = test_df["filename"].apply(
        lambda fname: fname.split("./data/test/")[-1]
    )
    test_df.to_csv(f"submission.csv", index=False)


if __name__ == "__main__":

    config = Configuration()
    inference(config)
