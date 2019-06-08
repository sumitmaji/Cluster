import os
from constants import *
import subprocess
from util import execute


os.environ[ENABLE_DEBUG] = 'true'
os.environ[MOUNT_PATH] = '/export'
os.environ[INSTALL_PATH] = '{0}/kubernetes/install_scripts_secure'.format(os.environ[MOUNT_PATH])
os.environ[REPOSITORY] = 'http://192.168.1.5'
os.environ[HOSTINTERFACE] = 'eth0'

command = "ifconfig {0} 2>/dev/null|awk '/inet addr:/ {{print $2}}'|sed 's/addr://'".format(os.environ[HOSTINTERFACE])
os.environ[HOSTIP] = execute(command)[0]

os.environ[WORKDIR] = '/export/tmp'
os.environ[SERVER_DNS] = 'master.cloud.com,node01.cloud.com,kubernetes.default.svc,kubernetes.default,kubernetes,kubernetes.default.svc.cloud,kubernetes.default.svc.cloud.uat,localhost,master,node01'
os.environ[SERVER_IP] = '11.0.0.1,11.0.0.2,172.18.0.1,127.0.0.1,192.168.1.7,192.168.1.1,192.168.1.2,192.168.1.3,192.168.1.4,192.168.1.5,192.168.1.6,192.168.1.8,192.168.1.9,192.168.1.10,192.168.1.11'
os.environ[SERVERS] = '11.0.0.2:node01.cloud.com'
os.environ[WORKERS] = '11.0.0.2:node01.cloud.com'
os.environ[NODES] = '11.0.0.2:node01.cloud.com'
os.environ[CLUSTER] = 'cloud.com'
os.environ[CERTIFICATE] = '{0}/kubecertificate'.format(os.environ[MOUNT_PATH])
os.environ[CERTIFICATE_MOUNT_PATH] = '{0}/certs/'.format(os.environ[CERTIFICATE])
os.environ[CA_CERTIFICATE] = '{0}/ca.crt'.format(os.environ[CERTIFICATE_MOUNT_PATH])
os.environ[API_SERVER] = 'https://master.cloud.com'
os.environ[CLIENT_CERTIFICATE] = '{0}/admin.crt'.format(os.environ[CERTIFICATE_MOUNT_PATH])
os.environ[CLIENT_KEY] = '{0}/admin.key'.format(os.environ[CERTIFICATE_MOUNT_PATH])
os.environ[ETCD_CLUSTERS] = '11.0.0.2:node01'
os.environ[HAPROXY] = '11.0.0.1'
os.environ[FLANNEL_NET] = '172.17.0.0/16'
os.environ[CLUSTERIPRANGE] = '172.18.0.0/24'
os.environ[CLUSTER_NON_MASQUEARADE_CIDR] = '172.17.0.0/15'
os.environ[API_SERVERS] = 'https://master.cloud.com'
os.environ[APISERVER_HOST] = 'https://master.cloud.com'
os.environ[ETCD_CLUSTERS_CERTS] = '11.0.0.2:node01.cloud.com'
os.environ[DOMAIN] = 'cloud.com'
os.environ[ENABLE_ETCD_SSL] = 'true'
os.environ[ENABLE_KUBE_SSL] = 'true'
os.environ[ENABLE_OIDC] = 'true'
os.environ[INGRESS_HOST] = 'master.cloud.com'
os.environ[INSTALL_INGRESS] = 'true'
os.environ[ETCDSERVERS] = 'http://11.0.0.2:2379'
os.environ[MASTER_1_IP] = '11.0.0.2'
os.environ[ADVERTISE_IP] = os.environ[MASTER_1_IP]
os.environ[ETCD_1_IP] = os.environ[MASTER_1_IP]
os.environ[ETCD_1_NAME] = 'node01'
os.environ[DNS_IP] = '172.18.0.2'
os.environ[YOUR_DOMAIN] = 'cloud.uat'
os.environ[INSTALL_KUBELET_ON_MASTER] = 'true'
os.environ[INSTALL_DASHBOARD] = 'true'
os.environ[INSTALL_SKYDNS] = 'true'
os.environ[INSTALL_HEAPSTER] = ' false'
os.environ[SKYDNS_DOMAIN_NAME] = 'cloud.uat'
os.environ[ETCD_VERSION] = 'etcd-v3.2.18-linux-amd64'
os.environ[FLANNEL_VERSION] = 'flannel-v0.10.0-linux-amd64'