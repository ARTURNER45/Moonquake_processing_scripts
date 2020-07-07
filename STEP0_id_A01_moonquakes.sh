#!/bin/bash
#---------------------
#This is a script that reads the text file that contains the list of A01 moonquakes at each station and network 
#---------------------

while read p; do
year=$(echo "$p" | awk -F' ' '{print $1}')
cent=19
date=$cent$year
day=$(echo "$p" | awk -F' ' '{print $2}'| awk '{sub ("^0*", "", $0); sub ("/0*", "/", $0); print}')
for d in $(find /Users/TheStuffofAlice/Dropbox/Apollo/$date -maxdepth 2 -type d)
do
  station=$(echo $d | awk -F"/" '{print $7}')
  comp=$(echo $d | awk -F"/" '{print $8}') 
  echo $station $comp $date $day
  dire='/Users/TheStuffofAlice/Dropbox/Apollo/A01_moonquakes/'$date'/'$station'/'$comp
  mkdir -p $dire
  fil='/Users/TheStuffofAlice/Dropbox/Apollo/'$date'/'$station'/'$comp'/'$station'.XA..'$comp'.'$date'.'$day
  cp "$fil" "$dire"	
done
done < /Users/TheStuffofAlice/Dropbox/Apollo/NAKAMURA_DATABASE/A1_moonquakes.txt


 
