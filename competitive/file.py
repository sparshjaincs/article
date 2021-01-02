class Write:
    def file_handling(self,language,code,snippet):
        if language == 'Python':
            string = f'''
import time
{code}

class Checker(Solution):
    def checking(self,testcase,solcase):
        try:
            start = time.time()
            for i in range(len(solcase)):
                value = {snippet}
                if solcase[i] != value:
                    return [False,'N/A ms','Wrong Anwser',solcase[i],value]
            end = round((time.time()-start)*1000,2)
            return [True,str(end) + ' ms',"Accepted",""]
        except Exception as exp:
            
            return ['error','N/A ms',"Runtime Error",exp]
            '''

            
            fp = open('pythonrun.py','w')
            fp.write(string)
            fp.close()

class Test:
    def test_handling(self,language,code,snippet):
        if language == 'Python':
            string = f'''
import time
{code}

class Checker(Solution):
    def checking(self,testcase,solcase):
        try:
            start = time.time()
            for i in range(len(testcase)):
                value = {snippet}


            end = round((time.time()-start)*1000,2)
            return [str(end) + ' ms',"Accepted",""]
        except Exception as exp:
            
            return [exp,"Runtime Error",""]
            '''

            
            fp = open('pythontest.py','w')
            fp.write(string)
            fp.close()









