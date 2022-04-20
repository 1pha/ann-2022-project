# ANN 2022 Classification Problem

I was assigned with GoogleNet [^1], a.k.a. Inception model to increase performance of retianl dataset which is to classify diabetic retinopathy from fundus images.
Since GoogleNet was released in 2014, there has been tremendous works to increase performance other than the model structure such as data augmentation, scheduling learning rate or more optimizers[^2]. Followings are widely used techniques applied in recent vision models to improve performance.

+ **RandAugment** [^3]: With typical datasets such as ImageNet or CIFAR, which are said to be _natural images_, this RandAugment generally improves performance. However with this specialized medical images, most of transformations used in RandAugment is not valid. Therefore I used 3 techniques - flips, slight level of rotation and zoom randomly.
+ **Weight Decay** [^4]: One way to reduce overfitting is by giving constraints on the norm of weight size. Here I tested with L2 and L1 norm to find the best one. Also Adam optimizer was used, compared to original inception model trained with Momentum SGD with 0.9 hyperparameter.
+ **Label Smoothing** [^5]: Typical classification uses one-hot vector as a class label. In order to give softer target labels to model, label smoothing was introduced. Here I tested with label temperature for 0.3.
+ **Learning rate Scheduling**: The original paper scheduled their learning rate by reducing their learning rate by 4% every 8 epochs. However with their models trained on larger dataset, training with same logic might not help. Therefore I scheduled to reduce learning rate when validation loss seemed to saturate.
+ **Early stoppings** ([Keras](https://keras.io/api/callbacks/early_stopping/)): I have monitored validation loss to halt training when no further improvement can be considered. Patience for early stopping was 8 epochs.
+ **Stochastic Depth** [^6]: This method only works for networks that has residuals so that the input pass can skip random layers. Since Inception does not have skip connections, this method was not used.

Therefore total **64 ($2^6$) configurations** were tested.
+ Initial Learning rate: $10^{-2}$, $10^{-3}$
+ Batchc size: 16, 32
+ Augmentation: Apply or Not
+ Weight Decay: L2 or None
+ Label Smoothing: Apply(=0.3) or Not
+ Learning rate Scheduling: Reduce on Plateau or Not


## Findings & Results
Project wandb results found in [LINK](https://wandb.ai/1pha/ann-2022) and also [the report](https://wandb.ai/1pha/ann-2022/reports/ANN-Report-Inception--VmlldzoxODYwMTkz).
Visualization of success/failure cases from validation dataset is stored [here](./analysis.ipynb).

[^1]: Szegedy, Christian, et al. "**Going deeper with convolutions.**" Proceedings of the IEEE conference on computer vision and pattern recognition. 2015.
[^2]: Bello, Irwan, et al. "**Revisiting resnets: Improved training and scaling strategies.**" Advances in Neural Information Processing Systems 34 (2021).
[^3]: Cubuk, Ekin D., et al. "**Randaugment: Practical automated data augmentation with a reduced search space.**" Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops. 2020.
[^4]: Krogh, Anders, and John Hertz. "**A simple weight decay can improve generalization.**" Advances in neural information processing systems 4 (1991).
[^5]: Müller, Rafael, Simon Kornblith, and Geoffrey E. Hinton. "**When does label smoothing help?.**" Advances in neural information processing systems 32 (2019).
[^6]: Huang, Gao, et al. "**Deep networks with stochastic depth.**" European conference on computer vision. Springer, Cham, 2016.
