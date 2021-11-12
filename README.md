# deploy

1. install kdb+  
   cp kdb+ to /tmp, install kdb+ into /q/  
   cp kc.lic 许可文件到/q  
   运行 source env.sh  
   #!/usr/bin/bash  
   export QLIC=/q  
   export QHOME=/q  
   
   如果是32位kdb+, 在suse下先安装包zypper install glibc-32bit  
   export QHOME=/home/toby/q  
   export PATH=/home/toby/q/l32:$PATH  
   alias q="rlwrap /home/toby/l32/q"  
2. 配置/mylab/datasource/tdx  /data/datasource/tdx  

3. cp q.xingye/feedhandler/xingye_ut.q ==> /mylab/q/feedhandler/xingye_ut.q  

