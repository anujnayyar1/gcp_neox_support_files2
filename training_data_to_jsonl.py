

## code to convert text file to json. Adds \\\ before each ", which may or may not be a good idea


import json 

path = '/Users/adambricknell/Desktop/gpt_neox_deployment/training_data/Training Data.txt'


# Open a file: file
file = open(path,mode='r')
 
# read all lines at once
all_of_it = file.read()
 
# close the file
file.close()



stories = ['This is the best story ever' + d for d in all_of_it.split('This is the best story ever')]
stories = stories[1:] # dropping as this first val is a delimiter


def split_by_chapter(story):
	x = story.split('Chapter 1')
	x[0] += ' Chapter 1'
	x[1] = x[1].replace("""<|endoftext|>""", '')
	x[1] = x[1].replace('"', '\\"')       
	return {'prompt':x[0], 'completion':x[1]}


prepped = [split_by_chapter(story) for story in stories]


outpath = '/Users/adambricknell/Desktop/gpt_neox_deployment/training_data/training_data.jsonl'
with open(outpath, 'w') as f:
    for item in prepped:
        f.write(json.dumps(item) + "\n")

"""
with open(outpath, 'r') as f:
	print(f.open(json.loads(item)))

"""





