import subprocess

def install_package(package_name):
    try:
        subprocess.check_call(['pip', 'install', package_name])
        print(f"Successfully installed {package_name}")
    except subprocess.CalledProcessError:
        print(f"Failed to install {package_name}")
install_package('request-boost')

from request_boost import boosted_requests
param = {'accept' : 'application/json',
         'Api-Token' : 'aeda4898bc892c3707ae2ca82aaa36f4b1864ac531e7c6afaf13789af6e64dfd365ad119'}
urls = []
params = []
for i in range(0,6400,100):
    time_start = time.time()
    url = "https://fudoggroup.api-us1.com/api/3/contacts?limit=1&status=1&offset="+str(i)
    #response = requests.get(url = URL, headers = PARAMS)
    #data = response.json()
    urls.append(url)
    params.append(param)
results = boosted_requests(urls=urls, no_workers=16, max_tries=5, timeout=5, headers=params, verbose=False, parse_json=True)
