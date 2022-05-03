================================how router works=======================
source (A) private ip ------->router (public ip/private ip)---->(A) PUBLIC ip--------->desination(B) source accepts the public ip of A
destination (B)public ip----->router (public ip/private ip)----->(B) PUBLIC ip --------->source (A) changes public to private.(previous ip)
so router is an device which changes the ip according the source and the destination
snat- source network address translation
dnat-destination network address translation
=================================================================


===============SERVER COFIG========
instalation
sudo apt innstall apache 2
configur
   /var/www/html
server start
systemctl strat apache2
==============CLIENT=================
***********************PROCEDURE***************************
 enter 
            #ssh username @ ip
example: 
           # ssh student @ student_ip

enter the client 
  	#ip
and 
	#password
		now you can acces the server of the other person
=================SERVER===========
*********************** PROCEDURE****************
SSH-secure shell home page
* install SSH
                                     #[sudo apt install openssh-server]

 enter                           # [ifconfig] 
and share 
                                  #[ip] 
and 
                                #[user name]
enter   
                              #[password]

then enter               #{ls} command
[shows the files of the client]

===================================

==============file sharing from client to server/Desktop=================

open text editor
 	enter "date.txt"

open terminal
	enter 
	# scp filename username @ ip:/home/student/desktop
enter
 	#password
then you can find the file on the server desktop
=====================from different path =============================
******************File sharing*******************
define the client path 
	# cd/home/student/music 
	( path of the client)
enter
	#scp /client directory/filename student name @ ip : server directory
example:
	# scp /home/student/music/dd1.py student @ ip :/home/student/music 
enter
	#password
 now you can find the file in music directory

****************folder sharing******************
create a folder in a directory

and enter
	## scp -r  /home/student/music/dd1.py student @ ip :/home/student/music 
*******************************************************************

===========service start & stop==================

	#systemctl stop ssh
enter 
 	#password
services will stop;

To check it workes or not;
	 enter

 # netstat -tnlp

to start the service again
enter 
	# systemctl start ssh
======================================

DAY 1:unix commands
DAY 2:converting file to process fg/bg
DAY 3: packet manger (install apache & ssh)
DAY 4:networking (subnet/dns/snat/dnat/)
user managing/creation/deletion
ctrl+alt+f3/f4/f5(Gui)
DAY 5:client to server files acces/folder access


=================================
commands:
uname(linux)
whoami(student)
ls /dev
ls /etc/
cd/ ----->ls
cd/proc ------>ls
df -hT (storage devices)
free -h  (memory usge)
top (task mangertop)
ps -aux
ctrl +a (word start)
ls - l (files)
ls -a (hidden files)
 lsb_release -a(system details)
uname -a (system name)
gedit ~/.bashrc (whichver sentence u gave at the end of the code,it will appaer on th terminal)



================================================================

*************************************CLOUD COMPUTING***********************************************************

why cloud had been designed?
Its an non paidable resource
cloud providers/service providers
there are 3 main cloud/servie providers
1.AWS(amazon web services)
2.ms(microsoftazuru)
3.gcp(google cloud platfrom)
 infrastructure as a service

===============================
creating aws account.
===============================
visuvlization -1990s
sohmen duker


premise -my data centre
platform as a service-
infrastructure as a service-
function as a service-
======================================
VIRTUAL BOX:
VirtualBox runs a single process on the host operating system for each virtual guest.
 All of the guest user code is run natively in ring 3, 
just as it would be if it were running in the host.  
As a result, user code will perform at native speed when running in a
guest virtual machine.

===============installing of docker.==========
	#sudo apt install docker.io
after install;
run 
	#netstat -tnlp    (to check whether the docker is installed or not)
to check whether the docker is active or not
	#systemctl status docker
and then enter
	#sudo docker ps  ( number of containers)
and then enter
	#sudo docker image      (to list iso's   )

now we are going run a light-weighted os-
os name: alpine (it is a os used for test services)
	#sudo docker run -it alpine

To login into the running container 
	#docker attach (container ID)
to run more than one container at once
	#sudo docker run -it --name shiva alpine

to remove the docker 
	# sudo docker rm -f <container id>
to check whether it is removed or not
	#sudo docker ps
whenever the permissions got denied,just add "sudo" before the specific command
to logout enter
	#cntrl+p+q at once
***********************containers*******************************


============================DEVOPS====================================
developer and operations
developer wrotes a code and then generate an artifat(valuable thing)
monito checks whether the data is efficient or not
the one who done the whole process is know as Devops engineer
automation of the whole process -ml

===========================================================
**************************** STORAGE***************************
three types of storage
1.block
2.object
3.file storage
-------------------------------------------------
* Block-
ls blk-partitions
sda-type of large hard disk
agent to alborate space in os--
fsck def sda 1// convert the backup file and revive the whole file sys
primary partiotion
ebs-elastic block storage
----------------------------------------------------------
to entre the instances and connect to terminal 
	#cd downolds (downloaded file address)
	#chmod 400 divya.pem(file name)
	#copy the command followed  by ssh // just run this command every tym u want to login
and now u can run the instance
to exit from the instance
	#exit
---------------------------------------
sudo su - loot
apt install apache2 -y
------------------------------------
lsblk
 rm -rf * / remove forcefully star
--------------------------------
EBS( )
1. volume
2. partition
3. format
4. mount
------------------------------------
step - 1 attach : 
------------------------------------------------
step -2 :
partition:
	# fdisk /dev/xvdf
	n -new
	p- primary
and enter (2)
 then the partiton will created
partioning has to be performaed once only or the data will be erased.
--------------------------------------------------
step 3:
fromating:
	#mkfs.ext4 /dev/xvdf //( format tables are generated)
-------------------------------------------------------------------
step 4:
and then mounting (attachment)
	#mount /dev/xvdf /var/www/html (for mounting)
and # lsblk (list block)
we can see the xvdf mounted
-------------------------------------------------------------------------
	#mkfs (file creation)
 		#cd /var/www/html
		#ls
----------------------------------
		#echo >shive . /var/www/html/imedx.html
 #umount /dev/xvdf
 #ls
 #rm -rf index.html
 #cd  #lsblk
# mount  /dev/xvdf /var/www/html
 #ls
----------------------------------------------------------------
docker images pull
 #docker images 
(if there is no images it shows none)
creatinf /pulling the images
 #sudo docker pull ubuntu:20.04
(images names as ubuntu***)

launch centos  |  
launch alpine  |     some types of containers 
launch ubuntu|

now launching a container
 # docker exec -it id(container) bash
we enter into the container 
 # docker exec -it id(container) date 
it only display the date but cant enter into the container
that means a contaioner can only perform a single task at a time only.
-------------------------------------------------
why do we use a docker ?
To launch the containers quickly without depend on other things more 
like indepedntely
----------------------------------------------------------------------
attching the containers
 #docker attach id(container)
-------------------------------------------------------
docker - host
it follows the container 
every docker container is a process not a os
----------------------------------------------------
there are a n num of ways to satrt a process like as manuallu
we cannot use anything that has before a docker run,we can only use the sources after the docker has been on running
-------------------------------------------------------
without port forwading we ecannot reach the processes in the 
iso(image ) is in docker hub and we pull that iso image and run
after that we run a docker and we either attach or execute the container
docker attach- to attch the process-bash
exec- to reach process that are in bg 
===========================
DEVOPS
1. coding->(SCM)-if the code is deleted we can restore and multiple users and we can know the changes of the code in particular part of a line.
2. build
3. test
4. devploy
5. monitoring
data restore/code restore is two types-1. backup 2. snapshot
backup-stores only copy the current daya data and refers the previos day data
snapshot-day to day backup 

----------------------------------GITHUB------------------------------------
gtihub is a code hosting platform,we can work on a project together from anywhere in the world.if we use it in a cloud it is a github or otherwise it is a git.
enables developers to save snapshots of their projects over time. Its 
generally best for individual use.
upload -push
ADD-track
commit=package
push to github
 add->commit->push
----------------------------
#mkdir project
# cd project
# ls -a 
op: . ..
==========intialize=============
# git init
#ls -a
 OP: . .. .git



 






 













