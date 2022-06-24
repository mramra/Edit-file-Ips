try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse
    
name=input("Enter Name File Ips:")
fin = open(name, "rt")
#output file to write the result to
fout = open("out.txt", "wt")
#for each line in the input file
for line in fin:
	#read replace the string and write to output file 
    parsed = urlparse(line)
    if parsed.port==None:
        if parsed.scheme=='http':
            fout.write(line.replace(line,line.strip()+":80\n"))
        else:
            fout.write(line.replace(line,line.strip()+":443\n"))
    else:
        fout.write(line)
#close input and output files
fin.close()
fout.close()