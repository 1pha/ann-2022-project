import os
import tensorflow as tf

from src import run, Configuration

for seed in [42, 43, 44, 45, 46]:
    for augmentation in [False, "soft", "hard"]:
        for pre_trained in [False, "freeze", "fine"]:

            config = Configuration()
            config.seed = seed
            config.use_augmentation = augmentation
            if pre_trained == False:
                config.use_pretrained = False
                config.linear_probing = False
                
            elif pre_trained == "freeze":
                config.use_pretrained = True
                config.linear_proibing = False
                
            elif pre_trained == "fine":
                config.use_pretrained = True
                config.linear_proibing = True
                
            tf.random.set_seed(config.seed)

            try:
                tf.keras.backend.clear_session()
                run(config)
            except:
                raise
