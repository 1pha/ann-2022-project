# ANN 2022 Classification Problem

I was assigned with GoogleNet, a.k.a. Inception model to increase performance of retianl dataset which is to classify diabetic retinopathy from fundus images.
Since GoogleNet was released in 2014, there has been tremendous works to increase performance other than the model structure such as data augmentation, scheduling learning rate or more optimizers[^1]. Followings are my plans to implement further.

+ RandAugment [^2]
+ Weight Decay 
+ Label Smoothing
+ Stochastic Depth [^4]:
+ Cosine Decay ([Keras](https://www.tensorflow.org/api_docs/python/tf/keras/optimizers/schedules/CosineDecay))
+ Early stoppings ([Keras](https://keras.io/api/callbacks/early_stopping/))

[^1]: Bello, Irwan, et al. "**Revisiting resnets: Improved training and scaling strategies.**" Advances in Neural Information Processing Systems 34 (2021).
[^2]: Cubuk, Ekin D., et al. "**Randaugment: Practical automated data augmentation with a reduced search space.**" Proceedings of the IEEE/CVF Conference on Computer Vision and Pattern Recognition Workshops. 2020.
[^4]: Huang, Gao, et al. "**Deep networks with stochastic depth.**" European conference on computer vision. Springer, Cham, 2016.
