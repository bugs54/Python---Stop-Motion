import pygame, cv2

class button:

   def __init__(self, size, position, text="button", txt_colour = (0,0,0), colour = (255,255,255), hover_colour = (220, 220, 220), press_colour = (190, 190, 190)):
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


      
def main():
   pygame.init()
   pygame.font.init()
   
   size = (1280, 720)

   screen = pygame.display.set_mode(size, pygame.RESIZABLE)

   running = True

   but = button( (100, 50), (50,50))
   while running:
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
      but.draw(pygame.mouse.get_pos(), False, screen)

      pygame.display.flip()
      


if __name__ == "__main__":
   main()