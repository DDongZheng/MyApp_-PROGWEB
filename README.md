# MyApp_PROGWEB  
### Nom: ZHENG&ensp;&ensp;&ensp;&ensp;&ensp;Prénom: Qianyuan  
MyApp   
|── backend  
|&ensp;&ensp;&ensp;&ensp;&ensp;|── Dockerfile  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── app.py  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── backend-deployment.yaml  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── backend-service.yaml  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── docker-compose.yml  
|── frontend  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── Dockerfile  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── frontend-deployment.yaml  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── frontend-service.yaml  
│&ensp;&ensp;&ensp;&ensp;&ensp;|── index.html  
|── kubernetes-rbac  
&ensp;&ensp;&ensp;&ensp;&ensp;|── bindings  
&ensp;&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;&ensp;|── pod-reader-global-clusterrolebinding.yaml  
&ensp;&ensp;&ensp;&ensp;&ensp;|&ensp;&ensp;&ensp;&ensp;&ensp;|── pod-reader-rolebinding.yaml  
&ensp;&ensp;&ensp;&ensp;&ensp;|── roles  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|── pod-reader-global-clusterrole.yaml  
&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;&ensp;|── pod-reader-role.yaml  
