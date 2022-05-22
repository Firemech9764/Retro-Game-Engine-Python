#this tool has been designed to create .asset text files containing graphics for frames, objects, and players
#to do- 
#  1)there are some known issues in movement part of designing, we need to keep the block fill after the pointer has been moved
#  2) there should be the option to remove the fill of a block 
#  3)allow to pick colours/ different ascii blocks or custom ascii values

import time
import os
import threading as t
import keyboard as k


class Designer: 
    
    command = ""
    save = False
    asset_name=""

    def main_screen(self):
        print("Arcade Game Engine V1.0 - Editor")
        print("\n\n\n\n\n\n 1 - Player  \n 2 - Frame\n 3 - Object\n\n\n\n")
        option = int(input("Choose Option: "))
        self.secondary_screen(option)


    def secondary_screen(self, option):
        
        if option == 2:
            os.system("clear")
            print("Arcade Game Engine V1.0 - Editor")
            print("\n\n\n\n\n")
            self.asset_name = input("Asset name: ")
            screen_width = int(input("Screen Width: "))
            screen_length = int(input("Screen height/length: "))
            os.system("clear")
            

            board = []
            arr = []
            for i in range(screen_length):
                arr=[]
                for j in range(screen_width):
                    arr.append(" ")
                board.append(arr)


            x,y = 0,0
            pointer = "+"
            
            
            def p(board,screen_length, screen_width,filled_list,y,x,f):
                os.system("clear")
                print("Arcade Game Engine V1.0 - Editor")
                print("\n\n\n")
                print("_"*(screen_width+2))
                i=-1

                while i<len(filled_list)-1:
                    i+=1
                    if filled_list[i][0]==y and filled_list[i][1]==x:
                            if f==False: 
                                board[filled_list[i][0]][filled_list[i][1]]="#"
                            else:
                                board[filled_list[i][0]][filled_list[i][1]]=" "
                    else:
                        board[filled_list[i][0]][filled_list[i][1]]="&"
                    
                for i in range(screen_length):
                    print("|"+"".join(board[i])+"|")
                print("_"*(screen_width+2))

                print("[AWSD keys format]\t[Press 'f' to fill block]")
                print("[Press 'enter', then 'p' to exit and save asset]\t[Press 'r' to remove fill]")

        
            filled_list = []
            board[y][x]="+"
            
            while True:
                
                if self.command=="a":
                    if x==0:
                        self.command=""
                    else:
                        board[y][x]=" "
                        x-=1
                        board[y][x]=pointer
                        p(board, screen_length,screen_width,filled_list,y,x, False)
                        self.command=""
                
                
                elif self.command=='d':
                    if x==screen_width-1:
                        self.command=""
                    else:
                        if board[y][x]==pointer:    
                            board[y][x]=" "
                        x+=1
                        board[y][x]=pointer
                        self.command=""
                        p(board,screen_length,screen_width,filled_list,y,x, False)


                elif self.command=="s":
                    if y==screen_length-1:
                        self.command=""
                    else:
                        if board[y][x]==pointer:
                            board[y][x]=" "
                        y+=1
                        board[y][x]=pointer
                        self.command=''
                        p(board,screen_length,screen_width,filled_list,y,x, False)
                
                elif self.command=='w':
                    if y==0:
                        self.command=""
                    else:
                        self.command=""
                        if board[y][x]==pointer:    
                            board[y][x]=" "
                        y-=1
                        board[y][x]=pointer
                        p(board,screen_length,screen_width,filled_list,y,x, False)
                
                elif self.command=="f":
                    filled_list.append([y,x])
                    self.command=""
                    p(board,screen_length,screen_width,filled_list,y,x, False)
                
                
                elif self.command=="r":    
                    self.command = ""
                    while [y,x] in filled_list:
                        filled_list.remove([y,x])
                    p(board,screen_length,screen_width,filled_list,y,x, True)


                elif self.command=="p":
                    self.save_screen(board, screen_length, screen_width, filled_list)    


    def save_screen(self, board, screen_length, screen_width, filled_list):
        os.system("clear")
        self.save=True
        print("Arcade Game Engine V1.0 - Editor")
        print("\n\n\n\n\n\n\n\n\n\n\n\n\n")
        
        print("Saving...")
        f = open((self.asset_name+".asset"), "w")
        f.write(str(screen_width))
        f.write("\n"+str(screen_length)+"\n")
        f.write(str(filled_list))
        exit()
        


    def listen(self,key):
        while True:
            incoming = str(k.read_key())
            
            if incoming[0]==key:
                self.command=key
                time.sleep(0.2)
            if self.save==True:
                exit()


designerObject = Designer()

#initialising keyboard listen functions
a = t.Thread(target = designerObject.listen, args="a")
d = t.Thread(target = designerObject.listen, args="d")
s = t.Thread(target = designerObject.listen, args="s")
w = t.Thread(target = designerObject.listen, args="w")
f = t.Thread(target = designerObject.listen, args="f")
r = t.Thread(target = designerObject.listen, args="r")
p = t.Thread(target = designerObject.listen, args="p")


a.start()
d.start()
s.start()
w.start()
f.start()
r.start()
p.start()


designerObject.main_screen()

