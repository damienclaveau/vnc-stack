#### Developer Quickstart on HDP Sandbox using Ambari Stacks
An Ambari Stack service package for VNC Server with the ability to install Eclipse as well to quickly start developing on HDP Hadoop

- Download HDP 2.2 sandbox VM image (Sandbox_HDP_2.2_VMware.ova) from [Hortonworks website](http://hortonworks.com/products/hortonworks-sandbox/)
- Import Sandbox_HDP_2.2_VMware.ova into VMWare and set the VM memory size to 8GB
- Now start the VM
- After it boots up, find the IP address of the VM and add an entry into your machines hosts file e.g.
```
192.168.191.241 sandbox.hortonworks.com sandbox    
```
- Connect to the VM via SSH (password hadoop) and start Ambari server
```
ssh root@sandbox.hortonworks.com
/root/start_ambari.sh
```

- To deploy the VNC stack, run below
```
cd /var/lib/ambari-server/resources/stacks/HDP/2.2/services
git clone https://github.com/abajwa-hw/vnc-stack.git   
sudo service ambari restart
```
- Then you can click on 'Add Service' from the 'Actions' dropdown menu in the bottom left of the Ambari dashboard:
On bottom left -> Actions -> Add service -> check VNC Server -> Next -> Next -> Enter password -> Next -> Deploy
![Image](../master/screenshots/screenshot-vnc-config.png?raw=true)

On successfull deployment you will see the VNC service as part of Ambari stack and will be able to start/stop the service from here:
![Image](../master/screenshots/screenshot-vnc-stack.png?raw=true)

When you've completed the install process, VNC server will be available at your VM's IP on display 1 with the password you setup
![Image](../master/screenshots/screenshot-vnc-clientsetup.png?raw=true)

On logging in you will see the CentOS desktop running on the sandbox
![Image](../master/screenshots/screenshot-vnc-clientlogin.png?raw=true)

Click the eclipse shortcut to start Eclipse
![Image](../master/screenshots/screenshot-vnc-eclipsestarted.png?raw=true)

- To remove the service: 
1. stop the service via Ambari
2. Delete the service
```
curl -u admin:admin -i -H 'X-Requested-By: ambari' -X DELETE http://sandbox.hortonworks.com:8080/api/v1/clusters/Sandbox/services/VNC
```
3. Remove artifacts /var/lib/ambari-server/resources/stacks/HDP/2.2/services/VNC/remove.sh
