# Using Locust to step through a Blue-Green Scenario

## Basic Setup
There's some [pre-work](COMMON-SETUP.md)

## Setup information for each of the VIPs
Within the ```vips.py``` file, edit the VIPS_INFO array, adding a record for each VIP. The fields are *virtual address*, *AS3 Tenant Name*, and *AS3 Application Name*.

```python
VIP_INFO = [
    ("192.0.2.10","Test","App"),
    ("192.0.2.11","Test2","App")
]
```

## Start a Locust Instance
at a command line, define the following environment variables
```bash
# IP or FQDN of BIG-IP
export BIGIP_ADDRESS="https://bigip.example.com"
# username with which to authenticate on the BIG-IP
export BIGIP_USER="admin"
# password for BIGI_USER
export BIGIP_PASS="supersecretpassword"
# number of seconds between steps in the blue-green workflow
export BLUEGREEN_STEP_WAIT="300"
export BLUEGREEN_STEP_WAIT_MIN="60"
```

in the same command line session run the following command to start locust. 
```shell
docker run --env BIGIP_USER=$BIGIP_USER --env BIGIP_PASS=$BIGIP_PASS --env BLUEGREEN_STEP_WAIT=$BLUEGREEN_STEP_WAIT -p 8089:8089 -v $PWD:/mnt/locust locustio/locust -f /mnt/locust/as3-bluegreen-test.py --host $BIGIP_ADDRESS
```

The [Docker site](https://docs.docker.com/) and others have more elaborate information on the various command line parameters. The options used here are:
- Environment variables are set within the docker container to be used by Locust
```shell
--env BIGIP_USER=$BIGIP_USER --env BIGIP_PASS=$BIGIP_PASS
```
- A port from within the container is exposed outside the container to provide access to the Locust UI
```shell
-p 8089:8089
```
- The current working directory is exposed as a volume within the container to provide access to the ```fast-as3-bluegree-test.py``` test tasks file
```shell
-v $PWD:/mnt/locust
```

## Run the test
- open ```http://hostname:8089```  
![locust ui](locust-1st-step.png)
- set the number of users to spawn and the spawn rate  
![locust ui](locust-2nd-step.png)
- watch the process  
![locust ui](locust-3rd-step.png)
