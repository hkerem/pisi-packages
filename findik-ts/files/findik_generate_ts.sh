#!/bin/bash

DB_REPLY=$(mysql --user=root --password= findik -e "select * from btk_user_info;" --batch | tail -1)
TS_USERNAME=$(echo $DB_REPLY| awk '{ print $1 }' )
TS_PASSWORD=$(echo $DB_REPLY| awk '{ print $2 }' )

java -jar /usr/share/findik/ts/ZamaneConsole-1.1.9.jar -z $1 http://tzd.kamusm.gov.tr 80 $TS_USERNAME $TS_PASSWORD >> /var/log/findik/ts/timestamp.log


