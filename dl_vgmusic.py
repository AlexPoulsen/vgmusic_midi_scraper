import requests
import pathlib
import sys
import os
import errno
import urllib

dl = []
with open("vgmusic_sources.txt", "r") as pagelist:
	for page in pagelist.read().split("\n"):
		if "http" in page:
			source = requests.get(page).text
			part = source.split(".mid")
			print(len(part), " "*(4-len(str(len(part)))), end="")
			counter = 1
			for p in part[:len(part)-1]:
				dl.append(page + (p + ".mid").split("<a href=\"")[-1])
				# print("-- ", new)
				print("|", end="")
				if counter % 120 == 0:
					print("\n", end="     ")
				counter += 1
			print("\n")
path = pathlib.Path(".") / "vgmusic_sources"
try:
	os.makedirs(path)
except OSError as e:
	if e.errno != errno.EEXIST:
		raise
counter = 1
print("downloading files")
print("     ", end="")
for file in dl:
	urllib.request.urlretrieve(file, path / file.split("/")[-1])
	print("|", end="")
	if counter % 120 == 0:
		print("\n", end="     ")
	counter += 1
print("\n")
