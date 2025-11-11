import pygame
import random
import os

class ScreenShot():
    def __init__(self): #inititate the class
        pygame.init()
        self.infoObject = pygame.display.Info() #check screen resolution
        print("If you are deploying online, please input 1. If you are deploying in person on this device, please input 2. In other cases, the size of your vignettes may be inappropriate.")
        while True:
            answer = int(input())
            if answer == 1:
                self.window_factor = 1
                break
            if answer == 2:
                self.window_factor = self.infoObject.current_h/1080
                break
        self.window_height =(722-141)*self.window_factor
        self.window_width = 900*self.window_factor
        self.line_width = self.window_width-175
        self.window = pygame.display.set_mode((self.window_width, self.window_height)) #game window
        self.black = (0, 0, 0, 255) #colours used in the game, based on rgb values
        self.gold = (255, 215, 0, 255)
        self.tan = (210, 180, 140, 255)
        self.orange = (255, 165, 0, 255)
        self.crimson = (220, 20, 60, 255)
        self.lightslateblue = (132, 112, 255, 255)
        self.cadetblue2 = (142, 229, 238, 255)
        self.dodgerblue = (30, 144, 255, 255)
        self.lightsteelblue = (176, 196, 222, 255)
        self.navyblue = (0, 0, 128, 255)
        self.cornflowerblue = (100, 149, 237, 255)
        self.royalblue3 = (58, 95, 205, 255)
        self.tomato = (255, 99, 71, 255)
        self.forestgreen = (34, 139, 34, 255)
        self.green = (0, 255, 0, 255)
        self.darkolivegreen3 = (162, 205, 90, 255)
        self.gainsboro = (220, 220, 220, 255)
        self.white = (255, 255, 255, 255)
        self.purple = (160, 32, 240, 255)
        self.arial = pygame.font.Font("fonts/calibril.ttf", int(26*self.window_factor)) #fonts for text shown to players
        self.arial2 = pygame.font.Font("fonts/calibril.ttf", int(24*self.window_factor))
        self.combinations = []
        self.character_count_list = []
        self.character_keys = []
        self.names = ["Grant Wells","Jacob Flynn","Bryan Short","Ethan Blake","Lucas Drake","Mason Brock","Caleb Hayes","Dylan Frost","Henry Shaw","Oscar Nash","Logan Miles","Aaron Quinn","Simon Craig","Travis Holt","Jasper Reed","Gavin Stone","Riley Burns","Jason Kemp","Tobias Hart","Brett Vaughn"]
    def choose_school_conditions(self): #different school combinations chosen
        final_list = []
        with open("randomised_list.txt") as file:
            for line in file:
                line1 = line.rstrip()
                final_list.append(line1)
        for i in final_list:
            res = eval(i)
            self.combinations.append(res)

    def text_into_paragraph(self, key): #convert base text into unique texts for each school/condition combination
        self.character_count = 0
        random.shuffle(self.names)
        name = self.names[0]
        school = key[1]
        path = f"vignette texts/{key[0]}.txt"
        f = open(path, "r")
        text = f.read()
        paragraphs = []
        characters = ""
        for i in text: #read the text; special characters used to insert names and breaks
            if i == "*":
                paragraphs.append(characters)
                self.character_count += len(characters)
                characters = ""
            elif i == "#":
                characters += school
            elif i == "&":
                characters += name
            else:
                characters += i
        paragraphs.append(characters)
        self.character_count += len(characters)
        paragraph_words = []
        for i in paragraphs: #separate the paragraphs into individual words
            word = ""
            count = 0
            words = []
            for u in i:
                count += 1
                if u != " ":
                    word += u
                if u == " " or count == len(i):
                    words.append(word)
                    word = ""
            paragraph_words.append(words)
        x = 25
        y = 25
        lines = []

        previous = ""
        for i in paragraph_words[0]: #paragraph 1; break the lines so they do not go over the edges
            test_arial = previous
            test_arial += i
            line = self.arial.render(test_arial, True, self.black)
            length = line.get_width()
            if length < self.line_width:
                previous = test_arial + " "
            if length >= self.line_width:
                lines.append((line, (x+5, y+5)))
                y += 30*self.window_factor
                previous = ""
        if length < self.line_width:
            lines.append((line, (x+5, y+5)))
            y += 30*self.window_factor
        y += 10*self.window_factor



        previous = ""
        for i in paragraph_words[1]: #paragraph 2
            test_arial = previous
            test_arial += i
            line = self.arial.render(test_arial, True, self.black)
            length = line.get_width()
            if length < self.line_width:
                previous = test_arial + " "
            if length >= self.line_width:
                lines.append((line, (x+5, y+5)))
                y += 30*self.window_factor
                previous = ""
        if length < self.line_width:
            lines.append((line, (x+5, y+5)))
            y += 30*self.window_factor
        y += 20*self.window_factor


        previous = ""
        for i in paragraph_words[2]: #paragraph 3
            test_arial = previous
            test_arial += i
            line = self.arial2.render(test_arial, True, self.black)
            length = line.get_width()
            if length < self.line_width:
                previous = test_arial + " "
            if length >= self.line_width:
                lines.append((line, (x+5, y+5)))
                y += 30*self.window_factor
                previous = ""
        if length < self.line_width:
            lines.append((line, (x+5, y+5)))
            y += 30*self.window_factor
        y += 20*self.window_factor


        previous = ""
        for i in paragraph_words[3]: #paragraph 4
            test_arial = previous
            test_arial += i
            line = self.arial2.render(test_arial, True, self.black)
            length = line.get_width()
            if length < self.line_width:
                previous = test_arial + " "
            if length >= self.line_width:
                lines.append((line, (x+5, y+5)))
                y += 30*self.window_factor
                previous = ""
        if length < self.line_width:
            lines.append((line, (x+5, y+5)))
            y += 30*self.window_factor
        y += 20*self.window_factor

        previous = ""
        for i in paragraph_words[4]: #paragraph 5
            test_arial = previous
            test_arial += i
            line = self.arial2.render(test_arial, True, self.black)
            length = line.get_width()
            if length < self.line_width:
                previous = test_arial + " "
            if length >= self.line_width:
                lines.append((line, (x+5, y+5)))
                y += 30*self.window_factor
                previous = ""
        if length < self.line_width:
            lines.append((line, (x+5, y+5)))
            y += 30*self.window_factor
        y += 20*self.window_factor

        self.window.fill(game.white)

        for i in lines: #draw the vignettes
            self.window.blit(i[0], i[1])

        pygame.display.update()
        try: #remove old files
            os.remove(f"images/{key[0]}_{key[1]}.png")
            print(f"file removed: {key[0]}_{key[1]}.png")
        except FileNotFoundError:
            print(f"file not found: {key[0]}_{key[1]}.png")
        
        pygame.image.save(self.window, f"images/{key[0]}_{key[1]}.png") #save new image
        print(f"image created: {key[0]}_{key[1]}.png")
game = ScreenShot()
game.choose_school_conditions()
game.text_into_paragraph(("vignette_placeholder", "Green High"))
count = 0
checked_combinations = []
for e in game.combinations: #create text for each unique combination
    for i in e:
        if i not in checked_combinations:
            count += 1
            game.text_into_paragraph(i)
            checked_combinations.append(i)
            game.character_count_list.append(game.character_count)
            game.character_keys.append(i)
average_characters = (sum(game.character_count_list))/len(game.character_count_list) #check character length, within 5% of mean character count
tolerance = 0.05*average_characters
tolerance_minumum = average_characters-tolerance
tolerance_maximum = average_characters+tolerance
print(tolerance)
vignette_spot = 0
print(f"Average character count: {average_characters}")
too_high_list = []
too_low_list = []
for i in game.character_count_list:
    if i < tolerance_minumum:
        print("vignette too low")
        too_low = game.character_keys[vignette_spot][0]
        if too_low not in too_low_list:
            too_low_list.append(too_low)

    if i > tolerance_maximum:
        print(i)
        print(tolerance_maximum)
        print("vignette too high")
        too_high = game.character_keys[vignette_spot][0]
        if too_high not in too_high_list:
            too_high_list.append(too_high)
    vignette_spot += 1
if len(too_high_list) == 0:
    print("no vignettes are too long")
else:
    print(too_high_list)
if len(too_low_list) == 0:
    print("no vignettes are too short")
print(too_low_list)
print(f"total vignettes: {count}")
pygame.quit()
