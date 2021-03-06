# My PhD thesis on "Learning from Unlabeled Interaction Frames"

**Author:** Jonathan Grizou

**Abstract:** This thesis investigates how a machine can be taught a new task from unlabeled human instructions, which is without knowing beforehand how to associate the human communicative signals with their meanings. The theoretical and empirical work presented in this thesis provides means to create calibration free interactive systems, which allow humans to interact with machines, from scratch, using their own preferred teaching signals. It therefore removes the need for an expert to tune the system for each specific user, which constitutes an important step towards flexible personalized teaching interfaces, a key for the future of personal robotics.Our approach assumes the robot has access to a limited set of task hypotheses, which include the task the user wants to solve. Our method consists of generating interpretation hypotheses of the teaching signals with respect to each hypothetic task. By building a set of hypothetic interpretation, i.e. a set of signal-label pairs for each task, the task the user wants to solve is the one that explains better the history of interaction.We consider different scenarios, including a pick and place robotics experiment with speech as the modality of interaction, and a navigation task in a brain computer interaction scenario. In these scenarios, a teacher instructs a robot to perform a new task using initially unclassified signals, whose associated meaning can be a feedback (correct/incorrect) or a guidance (go left, right, up, \ldots). Our results show that a) it is possible to learn the meaning of unlabeled and noisy teaching signals, as well as a new task at the same time, and b) it is possible to reuse the acquired knowledge about the teaching signals for learning new tasks faster. We further introduce a planning strategy that exploits uncertainty from the task and the signals' meanings to allow more efficient learning sessions. We present a study where several real human subjects control successfully a virtual device using their brain and without relying on a calibration phase. Our system identifies, from scratch, the target intended by the user as well as the decoder of brain signals.Based on this work, but from another perspective, we introduce a new experimental setup to study how humans behave in asymmetric collaborative tasks. In this setup, two humans have to collaborate to solve a task but the channels of communication they can use are constrained and force them to invent and agree on a shared interaction protocol in order to solve the task. These constraints allow analyzing how a communication protocol is progressively established through the interplay and history of individual actions.

Final version release: https://github.com/jgrizou/thesis_manuscript/releases/tag/final

Code associated to this work is availbale at: https://github.com/jgrizou/thesis_code

## Use

Run the python scripts: export_visuals_to_pdf and export_visuals_to_png

Use Latex to compile thesis.tex and generate the pdf.

### License

[![Creative Commons BY-NC-ND](https://i.creativecommons.org/l/by-nc-nd/4.0/88x31.png) ](http://creativecommons.org/licenses/by-nc-nd/4.0/)
