# Assignment \#4

## [Paper 3](paper3.pdf)

### Summary
+ This paper introduces interpretability method for deep learning models with injected stochasticity. Suggested methods are mathematically well proven and their visualization results are qualitatively better compared to preceding methods.

### Strengths
+ Their logics make sense enough. Improving the quality by injecting the adjacent nature of pixels was a nice idea and its effect was clearly shown.
+ Nice qualitative results compared to previous methods. Their saliency map is more easy to capture the original objects in the scene.
+ Their robustness were also clearly shown in by uncertainty explanation and quantitative results. Stronger perturbation did not upset the results.

### Weaknesses
+ The logical flow itself if plausible but not sure whehter they also makes sense in math literature. Also was not clear to catch the full understanding of the logic - such as, how are saliency map calculated at last, 
+ Due to page limits of ICLR 2021, Figure 8, the schematic description, which best explains the method was pushed to appendix.
+ Introduced soft-TV injects higher correlation between adjacent pixels. This improved the visualization with naive Gaussian standard prior. However, if task that requires logical relation between objects in a given image (e.g. visual question answering) this soft-TV would not help explaining the model.
+ It is questioned whether the inference time in quantiative results were fairly compared.

### Rating and Justification
+ Accept: Satisfied with proofs, but not confident if they are accurate.

### Additional Comments
+ None.

### Score
+ Weak accept

## [Paper 4](paper4.pdf)

### Summary
+ This paper introduces a additional affine-transformation inside the traditional 3D convolutional operation thereby trying to increase the performance and explainability. However, their intended results were not clearly shown in the context.

### Strengths
+ The approach of adding minimum number of parameters to traditional model to both increase the performance and explainability was novel.

### Weaknesses
+ It is still not clear why there needs a translation matrix Theta for every each time sequence. Moreover, there was no clear explanations on "Theoretically it should be possible to achieve a more efficient implementation of the 3TConv and we reserve the investigation of this matter for future work." Though it is trivial to show how affine transformation matrices are constructed with introduced 4 parameters - {s, r, t_x, t_y}, it would have been much better to show this with formula.
+ Most importantly, the main figure 1 which compares saliency and activation-maximization method from 3DConv and 3TConv, does not explain any novelty or difference between traditional and introduced methods and their interpretation is too subjective. It is also suspicious whether those channels were cherry picked since there are utterly many channels. It would have been better to fairly aggregate the results to make readers more comprehendable. However, it is said that we could not look up the attached video they mentioned.
+ Their Figure 2 & 3 are problematic in two ways: 1. Cannot understand what they convey 2. Nearly impossible to train their suggested networks from scratch (without pre-training).
+ Listed limitations and further works in the discussion part should have been done in their work.

### Rating and Justification
+ Reject: Their method was not clearly explained and both quantitative & qualitative results were utterly not persuasive.

### Additional Comments
+ Number of parameters listed in table 1 could be written in human interpretable way - i.e. 7.4M.
### Score
+ Clear Reject
## Relative Assessment
+ Paper 3 > Paper 4

## Reference

+ [Interpretable Machine Learning: Fundamental Principles and 10 Grand Challenges](https://arxiv.org/pdf/2103.11251.pdf)
    
    *5 Fundamental Principles*
    1. An interpretable machine learning model obeys a domain-specific set of constraints to allow it (or its predictions, or the data) to be more easily understood by humans. These constraints can differ dramatically depending on the domain.
    2. Despite common rhetoric, interpretable models do not necessarily create or enable trust – they could also enable distrust. They simply allow users to decide whether to trust them. In other words, they permit a decision of trust, rather than trust itself.
    3. It is important not to assume that one needs to make a sacrifice in accuracy in order to gain interpretability. In fact, interpretability often begets accuracy, and not the reverse. Interpretability versus accuracy is, in general, a false dichotomy in machine learning.
    4. As part of the full data science process, one should expect both the performance metric and interpretability metric to be iteratively refined.
    5. For high stakes decisions, interpretable models should be used if possible, rather than “explained” black box models.

    *10 Grand Challenges*
    1. Optimizing sparse logical models such as decision trees
    2. Optimization of scoring systems
    3. Placing constraints into generalized additive models to encourage sparsity and better interpretabilit
    4. Modern case-based reasoning, including neural networks and matching for causal inference
    5. Complete supervised disentanglement of neural networks
    6. Complete or even partial unsupervised disentanglement of neural networks
    7. Dimensionality reduction for data visualization
    8. Machine learning models that can incorporate physics and other generative or causal constraints
    9. Characterization of the “Rashomon set” of good models.
    10. Interpretable reinforcement learning
+ [**SSIM**](https://ieeexplore.ieee.org/document/1284395)(Structural Simlarity Index Measure)[^1]: Measure of comparing two images in terms of "knwon" human property of perceiving images - luminance, contrast and structure. The closer they are, SSIM being closer to 1. ([ref](https://www.crcv.ucf.edu/data/UCF101.php))
+ ICLR 2021 papers were *limited to 8 pages* without reference.
+ [**Jester**](https://openaccess.thecvf.com/content_ICCVW_2019/papers/HANDS/Materzynska_The_Jester_Dataset_A_Large-Scale_Video_Dataset_of_Human_Gestures_ICCVW_2019_paper.pdf)[^2] is a gesture recognition dataset, consist of 148k videos with 27 classes. Average duration of videos is 3 seconds.
+ [**UCF101**](https://www.crcv.ucf.edu/data/UCF101.php)[^3] is another action recognition dataset of realistic action videos, collected from YouTube. As the name insists, they have 101 categories with 13k videos.

[^1]: Wang, Zhou, et al. "**Image quality assessment: from error visibility to structural similarity.**" IEEE transactions on image processing 13.4 (2004): 600-612.

[^2]: Materzynska, Joanna, et al. "**The jester dataset: A large-scale video dataset of human gestures.**" Proceedings of the IEEE/CVF International Conference on Computer Vision Workshops. 2019.

[^3]: Soomro, Khurram, Amir Roshan Zamir, and Mubarak Shah. "**UCF101: A dataset of 101 human actions classes from videos in the wild.**" arXiv preprint arXiv:1212.0402 (2012).