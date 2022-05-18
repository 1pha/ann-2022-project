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

### Strengths

### Weaknesses

### Rating and Justification

### Additional Comments

### Score

## Relative Assessment

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
+ **SSIM**(Structural Simlarity Index Measure): Measure of comparing two images in terms of "knwon" human property of perceiving images - luminance, contrast and structure. The closer they are, SSIM being closer to 1.
