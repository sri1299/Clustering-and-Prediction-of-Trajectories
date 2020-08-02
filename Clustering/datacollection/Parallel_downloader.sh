#! /bin/bash

stt=$1
end=$2
stp=$3

stt_d=$((16#$stt));
end_d=$((16#$end));
diff_d=(`expr $end_d - $stt_d`);
echo "diff==="$diff_d;
stp_d=(`expr $diff_d / $stp `);

echo $stt_d $end_d $diff_d $stp_d;

loopvar=0;
curr_val=$stt_d;
while [ $loopvar -le $stp ];
do
	echo $curr_val $(expr $curr_val + $stp_d);
	./N.sh $curr_val $(expr $curr_val + $stp_d) & pids+=($!);
	loopvar=(`expr $loopvar + 1`);
	curr_val=(`expr $curr_val + $stp_d`);
done
echo ${pids[@]};

read $check; 

if [ $check=="kkkk" ];
then
	for i in ${pids[@]};
	do
		kill $i;
	done
fi
