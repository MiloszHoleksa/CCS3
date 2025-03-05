This repo contains the code for two models: an Long-Short Term Memory Model and a Hidden Markov Model for predicting event boundaries in a sequence of Eye-Tracking data. They were used in a study prepared for the Computational Cognitive Science Class. More info in the paper.

Abstract:

Abstract
This study is grounded in Event Segmentation Theory (EST) which posits
that when processing information, people inherently segment their conscious
experience into distinct events. Scientific literature stresses out a crucial role
that event segmentation plays in bridging perception and memory, by making
the observation that additional cognitive processing is involved around per-
ceived event boundaries, which leads to better memory encoding. We used
a dataset containing information gathered from a study where participants
watched a video with pre-determined event boundaries. After watching the
video participants’ memory regarding the events was measured using two
metrics. Eye tracking data of the gaze position and pupil size were gathered.
We built upon the findings of the study suggesting that event boundaries
lead to distinct gaze patterns and (a) developed a Hidden Markov Model
(HMM) and a Long Short-Term Memory model (LSTM) to predict the oc-
currence of event boundaries based on the eye tracking data, (b) attempted
to associate cognitive load and memory performance with the pupillometry
data during the processing of the events and (c) validate our models with in-
ternally collected data. The results of our study showed better performance
of the LSTM model compared to the HMM architecture used in previous
research. These results were partially confirmed by our internal validation
experiment, where the LSTM model had a higher accuracy than HMM, but
both models performed worse than on the external data.
