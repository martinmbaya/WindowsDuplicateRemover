import os
from os import listdir
from os.path import isfile, join
import subprocess

def main():
	# my_path = input("Enter starting path:\n")
	my_path = "F:\BACKUP FAT32"
	only_files = [f for f in listdir(my_path) if isfile(join(my_path, f))]
	only_duplicates = []
	list_length = len(only_files)
	for i in only_files:
		duplicated_name = str(str(i).split(".")[0]) + " - Copy." + str(str(i).split(".")[1])
		for k in range(list_length):
			if duplicated_name == str(only_files[k]):
				only_duplicates.append(str(i))

	print(only_duplicates)



def major():
	# my_path = input("Enter starting path:\n")
	my_path = "E:"
	only_duplicates = {}
	only_files = []
	for root, dirs, files in os.walk(my_path, followlinks=False):
		only_files.extend(files)
		if 'CVS' in dirs:
			dirs.remove('CVS')
	list_length = len(only_files)
	for i in only_files:
		try:
			#Create a name format of what a duplicated file would look like in Windows by adding ' - Copy' 
			duplicated_name = str(str(i).split(".")[0]) + " - Copy." + str(str(i).split(".")[1])
			for k in range(list_length):
				if list_length >= len(only_files):
					if duplicated_name == str(only_files[k]):
						my_dict_key = str(only_files[k])
						if my_dict_key in only_duplicates.keys():
							only_duplicates[my_dict_key] += 1
						else:
							only_duplicates[my_dict_key] = 1
						del only_files[k]

					if str(i) == str(only_files[k]) and only_files.index(i) != k:
						my_dict_key = str(i)
						if my_dict_key in only_duplicates.keys():
							only_duplicates[my_dict_key] += 1
						else:
							only_duplicates[my_dict_key] = 1
						del only_files[k]
						# if str(str(i).split(".")[1]) == 'jpg' or str(str(i).split(".")[1]) == 'db' or str(str(i).split(".")[1]) == 'png' or str(str(i).split(".")[1]) == 'txt':
						# 	pass
						# else:
						# 	only_duplicates[str(i)] = str(only_files[k])
				else:
					break
		except:
			for k in range(list_length):
				if list_length >= len(only_files):
					if str(i) == str(only_files[k]) and only_files.index(i) != k:
						my_dict_key = str(i)
						if my_dict_key in only_duplicates.keys():
							only_duplicates[my_dict_key] += 1
						else:
							only_duplicates[my_dict_key] = 1
						del only_files[k]
						# if str(str(i).split(".")[1]) == 'jpg' or str(str(i).split(".")[1]) == 'db' or str(str(i).split(".")[1]) == 'png' or str(str(i).split(".")[1]) == 'txt':
						# 	pass
						# else:
						# 	only_duplicates[str(i)] = str(only_files[k])
					else:
						break
					
				
	for keys in sorted(only_duplicates, key=only_duplicates.get, reverse=True):
		print (keys, " : ", only_duplicates[keys], " duplicate(s) found")

	

def bigger():
	# my_path = input("Enter starting path:\n")
	my_path = "E:\Trial"
	# log = open("Logs.log", 'r')
	# my_path = log.readline()
	# log.close()
	only_duplicates = {}
	only_files = {}
	for root, dirs, files, in os.walk(my_path, followlinks=False):
		for x in files:
			full_path = os.path.join(root, x)
			only_files[full_path] = x
			# only_files.extend(os.path.join(root, x) for x in files)
		if 'CVS' in dirs:
			dirs.remove('CVS')
	# [print(a, " : ", b) for a,b in only_files.items()]

	list_length = len(only_files)
	exclud = []
	for p,i in only_files.items():
		try:
			#Create a name format of what a duplicated file would look like in Windows by adding ' - Copy' 
			duplicated_name = str(str(i).split(".")[0]) + " - Copy." + str(str(i).split(".")[1])
			for k in only_files.keys():
				if k in exclud:
					pass
				else:
					if duplicated_name == str(only_files[k]):
						my_dict_key = str(only_files[k])
						if my_dict_key in only_duplicates.keys():
							only_duplicates[my_dict_key][0] += 1
							only_duplicates[my_dict_key].append(k)
						else:
							only_duplicates[my_dict_key] = [1, k]
						exclud.append(k)

					if str(i) == str(only_files[k]) and p != k:
						my_dict_key = str(i)
						if my_dict_key in only_duplicates.keys():
							only_duplicates[my_dict_key][0] += 1
							only_duplicates[my_dict_key].append(k)
						else:
							only_duplicates[my_dict_key] = [1, k]
						exclud.append(k)
						# if str(str(i).split(".")[1]) == 'jpg' or str(str(i).split(".")[1]) == 'db' or str(str(i).split(".")[1]) == 'png' or str(str(i).split(".")[1]) == 'txt':
						# 	pass
						# else:
						# 	only_duplicates[str(i)] = str(only_files[k])
		except:
			for k in only_files.keys():
				if k in exclud:
					pass
				else:
					if str(i) == str(only_files[k]) and p != k:
						my_dict_key = str(i)
						if my_dict_key in only_duplicates.keys():
							only_duplicates[my_dict_key][0] += 1
							only_duplicates[my_dict_key].append(k)
						else:
							only_duplicates[my_dict_key] = [1, k]
						exclud.append(k)
						# if str(str(i).split(".")[1]) == 'jpg' or str(str(i).split(".")[1]) == 'db' or str(str(i).split(".")[1]) == 'png' or str(str(i).split(".")[1]) == 'txt':
						# 	pass
						# else:
						# 	only_duplicates[str(i)] = str(only_files[k])
						
				
	# for keys in sorted(only_duplicates, key=only_duplicates.get, reverse=True):
	# 	print (keys, " : ", only_duplicates[keys], " duplicate(s) found")
	[print(a, " : ", b, "\n") for a,b in only_duplicates.items()]
	for value in only_duplicates.values():
		for i in range(value[0]):
			del_command = "del " + str(value[i+1])
			print(del_command)
			subprocess.Popen(del_command, shell=True)



			


if __name__ == '__main__':
	bigger()
