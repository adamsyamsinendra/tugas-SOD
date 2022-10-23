import sys, os
kilobytes = 1024
chunksize = int(4.5 * kilobytes)                   

def split(fromfile, todir, chunksize=chunksize): 
    if not os.path.exists(todir):                  
        os.mkdir(todir)                            
    else:
        for fname in os.listdir(todir):            
            os.remove(os.path.join(todir, fname)) 
    partnum = 0
    input = open(fromfile, 'rb')                   
    while 1:                                       
        chunk = input.read(chunksize)              
        if not chunk: break
        partnum  = partnum+1
        filename = os.path.join(todir, ('part%04d' % partnum))
        fileobj  = open(filename, 'wb')
        fileobj.write(chunk)
        fileobj.close()                            
    input.close(  )
    assert partnum <= 9999                         
    return partnum
            
if __name__ == '__main__':
    if len(sys.argv) == 2 and sys.argv[1] == '-help':
        print ('Use: split.py [file-to-split target-dir [chunksize]]')
    else:
        if len(sys.argv) < 3:
            interactive = 1
            fromfile = input('File yang akan dipisah? ')        
            todir    = input('Direktori untuk menyimpan file bagian? ')
        else:
            interactive = 0
            fromfile, todir = sys.argv[1:3]                 
            if len(sys.argv) == 4: chunksize = int(sys.argv[3])
        absfrom, absto = map(os.path.abspath, [fromfile, todir])
        print ('Splitting', absfrom, 'to', absto, 'by', chunksize)

        try:
            parts = split(fromfile, todir, chunksize)
        except:
            print ('Error Saat memisah')
        else:
            print ('Perpecahan selesai:', parts, 'bagian ada di', absto)
        if interactive: input('Tekan tombol Enter') 