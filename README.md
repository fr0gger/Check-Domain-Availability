# Check-Domain-Availability
This script can be use to verify if a domain is registered or not. 

# Requirement
  ```python
  pip3 install pywhois
  ```
  
# Usage
```python
usage: checkdomain.py [-h] [-d DOMAIN] [-f FILE]

checkDomain.py by Thomas Roccia

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        Check single domain
  -f FILE, --file FILE  Check domain list
  ```
  
# Examples
```python
python3 checkdomain.py -d tot0000000crefvervcd.com
[!] tot0000000crefvervcd.com is available!

python3 checkdomain.py -f domains.txt
[+] boisehosting.net already exist!
[+] fotoideaymedia.es already exist!
[+] dubnew.com already exist!
[!] tot0000000crefvervcd.com is available!
[+] stallbyggen.se already exist!
```

# Licence
[MIT](https://github.com/fr0gger/Check-Domain-Availability/blob/main/LICENSE)
