DEFAULT_BUCKET_SIZE=100
CHARACTERS=[" ","!",'"',"#","$","%","&","'","(",")","*","+",
            ",","-",".",'/',"0","1","2","3","4","5","6","7","8","9",
            ":",";","<","=",">","?","@","A","B","C","D","E","F",
            "G","H","I","J","K","L","M","N","O","P","Q","R",
            "S","T","U","V","W","X","Y","Z","[",'\\',"]","^","_",
            "a","b","c","d","e","f","g","h","i","j","k","l","m",
            "n","o","p","q","r","s","t","u","v","w","x","y","z",
            "{","|","}","~"]


def createTrips(txt, idx):
    trips = []
    if(idx==1):
        for i in xrange(len(txt)):
            currentTrip = ''
            if(i%3==1):
                try:
                    part2 = txt[i+1]
                except IndexError:
                    part2 = '$'
                try:
                    part3 = txt[i+2]
                except:
                    part3 = '$'
                currentTrip = txt[i] + part2 + part3 + ':' + str(i)
                trips.append(currentTrip)
        for i in xrange(len(txt)-2):
            currentTrip = ''
            if(i%3==2):
                try:
                    part2 = txt[i+1]
                except IndexError:
                    part2 = '$'
                try:
                    part3 = txt[i+2]
                except:
                    part3 = '$'
                currentTrip = txt[i] + part2 + part3 + ':' + str(i)
                trips.append(currentTrip)
    if (idx == 0):
        for i in xrange(len(txt)):
            currentTrip = ''
            if (i % 3 == 0):
                try:
                    part2 = txt[i + 1]
                except IndexError:
                    part2 = '$'
                try:
                    part3 = txt[i + 2]
                except:
                    part3 = '$'
                currentTrip = txt[i] + part2 + part3 + ':' + str(i)
                trips.append(currentTrip)
    return trips


def sortBucket():
    characters=CHARACTERS
    bucket={}
    for letter in characters:
        bucket[letter]=[]
    return bucket


#function returns list with items sorted
#in the current radix sort iteration
def getBucketItems(bucket):
    characters=CHARACTERS
    triplets=[]
    for letter in characters:
        if bucket[letter]!=[]:
            for triplet in bucket[letter]:
                triplets.append(triplet)
    return triplets


def radixSort(triplets):
    beginField=triplets
    # range(start,stop,step)
    for j in range(2,-1,-1):
        bucket=sortBucket()
        for triplet in triplets:
            # print triplet.split(":")[0][j]
            bucket[triplet.split(":")[0][j]].append(triplet)
            # print bucket
        triplets=getBucketItems(bucket)
    tIndexes=[]
    for i in range(len(triplets)):
        for j in range(len(beginField)):
            if beginField[j]==triplets[i]:
                tIndexes.append(j)
                break
    return triplets,tIndexes


if __name__=="__main__":

    allArrays = []

    tripsOneTwo = createTrips('mississippi',1)
    sortedTripsOneTwo = radixSort(tripsOneTwo)
    print sortedTripsOneTwo

    tripsZero = createTrips('mississippi', 0)
    sortedTripsZero = radixSort(tripsZero)
    print sortedTripsZero