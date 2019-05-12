import subprocess
import os
import env
from constants import *



"""
Executing script and reading the output
"""
proc = subprocess.Popen('./myscript.sh',    shell=True, 
                                            executable='bash',
                                            stdout=subprocess.PIPE)

str = proc.communicate()[0]
print(str.decode('utf-8'))                                            
print(proc.returncode)


"""
Setting and reading environment variable
"""
os.environ['ENABLE_DEBUG'] = 'true'
print(os.getenv('ENABLE_DEBUG'))


"""
Creating directory
"""
if not os.path.exists('./sumit/pramit'):
    os.makedirs('./sumit/pramit')
"""
Shell euivalent of touch
"""
open('./sumit1.txt','a').close()

"""
Get all files in current and csub directories
"""
for subdir, dirs, files in sorted(os.walk('/projects')):
#    print('Dirs:', dirs)
    for file in files:
#        print(subdir + os.sep + file)
        pass
        
"""
Get the file name
"""
print(os.path.basename('/projects/Cluster/sumit1.txt'))


"""
Add contents of to the files
"""
content = """global
        log 127.0.0.1 local0
        log 127.0.0.1 local1 notice
        maxconn 4096
        maxpipes 1024
        daemon
defaults
        log global
        mode tcp
        option tcplog
        option dontlognull
        option redispatch
        option http-server-close
        retries 3
        timeout connect 5000
        timeout client 50000
        timeout server 50000
        frontend default_frontend
        bind *:443
        default_backend master-cluster
backend master-cluster
#Install master nodes
"""

counter = 0
for server in os.environ[SERVERS].split(','):
    counter+=1
    ip_hostname = server.split(':')
    content = content + '        server master-{0} {1}:6443 check\n'.format(counter, ip_hostname[0])


content.split(',')
with open('cloud.txt','w') as f:
    f.write(content)
    
