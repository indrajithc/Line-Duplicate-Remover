import sys



with open(sys.argv[1]) as f:
    content = f.readlines()




content = [x.strip() for x in content] 

filterd = []

for each in content:

	exis = False
	for eachin in filterd:
		if( each == eachin):
			exis = True
			break;

	if( not exis and len( each ) > 4 ) :
		filterd.append( each 	 )


for index, each in enumerate(filterd):
	print( index ,">>  ", each )
	

file1 = open("filterd_hash","w")#write mode 
file1.write( "\n\n".join( filterd  ) ) 
file1.close() 