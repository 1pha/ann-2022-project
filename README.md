# ANN 2022 Classification Problem

I was assigned with GoogleNet, a.k.a. Inception model to increase performance of retianl dataset which is to classify diabetic retinopathy from fundus images.
Since GoogleNet was released in 2014, there has been tremendous works to increase performance other than the model structure such as data augmentation, scheduling learning rate or more optimizers[^1]. Followings are my plans to implement further.

+ RandAugment [^2]: In the usual 
+ Weight Decay 
+ Label Smoothing
+ Cosine Decay ([Keras](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay))
+ Early stoppings ([Keras](https://keras.io/api/callbacks/early_stopping/))
+ Stochastic Depth [^4]: This method only works for networks that has residuals so that the input pass can skip random layers. Since Inception does not have skip connections, this method was not used.
## Findings

### Best Configuration?


### Large Batch size did not help

In all cases, batch size of 32 failed to optimize while 16 was able to. Since we had around 1.2k training data, having larger batch sizes takes opportunity of watching 

### Failure Cases

Below is the best AUC results' confusion matrix.


[^1]: Bello, Irwan, et al. "**Revisiting resnets: Improved training and scaling strategies.**" Advances in Neural Information Processing Systems 34 (2021).
[^2]: Cubuk, Ekin D., et al. "**Randaugment: Practical automated data augmentation with a reduced search space.**" Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops. 2020.
[^4]: Huang, Gao, et al. "**Deep networks with stochastic depth.**" European conference on computer vision. Springer, Cham, 2016.
