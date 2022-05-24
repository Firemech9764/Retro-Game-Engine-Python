import os
import os
import threading
import time

class Window:
    
    #attributes of the window
    title="Arcade Game Engine V-1.0"
    window_width = 40
    window_length =10
    camera_movable = False
    screens=[] #each frame, at any instance will produce one screen, which would be stored here
    screen_change = False #if any screen is changed, this value will be true, so that the plot function can create a new board and pass it to draw function    
    updated_board = False #if the plot function applies the changes in the board, this will be set to true


    def find_priority(self, frames):
        return frames



    # each frame in the 'frames' array will be passed through this function, this function will use
    # this function to cycle through the 'screens' attribute of each frame object, after the given updation time    
    def frames_check(self, frame, index_of_this_frame): 
        x = 0
        last_screen_index = len(frame.screen)
        while True:
            if x==last_screen_index:
                x=0
            time.sleep(frame.updation_time)
            self.screens[index_of_this_frame]=frame.screen[x] #CHANGE zero to index_of_this frame
            self.screen_change = True
            while self.updated_board==False:
                pass
            self.updated_board=False
            x+=1
    
    def objects_check(self, o, objects):
        for i in range(len(o)):
            if o[i].x_position!=objects[i].x_position or o[i].y_position!=objects[i].y_position:
                return True
        return False


    def draw(self,player,board,objects):
        os.system("clear")
        for i in self.screens:
            for j in i:
                board[j[0]][j[1]]="&"

        #each object
        for i in objects:
            board[i.y_position][i.x_position] = i.avatar        
        
        board[player.y_position][player.x_position] = player.avatar[0]
        for i in range(self.window_length):
            print("".join(board[i]))




    def create_blank_board(self): # create a blank board of the required length and width
        board = []
        arr = []
        for i in range(self.window_length):
            arr=[]
            for j in range(self.window_width):
                arr.append(" ")
            board.append(arr)
        return board
        
        
    def plot(self, player, frames, objects): # creates the necessary screen at the instance in an array and then passes it to the draw function
        
        
        frames = self.find_priority(frames) # sort in ascending order all the frames on the basis of their priority values
        #lowest priority first 


        #inititate all the threads for handling the different frame objects through the frames_check() function
        frame_threads = []
        for i in range(len(frames)):
            frame_threads.append(threading.Thread(target=self.frames_check, args=(frames[i], i)))
            frame_threads[i].start()


        board = self.create_blank_board()
        x_position = player.x_position
        y_position = player.y_position       
        o = objects
        #main loop to check if there is a change in the board
        while True:
            #if there is a change in the screens, create a new board and pass it to draw funciton
            if self.screen_change==True:
                board = self.create_blank_board()
                self.updated_board=True

                self.draw(player, board, objects)
            if player.x_position!=x_position or player.y_position!=y_position:
                self.draw(player, board, objects)
                x_position = player.x_position
                y_position = player.y_position
            if self.objects_check(o,objects)==True:
                self.draw(player, board, objects)
                o=objects
            







class Frames:
    screen = []
    static = True
    priority = 0
    updation_time = 1 #in seconds to switch between screens of this frames, basically to achive animation


class Player:
    avatar = [] #all forms to animate
    rigid_body = False
    x_position = 0
    y_position = 0



class Objects:
    avatar = ""
    rigid_body = False
    x_position = 0
    y_position = 0
