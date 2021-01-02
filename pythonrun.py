
import time
class Solution:
    def longest_plaindromic_substring(self,s:str)->int:
        '''
        Write your code here
        return int
        '''
        return 1                
                

class Checker(Solution):
    def checking(self,testcase,solcase):
        try:
            start = time.time()
            for i in range(len(solcase)):
                value = self.longest_plaindromic_substring(testcase[i])
                if solcase[i] != value:
                    return [False,'N/A ms','Wrong Anwser',solcase[i],value]
            end = round((time.time()-start)*1000,2)
            return [True,str(end) + ' ms',"Accepted",""]
        except Exception as exp:
            
            return ['error','N/A ms',"Runtime Error",exp]
            