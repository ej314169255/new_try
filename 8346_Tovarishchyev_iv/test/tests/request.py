import shutil
import requests

def discovery ():
  url = 'https://reqbin.com/echo/get/json'
  response = requests.get(url, stream=True)

  with open('sample.json', 'wb') as out_file:
    shutil.copyfileobj(response.raw, out_file)
  print('The file was saved successfully')
  return 0
