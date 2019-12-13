import random
import multiprocessing
import re
from time import sleep


class FlipRace():
    
    def __init__(self,pattern_search=None,):
        self.cores=int(6)#free cores for parallel processing
        if not pattern_search==None:
            self.pattern_search()

    
    def build_pattern_combos(self,length,sides=2):
        slist=[str(i) for i in range(sides)]
        plist=['0']
        
        for i in range(length-1):
            plist2=[]
            for p in plist:
                for s in slist:
                    plist2.append(p+s)
                plist=plist2
        return plist           
            
    
    def pattern_search(self,runcount=None,flipcount=None,sides=None,patternlist=None,verbose=0):
        if __name__=='__main__':
            patternlist,runcount,sides=self.getinputs()
        else:
            if runcount==None:runcount=1000
            if patternlist==None:patternlist=['00','01']
            print(f'patternlist{patternlist}')
            if sides==None:sides=2
        if flipcount==None:
            patternlengthlist=[len(p) for p in patternlist]
            maxp=max(patternlengthlist)
            flipcount=10**(maxp+sides-1)
        runlist=self.flipper(runcount,flipcount=flipcount,sides=sides)
        patterncount=len(patternlist)
        self.patternlist=patternlist
        self.runlist=runlist;self.flipcount=flipcount;self.sides=sides;self.verbose=verbose
        with multiprocessing.Pool(processes=self.cores) as pool:
                pattern_win_list=pool.map(self.win_finder_wrapper,[i for i in range(patterncount)])
                sleep(2)
                pool.close()
                pool.join()
        results=pattern_win_list

        
        
        #for p in patternlist:
        #    results.append(self.win_finder(p,runlist,flipcount,sides,verbose=verbose))
        self.patternrunlistlist=results
        self.patternavgwinlist=[sum(rlist)/runcount for rlist in results]
        
        self.printsimpleresults(patternlist,self.patternavgwinlist)
        return
    
    def win_finder_wrapper(self,idx):
        print(f'wrapper starting idx:{idx}')
        return self.win_finder(self.patternlist[idx],self.runlist,self.flipcount,self.sides,verbose=self.verbose)
    
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
                patternlist.append(input(f'enter pattern# {i} with no spaces: '))
            sides=int(input('how many sides on the coin?: '))
            runcount=int(input('how many runs?: '))
        if do_default==1:
            sides=2
            patternlist=['00','01']
            runcount=1000
        return patternlist,runcount,sides
            

    def flipper(self, runcount,flipcount=50,sides=2):
        
        runcount=int(int(runcount/self.cores)*self.cores)
        #print(runcount)
        runlength=int(runcount/self.cores)
        random.seed(1)
        #runlist=[]
        self.flipcount=flipcount
        self.sides=sides
        arglist=[runlength]*self.cores
        #print('arglist len:',len(arglist))

            
        with multiprocessing.Pool(processes=self.cores) as pool:
                
                runlistlist=pool.map(self.flip_wrap,arglist)
                sleep(2)
                pool.close()
                pool.join()
        #print('runlistlist',runlistlist)
        runlist=[ii for i in runlistlist for ii in i]
        #print('runlist',runlist)
        return runlist
    
    def flip_wrap(self,runcount):
        arunlist=[]
        for _ in range(runcount):
            randstring=''
            for _ in range(self.flipcount):
                randstring+=str(random.randint(0,self.sides-1))
            arunlist.append(randstring)
        #print('flipper:arunlist:',arunlist)
        return arunlist
    
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
        
    
   
        
        
    
    
