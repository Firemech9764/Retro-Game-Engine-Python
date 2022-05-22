import time

class Window:
    
    #attributes of the window
    title="Arcade Game Engine V-1.0"
    window_width = 20
    window_length =10
    camera_movable = False
    screens=[] #each frame, at any instance will produc one screen, which would be stored here
    screen_change = False #if any screen is changed, this value will be true, so that the plot function can create a new board and pass it to draw function    
    updated_board = False #if the plot function applies the changes in the board, this will be set to true


    def find_priority(self, frames):
        output_frames = []
        l = len(frames)
        max = 0
        for i in range(l):
            for j in range(len(frames)):
                if frames[j].priority>max:
                    max = frames[j].priority
                    f = frames[j]
            frames.remove(j)
            output_frames.insert(0,j)
            max=0
        return output_frames



    # each frame in the 'frames' array will be passed through this function, this function will use
    # this function to cycle through the 'screens' attribute of each frame object, after the given updation time    
    def frames_check(self, frame, index_of_this_frame): 
        x = 0
        last_screen_index = len(frame.screen)
        while True:
            if x==last_screen_index:
                x=0
            time.sleep(frame.updation_time)
            self.screens[index_of_this_frame]=frame.screen[x]
            self.screen_change = True
            while self.updated_board==False:
                pass
            x+=1


    def draw(self,player,board,objects)




    def create_blank_board(self): # create a blank board of the required length and width
        board = [[[""]*self.window_width]]*self.window_length
        for i in range(self.window_length):
            arr=[]
            for j in range(self.window_width):
                arr.append(" ")
            board.append(arr)
        return board
        
        
    def plot(self, player, frames, objects): # creates the necessary screen at the instance in an array and then passes it to the draw function
        
        
        frames = self.find_priority(frames) # sort in ascending order all the frames on the basis of their priority values
        #lowest priority first 
        board = self.create_blank_board()


        #main loop to check if there is a change in the board
        while True:
            
            #if there is a change in the screens, create a new board and pas it to draw funciton
            if self.screen_change==True:
                board = self.create_blank_board()
                for i in self.screens:
                    for y in range(self.window_length):
                        for x in range(self.window_width):
                            board[y][x]=i[y][x]
                self.draw(player, board, objects)
            






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
    x_velocity = 0.0
    y_velocity = 0.0



class Objects:
    avatar = ""
    rigid_body = False
    x_velocity = 0.0
    y_velocity = 0.0

