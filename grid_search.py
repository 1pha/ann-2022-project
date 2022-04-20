import os
import tensorflow as tf

from src import run, Configuration

for learning_rate in [1e-2, 1e-3]:
    for batch_size in [16, 32]:
        for use_augmentation in [True, False]:
            for regularizer in ["l2", None]:
                for label_smoothing in [0.3, 0]:
                    for scheduler in ["plateau", None]:
                        config = Configuration()
                        tf.random.set_seed(config.seed)

                        config.learning_rate = learning_rate
                        config.batch_size = batch_size
                        config.use_augmentation = use_augmentation
                        config.regularizer = regularizer
                        config.label_smoothing = label_smoothing
                        config.scheduler = scheduler

                        config.output_dir = f"./models/LR-{learning_rate}_BSZ-{batch_size}_AUG-{use_augmentation}_REG-{regularizer}_LS-{label_smoothing}_SCH-{scheduler}"
                        os.makedirs(config.output_dir, exist_ok=True)
                        print(config.output_dir)
                        try:
                            tf.keras.backend.clear_session()
                            run(config)
                        except:
                            raise
