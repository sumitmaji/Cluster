import subprocess
import requests
import sys

def call(command):
    print('Command received for execution>>>> ', command)
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
        
    return [proc.communicate()[0].decode('utf-8').rstrip(), proc.returncode]
    
def execute(command):
    response = call(command)

    if(response[1] != 0):
        sys.exit('Error while executing command!!!!!')
    else:
        return response
    
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
             
