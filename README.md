# start Jenkins on local box:
systemctl start jenkins


# expose port in minikube:

kubectl expose deployment/python-app-deployment \
    --type='NodePort' \
    --port=5000

kubectl port-forward svc/python-app-deployment 5000:5000

minikube dashboard --url &

kubectl proxy &




On remote host:


# open k8s dashboard connection
ssh -L 12345:localhost:8001 jlewis@192.168.1.168


# open port to app
ssh -L 54321:localhost:5000 jlewis@192.168.1.168

# open port to jenkins on minikube box
ssh -L 8080:localhost:8080 jlewis@192.168.1.168



Endpoints:

# k8s dashboard
http://localhost:12345/api/v1/namespaces/kubernetes-dashboard/services/http:kubernetes-dashboard:/proxy

# Jenkins
http://localhost:8080

# App
http://localhost:5000
