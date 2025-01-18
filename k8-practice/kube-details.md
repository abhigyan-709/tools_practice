# what actually the kubernetes is 
Kubernetes is the container orchestration tool.
It is used to manage thousands of conatiners by implementing the concept of pods
Pods are the smallest operable unit in K8 environment 
Pods abstracts the Container and the Container Abstracts the user application 


# Advantages of the k8
1. Highly Scalable 
2. Highly Availability and Mangement with zero downtimes

# cluster component in k8 

1. Master Node - in production environment its more than one or minimum 2
2. Worker Node - can be 1 or more than 1
               - can be connected to more than one master node as well

## Components of Master Node
K8 have 5 major components

- API Server - entry point of the k8 cluster i.e. only way to interact with k8
    1. via CLI
    2. via GUI
    3. via API
- Controller Manager - monitors the state of the k8 cluster
    1. any pods that need to be restarted
    2. any pods that get deleted 
    3. sends the request to scheduler to start the pod or re-deploy the pod which gets deleted
- Scheduler - smartly schedules the pods based on the available resources
    1. Use to compare the old state and gets the details from the controller manager for the pods 
    2. after getting the details it starts the pods on the best available node/ worker node 
- etcd
    1. The most truth vaule of the k8
    2. stores the current state of the k8 in key value pair
    3. does not stores the databases of node, but the details of the clusters state in key value pair
    4. user have to manage the snapshot and backup storage on own as k8 doest not manages databases
- Virtual Network - way to connect the master node to the worker nodes

## Components of the Worker Node:
there are multiple components of the worker node
worker node have multiple components and 3 main services running on it.

#### Services running on k8 worker node
1. kubelet -  responsible for the communication between workernode and container
           - responsible for starting and scheduling the pods inside the worker node as directed by kube-scheduler from master 
           
2. kube-proxy - responsible for the communication by forwarding the resquests from services to the pods
           - must be installed in every node

3. container runtime - to manage and run containers inside the pod i.e. docker or other services


#### Components running on k8 worker node
1. Pod
    - Smallest unit in the k8 architecture to interact with
    - Ephemeral in nature
    - Can have mul
2. Ingress
    - describe inbound rule to access the application 
    - routes the traffic from user to the service
    - forward the requests from user to services
    - it is load balanced i.e multiple replica if pods can be done for the ingress
3. Services
    - mainly have 4 important services
        1. Static IPv4 for the internal pods communication
        2. NodePort
        3. LoadBalancer
        4. ClusterIP
4. kubelet
5. Deployment 
    - blueprint of the application infrasctructure for the pods 
    - can be managed by user in production env
    - scaling up and down can be done thorugh this file
    - can create multiple replicaset of the pods
6. Stateful Set 
    - same as deployment but for the database pods
    - as the persistent storage is required for the database 
    - replicates the database by using the same or shared storage volumes
    
7. Volumes or Storage blocks



## Important K8 commands with kubectl 
- getting the k8 components details
```bash
# get pods
$ kubectl get pods

# get deployments
$ kubectl get deployments

# get nodes
$ kubectl get nodes

# get services
$ kubectl get services

# get cluster info 
$ kubetctl cluster-info

# get replicasets
$ kubectl get replicasets

# get secrets
$ kubectl get secrets
```

- debugging the pods
```bash
# get pods
$ kubectl get pods

# describe pods for details
$ kubectl describe pod -pod-name

# get the pod logs 
$ kubectl logs -pod-name

# get into interactive terminal of pod
$ kubectl exec -it [pod-name] /bin/bash
```

- deleting the deployments or pods
```bash
# in general we dont deal with the pods directly 
$ kubectl get deployments
$ kubectl describe deployment [deployment-name]
$ kubectl delete deployment 

# create the deployment | services 
$ kubectl apply -f deployment.yaml
$ kubectl apply -f service.yaml
```