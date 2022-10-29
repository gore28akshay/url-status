# url-status

### Testing application image on local machine
**Step 1** :- Build docker image on local.
* a. ```docker build -t url-status -f Dockerfile .``` #at root level of folder url-status

**Step 2** :- Run docker image on local and start the application
* a. ```docker run -itd --rm --name url-status url-status sh```
* b. ```docker exec -it url-status sh``` #exec in container
* c. ```bash``` #to change sheel
* d. ```python3 app.py``` #start the application

**Step 3** :- Test the application
* a. ```docker exec -it url-status sh``` #Open another terminal and exec in the container.
* b. ```curl localhost```
* c. Should give output-1 as below.

### Deploying application on kubernetes.
**Step 1** :- Applying yaml files to deploy application
* a. ```kubectl apply -f url-deployment.yaml``` #deployment
* b. ```kubectl apply -f service.yaml``` #service deployment

**Step 2**  :- Test the deployment and service
* a. ```kubectl port-forward deploy/url-status-deployment 8080:80``` #port forward to test deployment
* b. ```curl localhost:8080``` #execute command from local machine
* c. ```kubectl port-forward svc/url-status-service 8080:80``` #port forward to test service
* d. ```curl localhost:8080``` #execute command from local machine
* e. Above two commands will give output-2 as below

### Deploying grafana and prometheus on kubernetes.
**Step 1**  :- Applying yaml files to deploy prometheus and grafana
* a. ```kubectl apply -f url-prometheus.yaml```

**Step 2** : Open prometheus UI using port-forward.
* a. ```kubectl port-forward svc/prometheus-server 8080:9090``` #port forward to test prometheus
* b. Open any browser on local machine and access prometheus using below url.
      http://localhost:8080  
      This should give output-3  
* c. Check if the application is being scraped by prometheus using below url
      http://localhost:8080/targets  
      This should give output-4  
      This screen shows that our target url-status is getting scraped by prometheus.  

**Step 3** :- Open grafana UI using port-forward.
* a. kubectl port-forward svc/grafana 8080:3000
      This should give output-5
      Login using default grafana uername:password as admin:admin
      Set new password as per choice
* b. Configure datasource using "Data Sources" option in welcome panel.
      Refer output-6
* c. Add url of prometheus in HTTP text box in below image. Url of prometheus would be
      http://prometheus-server.default.svc.cluster.local:9090
      Refer output-7
* d. Click on "Save & test" button at the bottom of screen.
      Refer output-8
* e. Verify that the above source is default in grafana.

**Step 4** :- Creating panels in grafana using Query.
a. Query to create panel which shows status of https://httpstat.us/200
   ```sample_external_url_up{url="https://httpstat.us/200"}```
b. Query to create panel which shows response time of https://httpstat.us/200
   ```sample_external_url_response_ms{url="https://httpstat.us/200"}```
c. Query to create panel which shows status of https://httpstat.us/503
   ```sample_external_url_up{url="https://httpstat.us/503"}```
d. Query to create panel which shows response time of https://httpstat.us/503
   ```sample_external_url_response_ms{url="https://httpstat.us/503"}```

Alternatively import dashboards using the json files uploaded at root of folder.
