#!/bin/bash
. /usr/share/findik/scripts/btk-include

PATH=$PATH:/opt/sun-jre/bin

FILE_NAME=$1

DB_REPLY=$(mysql_query "select ts_username,ts_password from btk_user_info order by ts_username limit 1" )
TS_USERNAME=$(echo $DB_REPLY| awk '{ print $1 }' )
TS_PASSWORD=$(echo $DB_REPLY| awk '{ print $2 }' )

java -jar /usr/share/findik/ts/ZamaneConsole-1.1.9.jar -z $FILE_NAME http://tzd.kamusm.gov.tr 80 $TS_USERNAME $TS_PASSWORD >> /var/log/findik/ts/timestamp.log

FILE_SIZE=$(ls -l $FILE_NAME|awk '{print $5}')

mysql_query "insert into btk_timestamp_history values ('','$FILE_NAME', $FILE_SIZE)"
