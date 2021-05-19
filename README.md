# Please Read to utilize this efficiently 
The file contains many useful linux commands, tools and information on how the OS works. 

This file is very useful for anyone who uses linux, anyone who prepares for LFCS, LFCE and OSCP and more. 

The file can be searched manually or using the finder.py draft script as shown in the following example:

└─$ ./finder.py du
{ du }


du -h                                                                           ** -h, --human-readable  print sizes in human readable format (e.g., 1K 234M 2G) <br/>
du  -sh * | sort -nr                                                            ** Sort folder by sizes <br/> 
du -sch /*                                                                      ** The sort I used many times and tired it. <br/>
du --max-depth=1 -hx /                                                          ** very handy one<br/>
                                                                                ** -d, --max-depth=N => Just go down one level from / and sum up everything recursively underneath in the tree. <br/>
                                                                                ** -x, --one-file-system  => skip directories on different file systems Stay on one filesystem; don't look at directories that are not on the / partition. In this case that means ignore:
                                                                                /dev /proc /run /sys <br/>


