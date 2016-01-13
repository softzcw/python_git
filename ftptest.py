#coding=utf-8
import winrm
username='biaogeuser'
passwd='Ao7,*/$yRc8*IS4s^*'
ftpname='lixiaoyang'
ftppasswd='lxy(*23ec35'
#dirname=raw_input("请输入你要下载的目录:")
filename='testfile.py'
f=open("d:\\ip.txt")
ip_list=f.readlines()

for ip in ip_list:
	s = winrm.Session(ip,auth=(username,passwd))
	ftp_cmd='wget'
	ftp_cmd_arg='-P'+' '+'d:\\'+' '+'ftp://'+ftpname+':'+ftppasswd+'@'+'117.79.91.177'+'/'+filename
	print ftp_cmd+ftp_cmd_arg
	r = s.run_cmd(ftp_cmd,[ftp_cmd_arg])
	print r.status_code
	print r.std_out
