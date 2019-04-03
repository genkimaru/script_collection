#!/bin/bash
beeline --showHeader=false --silent=true --outputformat=csv2 -u "jdbc:hive2://hive2.cioprd.local:10001/default;transportMode=http;httpPath=cliservice;principal=hive/hive2.cioprd.local@CIOPRD.LOCAL" -e " show databases;!exit ;" > databases

for database in `cat databases`
do
  {
  beeline --showHeader=false --silent=true --outputformat=csv2 -u "jdbc:hive2://hive2.cioprd.local:10001/default;transportMode=http;httpPath=cliservice;principal=hive/hive2.cioprd.local@CIOPRD.LOCAL" -e " use $database ;  show tables ; !exit ;" > ./tables/$database
  rm -rf ./schema/$database
  for table in `cat ./tables/$database`
  do
     beeline --showHeader=false --silent=true --outputformat=csv2 -u "jdbc:hive2://hive2.cioprd.local:10001/default;transportMode=http;httpPath=cliservice;principal=hive/hive2.cioprd.local@CIOPRD.LOCAL" -e "use $database ; show create table $table ;" >> ./schema/$database
  done
  }
done
