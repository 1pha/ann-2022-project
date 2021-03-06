import json
from dataclasses import dataclass, field


@dataclass
class Configuration:

    epochs: int = field(default=200, metadata={"help": "How many epochs to run."})
    batch_size: int = field(default=32, metadata={"help": "Control batch size"})
    early_stop: bool = field(
        default=True, metadata={"help": "To use early stopping callbacks or not."}
    )
    patience: int = field(
        default=15, metadata={"help": "Will monitor on loss with epoch-wise. Default=5"}
    )
    seed: int = field(default=42, metadata={"help": "Randomized seeds."})
    optimizer: str = field(default="adam", metadata={"help": "Which optimizer to use."})
    learning_rate: float = field(
        default=1e-3, metadata={"help": "Initial learning rate to use."}
    )
    weight_decay: float = field(
        default=1e-2,
        metadata={"help": "Intensity of L2-weight decay regularization. Default=1e-2"},
    )
    label_smoothing: float = field(
        default=0.0,
        metadata={
            "help": "Intensity of label smoothing. If 0 given, we do not use label smoothing. Around .2 is roughly okay."
        },
    )
    use_augmentation: bool = field(
        default=True, metadata={"help": "Whether to use augmentation or not. Put `False`, `soft` or `hard`."}
    )
    output_dir: str = field(
        default=None,
        metadata={
            "help": "Indicating model directory name. Please assign this before you train."
        },
    )
    scheduler: str = field(
        default=None,
        metadata={"help": "Learning rate scheduler. Use one of 'cosine' or 'cyclic'"},
    )
    maximal_learning_rate: float = field(
        default=1e-3,
        metadata={
            "help": "Maximal value of learning rate when cyclie scheduler was used."
        },
    )
    regularizer: str = field(
        default=None,
        metadata={
            "help": "Which regularizer to use. Default as None, which means we don't use regularizer. Either choose l1 or l2. Regularizer will be applied to all weights and biases."
        },
    )
    reg_lambda: float = field(
        default=1e-5, metadata={"help": "Weights for regularizer term."}
    )
    use_pretrained: bool = field(
        default=False,
        metadata={"help": "Load pre-trained Inception models"}
    )
    linear_probing: bool = field(
        default=False,
        metadata={"help": "If False, do not train pre-trained models. If True, update pre-trained weights."}
    )
    def to_dict(self):
        return vars(self)

    def save(self, fname: str):

        fname += "/config.json"
        configs = self.to_dict()
        with open(fname, "w") as f:
            json.dump(configs, f, indent=4, sort_keys=True)
