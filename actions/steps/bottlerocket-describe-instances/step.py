#!/usr/bin/env python
from functools import partial

import boto3
from nebula_sdk import Interface, Dynamic as D


def instance_to_dict(ec2, instance):
    shape = ec2.meta.client.meta.service_model.shape_for('Instance')
    attrs = instance.meta.resource_model.get_attributes(shape)

    d = {}
    for mapped, (name, shape) in attrs.items():
        d[name] = getattr(instance, mapped)

    return d


relay = Interface()

sess = boto3.Session(
  aws_access_key_id=relay.get(D.aws.connection.accessKeyID),
  aws_secret_access_key=relay.get(D.aws.connection.secretAccessKey),
  region_name=relay.get(D.aws.region),
)
ec2 = sess.resource('ec2')
raw_instances = ec2.instances.all()
print('Found the following Bottlerocket instances:\n')
print("{:<30} {:<30} {:<30} {:<30} {:<30}".format('ID', 'STATE', 'TYPE', 'VPC', 'KEY PAIR'))
for instance in raw_instances:
  print("{:<30} {:<30} {:<30} {:<30} {:<30}".format(instance.instance_id, instance.state['Name'], instance.instance_type, instance.vpc_id, instance.key_name))
instances = list(map(partial(instance_to_dict, ec2), ec2.instances.all()))

print('\nAdding {0} instance(s) to the output `instances`'.format(len(instances)))
relay.outputs.set('instances', instances)