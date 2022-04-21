# takes the name of a file as command line argument
# writes the names of all crypto currencies in the first page of https://crypto.com/price in a intermediate file
# takes each line from intermediate file and extracts the corresponding USD values
# writes the values to the file provided as argument and removes the intermediate file

import os, sys, time
from threading import *
import home, currency

def main():
     star = time.time()
     if(len(sys.argv)<2):
          print("usage:")
          print("python3 <script file> <file to write the currency values to>")
          exit()

     print("---extracting currency names---")
     home.scrape()
     work = []
     rfile = open(home.wfile, 'r')
     if(sys.argv[1] in os.listdir()):
          tfile = open(sys.argv[1], 'r+')
          tfile.seek(0); tfile.truncate()
          tfile.close()
     afile = open(sys.argv[1], 'a')
     print("---extracting values and writing to file---")

     for lin in (rfile.readlines()):
          key = lin.strip('\n')
          td = Thread(target=currency.scrape(key, afile))
          work.append(td)

     for w in work:
          w.start()
          w.join()
     # to not remove the intermediate file, remove the following statement
     os.remove(home.wfile)
     print("time taken: ",round(time.time()-star)," seconds")

if __name__=='__main__':
     main()
