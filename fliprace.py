import random
import re


def flipper(runcount,flipcount=50,sides=2):
    random.seed(1)
    runlist=[]
    for _ in range(runcount):
        randstring=''
        for _ in range(flipcount):
            randstring+=str(random.randint(0,sides-1))
        runlist.append(randstring)
    return runlist

def win_finder(win_pattern_string,runlist,verbose=0):
    winlist=[]
    for runstring in runlist:
        win_idx=re.search(win_pattern_string,runstring).end()
        if verbose==1: 
            print(f'win_idx:{win_idx} for {win_pattern_string} in {runstring}')
        winlist.append(win_idx)
    return winlist

def win_compare(pattern1,pattern2,runcount=10000,flipcount=None,sides=2,verbose=0):
    if flipcount==None:
        if len(pattern1)>len(pattern2):
            flipcount=10**(len(pattern1))
        else:
            flipcount=10**(len(pattern2))
    runlist=flipper(runcount,flipcount,sides=2)
    winlist1=win_finder(pattern1,runlist,verbose=verbose)
    winsum1=sum(winlist1)
    winlist2=win_finder(pattern2,runlist,verbose=verbose)
    winsum2=sum(winlist2)
    avgwin1=winsum1/runcount
    avgwin2=winsum2/runcount
    print(f'pattern1:{pattern1} wins after {avgwin1} rolls')
    print(f'pattern2:{pattern2} wins after {avgwin2} rolls')
    
    
if __name__=='__main__':
    
    do_default=int(input('type 1 if you want to run the default or 0 if you want to enter your own details: '))
    if do_default==0:
        pattern1=input('enter pattern1 with no spaces: ')
        pattern2=input('enter pattern2 with no spaces: ')
        runcount=int(input('how many runs?'))
        win_compare(pattern1,pattern2,runcount)
    
    if do_default==1:
        win_compare('00','01',runcount=1000,verbose=0)
        
        
    
    
