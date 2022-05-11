# Paper Review Assignment \#3

## Directions
The review for each paper should be structured as follows:

+ _**Summary**_: Explain the key ideas, contributions, and their significance. This is your abstract of the paper. The summary should be phrased to help the authors of the paper [and potential editors] to understand the rest of your review and to be confident that you understand the paper.

+ _**Strengths**_: What about the paper provides value -- interesting ideas that are experimentally validated, an insightful organization of related work, new tools, impressive results, something else?  Most importantly, what can someone interested in the topic learn from the paper?

+ _**Weaknesses**_: What detracts from the contributions? Is the necessary literature cited? Does the paper lack controlled experiments and - if possible - statistical tests to validate the contributions? Are there misleading claims or technical errors? Is it possible to understand (and ideally reproduce) the method and experimental setups by reading the paper?

+ _**Rating and Justification**_: Carefully explain why the paper should be accepted or not.  This section should make clear which of the strengths and weaknesses you consider most significant.

+ _**Additional comments**_: minor suggestions, questions, corrections, etc. that can help the authors improve the paper, but are not crucial for the overall recommendation.

+ Next, give _**a score for each paper**_ out of             clear reject, weak reject, weak accept, clear accept         for each paper.

+ Finally, as this may be easier sometimes, provide a _**RELATIVE assessment of the two papers**_: which one did you like better and why? 

## [Paper 1](paper1.pdf)

### Summary
+ This paper suggests a new model based on multi-layer perceptron (MLP), which was regarded as vanilla model to be complete complex tasks. The major contribution of this paper is a comparable results with typical models and scalability proven.

### Strengths
+ Suggested method is interesting and their results show that gMLP has comparable ability to capture local relationships, especially in visionary tasks.
+ As suggested architecture is far different from typical models widely used in comparing tasks, doing the fair comparison between these models is tough but done well, such as using reached best perplexity instead of naive number of parameters of models. 
+ Well analyzed weakness on tasks requiring cross-sentence comprehension. It was well controlled experiment figuring out where attention is strong at.

### Weaknesses
+ Explaining spatial gating unit was not clear, e.g. how to split the introduced effective split of Z was not produced. It still remains unclear that what splitting the token embeddings into half affects the training. In depth meaning of each process is definitely required.
+ Visualizing weight was great, but we should question how to get an explanation from this gMLP model. The typical transformer models were able to retrieve the explanation by instance level, i.e. visualizing [CLS] tokens' attention relation with other visual tokens. In contrast there is no representative embeddings or tokens to be utilized for its explanability. 


### Rating and Justification
+ Accepted: The suggested ideas are novel and well compared with conventional models but lacks persuasiveness in their methods.

### Additional Comments
+ Comparing higher resolution trained results would make this work more valuable.

### Score
+ Weak accept

## [Paper 2](paper2.pdf)

### Summary
+ This work presents a simple but intuitive multi-layer perceptron based architecture which tries to imitate transformers' input processing procedure. Their justification of introduced methods was well proven by well-designed series of experiments.

### Strengths
+ Building up transformers behavior was novel and makes sense. Their architecture was well justified through a series of ablation studies including removal/substitution of linear interaction layer to mlp or convolutions.
+ Various training scheme shows chance that the model is applicable with new techniques and also scalable from Table 3.
<!-- + Performance results are well listed. Starting with comparing multiple task performances with typical models, visualization of weights and possible weakpoints of the model innates, such as vulnerable to overfitting were nicely tested. -->
+ Visualization of linear layers inside the models was great and their effects were clearly shown. Analyzing sparsity of the weights were also a good idea.
<!-- + Ablation studies were well done by comparing the substitutes of the typical model including layer normalization or class token used in ViT. Experiment with utterly large models were also good to prove its scalability. Trends of performance improvement by reducing the patch size (therby splitting models into many more patches) were aligned with results from ViT. -->

### Weaknesses
+ Due to the simplicity and innate nature of linear layers which is not data-driven, the model is efficient but their performance is still way behind the ViTs e.g., DeiT-S is superior to ResMLP-S24 in both efficiency and performance wise. Improving this remains as further work. 

### Rating and Justification
+ Accept: Their substitution of attention mechanism was well developed and clear evidence of their effects through experiment sequence.

### Additional Comments
+ None
### Score
+ Strong Accept

### Relative Assessment
+ Paper 2 > Paper 1

## Review of Writing reviews
+ Definitely writing reviews makes people easy to catch weaknesses of a given paper. This objective attitude should be applied to my work as well...

+ To me, it was hard to choose between: well-made experiment with lag of performance vs. quite lack of experiment but comparable performance. I think I would rather choose the paper that has gives more insight to the community.

+ Firm understanding of introduced method has powerful role with having persuasiveness of rest of the paper.

## Reference

+ _perplexity_: A metric to evaluate generated sentences from language models, widely used in machine translation and text summarization. Defined as inverse geometric average of generation probability for the sentence. If a given sentence is more likely to be generated, its perplexity _decreases_.