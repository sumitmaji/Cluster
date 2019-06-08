from util import execute;
import os

class Certificate:
    def __init__(self):
        pass
        
    def selfSigned(self):
        print('Generating selfsigned certificate')
        command = 'openssl req -new -x509 -nodes -keyout ca.key -out \
        ca.crt -days 3650 -passin pass:sumit -subj \
        "/C={0}/ST={1}/L={2}/O={3}/OU={4}/CN={5}/emailAddress={6}"'.format(os.environ.get('COUNTRY', 'IN'),os.environ.get('STATE', 'UP'),os.environ.get('LOCALITY', 'GN'),os.environ.get('ORGANIZATION', 'IT'),os.environ.get('ORGU', 'FI'),os.environ.get('COMMONNAME', 'kube-system'),os.environ.get('EMAIL', 'skmaji1@outlook.com'))
        execute(command);

