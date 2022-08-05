rm build/*.aux build/*.log build/*.synctex.gz

for dest_dir in "statistics_program", "basic_probability_problems"
do
	for f in $(ls ${dest_dir}/*.pdf)
	do
		f_name=$(basename "${f}")
		(cmp "build/${f_name}" "${dest_dir}/${f_name}" > dev/null) || (cp "build/${f_name}" "${dest_dir}/${f_name}" && echo "${f_name} moved")
	done
done

