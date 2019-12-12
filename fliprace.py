import random
import re

class FlipRace():
    
    def __init__(self,pattern_search=None,):
        if not pattern_search==None:
            self.pattern_search()
        pass
    
    def pattern_search(self,runcount=None,flipcount=None,sides=None,patternlist=None,verbose=0):
        
        
        if __name__=='__main__':
            patternlist,runcount,sides=self.getinputs()
        else:
            if runcount==None:runcount=1000
            if patternlist==None:patternlist=['00','01']
            if sides==None:sides=2
        if flipcount==None:
            patternlengthlist=[len(p) for p in patternlist]
            maxp=max(patternlengthlist)
            flipcount=10**(maxp+sides-1)
            
        runlist=self.flipper(runcount,flipcount=flipcount,sides=sides)
        results=[]
        for p in patternlist:
            results.append(self.win_finder(p,runlist,flipcount,sides,verbose=verbose))
        self.patternrunlistlist=results
        self.patternavgwinlist=[sum(rlist)/runcount for rlist in results]
        
        self.printsimpleresults(patternlist,self.patternavgwinlist)
        return
    
    def printsimpleresults(self,patternlist,scorelist):
        for i,p in enumerate(patternlist):
            print(f'pattern#{i}({p}) has score:{scorelist[i]}')
                
    def getinputs(self,):
        #this should only be called if __name__=='__main__', i.e., the .py file is being run from the console
        do_default=int(input('type 1 if you want to run the default or 0 if you want to enter your own details: '))
        if do_default==0:
            patterncount=int(input('how many patterns do you want to try?: '))
            patternlist=[];i=0
            for i in range(patterncount):
                i+=1
                patternlist.append(input('enter pattern#{i} with no spaces: '))
            sides=int(input('how many sides on the coin?: '))
            runcount=int(input('how many runs?: '))
        if do_default==1:
            sides=2
            patternlist=['00','01']
            runcount=1000
        return patternlist,runcount,sides
            

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
                    print(f'extension #{i}of runstring. win_idx:{win_idx} for {win_pattern_string} in {runstring}')  
            winlist.append(win_idx)
        return winlist



    
if __name__=='__main__':
    test=FlipRace(pattern_search=True)
        
    
   
        
        
    
    
