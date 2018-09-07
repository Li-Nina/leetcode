#!/bin/bash

symbols_pro=$(curl https://api.huobi.pro/v1/common/symbols)
pro_symbols=""

for row in $(echo ${symbols_pro//-/_} | jq -c ".data[]");do
	pro_symbols=${pro_symbols}" "$(echo ${row} | jq ".base_currency + .quote_currency")
done

actives=$(ps -ef|grep market_websocket_huobi|grep -v 'grep'|awk '{print $10}')
array=($pro_symbols)    
for each in ${array[*]}  
	do  
		item=$(echo $each | sed 's/\"//g')
		#echo $item
		if [[ ! $actives =~ $item ]];then
			cd /root/work/bitcoin/market
			nohup ./market_websocket_huobi.py $item >/dev/null 2>&1 &
			#echo "oh no!"
		fi		
   	done  


symbols_hax=$(curl https://api.hadax.com/v1/hadax/common/symbols)
hadax_symbols=""

for row in $(echo ${symbols_hax//-/_} | jq -c ".data[]");do
        hadax_symbols=${hadax_symbols}" "$(echo ${row} | jq ".base_currency + .quote_currency")
done

actives=$(ps -ef|grep market_websocket_hadax|grep -v 'grep'|awk '{print $10}')
array=($hadax_symbols)
for each in ${array[*]}
	do
                item=$(echo $each | sed 's/\"//g')
		#echo $item
                if [[ ! $actives =~ $item ]];then
			cd /root/work/bitcoin/market
                        nohup ./market_websocket_hadax.py $item >/dev/null 2>&1 &
			#echo "oh no!"
                fi
        done
