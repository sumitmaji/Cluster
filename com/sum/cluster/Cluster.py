from com.sum.certificate.Certificate import Certificate
from constants import ETCD_CLUSTERS_CERTS, WORKERS, NODES, WORKDIR, WORKSPACE;
import os;
from util import writeContentToFile, downloadFile;

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
        
    
    def installBinaries(self):
        
        os.makedirs(os.environ[WORKDIR], 755, True)
        os.chdir(os.environ[WORKDIR])
        
        if(not os.path.exists('./'+os.environ[WORKSPACE])):
            os.mkdir(os.environ[WORKSPACE])
                
        os.chdir(os.environ[WORKSPACE])
        
        if(not os.path.exists('./kubernetes-server-linux-amd64.tar.gz')):
            downloadFile('https://dl.k8s.io/v1.10.0/kubernetes-server-linux-amd64.tar.gz', 'kubernetes-server-linux-amd64.tar.gz')
            downloadFile('https://github.com/coreos/etcd/releases/download/v3.2.18/etcd-v3.2.18-linux-amd64.tar.gz', 'etcd-v3.2.18-linux-amd64.tar.gz')
            downloadFile('https://github.com/coreos/flannel/releases/download/v0.10.0/flannel-v0.10.0-linux-amd64.tar.gz', 'flannel-v0.10.0-linux-amd64.tar.gz')
            
        