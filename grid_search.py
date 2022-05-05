import os
import tensorflow as tf

from src import run, Configuration

#for seed in [42, 47, 48, 49, 50, 51]:
for seed in [51]:
    for augmentation in [False, "soft", "hard"]:
        for pre_trained in ["no_trained", "freeze", "fine"]:

            config = Configuration()
            config.seed = seed
            config.use_augmentation = augmentation
            if pre_trained == "no_trained":
                config.use_pretrained = False
                config.linear_probing = False
                
            elif pre_trained == "freeze":
                config.use_pretrained = True
                config.linear_probing = False
                
            elif pre_trained == "fine":
                config.use_pretrained = True
                config.linear_probing = True
                
            tf.random.set_seed(config.seed)
            config.output_dir = f"Seed{seed}-Aug{augmentation}-{pre_trained}"

            try:
                tf.keras.backend.clear_session()
                run(config)
            except:
                raise
