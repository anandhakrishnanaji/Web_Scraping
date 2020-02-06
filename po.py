import requests
with requests.Session() as s:
    url = 'https://www.reddit.com/login/'
    uurl='https://www.reddit.com/user/anandhakris'
    payload={'loginUsername':'*type-your-user_id*','loginPassword':'*type-your-password*'}
    post = s.post(url, data=payload)
    r = s.get(uurl)
    print(r.content)
#To Run
#python3 po.py > filename.html
#firefox filename.html  
# https://pybit.es/requests-session.html
