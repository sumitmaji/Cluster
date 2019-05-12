import subprocess

def execute(command):
    proc = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE)
    return [proc.communicate()[0].decode('utf-8').rstrip(), proc.returncode]
    
