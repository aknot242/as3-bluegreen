## Install AS3 on the target BIG-IPs
- Follow [these directions](https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/installation.html#installation) to install AS3  

## Enable BurstHandling for AS3
 - Follow [these directions](https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/burst-handling.html?highlight=burst)
 - Or, execute this curl command
```
 curl --header "Content-Type: application/json" -X POST -u admin:adminpassword -k https://bigipaddress/mgmt/shared/appsvcs/settings -d '{ "burstHandlingEnabled": true }'
``` 
 - Or, if you have the VS Code [Rest Client extension](https://marketplace.visualstudio.com/items?itemName=humao.rest-client) installed, use the following 
 
 
 ```
###
# @name setbursthandling
#
POST https://bigip/mgmt/shared/appsvcs/settings
Authorization: Basic {{$dotenv user}} {{$dotenv password}} 
Content-Type: application/json

{
    "burstHandlingEnabled": true
}
 ```

## Enable AS3 Best Practices memory configuration
TBD look [here](https://clouddocs.f5.com/products/extensions/f5-appsvcs-extension/latest/userguide/best-practices.html)

## Install Docker
If you don't already have Docker installed, [install Docker](https://docs.docker.com/get-docker/)