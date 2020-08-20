# GPLv3 -] devBioS [- Hack the Planet!
# -------------------------------------
# This is a solver if you found the "encoded" key on the DEFCON 28 DCZIA Challenge picture.
# It is trying to rotate the "encoded part" by one, remove the 5 possible extra characters and use the two possible grid alignments of Polybius
# After that it checks if it can find english words in the deciphered text, if so it will print the result

import detectEnglish

key = "DCZIA"
try_remove_letters =["J","V","W","Q","Z"]

code="11124333112224153542441442211"
#code ="11224414424535142221133342111" #reversed
mycodelist = [char for char in code]  
def rotate(l, n):
    return l[n:] + l[:n]
def generate_grid(key,letter_to_remove):
    # letter to remove will remove the letter from the aplhabet, best choises are J V W Q Z
    # key = the KEY to inject into grid or "ABCDE" for a standard grid without cipher key
    gridtxt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    
    #remove the letters of the key:
    for keyletter in key:
        gridtxt = gridtxt.replace(keyletter, '')

    #remove the letter_to_remove
    gridtxt = gridtxt.replace(letter_to_remove, '')

    #add the key before the rest of possible letters
    gridtxt = key + gridtxt

    #split into the grid (equal to 5 parts):
    x = 5
    grid = [gridtxt[y-x:y] for y in range(x, len(gridtxt)+x,x)]
    return grid

def main():
    for remove_letter in try_remove_letters:
        grid=generate_grid(key,remove_letter)
        rot = 0
        for i in range(40):
            mycodelistrot = rotate(mycodelist,rot)
            rot +=1
            a=0
            bigram=[]
            tmpgr = []
            for i in mycodelistrot:
                tmpgr.append(i)
                a+=1
                if a == 2:
                    bigram.append(tmpgr)
                    tmpgr = []
                    a=0

            #convert in "normal way" (row then column)
            solver = []
            for bigr in bigram:
                solver.append(grid[int(bigr[0])-1][int(bigr[1])-1])    
            #print(bigram)
            #print("".join(solver))
            #print(("".join(solver)).lower())

            #convert in "unusual way" (column then row)
            solver = []
            for bigr in bigram:
                solver.append(grid[int(bigr[1])-1][int(bigr[0])-1])    
            
            #if at least 2 english words from dictionary.txt are found the result will be printed
            if detectEnglish.isEnglish("".join(solver),wordPercentage=2):
                print("".join(solver))


main()

