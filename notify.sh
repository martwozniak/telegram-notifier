# Call notifier script
# TODO: Add messege as an argument to this script like python3 main.py "Site is down", python3 main.py "Disk space is running low"

 #!/bin/bash
 if [ "$#" -eq  "0" ]
   then 
    # Call without arguments
    # Send default error message
    python3 main.py
 else
    # Call with argument - message
    python3 main.py "$1"
    # Remember: If sentence have more than 1 word use ""
 fi



# Remember to give this script permissions
# chmod +x notify.sh

# Calling:
# ./notify.sh