#!/usr/bin/env python
# coding: utf-8

# In[1]:


theBoard = {'1': ' ' , '2': ' ' , '3': ' ',
            '4': ' ' , '5': ' ' , '6': ' ',
            '7': ' ' , '8': ' ' , '9': ' '}

def PrintBoard(Board):
    print(Board['1'] + '|' + Board['2'] + '|' + Board['3'])
    print('-+-+-')
    print(Board['4'] + '|' + Board['5'] + '|' + Board['6'])
    print('-+-+-')
    print(Board['7'] + '|' + Board['8'] + '|' + Board['9'])
    


# In[2]:


def game():
    turn = 'x'
    count = 0
    
    for i in range(10):
        
        PrintBoard(theBoard)
        print(" Its Your Turn " + turn + " Move To Which Place? ")
        move = input()
        
        if theBoard[move] == ' ':
            theBoard[move] =turn
            count +=1
        else:
            print("That place is already taken. \n Choose another place")
            continue
            
        if count >=5:

            if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(" *** " + turn + " Won. ***")
                break
                    
            elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ':
                printBoard(theBoard)
                print("\n Game Over \n")
                print(turn + "Won")
                break
                
            elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(turn + "Won")
                break
                
            elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(turn + "Won")
                break
                
            elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(turn + "Won")
                break
                
            elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(turn + "Won")
                break
                
            elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(turn + "Won")
                break
                
            elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ':
                PrintBoard(theBoard)
                print("\n Game Over \n")
                print(turn + " Won ")
                break
                
        if count==9:
            print(' \n Game Over')
            print('\n Its A Tie!')
    
        if turn =='x':
            turn = '0'
            
        else:
            turn = 'x'
        
        


# In[3]:


game()


# In[ ]:




