import numpy as np
import pandas as pd

def make_subject_stimlists(subject_idx):

    # The list of head nouns
    heads = ['Bag', 'Bell', 'Boat', 'Bone', 'Bow', 'Cane', 'Car', 'Cross', 'Cup',
           'Disc', 'Flag', 'Fork', 'Hand', 'Heart', 'House', 'Key', 'Lamp',
           'Leaf', 'Lock', 'Note', 'Plane', 'Shoe', 'Square', 'Star', 'Tree']

    # define the colors, list nouns, and consonant strings in matching order
    colors = ['Red','Blue','Pink','Black','Green','Brown']
    listmods = ['Cup','Boat','Lamp','Plane','Cross','House']
    consonants = ['xkq','qxsw','mtpv','rjdnv','wvcnz','zbxlv']

    ### Pseudo-randomly create the list conditions, so that they meet the following constraints:
    ## 1. No list item is the same noun repeated (e.g., cross cross)
    ## 2. No list modifier/adjective is repeated with a head noun more than 2 times.
    extraIdx = np.random.choice(6,1,replace=False) # 24 + 1
    good = 0
    while good == 0:
        listmods1 = listmods * 4
        listmods1.append(listmods[extraIdx[0]])
        np.random.shuffle(listmods1)
        listmods2 = np.random.permutation(listmods1)
        listmods3 = np.random.permutation(listmods1)
        listmods4 = np.random.permutation(listmods1)
        listmods_ar = np.array([listmods1,listmods2,listmods3,listmods4])
        # Check constraints: If pass, use this randomization
        bad = 0
        for i in range(0,len(listmods1)):
            if heads[i] in listmods_ar[:,i]: # no items with repeated noun
                bad = 1
        if bad == 0:
            for i in range(0,len(listmods1)):
                if len(np.unique(listmods_ar[:,i])) < 3: # 3 unique items. set to 4 for no repetition.
                    bad = 1
        if bad == 0:
            good = 1

    # Use these to make the phrase and consonant string conditions:
    phrase1, phrase2, phrase3, phrase4 = [],[],[],[]
    conso1, conso2, conso3, conso4 = [],[],[],[]
    phrase_ar = [phrase1,phrase2,phrase3,phrase4]
    conso_ar = [conso1,conso2,conso3,conso4]
    # For each of the 4 sets:
    for c in range(0,len(listmods_ar)):
        listmods_c = listmods_ar[c]
        # For each item in that set:
        for item in listmods_c:
            # grab the color that should be included in the phrase condition
            phrase_ar[c].append(colors[np.where(np.asarray(listmods) == item)[0][0]])
            # and the coresponding length-matched consonant string
            conso_ar[c].append(consonants[np.where(np.asarray(listmods) == item)[0][0]])

    ## Create the complete stimuli lists with images:
    tmp = []
    for k in range(0,len(listmods_ar[0])):
        tmp.append([phrase_ar[0][k],conso_ar[0][k],listmods_ar[0][k],heads[k],'match',0,1])
    for k in range(0,len(listmods_ar[1])):
        tmp.append([phrase_ar[1][k],conso_ar[1][k],listmods_ar[1][k],heads[k],'match',0,2])
    for k in range(0,len(listmods_ar[2])):
        tmp.append([phrase_ar[2][k],conso_ar[2][k],listmods_ar[2][k],heads[k],'mismatch',1,0])
    for k in range(0,len(listmods_ar[3])):
        tmp.append([phrase_ar[3][k],conso_ar[3][k],listmods_ar[3][k],heads[k],'mismatch',2,0])
    Subject_df = pd.DataFrame(tmp,columns=['Modifier','Consonant','ListMod','Head','Match','MisMatchType','ListMatch'])
    Subject_df.to_csv('redboat/SubjectLists/Subject_%s_List.csv' %(subject_idx+1))

    # Create a list of images for this subject:
    df = pd.read_csv('redboat/SubjectLists/Subject_%s_List.csv' %(subject_idx+1))
    mods = np.asarray(df['Modifier'])
    heads = np.asarray(df['Head'])
    listmods = np.asarray(df['ListMod'])
    matchtype = np.asarray(df['MisMatchType'])
    listmatch = np.asarray(df['ListMatch'])
    # Create a list of all of the possible combos:
    totallist = []
    for i in range(0,len(heads)):
        head = heads[i]
        for j in range(0,len(mods)):
            totallist.append([mods[i] + '_' + head])
    # And another for the file name format:
    totallist = np.unique(totallist)
    no_sep = [str.split(i,'_')[0] + str.split(i,'_')[1] for i in totallist]

    # Now get the stim: 2 word trials in composition:
    images_comp2 = []
    # Based on the match type, assign the images:
    for i in range(0,len(matchtype)):
        item = matchtype[i]
        if item == 0:
            images_comp2.append(mods[i] + heads[i] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 1:
            # matches the modifier
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] == mods[i]]
            # does not match the head:
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            # Get a random item from there:
            rand_id = np.random.randint(0,len(tmp),1)[0]
            # use that image:
            images_comp2.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 2:
            # matches the head
            tmp = [kk for kk in totallist if str.split(kk,'_')[1] == heads[i]]
            # does not match the modifier:
            tmp = [kk for kk in tmp if str.split(kk,'_')[0] != mods[i]]
            # get a random item from there
            rand_id = np.random.randint(0,len(tmp),1)[0]
            # use that image
            images_comp2.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
    df['Image_Comp2'] = images_comp2

    # 1 word trials in composition:
    images_comp1 = []
    for i in range(0,len(matchtype)):
        item = matchtype[i]
        if item == 0:
            images_comp1.append(mods[i] + heads[i] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 1:
            # mismatches the head, can use the same items as before:
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] == mods[i]]
            # does not match the head:
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            # Get a random item from there:
            rand_id = np.random.randint(0,len(tmp),1)[0]
            # use that image:
            images_comp1.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 2:
            # mismatches the modifier: need to re generate these ones bc they match the head
            # Same thing as above:
            # mismatches the head, can use the same items as before:
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] == mods[i]]
            # does not match the head:
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            # Get a random item from there:
            rand_id = np.random.randint(0,len(tmp),1)[0]
            # use that image:
            images_comp1.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))

    df['Image_Comp1'] = images_comp1

    # Do this again to get the items for 1 word in list:
    images_list1 = []
    for i in range(0,len(matchtype)):
        item = matchtype[i]
        if item == 0:
            images_list1.append(mods[i] + heads[i] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 1:
            # mismatches the head, can use the same items as before:
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] == mods[i]]
            # does not match the head:
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            # Get a random item from there:
            rand_id = np.random.randint(0,len(tmp),1)[0]
            # use that image:
            images_list1.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 2:
            # mismatches the modifier: need to re generate these ones bc they match the head
            # Same thing as above:
            # mismatches the head, can use the same items as before:
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] == mods[i]]
            # does not match the head:
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            # Get a random item from there:
            rand_id = np.random.randint(0,len(tmp),1)[0]
            # use that image:
            images_list1.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))

    df['Image_List1'] = images_list1

    # Now for the 2 item list task:
    images_list2 = []
    for i in range(0,len(matchtype)):
        item = matchtype[i]
        lm = listmatch[i]
        if item == 0:
            if lm == 1:
                # Match to the first item
                tmp = [kk for kk in totallist if str.split(kk,'_')[1] == listmods[i]]
                rand_id = np.random.randint(0,len(tmp),1)[0]
                images_list2.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
            if lm == 2:
                # Match to the second item
                tmp = [kk for kk in totallist if str.split(kk,'_')[1] == heads[i]]
                rand_id = np.random.randint(0,len(tmp),1)[0]
                images_list2.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 1:
            # total mismatch
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] != listmods[i]]
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            rand_id = np.random.randint(0,len(tmp),1)[0]
            images_list2.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))
        if item == 2:
            # total mismatch
            tmp = [kk for kk in totallist if str.split(kk,'_')[0] != listmods[i]]
            tmp = [kk for kk in tmp if str.split(kk,'_')[1] != heads[i]]
            rand_id = np.random.randint(0,len(tmp),1)[0]
            images_list2.append(str.split(tmp[rand_id],'_')[0] + str.split(tmp[rand_id],'_')[1] + '_%s' %(np.random.randint(1,4,1)[0]))

    df['Image_List2'] = images_list2
    df.to_csv('redboat/SubjectLists/Subject_%s_ImageList.csv' %(subject_idx+1))

    ################## Write out the stimuli lists for the subject ############

    ###########     LIST    BLOCKS ##############
    consos = np.asarray(df['Consonant'])
    list_ims1 = np.asarray(df['Image_List1'])
    list_ims2 = np.asarray(df['Image_List2'])

    tmp1 = np.transpose([listmods,heads,list_ims2])
    tmp2 = np.transpose([consos,heads, list_ims1])
    tmp = np.vstack([tmp1,tmp2])

    # Make some condition labels
    tmp_labeled =  []
    for item in tmp:
        if item[0] in np.unique(consos):
            tmp_labeled.append([item[0],item[1],item[2],'1word'])
        else:
            tmp_labeled.append([item[0],item[1],item[2],'2word'])

    # Shuffle and split into blocks with equal number of conditions:
    good = 0
    while good == 0:
        np.random.shuffle(tmp_labeled)
        b1 = tmp_labeled[0:50]
        b2 = tmp_labeled[50:100]
        b3 = tmp_labeled[100:150]
        b4 = tmp_labeled[150:200]
        if sum(np.asmatrix(b4)[:,3] == '1word')[0] == 25:
            if sum(np.asmatrix(b3)[:,3] == '1word')[0] == 25:
                if sum(np.asmatrix(b2)[:,3] == '1word')[0] == 25:
                    if sum(np.asmatrix(b1)[:,3] == '1word')[0] == 25:
                        good = 1

    # re-shuffle to eliminate any more than 3 of same condition in a row:
    blocks = [b1,b2,b3,b4]
    for bi in blocks:
        count = 0
        while count < len(bi)-3:
            np.random.shuffle(bi)
            bi_tmp = np.asmatrix(bi)[:,3]
            count = 0
            for i in range(3,len(bi_tmp)):
                item_i = bi_tmp[i]
                if len( [it for it in [bi_tmp[i-1][0,0],bi_tmp[i-2][0,0],bi_tmp[i-3][0,0]] if it == item_i]) < 3:
                    count += 1

    # Now write it out :
    jitters = [200,300,400,500,600] * 10
    for b in range(0,len(blocks)):
        bi = blocks[b]
        np.random.shuffle(jitters) # random jitter: uniform discrete distribution.
        df_tmp = pd.DataFrame(jitters,columns=['jitter'])
        word1list, word2list = [],[]
        code1s, code2s = [], []
        image_list = []
        for i in range(0,len(bi)):
            word1list.append(bi[i][0].lower())
            word2list.append(bi[i][1].lower())
            image_list.append(bi[i][2] + ';')
            if bi[i][3] == '1word':
                code1s.append(1)
                code2s.append(2)
            elif bi[i][3] == '2word':
                code1s.append(4)
                code2s.append(8)
        df_tmp['word'] = word1list
        df_tmp['code1'] = code1s
        df_tmp['word2'] = word2list
        df_tmp['code2'] = code2s
        df_tmp['image'] = image_list
        df_tmp.to_csv('redboat/SubjectLists/Subject_%s_List_Block_%s' %(subject_idx+1,b),index=None,sep = " ")

    ########### COMPOSITION BLOCKS ##############
    comp_ims1 = np.asarray(df['Image_Comp1'])
    comp_ims2 = np.asarray(df['Image_Comp2'])

    tmp1 = np.transpose([mods,heads,comp_ims2])
    tmp2 = np.transpose([consos,heads, comp_ims1])
    tmp = np.vstack([tmp1,tmp2])

    # Make some condition labels
    tmp_labeled =  []
    for item in tmp:
        if item[0] in np.unique(consos):
            tmp_labeled.append([item[0],item[1],item[2],'1word'])
        else:
            tmp_labeled.append([item[0],item[1],item[2],'2word'])

    # Shuffle and split into blocks with equal number of conditions:
    good = 0
    while good == 0:
        np.random.shuffle(tmp_labeled)
        b1 = tmp_labeled[0:50]
        b2 = tmp_labeled[50:100]
        b3 = tmp_labeled[100:150]
        b4 = tmp_labeled[150:200]
        if sum(np.asmatrix(b4)[:,3] == '1word')[0] == 25:
            if sum(np.asmatrix(b3)[:,3] == '1word')[0] == 25:
                if sum(np.asmatrix(b2)[:,3] == '1word')[0] == 25:
                    if sum(np.asmatrix(b1)[:,3] == '1word')[0] == 25:
                        good = 1

    # re-shuffle to eliminate any more than 3 in a row:
    blocks = [b1,b2,b3,b4]
    for bi in blocks:
        count = 0
        while count < len(bi)-3:
            np.random.shuffle(bi)
            bi_tmp = np.asmatrix(bi)[:,3]
            count = 0
            for i in range(3,len(bi_tmp)):
                item_i = bi_tmp[i]
                if len( [it for it in [bi_tmp[i-1][0,0],bi_tmp[i-2][0,0],bi_tmp[i-3][0,0]] if it == item_i]) < 3:
                    count += 1

    # Now write it out :
    jitters = [200,300,400,500,600] * 10
    for b in range(0,len(blocks)):
        bi = blocks[b]
        np.random.shuffle(jitters)
        df_tmp = pd.DataFrame(jitters,columns=['jitter'])
        word1list, word2list = [],[]
        code1s, code2s = [], []
        image_list = []
        for i in range(0,len(bi)):
            word1list.append(bi[i][0].lower())
            word2list.append(bi[i][1].lower())
            image_list.append(bi[i][2] + ';')
            if bi[i][3] == '1word':
                code1s.append(16)
                code2s.append(32)
            elif bi[i][3] == '2word':
                code1s.append(64)
                code2s.append(128)
        df_tmp['word'] = word1list
        df_tmp['code1'] = code1s
        df_tmp['word2'] = word2list
        df_tmp['code2'] = code2s
        df_tmp['image'] = image_list
        df_tmp.to_csv('redboat/SubjectLists/Subject_%s_Composition_Block_%s' %(subject_idx+1,b),index=None, sep =" ")
