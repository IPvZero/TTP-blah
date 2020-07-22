import json
from ttp import ttp
from nornir import InitNornir
from nornir.plugins.tasks.networking import netmiko_send_command
from nornir.plugins.functions.text import print_result


nr = InitNornir(config_file="config.yaml")

def test(task):

   r = task.run(netmiko_send_command,command_string="show run int g0/1")
   datatoparse = r.result
   print(datatoparse)


   ttp_template="""
   interface {{ interface }}
   description {{ description }}
   ip address {{ ip }} {{ mask }}
   """

   parser = ttp(data=datatoparse, template=ttp_template)
   parser.parse()
   res = json.loads(parser.result(format='json')[0])
   print(res)



results = nr.run(task=test)
import ipdb
ipdb.set_trace()
