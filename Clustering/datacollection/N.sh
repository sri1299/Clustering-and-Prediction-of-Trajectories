#! /bin/bash

a={0,1,2,3,4,5,6,7,8,9,a,b,c,d,e,f};
echo $a;

stt=$1
end=$2

loopvar=$stt;

while [ $loopvar -le $end ];
do
	hform=$(printf '%x' $loopvar);
	echo $hform;
	node index.js $hform; 
	loopvar=`expr $loopvar + 1`;
done

