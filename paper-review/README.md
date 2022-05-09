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
+ This paper suggests a new model based on multi-layer perceptron (MLP), which was regarded as vanilla model to be complete complex tasks. THe major contribution of this paper is a comparable results with typical models and scalability proven.

### Strengths
+ Suggested method is interesting and their results show that gMLP has comparable ability to capture local relationships, especially in visionary tasks.
+ As suggested architecture is far different from typical models widely used in comparing tasks, doing the fair comparison between these models is tough but done well, such as using reached best perplexity instead of naive number of parameters of models. 
+ Suggested aMLP to show effects of attention/gating mechanism was fair and great, by viewing their results from multiple criteria. 

### Weaknesses
+ Explaining spatial gating unit was not clear, e.g. how to split the introduced effective split of Z was not produced. It still remains unclear that what splitting the token embeddings into half and sending one of two to spatial projections do or why they work. In depth meaning of each process is definitely required.
+ Listed comparison results with language models are highly contrasted with bias, based on gMLP results, e.g. results from perplexity is highlighted while tasks requiring multiple sentences such as MNLI or SQuAD are diminished. There is a clear lack of understandings for gMLP in long documents and these were shortly analyzed. Furthermore, alternative to this lack of performance was increasing model sizes, which is in most cases makes sense in other works as well. Their reported higher results on such cross-sentence tasks were achieved by 3 times larger model compared to BERT, which implies scalabiliy of this architecture but similar performance with drastic superiority in number of parameters was expected.
+ Comparing attention mechanism only with BERT is not sufficient. There are many newly introduced attentions in order to deal with various applications such as Sparse attention or Swin, who are variations of attention mechanisms to capture far/local relations respectively.
+ Visualizing weight was great, but we should question how to get an explanation from this gMLP model. The typical transformer models were able to retrieve the explanation by instance level, i.e. visualizing [CLS] tokens' attention relation with other visual tokens. In contrast there is no representative embeddings or tokens to be utilized for explanability. However, if model is pre-trained with additional token, this might not be impossible.
+ aMLp, suggested for ablation study, outperforms on tasks requiring comprehension of multiple/cross-sentences. This seemed to me that gMLP outperforms in a task that requires localization while attention mechanisms helps capturing far relations.


### Rating and Justification
+ Accepted: The suggested ideas are novel and well compared with conventional models but extra analysis on their results are required.

### Additional Comments
+ Results from training higher resolution in vision works would have made this work better.

### Score
+ Weak accept

## [Paper 2](paper2.pdf)

### Summary
+ This work presents a simple but intuitive multi-layer perceptron based architecture which tries to imitate transformers' input processing procedure. Their results are well proven by sequential of ablation studies.

### Strengths
+ Seuqence of experiments are well designed. Starting with comparing multiple task performances with typical models, visualization of weights and possible weakpoints of the model innates, such as vulnerable to overfitting. 
+ Visualization of linear layers inside the models was great and their effects were clearly shown. Analyzing sparsity of the weights were also a good idea.
+ Ablation studies were well done by comparing the substitutes of the typical model has including layer normalization or class token used in ViT. Experiment with utterly large models were also great.
+ Trends of performance improvement by reducing the patch size (therby splitting models into many more patches) were aligned with previous results on ViT.

### Weaknesses
+ Due to the simplicity and innate nature of linear layers which is not data-driven, the model is efficient but their performance is still way behind the ViTs. Extension of figuring this out is necessary.

### Rating and Justification
+ Accept:

### Additional Comments

### Score
+ Strong Accept:

### Relative Assessment
+ Paper 2 > Paper 1

## Review of Writing reviews
+ Definitely writing reviews makes people easy to catch weaknesses of a given paper. This objective attitude should be applied to my work as well...

+ To me, it was hard to choose between: well-made experiment with lag of performance vs. quite lack of experiment but comparable performance. I think I would rather choose the paper that has gives more insight to the community.

## Reference

+ _perplexity_: A metric to evaluate generated sentences from language models, widely used in machine translation and text summarization. Defined as inverse geometric average of generation probability for the sentence. If a given sentence is more likely to be generated, its perplexity _decreases_.