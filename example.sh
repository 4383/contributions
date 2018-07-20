clear
while true
do
	for el in $(seq 0 50); do
		contributions "BADASS" <fake-repo-url> <github-user-name> <github-password-or-token> "<git-username>" <git-user-email> -t 0 --simulate  -p 0 -l ${el} -t 0 --simulate -s " "
		sleep 0.7
		clear
	done
done
