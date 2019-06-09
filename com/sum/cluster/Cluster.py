from com.sum.certificate.Certificate import Certificate
from constants import ETCD_CLUSTERS_CERTS, WORKERS, NODES;
import os;
from util import writeContentToFile;

class Cluster:

    def __init__(self):
        pass
        
    def installCertificates(self):
        
        cert = Certificate()
        
        #Create certificate autority certificates
        cert.caCert()
        
        #Create server certificates
        cert.createServerCert()
        
        #Create certificates of the process
        users = list('admin kube-proxy kubelet kube-controller-manager kube-scheduler master.cloud.com'.split(" "))
        
        for user in users:
            cert.createCert(user)
            
        #Install worker nodes certificates
        for worker in os.environ[WORKERS].split(','):
            ip_hostname = worker.split(':')
            cert.workerCert(ip_hostname[1], ip_hostname[0])
            
        writeContentToFile('basic_auth.csv','admin,admin,admin')
        
        #Install worker nodes certificates
        for worker in os.environ[ETCD_CLUSTERS_CERTS].split(','):
            ip_hostname = worker.split(':')
            cert.peerCert(ip_hostname[0],ip_hostname[1],'etcd','server')
        
        #Install worker nodes certificates
        for worker in os.environ[NODES].split(','):
            ip_hostname = worker.split(':')
            cert.peerCert(ip_hostname[0],ip_hostname[1],'etcd','client')
        
        