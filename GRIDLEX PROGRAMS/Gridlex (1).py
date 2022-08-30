def valid_move_or_not(piece,currentpos,nextpos):
        if piece=='Knight':
            if ord(currentpos[0])+1==ord(nextpos[0]) or ord(currentpos[0])-1==ord(nextpos[0]) and ord(currentpos[1])+2==ord(nextpos[1]) :
                return True
            elif ord(currentpos[0])+2==ord(nextpos[0]) or ord(currentpos[0])-2==ord(nextpos[0]) and ord(currentpos[1])+1==ord(nextpos[1]) :
                return True
            elif ord(currentpos[0])+2==ord(nextpos[0]) or ord(currentpos[0])-2==ord(nextpos[0]) and ord(currentpos[1])-1==ord(nextpos[1]) :
                return True
            else:
                return False
        else:
            if piece=='Bishop':
                if  currentpos[0]!=nextpos[0] and ord(currentpos[1])!=ord(nextpos[1]):
                    return True
                else:
                    return False

if __name__=='__main__':
    #you can run your tests here
    print(valid_move_or_not("Knight","a1","a2"))
