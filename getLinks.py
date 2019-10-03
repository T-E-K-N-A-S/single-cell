from bs4 import BeautifulSoup
import requests
import os
  
URL = "https://support.10xgenomics.com/single-cell-gene-expression/datasets"
r = requests.get(URL) 
  
soup = BeautifulSoup(r.content, 'html.parser') 
# print(soup.prettify()) 
bd = soup.find(class_ = 'ans-body datasets')
ul = bd.find_all('ul')
a = ul[-1].find_all('a')
# os.mkdir('datasets')
bashfile = 'download_datasets.sh'
server_path = 'http://cf.10xgenomics.com/samples/cell-exp/1.1.0/'
f = open(bashfile,'w')
li = open('datasets.txt','w')
for i in a:
    d = i['href'].split('/')[-1]
    command = 'wget '+ server_path + d + '/' + d + '_raw_gene_bc_matrices.tar.gz\n'
    f.write(command)
    # os.mkdir(d)
    f.write('mkdir ' + d + '\n' )
    untar = 'tar -xzvf ' + d + '_raw_gene_bc_matrices.tar.gz --directory ' + d + '\n'
    f.write(untar)
    li.write(d + '\n')
    print(command)

