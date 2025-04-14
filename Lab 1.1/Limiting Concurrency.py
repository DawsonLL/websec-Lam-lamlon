import requests
from bs4 import BeautifulSoup

def time_decorator(func):
  """
  Takes a function and returns a version of it that prints out the elapsed time for executing it
  :param func: Function to decorate
  :return: Function which outputs execution time
  :rtype: Function
  """
  def inner(*args, **kwargs):
      s = time.perf_counter()
      return_vals = func(*args, **kwargs)
      elapsed = time.perf_counter() - s
      print(f'Function returned: {return_vals}')
      return(elapsed)
  return(inner)

def getUrlTitle(url):
  """
    This function returns the <title> of an HTML document given its URL
    :param url: URL to retrieve
    :type url: str
    :return: Title of URL
    :rtype: str
  """
  #resp = requests.get(url)

  #resp = requests.get('https://thefengs.com/wuchang/courses/cs495/urls.txt')
  #urls = resp.text.strip().split('\n')

  resp = httpx.get('https://thefengs.com/wuchang/courses/cs495/urls.txt')
  urls = resp.text.strip().split('\n')


  soup = BeautifulSoup(resp.text,'html.parser')
  if soup.find('title'):
    return(soup.find('title').text)
  else:
    return ('')

@time_decorator # applies the decorator to the getsequential function
def getSequential(urls):
    """
    Given a list of URLs, retrieve the title for each one using a single synchronous process
    :param urls: List of URLs to retrieve
    :type urls: list of str
    :return: list of titles for each URL
    :rtype: list of str
    """
    titles = []
    for u in urls:
        titles.append(getUrlTitle(u))
    return(titles)

import time



import multiprocessing

@time_decorator
def getMulti(urls, num_processes):
    """
    Given a list of URLs, retrieve the title for each one using a single synchronous process
    :param urls: List of URLs to retrieve
    :type urls: list of str
    :param num_processes: Number of processes to use
    :type num_processes: int
    :return: list of str
    :rtype: list of str
    """
    p = multiprocessing.Pool(num_processes)
    titles = p.map(getUrlTitle, urls)
    p.close()
    return(titles)

import asyncio, httpx

async def agetUrlTitle(client, url):
    """
    This asynchronous function returns the <title> of an HTML document given its URL
    :param url: URL to retrieve
    :type client: HTTPX client
    :type url: str
    :return: Title of URL
    :rtype: str
    """
    resp = await client.get(url, follow_redirects=True)
    soup = BeautifulSoup(resp.text,'html.parser')
    if soup.find('title'):
      return(soup.find('title').text)
    else:
      return ('')

async def async_main(urls):
    async with httpx.AsyncClient(timeout=60.0) as client:
      titles = [ agetUrlTitle(client, u) for u in urls ]
      results = await asyncio.gather(*titles)
    return(results)

@time_decorator
def getAsync(urls):
    """
    Given a list of URLs, retrieve the title for each one using a single synchronous process
    :param urls: List of URLs to retrieve
    :type urls: list of str
    :return: list of str
    """
    return(asyncio.run(async_main(urls)))

if __name__ == '__main__':
    '''
    concurrencies = [10, 5, 2]

    for c in concurrencies:
    fetch_time = getMulti(urls,c)
    print(f'{c} {fetch_time:0.2f}')
    '''
    resp = httpx.get('https://thefengs.com/wuchang/courses/cs495/urls.txt')
    urls = resp.text.strip().split('\n')
    concurrencies = [25, 20, 15, 10, 5, 2, 1]
    elapsed = []
    for concurrency in concurrencies:
        total_time = 0
        for i in range(0,len(urls),concurrency):
            fetch_time = getAsync(urls[i:i+concurrency])
            total_time += fetch_time
    elapsed.append(total_time)
    print(f'Async version {concurrency}: {total_time:0.2f}')

    print(list(zip(concurrencies, elapsed)))

import matplotlib.pyplot as plt

plt.scatter(concurrencies, elapsed)
plt.title("Personalize title using your OdinId")
plt.xlabel("Number of Concurrent Requests")
plt.ylabel("Retrieval Time")
plt.show()