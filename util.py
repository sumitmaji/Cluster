import subprocess
import requests

def execute(command):
    print('Command received for execution>>>> ', command)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return [proc.communicate()[0].decode('utf-8').rstrip(), proc.returncode]
    
def writeContentToFile(fileName, content):
    with open(fileName,'w') as f:
            f.write(content)
            
def downloadFile(url, fileName):
    r = requests.get(url, stream = True) 
  
    with open(fileName,"wb") as file: 
        for chunk in r.iter_content(chunk_size=1024): 
  
            # writing one chunk at a time to pdf file 
            if chunk: 
                file.write(chunk) 
             
