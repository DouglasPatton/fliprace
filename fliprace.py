import random
import re

def class FlipRace():
    
    def __init__(self,pattern_search=None,):
        if not pattern_search==None:
            self.do_pattern_search()
        pass
    
    def do_pattern_search(self,runcount=None,flipcount=None,sides=None,pattern_count=None)
        
        
        if __name__=='__main__':
            self.getinputs()
        else:
            if runcount==None:
                runcount=1000
            if flipcount==None:
                flipcount=50
            if 
    def getinputs(self,):
        #this should only be called if __name__=='__main__', i.e., the .py file is being run from the console
        do_default=int(input('type 1 if you want to run the default or 0 if you want to enter your own details: '))
        if do_default==0:
            pattern1=input('enter pattern1 with no spaces: ')
            pattern2=input('enter pattern2 with no spaces: ')
            runcount=int(input('how many runs?'))
            win_compare(pattern1,pattern2,runcount)

        if do_default==1:
            win_compare('00','01',runcount=1000,verbose=0)

    def flipper(self, runcount,flipcount=50,sides=2):
        random.seed(1)
        runlist=[]
        for _ in range(runcount):
            randstring=''
            for _ in range(flipcount):
                randstring+=str(random.randint(0,sides-1))
            runlist.append(randstring)
        return runlist

    def win_finder(self, win_pattern_string,runlist,flipcount,sides,verbose=0):
        winlist=[]
        for runstring in runlist:
            win_idx=re.search(win_pattern_string,runstring).end()
            if verbose==1: 
                print(f'win_idx:{win_idx} for {win_pattern_string} in {runstring}')    
            i=0
            while win_idx==None:
                i+=1
                runstring.extend(self.flipper(1,flipcount=flipcount,sides=sides))
                win_idx=re.search(win_pattern_string,runstring).end()
                if verbose==1: 
                    print(f'extension #{}of runstring. win_idx:{win_idx} for {win_pattern_string} in {runstring}')  
            winlist.append(win_idx)
        return winlist

    def win_compare(self,patternlist,runcount=10000,flipcount=None,sides=2,verbose=0):
        for pattern in patternlist:
            
        runlist=self.flipper(runcount,flipcount=flipcount,sides=sides)
        winlist1=self.win_finder(pattern1,runlist,flipcount,sides,verbose=verbose)
        winsum1=sum(winlist1)
        winlist2=self.win_finder(pattern2,runlist,flipcount,sides,verbose=verbose)
        winsum2=sum(winlist2)
        avgwin1=winsum1/runcount
        avgwin2=winsum2/runcount
        print(f'pattern1:{pattern1} wins after {avgwin1} rolls')
        print(f'pattern2:{pattern2} wins after {avgwin2} rolls')

    
if __name__=='__main__':
    test=FlipRace(pattern_search=True):
        
    
   
        
        
    
    
