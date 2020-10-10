Scalp是用于Apache服务器，旨在查找安全问题的日志分析器。主要理念是浏览大量日志文件并通过从HTTP/GET中提取可能的攻击。
Scalp是python脚本，所以要求我们的机器中安装python。


$ python scalp-0.4.py --help
Scalp the apache log! by Romain Gaucher - http://rgaucher.info
usage:  ./scalp.py [--log|-l log_file] [--filters|-f filter_file] [--period time-frame] [OPTIONS] [--attack a1,a2,..,an]
                   [--sample|-s 4.2]
   --log       |-l:  the apache log file './access_log' by default
   --filters   |-f:  the filter file     './default_filter.xml' by default
   --exhaustive|-e:  will report all type of attacks detected and not stop
                     at the first found
   --tough     |-u:  try to decode the potential attack vectors (may increase
                     the examination time)
   --period    |-p:  the period must be specified in the same format as in
                     the Apache logs using * as wild-card
                     ex: 04/Apr/2008:15:45;*/Mai/2008
                     if not specified at the end, the max or min are taken
   --html      |-h:  generate an HTML output
   --xml       |-x:  generate an XML output
   --text      |-t:  generate a simple text output (default)
   --except    |-c:  generate a file that contains the non examined logs due to the
                     main regular expression; ill-formed Apache log etc.
   --attack    |-a:  specify the list of attacks to look for
                     list: xss, sqli, csrf, dos, dt, spam, id, ref, lfi
                     the list of attacks should not contains spaces and comma separated
                     ex: xss,sqli,lfi,ref
   --output    |-o:  specifying the output directory; by default, scalp will try to write
                     in the same directory as the log file
   --sample    |-s:  use a random sample of the lines, the number (float in [0,100]) is
                     the percentage, ex: --sample 0.1 for 1/1000


$ python scalp-0.4.py -l access.log -f default_filter.xml --html