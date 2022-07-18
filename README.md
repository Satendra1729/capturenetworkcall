# capturenetworkcall Sample command 
python Script.py -u https://www.google.com/ -e www.google.com/

Sample command will print the request object of url which ends with "www.google.com/". 

e.g. 
Request(method='GET', url='https://www.google.com/', headers=[('user-agent', 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:102.0) Gecko/20100101 Firefox/102.0'), ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8'), ('accept-language', 'en-US,en;q=0.5'), ('accept-encoding', 'gzip, deflate, br'), ('upgrade-insecure-requests', '1'), ('sec-fetch-dest', 'document'), ('sec-fetch-mode', 'navigate'), ('sec-fetch-site', 'none'), ('sec-fetch-user', '?1'), ('te', 'trailers')], body=b'')

