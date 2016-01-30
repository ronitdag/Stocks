#Ronit Ghosh Lab 4 72805756 Late Pass 
import urllib.request
import urllib.error
import http.client


def show_url_contents(url) -> None:
   while True:
      if len(url)==0:
         return
      else:
         return _download_and_print_url(url)
         break
      
def _download_and_print_url(url:str)->None:
   response=None
   try:
      response=urllib.request.urlopen(url)
      return _get_url_contents(response)
   except urllib.error.HTTPError as e:
      print('Filed to download contents or URL')
      print('Status code: {}'.format(e.code))
      print()
   finally:
      if response!=None:
         response.close()

def _get_url_contents(response):
   content_bytes=response.read()
   content_string=content_bytes.decode(encoding='utf-8')
   content_lines=content_string.splitlines()

   return content_lines


def _final_url_contents():
   download=show_url_contents(url)
   Date=[]
   Closing_price=[]
   Days=[]
   for i in download:
      temp=i.split(',')
      temp_Date=temp[0]
      temp_Closing=temp[4]
      Date.append(temp_Date)
      Closing_price.append(temp_Closing)
      temp_list= [Date, Closing_price]
   return temp_list

