from sys import argv
from os import system, path
file=argv[1]
extension=path.splitext(file)[1]
try:
	arch=argv[2]
except:
	print("[*] no architecture passed, using 32 bit")
	arch=32

if int(arch) == 32:
	print("[+] compiling {} with nasm with 32 bit architecture..".format(file))
	system("nasm -f elf32 {}".format(file))
	print("[*] done!")

	print("[+] linking object file..")
	system("ld -m elf_i386 -o {} {} ".format(file.replace(extension,""),file.replace(extension,".o")))
	print("[*] done!")


	system("rm {}".format(file.replace(extension,".o")))
elif int(arch) == 64:
	print("[+] compiling {} with nasm with 64 bit architecture..".format(file))
	system("nasm -f elf64 {}".format(file))
	print("[*] done!")

	print("[+] linking object file..")
	system("ld -o {} {} ".format(file.replace(extension,""),file.replace(extension,".o")))
	print("[*] done!")


	system("rm {}".format(file.replace(extension,".o")))
else:
	print("[*] invalid architecture passed, using 32")
	print("[+] compiling {} with nasm with 32 bit architecture..".format(file))
	system("nasm -f elf32 {}".format(file))
	print("[*] done!")

	print("[+] linking object file..")
	system("ld -m elf_i386-o {} {} ".format(file.replace(extension,""),file.replace(extension,".o")))
	print("[*] done!")


	system("rm {}".format(file.replace(extension,".o")))
