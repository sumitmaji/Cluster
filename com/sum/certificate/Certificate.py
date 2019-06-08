from util import execute, writeContentToFile;
import os;
from constants import SERVER_DNS, SERVER_IP;
import env;

class Certificate:
    def __init__(self):
        pass
        
    def selfSigned(self):
        
        command = 'openssl req -new -x509 -nodes -keyout ca.key -out \
        ca.crt -days 3650 -passin pass:sumit -subj \
        "/C={0}/ST={1}/L={2}/O={3}/OU={4}/CN={5}/emailAddress={6}"'.format(os.environ.get('COUNTRY', 'IN'),os.environ.get('STATE', 'UP'),os.environ.get('LOCALITY', 'GN'),os.environ.get('ORGANIZATION', 'IT'),os.environ.get('ORGU', 'FI'),os.environ.get('COMMONNAME', 'kube-system'),os.environ.get('EMAIL', 'skmaji1@outlook.com'))
        execute(command);

    def createCert(self, user):
        command = 'openssl genrsa -out {0}.key 2048'.format(user)
        execute(command)
        
        command = 'openssl req -new -key {0}.key -out {0}.csr -subj "/CN={0}"'.format(user)
        execute(command)
        
        command = 'openssl x509 -req -in {0}.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out {0}.crt -days 7200'.format(user)
        execute(command)

    def createServerCert(self):
        
        content = """[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
"""
        
        counter = 1
        for server in os.environ[SERVER_DNS].split(','):
            content = content + 'DNS.{0} = {1}\n'.format(counter, server)
            counter += 1

        counter = 1
        for server in os.environ['SERVER_IP'].split(','):
            content = content + 'IP.{0} = {1}\n'.format(counter, server)
            counter += 1
            
        with open('server-openssl.cnf','w') as f:
            f.write(content)
            
        #Create a private key
        command='openssl genrsa -out server.key 2048'
        execute(command)
        
        #Create CSR for the server
        command = 'openssl req -new -key server.key \
        -subj "//C={0}/ST={1}/L={2}/O={3}/OU={4}/CN={5}/emailAddress={6}" \
        -out server.csr -config server-openssl.cnf'.format(os.environ.get('COUNTRY', 'IN'),os.environ.get('STATE', 'UP'),os.environ.get('LOCALITY', 'GN'),os.environ.get('ORGANIZATION', 'IT'),os.environ.get('ORGU', 'FI'),os.environ.get('COMMONNAME', 'kube-system'),os.environ.get('EMAIL', 'skmaji1@outlook.com'))
        execute(command)
        
        #Create a self signed certificate
        command = 'openssl x509 -req -in server.csr -CA ca.crt -CAkey ca.key -CAcreateserial -out server.crt \
        -days 10000 -extensions v3_req -extfile server-openssl.cnf'
        execute(command)
        
        #Verify a Private Key Matches a Certificate
        command = 'openssl x509 -noout -text -in server.crt'
        
        
    def workerCert(self, hostname, ip):
        content = """[req]
req_extensions = v3_req
distinguished_name = req_distinguished_name
[req_distinguished_name]
[ v3_req ]
basicConstraints = CA:FALSE
keyUsage = nonRepudiation, digitalSignature, keyEncipherment
subjectAltName = @alt_names
[alt_names]
"""
        content = content + 'DNS.1 = {0}\n'.format(hostname)
        content = content + 'IP.1 = {0}\n'.format(ip)
        
        writeContentToFile('node-openssl.cnf', content)
        
        #Create a private key
        command = 'openssl genrsa -out {0}.key 2048'.format(hostname)
        execute(command)
        
        #Create CSR for the node
        command = 'openssl req -new -key {0}.key -subj "/CN={1}" -out {0}.csr -config node-openssl.cnf'.format(hostname, ip)
        execute(command)
        
        #Create a self signed certificate
        command = 'openssl x509 -req -in {0}.csr -CA ca.crt -CAkey ca.key \
        -CAcreateserial -out {0}.crt -days 10000 -extensions v3_req -extfile \
        node-openssl.cnf'.format(hostname)
        execute(command)
        
        #Verify a Private Key Matches a Certificate
        command = 'openssl x509 -noout -text -in {0}.crt'.format(hostname)
        execute(command)