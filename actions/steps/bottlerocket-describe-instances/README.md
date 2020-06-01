# bottlerocket-describe-instances

This [AWS Bottlerocket](https://aws.amazon.com/bottlerocket/) step container lists the Bottlerocket
instances in an AWS region and sets an output, `instances`, to an array containing
information about them.

## Specification

| Setting | Child setting | Data type | Description | Default | Required |
|---------|---------------|-----------|-------------|---------|----------|
| `aws` || mapping | A mapping of AWS account configuration. | None | True |
|| `connection` | AWS Connection | Relay Connection for the AWS account. Use the Connection sidebar to configure the AWS Connection | None | True |
|| `region` | string | The AWS region to use (for example, `us-west-2`). | None | True |

## Outputs

| Name | Data type | Description |
|------|-----------|-------------|
| `instances` | array of mappings | The Bottlerocket instances in the given region. |

## Example

```yaml
steps:
# ...
- name: bottlerocket-describe-instances
  image: projectnebula/bottlerocket-describe-instances
  spec:
    aws:
      connection: !Connection { type: aws, name: my-aws-account } 
      region: us-west-2
```

## Example output `instances`
```
[
   {
      "AmiLaunchIndex":0,
      "ImageId":"ami-0323c3dd2da7fb37d",
      "InstanceId":"i-0d7ce1cc8568040ba",
      "InstanceType":"t2.micro",
      "KernelId":"None",
      "KeyName":"my-keypair1",
      "LaunchTime":datetime.datetime(2020,5,18,23,50,14,"tzinfo=tzlocal())",
      "Monitoring":{
         "State":"disabled"
      },
      "Placement":{
         "AvailabilityZone":"us-east-1c",
         "GroupName":"",
         "Tenancy":"default"
      },
      "Platform":"None",
      "PrivateDnsName":"ip-172-31-50-221.ec2.internal",
      "PrivateIpAddress":"172.31.50.221",
      "ProductCodes":[

      ],
      "PublicDnsName":"ec2-3-89-89-90.compute-1.amazonaws.com",
      "PublicIpAddress":"3.89.89.90",
      "RamdiskId":"None",
      "State":{
         "Code":16,
         "Name":"running"
      },
      "StateTransitionReason":"",
      "SubnetId":"subnet-b0be609d",
      "VpcId":"vpc-98b2a6ff",
      "Architecture":"x86_64",
      "BlockDeviceMappings":[
         {
            "DeviceName":"/dev/xvda",
            "Ebs":{
               "AttachTime":datetime.datetime(2020,5,11,19,53,25,"tzinfo=tzlocal())",
               "DeleteOnTermination":True,
               "Status":"attached",
               "VolumeId":"vol-01520ea868d53d293"
            }
         }
      ],
      "ClientToken":"",
      "EbsOptimized":False,
      "EnaSupport":True,
      "Hypervisor":"xen",
      "IamInstanceProfile":"None",
      "InstanceLifecycle":"None",
      "ElasticGpuAssociations":"None",
      "ElasticInferenceAcceleratorAssociations":"None",
      "NetworkInterfaces":[
         {
            "Association":{
               "IpOwnerId":"amazon",
               "PublicDnsName":"ec2-3-89-89-90.compute-1.amazonaws.com",
               "PublicIp":"3.89.89.90"
            },
            "Attachment":{
               "AttachTime":datetime.datetime(2020,5,11,19,53,24,"tzinfo=tzlocal())",
               "AttachmentId":"eni-attach-0810dc89921bfb32a",
               "DeleteOnTermination":True,
               "DeviceIndex":0,
               "Status":"attached"
            },
            "Description":"",
            "Groups":[
               {
                  "GroupName":"launch-wizard-32",
                  "GroupId":"sg-055e3c6c1245b30ac9"
               }
            ],
            "Ipv6Addresses":[

            ],
            "MacAddress":"12:7c:f1:49:20:a5",
            "NetworkInterfaceId":"eni-033397b08b96d1f3a",
            "OwnerId":"180094860577",
            "PrivateDnsName":"ip-172-31-50-221.ec2.internal",
            "PrivateIpAddress":"172.31.50.221",
            "PrivateIpAddresses":[
               {
                  "Association":{
                     "IpOwnerId":"amazon",
                     "PublicDnsName":"ec2-3-89-89-90.compute-1.amazonaws.com",
                     "PublicIp":"3.89.89.90"
                  },
                  "Primary":True,
                  "PrivateDnsName":"ip-172-31-50-221.ec2.internal",
                  "PrivateIpAddress":"172.31.50.221"
               }
            ],
            "SourceDestCheck":True,
            "Status":"in-use",
            "SubnetId":"subnet-b0b2309d",
            "VpcId":"vpc-9834a6ff",
            "InterfaceType":"interface"
         }
      ],
      "OutpostArn":"None",
      "RootDeviceName":"/dev/xvda",
      "RootDeviceType":"ebs",
      "SecurityGroups":[
         {
            "GroupName":"launch-wizard-32",
            "GroupId":"sg-055e3c6c1245b30ac9"
         }
      ],
      "SourceDestCheck":True,
      "SpotInstanceRequestId":"None",
      "SriovNetSupport":"None",
      "StateReason":"None",
      "Tags":"None",
      "VirtualizationType":"hvm",
      "CpuOptions":{
         "CoreCount":1,
         "ThreadsPerCore":1
      },
      "CapacityReservationId":"None",
      "CapacityReservationSpecification":{
         "CapacityReservationPreference":"open"
      },
      "HibernationOptions":{
         "Configured":False
      },
      "Licenses":"None",
      "MetadataOptions":{
         "State":"applied",
         "HttpTokens":"optional",
         "HttpPutResponseHopLimit":1,
         "HttpEndpoint":"enabled"
      }
   }
   ...
]
```