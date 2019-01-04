import numpy as np
import pandas as pd

def write_scenario_files(subject_idx, FirstBlock, MatchButton):

    subject_idx = subject_idx+1

    if FirstBlock == 'composition':
      Block1 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_0' %subject_idx)
      Block2 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_0' %subject_idx)
      Block3 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_1' %subject_idx)
      Block4 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_1' %subject_idx)
      Block5 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_2' %subject_idx)
      Block6 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_2' %subject_idx)
      Block7 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_3' %subject_idx)
      Block8 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_3' %subject_idx)

    if FirstBlock == 'list':
      Block1 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_0' %subject_idx)
      Block2 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_0' %subject_idx)
      Block3 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_1' %subject_idx)
      Block4 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_1' %subject_idx)
      Block5 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_2' %subject_idx)
      Block6 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_2' %subject_idx)
      Block7 = pd.read_csv('redboat/SubjectLists/Subject_%s_List_Block_3' %subject_idx)
      Block8 = pd.read_csv('redboat/SubjectLists/Subject_%s_Composition_Block_3' %subject_idx)

    Blocks = [Block1,Block2,Block3,Block4,Block5,Block6,Block7,Block8]
    if FirstBlock == 'composition':
        if MatchButton == 'left':
             Templatefname = 'redboat/ScenarioTemplate_CompositionFirst_MatchLeft.txt'
        if MatchButton == 'right':
             Templatefname = 'redboat/ScenarioTemplate_CompositionFirst_MatchRight.txt'

    if FirstBlock == 'list':
        if MatchButton == 'left':
             Templatefname = 'redboat/ScenarioTemplate_ListFirst_MatchLeft.txt'
        if MatchButton == 'right':
             Templatefname = 'redboat/ScenarioTemplate_ListFirst_MatchRight.txt'

    # Open up the template scenario file & get the start of the sections:
    inserts = []
    with open(Templatefname,'r') as file:
       for num, line in enumerate(file, 1):
           if 'start_here' in line:
               inserts.append(num-1)

    if len(inserts) != 8:
      print("WARNING: INCORRECT NUMBER OF TEMPLATES IN SCENARIO FILE")

    # Read in the file this time:
    with open(Templatefname,'r') as file:
      data = file.readlines()

    # Write the new file for this subject:
    for ii in range(0,len(inserts)):
      df_tmp = Blocks[ii]
      insert = inserts[ii]
      for k in range(0,50):
          data[insert+k] = df_tmp.values[k][0] + '\r\n'

    # and write everything out:
    with open('redboat/ScenarioFiles/Subject_%s_Scenario_%s_%s.txt' %(subject_idx, FirstBlock, MatchButton),'w') as file2:
      file2.writelines(data)
    file2.close()
    file.close()
