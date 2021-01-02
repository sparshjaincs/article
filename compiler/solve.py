import subprocess
import datetime
import win32process, win32api, win32con
class compile:
 
    def __init__(self):
        pass
    def getoutput(self,lang,file):
        proc = subprocess.Popen([lang, file ], stdin =subprocess.PIPE ,stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        proc.wait()
        #   proc.stdin.write(b"hello\nhello world\nhella")
        val = proc.communicate(input= b"hello",timeout=15)
        hproc = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION, False, proc.pid)
        times = win32process.GetProcessTimes(hproc)
        win32api.CloseHandle(hproc)
        sol = val[0].decode("utf-8") 
        value = subprocess.call([lang,file])
        if value == 0:
            time = round(times['UserTime'] * (10 ** (-6)),2)
        else:
            time = 'N/A'
        return [sol,value,time] #KernalTime
    def compile_python(self,data):
        fp = open('python.py',"w")
        fp.write(data)
        fp.close()
        output = self.getoutput('python','python.py')
        return output
    def getoutputcpp(self):
        try:
            s = subprocess.check_call("gcc cplusplus.cpp -o out1;./out1", shell = True) 
            flag = 0
        except Exception as exp:
            s = str(exp)
            flag = 1
        return [s,flag]

    def compile_cpp(self,data):
        fp = open('cplusplus.cpp','w')
        fp.write(data)
        fp.close()
        output = self.getoutputcpp()
        return output
    def execute(self,data,lang="Python"):
        sol = ""
        if lang == 'Python':
            sol = self.compile_python(data)
        elif lang == "CPP":
            sol = self.compile_cpp(data)
        return sol



