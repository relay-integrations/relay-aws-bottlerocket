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
      "ImageId":"ami-06851e719b3441357",
      "InstanceId":"i-04ba78df6e2010d25",
      "InstanceType":"t2.micro",
      "KernelId":"None",
      "KeyName":"kenaz-keypair1",
      "LaunchTime":datetime.datetime(2020,6,1,21,24,45,"tzinfo=tzlocal())",
      "Monitoring":{
         "State":"disabled"
      },
      "Placement":{
         "AvailabilityZone":"us-east-1e",
         "GroupName":"",
         "Tenancy":"default"
      },
      "Platform":"None",
      "PrivateDnsName":"ip-172-31-47-64.ec2.internal",
      "PrivateIpAddress":"172.31.47.64",
      "ProductCodes":[

      ],
      "PublicDnsName":"ec2-54-158-189-43.compute-1.amazonaws.com",
      "PublicIpAddress":"54.158.189.43",
      "RamdiskId":"None",
      "State":{
         "Code":16,
         "Name":"running"
      },
      "StateTransitionReason":"",
      "SubnetId":"subnet-e322e2df",
      "VpcId":"vpc-98b2a6ff",
      "Architecture":"x86_64",
      "BlockDeviceMappings":[
         {
            "DeviceName":"/dev/xvda",
            "Ebs":{
               "AttachTime":datetime.datetime(2020,6,1,21,24,46,"tzinfo=tzlocal())",
               "DeleteOnTermination":True,
               "Status":"attached",
               "VolumeId":"vol-0d7e37a31ab1e1b8a"
            }
         },
         {
            "DeviceName":"/dev/xvdb",
            "Ebs":{
               "AttachTime":datetime.datetime(2020,6,1,21,24,46,"tzinfo=tzlocal())",
               "DeleteOnTermination":True,
               "Status":"attached",
               "VolumeId":"vol-0e6ac859412397494"
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
               "PublicDnsName":"ec2-54-158-189-43.compute-1.amazonaws.com",
               "PublicIp":"54.158.189.43"
            },
            "Attachment":{
               "AttachTime":datetime.datetime(2020,6,1,21,24,45,"tzinfo=tzlocal())",
               "AttachmentId":"eni-attach-0e5bec61bcee116bc",
               "DeleteOnTermination":True,
               "DeviceIndex":0,
               "Status":"attached"
            },
            "Description":"",
            "Groups":[
               {
                  "GroupName":"launch-wizard-37",
                  "GroupId":"sg-0b24f1341f73e1c31"
               }
            ],
            "Ipv6Addresses":[

            ],
            "MacAddress":"06:68:26:f0:12:dd",
            "NetworkInterfaceId":"eni-0fc43d669a505069f",
            "OwnerId":"180094860577",
            "PrivateDnsName":"ip-172-31-47-64.ec2.internal",
            "PrivateIpAddress":"172.31.47.64",
            "PrivateIpAddresses":[
               {
                  "Association":{
                     "IpOwnerId":"amazon",
                     "PublicDnsName":"ec2-54-158-189-43.compute-1.amazonaws.com",
                     "PublicIp":"54.158.189.43"
                  },
                  "Primary":True,
                  "PrivateDnsName":"ip-172-31-47-64.ec2.internal",
                  "PrivateIpAddress":"172.31.47.64"
               }
            ],
            "SourceDestCheck":True,
            "Status":"in-use",
            "SubnetId":"subnet-e322e2df",
            "VpcId":"vpc-98b2a6ff",
            "InterfaceType":"interface"
         }
      ],
      "OutpostArn":"None",
      "RootDeviceName":"/dev/xvda",
      "RootDeviceType":"ebs",
      "SecurityGroups":[
         {
            "GroupName":"launch-wizard-37",
            "GroupId":"sg-0b24f1341f73e1c31"
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
]
```