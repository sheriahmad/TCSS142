##Author Sheheryar Ahmad
##5/22/2015
##TCSS142 Spr 15

def norm(j):
	if j == '?':
		return 0.0
	else:
		return float(j)

def classify(a, ref):
	k = 0.0
	for i in range(len(ref)):
		if a[i] > ref[i]:
			k += 1
	
	if k > len(ref)/2:
		return 1.0
	else:
		return 0.0


def csvread(filename, output, testfile):
	# reading the training file lines
	lines = open(filename).read().splitlines()
	
	# number of attributes (+ healthy/ill) by splitting each line with comma (csv format)
	dim = len(lines[0].split(','))
	num = len(lines)
	
	val_h = [0.0]*(dim - 1)
	val_s = [0.0]*(dim - 1)
	l_h = 0
	l_s = 0
	l_s = l_h
	
	# calculating the number of healthy and ill patients
	for i in lines:
		if int(i[-1]) == 0:
			l_h += 1
		else:
			l_s += 1
	
	# calculating average vectors
	for i in lines:
		k = i.split(',')
		numbers = [float(j) if j != '?' else 0.0 for j in k]
		if numbers[-1] == 0.0:
			val_h = [val_h[k] + numbers[k]/l_h for k in range(dim - 1)]
		else:
			val_s = [val_s[k] + numbers[k]/l_s for k in range(dim - 1)]
	
	ref = [(i + j)/2.0 for i, j in zip(val_h, val_s)]
	
	# classification on the training set
	a = 0.0
	for i in lines:
		k = i.split(',')
		numbers = [float(j) if j != '?' else 0.0 for j in k]
		t = classify(numbers[:-1], ref)
		if (t > 0.0 and numbers[-1] > 0.0) or (t == 0.0 and numbers[-1] == 0):
			a += 1.0
	
	print("Healthy patient average : ", [round(i, 2) for i in val_h])
	print("Ill patient average : ", [round(i, 2) for i in val_s])
	print("Separator values : ", [round(i, 2) for i in ref])
	print("classification accuracy on training set : " , round(a/(l_h + l_s),2))
	
	# classification on the test set
	f = open(output, 'w')
	f.write('id,disease\n')
	lines = open(testfile).read().splitlines()
	for i in lines:
		k = i.split(',')
		numbers = [float(j) if j != '?' else 0.0 for j in k]
		f.write(str(int(numbers[0])) + ',' + str(int(classify(numbers[1:], ref))) + '\n')

def main():
	trainfile = input('Enter training set filename\n')
	testset = input('Enter test set filename\n')
	outputfile = input('Enter output filename\n')
	csvread(trainfile, outputfile, testset)

main()
norm()
classify()
csvread()

