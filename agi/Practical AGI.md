# Practical AGI

Long term storage <-> Hard drive
Short term storage <-> Memory
Processing <-> CPU/Processor

## Reactive behaviors

1. Deconstructs incoming stimuli.
2. Matches the stimuli with already perceived stimuli patterns.
	1. Evaluate existing responses and offer alternate responses if the current ones are unsatisfactory.
	2. Records the selected response for further analysis.
3. Executes the selected response.
	1. Records the result of the response on the environment (other agents).

### Examples

#### High volume audio

1. Audio amplitude is obtained.
2. High amplitude audio stimuli are queried in the KB.
	1. Current responses are "doing nothing", which is satisfactory.
	2. Decision is stored (use count incremented).
3. AGI does nothing.
	1. Environment does not change.

## Proactive behaviors

* Internally generates desires.
* Determines goals and objectives to fulfill those desires.
* Plans a path to reach those goals and objectives.
	* Decomposes a goal/objective into sub-goals/objectives until concrete actions can be executed.
* Executes the necessary steps to reach those goals and objectives.
* Evaluate if the taken steps have brought the it closer of further from its initially defined target.
* Re-adjusts its plan as necessary.

### Examples