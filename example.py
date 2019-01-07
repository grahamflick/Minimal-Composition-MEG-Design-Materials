from StimListGen import *
from WritingScenarios import *
# set number of subject scenario files
N = 32
# Alternate which block type occurs first
First = ['composition','list','composition','list'] * (N/4) # adjust for remainders
# And which button is the "match" response
Button =['left','left','right','right'] * (N/4) # adjust for remainders
# Generate the scenario files
for i in range(0,N):
    subject_idx = i
    FirstBlock = First[i]
    MatchButton = Button[i]
    make_subject_stimlists(subject_idx)
    write_scenario_files(subject_idx, FirstBlock, MatchButton)
