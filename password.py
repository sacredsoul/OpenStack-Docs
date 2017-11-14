# -*- coding:utf-8 -*-
import os
import json
import urllib.request
def get_data():
	data = urllib.request.urlopen("http://169.254.169.254/openstack/latest/meta_data.json").read().decode()
	return data
def parse_data(data):
	json_data = json.loads(data)
	adminPass = json_data.get("meta").get("admin_pass")
	os.system("net user Admin /active:yes")
	os.system("net user Admin %s" % adminPass)
data = get_data()
parse_data(data)