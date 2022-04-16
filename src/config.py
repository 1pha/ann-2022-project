import json
from dataclasses import dataclass, field


@dataclass
class Configuration:

    epochs: int = field(default=30, metadata={"help": "How many epochs to run."})
    early_stop: bool = field(
        default=True, metadata={"help": "To use early stopping callbacks or not."}
    )
    patience: int = field(
        default=5, metadata={"help": "Will monitor on loss with epoch-wise. Default=5"}
    )
    randaugment_n: int = field(
        default=3, metadata={"help": "How many augmentation methods to use."}
    )
    randaugment_m: int = field(
        default=2, metadata={"help": "Intensity of randaugment."}
    )
    seed: int = field(default=42, metadata={"help": "Randomized seeds."})
    learning_rate: float = field(
        default=1e-3, metadata={"help": "Initial learning rate to use."}
    )
    weight_decay: float = field(
        default=1e-2, metadata={"help": "Intensity of L2-weight decay regularization. Default=1e-2"}
    )
    label_smoothing: float = field(
        default=0.,
        metadata={"help": "Intensity of label smoothing. If 0 given, we do not use label smoothing. Around .2 is roughly okay."}
    )
    use_augmentation: bool = field(
        default=True,
        metadata={"help": "Whether to use augmentation or not."}
    )

    def to_dict(self):
        return vars(self)

    def save(self, fname: str):

        fname += "config.json"
        configs = self.to_dict()
        with open(fname, "w") as f:
            json.dump(configs, f)
