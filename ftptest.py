#coding=utf-8
import winrm
username='user'
passwd='password'
ftpname='li'
ftppasswd='lxy'
#dirname=raw_input("请输入你要下载的目录:")
filename='testfile.py'
f=open("d:\\ip.txt")
ip_list=f.readlines()

for ip in ip_list:
	s = winrm.Session(ip,auth=(username,passwd))
	ftp_cmd='wget'
	ftp_cmd_arg='-P'+' '+'d:\\'+' '+'ftp://'+ftpname+':'+ftppasswd+'@'+'192.168.1.1'+'/'+filename
	print ftp_cmd+ftp_cmd_arg
	r = s.run_cmd(ftp_cmd,[ftp_cmd_arg])
	print r.status_code
	print r.std_out
