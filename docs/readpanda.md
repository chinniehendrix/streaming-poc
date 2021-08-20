Streaming PoC

Create a K8s cluster locally
minikube start --memory=8Gi --cpus=2 --driver=hyperkit --profile streaming-poc

Use RedPanda instead of Kafka
https://vectorized.io/docs/quick-start-kubernetes/

Installing cert-manager is required for running RedPanda as it needs it to manage certificate for mutual TLS

helm repo add jetstack https://charts.jetstack.io && \
helm repo update && \
helm install \
  cert-manager jetstack/cert-manager \
  --namespace cert-manager \
  --create-namespace \
  --version v1.2.0 \
  --set installCRDs=true

After installing cert-manager, verifying that it is running properly using:
https://cert-manager.io/docs/installation/verify/

RedPanda installation:

helm repo add redpanda https://charts.vectorized.io/ && \
helm repo update

kubectl apply \
-k https://github.com/vectorizedio/redpanda/src/go/k8s/config/crd?ref=$VERSION

helm install \
--namespace redpanda-system \
--create-namespace redpanda-system \
--version $VERSION \
redpanda/redpanda-operator

Create a test one-node RP cluster
kubectl create ns chat-with-me
kubectl apply \
-n chat-with-me \
-f https://raw.githubusercontent.com/vectorizedio/redpanda/dev/src/go/k8s/config/samples/one_node_cluster.yaml

Use RPK to test the cluster

Check the status of the cluster
kubectl -n chat-with-me run -ti --rm \
--restart=Never \
--image vectorized/redpanda:$VERSION \
-- rpk --brokers one-node-cluster-0.one-node-cluster.chat-with-me.svc.cluster.local:9092 \
cluster info

Create a topic
kubectl -n chat-with-me run -ti --rm \
--restart=Never \
--image vectorized/redpanda:$VERSION \
-- rpk --brokers one-node-cluster-0.one-node-cluster.chat-with-me.svc.cluster.local:9092 \
topic create chat-rooms -p 5

Show the list of topics
kubectl -n chat-with-me run -ti --rm \
--restart=Never \
--image vectorized/redpanda:$VERSION \
-- rpk --brokers one-node-cluster-0.one-node-cluster.chat-with-me.svc.cluster.local:9092 \
topic list

