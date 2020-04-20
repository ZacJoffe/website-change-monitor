# website-change-monitor
A script to monitor the change of a webpage.

## Usage
The script will compare the HTML of a given page to that of itself after a default of 60 seconds. This can be changed with the optional `--sleep` flag. If the script detects a change, it will send an email to the `reveiver_gmail` from the `sender_gmail` account.

Example usage:
```
./monitor.py -e [sender_gmail] -p [sender_password] -r [receiver_gmail] --url [url_to_monitor]
```

Note that I hardcoded the Gmail SMTP servers so the scipt will add the `@gmail.com` extension to your account name. Thus, omit it in the arguments.
