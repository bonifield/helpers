### Files
- bash-array-comparison.sh
	- How to compare two arrays in Bash
- bash-array-usage.sh
	- Examples of working with Bash arrays
- bash-checks-comparisons.sh
- 	- Various comparisons and equality checks
- bash-getopts.sh
	- Uses Bash cases to add switch functionality to scripts
- bash-if-while-for-functions.sh
	- Examples of Bash if/elif/else, while, and for statements in both functions and one-liners
- bash-yesno.sh
	- Simple Yes/No comparison check, accounting for case

---

| Variable | Description |
| --- | --- |
| $0 | name of current script |
| $1 - $9 | first nine script arguments |
| $# | count of arguments |
| $@ | all arguments |
| $? | exit status of most recent process |
| $$ | process ID of running script |
| $USER | current username |
| $HOSTNAME | machine hostname |
| $RANDOM | a random number |
| $LINENO | current line number |

---

| Operator | True If |
| --- | --- |
| !EXPRESSION | The EXPRESSION is false. |
| -n STRING | STRING length is greater than zero |
| -z STRING | The length of STRING is zero (empty) |
| STRING1 != STRING2 | STRING1 is not equal to STRING2 |
| STRING1 = STRING2 | STRING1 is equal to STRING2 |
| INTEGER1 -eq INTEGER2 | INTEGER1 is equal to INTEGER2 |
| INTEGER1 -ne INTEGER2 | INTEGER1 is not equal to INTEGER2 |
| INTEGER1 -gt INTEGER2 | INTEGER1 is greater than INTEGER2 |
| INTEGER1 -lt INTEGER2 | INTEGER1 is less than INTEGER2 |
| INTEGER1 -ge INTEGER2 | INTEGER1 is greater than or equal to INTEGER 2 |
| INTEGER1 -le INTEGER2 | INTEGER1 is less than or equal to INTEGER 2 |
| -d FILE | FILE exists and is a directory |
| -e FILE | FILE exists |
| -r FILE | FILE exists and has read permission |
| -s FILE | FILE exists and it is not empty |
| -w FILE | FILE exists and has write permission |
| -x FILE | FILE exists and has execute permission |
