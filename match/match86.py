






def Choose( errors, markerNum ):                                
    done = False
    errorCount = 0
    while not done:
        position = 0                                            
        for i in errors:
            if i == errorCount:
                done = True
                print( "Marker {0} has {1} errors at position {2}".format( markerNum, errorCount, position ) )
                break
            position = position + 1
        errorCount = errorCount + 1

def Test( pSequence, markers ):                                 
    pSequenceLen = len( pSequence )                             
    markerNum = 1
    for s in markers:                                           
        errors = []                                             
        markerLen = len( s )                                    
        for i in range( 0, pSequenceLen-markerLen ):            
            errorCounter = 0
            for z in range( markerLen ):
                if pSequence[i+z] != s[z]:                      
                    errorCounter = errorCounter+1
            errors.append( errorCounter )
        Choose( errors, markerNum )                             
        markerNum = markerNum + 1

def Main():
    found = False
    while not found:
        try:
            fileName = input( "Please enter the name of the file you would like to import: " )
            file = open( fileName, "r" )
            found = True
        except IOError:
            print( "Sorry, that file was not found.  Please try again." )
    
    pSequence = file.readline()                                 
    pSequence = pSequence.strip()                   
    
    markers = []                                                
    for line in file:                                           
        markers.append( line.strip() )
    
    Test( pSequence, markers )                                  
    
Main()