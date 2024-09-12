#!/bin/bash

# init proj specific variables
dataset="/home/data/NDClab/datasets/thrive-dataset"
childdata="true"
[[ $childdata == true ]] && childdata="true"

# determine if sourcedata/raw has session folders, reproduce session+run structure in checked
ses_re='^s[0-9]+_r[0-9]+$'
ses_names=()
for i in $(find $dataset/sourcedata/raw -maxdepth 1 -type d); do
  if [[ $(basename $i) =~ $ses_re ]]; then ses_names+=($(basename $i)/); fi
done
IFS=$'\n' && ses_names=($(sort <<<"${ses_names[*]}")) && unset IFS
[[ ${#ses_names[@]} -eq 0 ]] && ses_names="none"

# load in functions & variables
source /home/data/NDClab/tools/lab-devOps/scripts/monitor/tools.sh

usage() { echo "Usage: sh hallMonitor.sh [-m/-r] [string list of replacement or mapping]" 1>&2; exit 1; }

echo "checking that the data dictionary is up to date since last setup"
output=$( python ${dataset}/data-monitoring/check-datadict.py $dataset)
echo -e "$output"

echo "calling verify-copy.py"
output=$( python ${dataset}/data-monitoring/verify-copy.py $dataset)
echo -e "$output"


error_detected=false

for ses in ${ses_names[@]}
do
	[[ $ses == "none" ]] && ses="" # if no session directories set ses to empty
	if [ ! -d $raw/${ses}redcap ]; then
		echo "No redcap folder found in $raw/$ses directory"
                redcaps=("")
	else
		echo "Accessing $raw/${ses}redcap"
		# if redcap does not exist in checked, create it
		if [ ! -e "$check/redcap" ]; then
			mkdir -p $check/redcap
		fi

		# store file names in array and get most recent file, check if stem is correct
		redcaps=($( get_new_redcaps $raw/${ses}redcap ))
		for redcap_file in ${redcaps[@]}; do
			if [[ "$redcap_file" =~ "Error:" ]]; then
				echo -e "$redcap_file"
				echo -e "\t ${RED}Error detected in redcap. View above${NC}"
				error_detected=true
				continue
			fi
			echo -e "\t Newest Redcap found: $redcap_file"
			
			# move only if data does not already exist in checked
                        cmp --silent "$raw/${ses}redcap/$redcap_file" "$check/redcap/$redcap_file"
                        same_file=$(echo $?)
			if [ -f "$check/redcap/$redcap_file" ] && [ $same_file -eq 0 ]; then
				echo -e "\t redcap/$redcap_file already exists in checked, skipping copy \n"
				continue
			fi

			echo -e "\t ${GREEN}Data passes criteria${NC}"


			echo -e "\t copying $redcap_file to $check/$dir"
			cp $raw/${ses}redcap/$redcap_file $check/\redcap

		# rename columns in checked using replace or map
			while getopts ":rm" opt; do
				case ${opt} in
				r)
					python ${dataset}/data-monitoring/rename-cols.py $check/$dir/$redcap_file "replace" $2 ;;
				m)
					python ${dataset}/data-monitoring/rename-cols.py $check/$dir/$redcap_file "map" $2 ;;
				:)
				esac 
			done
		done
	fi

        if [[ ! ${redcaps[*]} == "" ]]; then
	    echo "updating tracker, ses: $ses, redcaps: ${redcaps[*]}"
            command=$(echo "echo $raw/${ses}redcap/{$(echo ${redcaps[*]} | sed 's/ /,/g')}")
            redcap_files=$(eval $command); redcap_files=${redcap_files// /,} # comma separated list of redcaps in optional session folder
            [[ ${redcaps[*]} == "" ]] && redcap_files=none
            [[ $ses == "" ]] && ses="none"
            if [[ $ses == "none" ]]; then
	        # update trackers
	        output=$( python ${dataset}/data-monitoring/update-tracker.py "${check}" $dataset $redcap_files $ses $childdata)
                echo "args: ${dataset}/data-monitoring/update-tracker.py "${check}" $dataset $redcap_files ${ses} $childdata"
                echo -e "$output"
            else
                echo "checking redcaps in session folder ${ses:0:-1}"
                output=$(check_redcaps_in_right_session_folders ${ses:0:-1} ${redcap_files})
                [[ $? == 1 ]] && echo "$output" && exit 1
	        ses_re='^.*'${ses:0:-1}'.*$'
	        output=$( python ${dataset}/data-monitoring/update-tracker.py "${check}" $dataset $redcap_files ${ses:0:-1} $childdata)
		echo "args: ${dataset}/data-monitoring/update-tracker.py "${check}" $dataset $redcap_files ${ses:0:-1} $childdata"
                echo -e "$output"
	    fi
            output=$( python ${dataset}/data-monitoring/check_existence_datatype_folders.py $dataset $redcap_files ${ses:0:-1})
            echo -e "$output"
        fi

done

