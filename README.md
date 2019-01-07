# Bemis &amp; Pylkkanen 2011
Bemis, D. K., & Pylkkänen, L. (2011). Simple composition: A magnetoencephalography investigation into the comprehension of minimal linguistic phrases. Journal of Neuroscience, 31(8), 2801-2814.

# Outline of this repository:
This repo contains code and materials to run an experimental procedure that closely follows B & P 2011. The experiment is written in Presentation's SDL language, using a pair of python scripts to generate pseudo-random stimuli lists for a set of subjects. For an example of how to use these scripts, see example.py . A compatible anaconda environment is also included. Experimental materials are located in redboat/Stim. 

# Outline of the Presentation Code:
The experimental code uses "Template" files to present trials. The primary template file is "MainTrial_Phrase.tem". This contains the definition of a single trial, used in every condition. The $ items are read in from each subject's "Scenario" file. Scenario files are generated using the python scripts included here. To modify the timing parameters of the trials, one needs only change the ".tem" files. To modify instructions or stimuli, one can modify either the individual subjects' Scenario files, or the python scripts used to generate them. 

# Experiment Summary
Subjects performed two tasks, in alternating blocks: 

In "Phrase" or "Composition" blocks, subjects read either a phrase made of a color adjective and noun (e.g. red boat) or a non-word and word combination (xyk boat). They then saw an image, and used a button press to indicate whether the image matched all of the words on that trial.

In "List" or "non-composition" blocks, subjects read either a list of two nouns (key, boat) or a non-word and word combination (xyk boat). They then saw an image, and used a button press to indicate whether the image matched any of the words on that trial.

# Experimental materials

25 critical head nouns (bad, bell, boat, bone, bow, cane, car, cross, cup, disc, flag, fork, hand, heart, house, key, lamp, leaf, lock, note, plane, shoe, square, star, tree).

6 color adjectives (red, blue, pink, black, green, brown)

6 length-matched unpronounceable consonant strings (xkq, qxsw, mtpv, rjdnv, wvcnz, zbxlv)

6 length-matched nouns, appearing in the 1st position of lists (cup, boat, lamp, plane, cross, house)

Each task contained 100 trials in each of the 2-word and 1 word conditions, with 4 repetitions of each critical head noun. Each task contained an equal number of match/mismatch trials. In 2 word list trials, half of the matches were to the 1st item, and the other to the 2nd item. In 2 word phrase trials, half of the mismatches were due to the adjective and half were due to the noun. The 200 total trials in each task were divided into 4 blocks of 50, with an equal number of 1-word and 2-word trials in eahch block. Block order was balanced across subjects, as was the button (left/right) that corresponded to the match response. 

Constraints on stimulus generation:

i. No list condition trial was allowed to be a noun repeated (e.g. cross, cross).

ii. No 1st word item could appear with a single noun more than twice.

# Deviations from Bemis & Pylkkanen 2011:

1. For each subject, B & P selected set of 50 images that were repeated in each the 1-word and 2-word condition of each task. Here, 200 images are pseudo-randomly selected for each subject, with the desired number of match/mismatch trials.

2. B & P used a random ISI between trials sampled from a normal distribution with mean of 400 ms. Here, a discrete uniform distribution across 200, 300, 400, 500, and 600 ms was used, and added to an initial 100 ms of blank screen on each trial.

3. The present version includes a balance of left/right responses across subjects.

4. This version does not include the symbol string condition used in B & P.

# Timing parameters for trials:

In both list and composition task:

Blank Screen: 100ms + random jitter (see above)

Fixation Cross: 300 ms

ISI: 300 ms

Word 1: 300 ms

ISI: 300 ms

Word 2: 300 ms

ISI: 300 ms

Image: Until subject response
