import pygame, cv2, numpy

class button:

   def __init__(self, size, position, text="button", txt_colour = (0,0,0), colour = (255,255,255), hover_colour = (220, 220, 220), press_colour = (160, 160, 160)):
      self.size = size
      self.position = position
      self.text = text
      self.txt_colour = txt_colour
      self.colour = colour
      self.hover_colour = hover_colour
      self.press_colour = press_colour
   
   def mouse_over(self, mouse_pos):
      # check if the mouse is in the button area
      if self.position[0] <= mouse_pos[0] <= self.position[0]+self.size[0] and self.position[1] <= mouse_pos[1] <= self.position[1]+self.size[1]:
         return True
      else:
         return False
   
   def draw(self, mouse_pos, mouse_down, screen):

      # get the right colour for the background
      if self.mouse_over(mouse_pos):
         if mouse_down:
            bg = self.press_colour
         else:
            bg = self.hover_colour
      else:
         bg = self.colour

      # create the text surface
      font = pygame.font.Font(pygame.font.get_default_font(), 128)

      size = font.size(self.text)

      text = font.render(self.text, True, self.txt_colour)

      if size[0]/self.size[0] > size[1]/self.size[1]:
         text = pygame.transform.scale(text, self.size)
      else:
         text = pygame.transform.scale(text, self.size)
      
      # draw
      rect = pygame.Rect(self.position[0], self.position[1],self.size[0],self.size[1])
      pygame.draw.rect(screen, bg, rect)
      screen.blit(text,self.position)

class feed:
   def __init__(self, size, pos):
      self.cam = 0
      self.size = size
      self.pos = pos
      self.vid = cv2.VideoCapture(self.cam)

   def next_frame(self):
      # read frame
      ret, frame = self.vid.read()
      frame = cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
      

      # crop and scale frame
      dem = frame.shape
      
      if dem[0]/self.size[1] > dem[1]/self.size[0]:
         frame = frame[0:int(self.size[1]*dem[1]/self.size[0]), 0:dem[1]]
      else:
         frame = frame[0:dem[0], 0:int(self.size[0]*dem[0]/self.size[1])]
         
      frame = frame[0:dem[0], 0:dem[1]]
      frame = cv2.resize(frame, self.size)

      # return image
      frame = numpy.rot90(frame)
      return pygame.surfarray.make_surface(frame)
   
   def quit(self):
      self.vid.release()
   


      
def main():
   pygame.init()
   pygame.font.init()
   
   size = (1280, 720)

   screen = pygame.display.set_mode(size)

   running = True

   zone_colour = (245, 245, 245)

   # file manage zone
   file = pygame.Rect(900, 10, 370, 216)

   # settings zone
   settings = pygame.Rect(900, 236, 370, 216)

   # frame bar zone
   frames = pygame.Rect(10, 570, 1260, 140)

   # livefeed zone
   live = pygame.Rect(10, 10, 880, 550)

   # define all the buttons

   video = feed((880, 550), (10, 10))

   while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
      # Get all the mouse info
      mou_pos = pygame.mouse.get_pos()
      mou_state = pygame.mouse.get_pressed()[0]

      # draw the zone
      pygame.draw.rect(screen, zone_colour, file)
      pygame.draw.rect(screen, zone_colour, settings)
      pygame.draw.rect(screen, zone_colour, frames)
      pygame.draw.rect(screen, zone_colour, live)

      screen.blit(video.next_frame(), (10,10))
      
      pygame.display.flip()
      


if __name__ == "__main__":
   main()