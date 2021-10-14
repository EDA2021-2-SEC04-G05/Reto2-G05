import csv
import config as cf

artworksfile = cf.data_dir.replace("\\","/") + '/Artworks-utf8-small.csv'
input_file = csv.DictReader(open(artworksfile,encoding= 'utf-8')) 
for artworks in input_file:
    print(artworks.keys())