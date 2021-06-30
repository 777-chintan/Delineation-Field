#combine json files

import glob
import os
from pathlib import Path
import json
import pickle

"""
json_files_path=Path('/home/shreyans/Desktop/Agricultural-delineation/ForAfric-Agricultural-Fields-Delineation-master/data1024_part_1_2_MIX')
out_path=Path('/home/shreyans/Desktop/Agricultural-delineation/ForAfric-Agricultural-Fields-Delineation-master/data1024_part_1_2_MIX')

cocojson = {
        "info": {},
        "licenses": [],
        'categories': [{'supercategory': 'AgriculturalFields',
                        'id': 1,  # needs to match category_id.
                        'name': 'field'}]}

for f in glob.glob(os.path.join(json_files_path,"*.json")):
    print(f)
    with open(f,'r') as infile:
         coco=json.load(infile)
         for item in coco['images']:
             cocojson.setdefault('images', []).append(item)
         for item in coco['annotations']:
             cocojson.setdefault('annotations', []).append(item)

with open(os.path.join(out_path,"annotation.json"),'w') as outfile:
     json.dump(cocojson, outfile, indent=4)
     print('Writing merged json file...')
"""


inpath_pkl=Path('/home/shreyans/Desktop/Agricultural-delineation/ForAfric-Agricultural-Fields-Delineation-master/data1024_part_1_2_MIX')
outpath_pkl=Path('/home/shreyans/Desktop/Agricultural-delineation/ForAfric-Agricultural-Fields-Delineation-master/data1024_part_1_2_MIX')

chip_dfs={}
for f in glob.glob(os.path.join(outpath_pkl,"*.pkl")):
    print(f)
    with open(f,'rb') as infile:
         coco=pickle.load(infile)
         for key in coco.keys():
             chip_dfs[key]=coco[key]
    
pkl_out= outpath_pkl / 'chip_dfs.pkl'
pkl_out.parent.mkdir(parents=True, exist_ok=True)
with open(pkl_out, "wb") as f:
     pickle.dump(chip_dfs, f)
     print(f'Writing merged pickle file...')

