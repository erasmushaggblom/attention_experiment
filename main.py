import random
import asyncio
import pygame
import sys #used to define the code platform for API requests

class EyeTracker(): #create calss for tasks in the experiment
    def __init__(self): #inititate the class
        pygame.init()
        random.seed()
        self.clock = pygame.time.Clock() #function to advance time
        self.roundnumber = 0
        self.roundstandard = 10
        self.time = 0
        self.vignette_time = 0
        self.vignette_timer = 0 #how much time is spent in a given vignette before the buttons to choose an action are shown
        self.infoObject = pygame.display.Info()
        self.is_emscripten = sys.platform == "emscripten"
        if not self.is_emscripten:
            self.window_multiplier = self.infoObject.current_h/1080
            print("not ems")
        else:
            self.window_multiplier = 1
            print("ems")
        self.window_height = 1080*self.window_multiplier #height of game window
        self.window_width = 1920*self.window_multiplier #width of game window
        self.board = []
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
        self.schoolranking = [0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 ]
        self.historical_rankings = [] #list of historical rankings
        self.choice_area_height = self.window_height/3.5 #height of the area reserved for policy choice screen
        self.choice_area_width = self.window_width-((self.window_width)/2)
        self.performance_information_box_height = self.window_height-self.choice_area_height-50
        self.performance_information_box_width = self.window_width/2-60
        self.vignette_button_width = self.window_width/4.16
        self.vignette_button_height = self.window_height/10
        self.vignette_buttons_1 = []
        self.vignette_buttons_2 = []
        self.option_choice = None
        self.option_chosen = False
        self.click_counter = 0
        self.button_clicked = False
        self.button_chosen = None
        self.show_vignette_buttons = False
        self.vignette_locations = []
        self.arial = pygame.font.Font("fonts/calibril.ttf", int(23*self.window_multiplier)) #fonts for text shown to players, four fonts in use currently
        self.arial2 = pygame.font.Font("fonts/calibril.ttf", int(24*self.window_multiplier))
        self.vignettes = []
        self.chosen_vignettes = []
        self.vignette_number = 0
        self.show_performance_information = False
        self.show_introduction = True
        self.show_end_round_screen = False
        self.show_postgame = False
        self.options = []
        self.choice_made = False
        self.school1 = None
        self.school2 = None
        self.vignette_choices = []
        self.participant = 1
        self.vignette1 = None
        self.vignette2 = None
        self.current_choice1 = []
        self.current_choice2 = []
        self.randomisation_done = False
        self.counter = 0    
        self.multiple_choice_school = None
        self.multiple_choice_vignette = None
        self.multiple_choice_logo = None
        self.logo1 = None
        self.logo2 = None
        self.multiple_choice_made = False
        self.multiple_choice_correct = False
        self.multiple_choices = []
        self.multiple_choice_true_statement = None
        self.show_logo = True





    def finish_game(self): #finish the game
        self.add_final_output()
        self.rename_output()
        raise SystemExit

    def choose_school_conditions(self):
        final_list = []
        with open("randomised_list.txt") as file:
            for line in file:
                line1 = line.rstrip()
                final_list.append(line1)
        seed = random.randrange(0, 301)
        used_list = final_list[seed]
        res = eval(used_list)
        self.school_conditions = res

    def draw_game_board(self): #draw different game areas
        pygame.draw.rect(self.window, self.purple, self.board[0])
        pygame.draw.rect(self.window, self.forestgreen, self.board[1])
        pygame.draw.rect(self.window, self.forestgreen, self.board[2])
        pygame.draw.rect(self.window, self.tan, self.board[3])
        pygame.draw.rect(self.window, self.tan, self.board[4])


    def create_game_board(self): #create areas in the game that can be individually updated
        rect1 = pygame.Rect(self.window_width-((self.window_width)/2)-10, 0, 20, self.window_height-self.choice_area_height) # bar separating left and right screens
        rect2 = pygame.Rect(0, self.window_height-self.choice_area_height, self.choice_area_width, self.choice_area_height) #left policy choice screen
        rect3 = pygame.Rect(self.window_width/2, self.window_height-self.choice_area_height, self.choice_area_width, self.choice_area_height) #right policy choice screen
        rect4 = pygame.Rect(25, 5, self.performance_information_box_width, self.performance_information_box_height) #left performance information box
        rect5 = pygame.Rect(self.window_width/2+35, 5, self.performance_information_box_width, self.performance_information_box_height) #right performance information box
        self.board.append(rect1)
        self.board.append(rect2)
        self.board.append(rect3)
        self.board.append(rect4)
        self.board.append(rect5)

        self.vignette_locations.append(rect4)
        self.vignette_locations.append(rect5)

    def draw_vignette(self):
        self.multiple_choice_made = False
        texts = self.chosen_vignettes[self.vignette_number][0]
        self.school1 = self.chosen_vignettes[self.vignette_number][2][0]
        self.school2 = self.chosen_vignettes[self.vignette_number][2][1]
        if self.randomisation_done == False:
            self.create_vignette_buttons()
        vignette1_name = self.chosen_vignettes[self.vignette_number][3][0]
        vignette2_name = self.chosen_vignettes[self.vignette_number][3][1]
        self.vignette1 = vignette1_name
        self.vignette2 = vignette2_name
        if self.show_logo == True:
            logo1 = pygame.image.load(f"images/{self.school1}.png")
            logo2 = pygame.image.load(f"images/{self.school2}.png")

            logo1_width = logo1.get_width()

            self.logo1 = logo1
            self.logo2 = logo2

        vignette1 = pygame.image.load(f"images/{vignette1_name}_{self.school1}.png")
        vignette2 = pygame.image.load(f"images/{vignette2_name}_{self.school2}.png")
        texts1 = [texts[0]]
        texts2 = [texts[1]]
        count = 0
        for i in self.vignette_locations:
            text_start_x = i[0]
            text_start_y = i[1]
            if count == 0:
                self.window.blit(vignette1, (text_start_x, text_start_y+141))
                if self.show_logo == True:
                    self.window.blit(logo1, (text_start_x+self.performance_information_box_width-logo1_width, text_start_y))
                y = text_start_y+20
                for u in texts1:
                    for e in u:
                        self.window.blit(e, (text_start_x+5, y))
                        y += 30

            else:
                self.window.blit(vignette2, (text_start_x, text_start_y+141))
                if self.show_logo == True:
                    self.window.blit(logo2, (text_start_x+self.performance_information_box_width-logo1_width, text_start_y))
                y = text_start_y+20
                for u in texts2:
                    for e in u:
                        self.window.blit(e, (text_start_x+5, y))
                        y += 30
            count += 1


    def create_vignette_buttons(self):
        self.vignette_buttons_1 = []
        extra_space = (self.window_width-(self.vignette_button_width*4))/5
        self.vignette_buttons_2 = []
        check_spot = self.window_height-self.choice_area_height+20+self.vignette_button_height*0.8
        extra_height = (self.window_height-(self.window_height-(self.window_height-check_spot))-self.vignette_button_height)/2
        new_spot = check_spot+extra_height


        rect3 = pygame.Rect(extra_space, new_spot, self.vignette_button_width, self.vignette_button_height) # bar separating left and right screens
        text_label3 = f"Commend {self.school1} for their performance"
        text3 = self.arial2.render(text_label3, True, self.black)
        rect4 = pygame.Rect(extra_space*2+self.vignette_button_width, new_spot, self.vignette_button_width, self.vignette_button_height) # bar separating left and right screens
        text_label4 = f"Warn {self.school1} about their performance"
        text4 = self.arial2.render(text_label4, True, self.black)
        rect7 = pygame.Rect(extra_space*3+self.vignette_button_width*2, new_spot, self.vignette_button_width, self.vignette_button_height) # bar separating left and right screens
        text_label7 = f"Commend {self.school2} for their performance"
        text7 = self.arial2.render(text_label7, True, self.black)
        rect8 = pygame.Rect(extra_space*4+self.vignette_button_width*3, new_spot, self.vignette_button_width, self.vignette_button_height) # bar separating left and right screens
        text_label8 = f"Warn {self.school2} about their performance"
        text8 = self.arial2.render(text_label8, True, self.black)
        self.vignette_buttons_1.append((rect3, text3, text_label3))
        self.vignette_buttons_1.append((rect4, text4, text_label4))
        self.vignette_buttons_2.append((rect7, text7, text_label7))
        self.vignette_buttons_2.append((rect8, text8, text_label8))

        self.randomise_button_options()

    def randomise_button_options(self):
        pass

    def click_box(self, x: int, y: int, box: pygame.rect): #checks if a click by the player is in a rectangle
        points_in_boxx = []
        points_in_boxy = []
        boxx = box[0]
        boxy = box[1]
        boxwidth = box[2]
        boxheight = box[3]
        count = 0
        for i in range(boxwidth):
            points_in_boxx.append(boxx+i)
        for i in range(boxheight):
            points_in_boxy.append(boxy+i)
        for i in points_in_boxx:
            if x == i:
                count += 1
        for i in points_in_boxy:
            if y == i:
                count += 1
        if count == 2:
            return True
        return False 
    

    def click_circle(self, x: int, y: int, circle: tuple): #checks if a click by the player is in a circle
        circlex = circle[0]
        circley = circle[1]
        radius = circle[2]
        if abs(x - circlex) < radius and abs(y - circley) < radius:
            return True
        return False

    def draw_vignette_buttons(self):
        if self.choice_made == False:
            box_width = self.vignette_button_width*3
            box_height = self.vignette_button_height*0.8
            x = (self.choice_area_width*2-box_width)/2
            y = self.window_height-self.choice_area_height+20
            rect1 = pygame.Rect(x, y, box_width, box_height)
            pygame.draw.rect(self.window, self.gainsboro, rect1)

            text_label = f"Please choose one action to perform for either {self.school1} or {self.school2} by clicking on it"
            text = self.arial2.render(text_label, True, self.black)
            coords = self.center_text(text, box_width, box_height, x, y)
            self.window.blit(text, coords)

            for i in self.vignette_buttons_1:
                text = i[1]
                x = i[0][0]
                y = i[0][1]
                coords = self.center_text(text, self.vignette_button_width, self.vignette_button_height, x, y)
                pygame.draw.rect(self.window, self.gold, i[0])
                self.window.blit(text, coords)

            for i in self.vignette_buttons_2:
                text = i[1]
                x = i[0][0]
                y = i[0][1]
                coords = self.center_text(text, self.vignette_button_width, self.vignette_button_height, x, y)
                pygame.draw.rect(self.window, self.gold, i[0])
                self.window.blit(text, coords)


    def center_text(self, text, canvas_width, canvas_height, x, y):
            text_width = text.get_width()
            extra = canvas_width-text_width
            text_position_x = x+extra/2
            text_height =text.get_height()
            extra = canvas_height-text_height
            text_position_y = y+extra/2

            return (text_position_x, text_position_y)

    def create_vignettes(self):
        count = 1
        for i in self.school_conditions:
            condition = i[0]
            school = i[1]
            vignette_label = f"Vignette {count}"
            count += 1
            text1 = self.arial.render(f"A school performance report for {school} is presented below.", True, self.black)
            text3 = self.arial.render(f"Please familiarise yourself with the report.", True, self.black)
            if condition == "narrative_historical_negative_1" or condition == "narrative_historical_negative_2" or condition == "narrative_historical_positive_1" or condition == "narrative_historical_positive_2": 
                text2 = self.arial.render(f"The report concerns the experiences of a student over ten years.", True, self.black)
            if condition == "narrative_relative_negative_1" or condition == "narrative_relative_negative_2" or condition == "narrative_relative_positive_1" or condition == "narrative_relative_positive_2": 
                text2 = self.arial.render(f"The report concerns the experiences of a student compared to other schools.", True, self.black)
            if condition == "statistical_historical_negative_1" or condition == "statistical_historical_negative_2" or condition == "statistical_historical_positive_1" or condition == "statistical_historical_positive_2": 
                text2 = self.arial.render(f"The report concerns the performance of the school over ten years.", True, self.black)
            if condition == "statistical_relative_negative_1" or condition == "statistical_relative_negative_2" or condition == "statistical_relative_positive_1" or condition == "statistical_relative_positive_2": 
                text2 = self.arial.render(f"The report concerns the performance of the school compared to other schools.", True, self.black)
            if condition == "no_comparison_1" or condition == "no_comparison_2": 
                text2 = self.arial.render(f"The report concerns the results of students at the school in different subjects.", True, self.black)
            if condition == "no_comparison_3" or condition == "no_comparison_4": 
                text2 = self.arial.render(f"The report concerns a student's experiences at the school.", True, self.black)
            


            vignette_content = [text1, text2, text3]
            self.vignettes.append((vignette_content, vignette_label))

    def choose_cases(self):
        number = int(len(self.vignettes)/2)
        self.roundstandard = number
        for i in range(number):
            vignette1 = self.school_conditions[i][0]
            vignette2 = self.school_conditions[i+number][0]
            vignette1_school = self.school_conditions[i][1]
            vignette2_school = self.school_conditions[i+number][1]
            vignette1_text = self.vignettes[i][0]
            vignette1_label = self.vignettes[i][1]
            vignette2_text = self.vignettes[i+number][0]
            vignette2_label = self.vignettes[i+number][1]
            self.chosen_vignettes.append(((vignette1_text, vignette2_text), (vignette1_label, vignette2_label), (vignette1_school, vignette2_school), (vignette1, vignette2)))
        random.shuffle(self.chosen_vignettes)
        self.vignette_order = []
        for i in self.chosen_vignettes:
            schools = i[2]
            vignettes = i[3]
            self.vignette_order.append((schools, vignettes))

    def rename_output(self): #renames the output file to an unique name
        filename = f"participant_{self.participant}"
        lines = []
        with open("output/output_file.txt") as original_file:
            for i in original_file:
                lines.append(i)
        with open(f"output/{filename}.txt", "w") as new_file:
            for i in lines:
                new_file.write(i)

    def create_output_file(self): #creates the output file, currently as a .txt file
        with open("output/output_file.txt", "w") as my_file:
            my_file.write(f"Participant {self.participant}")
            my_file.write("\n")

    def add_to_output(self, text):
        with open("output/output_file.txt", "a") as my_file:
            my_file.write(f"{text}")
            my_file.write("\n")

    def add_final_output(self): #adds final notes to the output file
        with open("output/output_file.txt", "a") as my_file:
            my_file.write(f"school and vignette order: {self.vignette_order}")
            my_file.write("\n")
            my_file.write(f"options chosen: {self.vignette_choices}")
            my_file.write("\n")
            my_file.write(f"multiple choices: {self.multiple_choices}")
            my_file.write("\n")

    def check_participant_number(self): #checks the number of participants
        count = 0
        words2 = []
        try:
            with open("output/output_file.txt") as my_file:
                for i in my_file:
                    text = i
                    count += 1
                    if count == 1:
                        break
        except FileNotFoundError:
            return
        words = text.split(" ")
        for i in words:
            words2.append(i.strip())
        participant_number = int(words2[1])
        if self.participant <= participant_number:
            participant_number += 1
            self.participant = participant_number

    def increase_click_counter(self): #tracks how many inputs have been made by the player
        mouse_presses = pygame.mouse.get_pressed()
        if mouse_presses[0]:
            self.click_counter += 1

    def draw_introduction_screen(self):
        self.options = []
        text_start_x = 300*self.window_multiplier
        text_start_y = 300*self.window_multiplier
        text = self.arial2.render(f"In this exercise, you are acting as the school district manager responsible for evaluating school performance.", True, self.black)
        self.window.blit(text, (text_start_x, text_start_y))
        text_start_y += 40*self.window_multiplier
        text = self.arial2.render(f"You will be shown a series of performance reports from principals of schools within your district. The reports will be presented to you two at a time.", True, self.black)
        self.window.blit(text, (text_start_x, text_start_y))
        text_start_y += 40*self.window_multiplier
        text = self.arial2.render(f"For each pair of reports, you need to either commend or warn one school about their performance.", True, self.black)
        self.window.blit(text, (text_start_x, text_start_y))
        text_start_y += 40*self.window_multiplier
        text = self.arial2.render(f"After you have made your choice, you will be asked a multiple choice question on one of the reports you just read.", True, self.black)
        self.window.blit(text, (text_start_x, text_start_y))
        text_start_y += 40*self.window_multiplier
        text = self.arial2.render(f"The exercise will end once you have read each pair of reports, made a choice for them and answered a multiple choice question for each pair.", True, self.black)
        self.window.blit(text, (text_start_x, text_start_y))
        text_start_y += 40*self.window_multiplier
        rect_x = self.window_width/2-self.vignette_button_width/2
        rect_y = self.window_height/2-self.vignette_button_height/2+100
        rect1 = pygame.Rect(rect_x, rect_y, self.vignette_button_width, self.vignette_button_height) # button to progress to the first vignette
        self.options.append((rect1, None))
        pygame.draw.rect(self.window, self.gold, rect1)
        text = self.arial2.render(f"Click here to progress to the first reports", True, self.black)
        coords = self.center_text(text, self.vignette_button_width, self.vignette_button_height, rect_x, rect_y)
        self.window.blit(text, coords)


    def draw_end_round_screen(self):
        if self.multiple_choice_school == None:
            self.questions = []
            seed = random.randrange(0,2)
            if seed == 1:
                self.multiple_choice_school = self.school1
                self.multiple_choice_vignette = self.vignette1
                if self.show_logo == True:

                    self.multiple_choice_logo = self.logo1
            if seed == 0:
                self.multiple_choice_school = self.school2
                self.multiple_choice_vignette = self.vignette2
                if self.show_logo == True:
                    self.multiple_choice_logo = self.logo2

        if self.multiple_choice_vignette != None:
            if len(self.questions) == 0:
                school = self.multiple_choice_school

                if self.multiple_choice_vignette == "no_comparison_1":
                    question1 = f"Some students at {school} have had inconsistent learning results"
                    question2 = f"Some students at {school} with previously excellent results have been doing poorly recently"
                    question3 = f"Some students at {school} have had poor results for all subjects"

                if self.multiple_choice_vignette == "no_comparison_2":
                    question1 = f"Some students at {school} have had difficulties with a few other students"
                    question2 = f"There have been issues with bullying of some students at {school}"
                    question3 = f"Some students at {school} have had issues making friends"

                if self.multiple_choice_vignette == "no_comparison_3":
                    question1 = f"There was a lot of variation in student learning results between subjects at {school}"
                    question2 = f"Very few students at {school} had moderate, though not excellent, scores"
                    question3 = f"Results at {school} did not reach the acceptable threshold of 60% in any subject"

                if self.multiple_choice_vignette == "no_comparison_4":
                    question1 = f"The highest rate of students scoring well at {school} was in math"
                    question2 = f"The results among different students at {school} were quite similar"
                    question3 = f"Most students at {school} scored neither very well nor very poorly"

                if self.multiple_choice_vignette == "statistical_historical_negative_1":
                    question1 = f"Average test scores at {school} were the worst since testing began in 2014"
                    question2 = f"Learning outcomes at {school} have gone down after a period of improvement"
                    question3 = f"Learning result issues at {school} were the least significant in science"

                if self.multiple_choice_vignette == "statistical_historical_negative_2":
                    question1 = f"Test scores in reading at {school} were close to the average over previous years"
                    question2 = f"Learning results at {school} have declined each year since 2014"
                    question3 = f"Learning results at {school} primarily declined because of a decrease in science scores"
        
                if self.multiple_choice_vignette == "statistical_historical_positive_1":
                    question1 = f"Student test results at {school} were the highest in years"
                    question2 = f"Student test results at {school} were particularly excellent in reading"
                    question3 = f"One possible area of improvement at {school} was science"    

                if self.multiple_choice_vignette == "statistical_historical_positive_2":
                    question1 = f"Results at {school} were particularly strong in reading"
                    question2 = f"Student test results at {school} have increased every year recently"
                    question3 = f"Results at {school} were especially strong in the previous year"

                if self.multiple_choice_vignette == "statistical_relative_negative_1":
                    question1 = f"Learning results at {school} were the weakest in the region this year"
                    question2 = f"Parents at {school} will visit other schools to discuss transferring"
                    question3 = f"The weakest subject at {school} this year was reading" 

                if self.multiple_choice_vignette == "statistical_relative_negative_2":
                    question1 = f"Other schools in the area scored much better in reading than {school}"
                    question2 = f"Test scores at {school} were lowest in science"
                    question3 = f"Learning results at {school} were joint-lowest in the region" 

                if self.multiple_choice_vignette == "statistical_relative_positive_1":
                    question1 = f"Student test results at {school} were over 10% higher than the region average"
                    question2 = f"The primary reason for the high performance at {school} was a great result in math"
                    question3 = f"Student test results at {school} were the second best in the region" 

                if self.multiple_choice_vignette == "statistical_relative_positive_2":
                    question1 = f"Parents at other schools have requested to transfer to {school}"
                    question2 = f"There was high variance in results between subjects at {school}"
                    question3 = f"Student test results at {school} were first place among six schools in the area" 

                if self.multiple_choice_vignette == "narrative_historical_negative_1":
                    question1 = f"Some students at {school} feel their teachers have not been supportive"
                    question2 = f"Students having trouble at {school} have fallen behind in their math scores"
                    question3 = f"Staff at {school} have tried for a long time to fix the reported issues" 

                if self.multiple_choice_vignette == "narrative_historical_negative_2":
                    question1 = f"Some students at {school} have lost the progress in grades they previously made"
                    question2 = f"The students having trouble at {school} want to study engineering"
                    question3 = f"Some students at {school} feel their teachers are pushing them too hard" 

                if self.multiple_choice_vignette == "narrative_historical_positive_1":
                    question1 = f"Students doing well at {school} would like to work in the research industry in the future"
                    question2 = f"Students at {school} have always had a love of reading"
                    question3 = f"The students doing well at {school} have always had great grades" 

                if self.multiple_choice_vignette == "narrative_historical_positive_2":
                    question1 = f"Students at {school} have improved their grades over four years"
                    question2 = f"Students transferring to {school} were warned that they would do worse than others"
                    question3 = f"Teachers at {school} actively approach students to advise them" 

                if self.multiple_choice_vignette == "narrative_relative_negative_1":
                    question1 = f"Students having trouble at {school} have found teachers to be too rigid"
                    question2 = f"{school} expects students to deal with any issues that arise themselves"
                    question3 = f"Teachers at {school} have been unwilling to address the issues students are having" 

                if self.multiple_choice_vignette == "narrative_relative_negative_2":
                    question1 = f"Some students at {school} feel that they are not allowed to work independently enough"
                    question2 = f"Students at {school} have not been able to change teachers despite asking"
                    question3 = f"Students having trouble at {school} have a favourite teacher they want to work with" 

                if self.multiple_choice_vignette == "narrative_relative_positive_1":
                    question1 = f"Students who transferred to {school} have explored different parts of the curriculum"
                    question2 = f"Teachers at {school} have pushed students to focus on particular subjects"
                    question3 = f"Some students transferred to {school} because their parents heard the teaching there was great" 

                if self.multiple_choice_vignette == "narrative_relative_positive_2":
                    question1 = f"Teachers at {school} focus on helping students find areas they excel at"
                    question2 = f"Many students at other schools have heard that {school} is a great school"
                    question3 = f"Some students previously at {school} no longer need special support" 

                self.questions.append((question1, True))
                self.multiple_choice_true_statement = question1
                self.questions.append((question2, False))
                self.questions.append((question3, False))
                random.shuffle(self.questions)


        self.options = []
        text_start_x = 400*self.window_multiplier
        text_start_y = 200*self.window_multiplier
        if self.multiple_choice_made == True:
            if self.multiple_choice_correct == True:
                correct = "correct"
            else:
                correct = "incorrect"
            text = self.arial2.render(f"You have completed report pair {self.vignette_number} of 10", True, self.black)
            self.window.blit(text, (text_start_x, text_start_y))
            text_start_y += 50
            text = self.arial2.render(f"Your answer was {correct}!", True, self.black)
            self.window.blit(text, (text_start_x, text_start_y))
            text_start_y += 50
            text = self.arial2.render(f"The correct answer was:                       {self.multiple_choice_true_statement}", True, self.black)
            self.window.blit(text, (text_start_x, text_start_y))
            text_start_y += 50   
            rect_x = self.window_width/2-self.vignette_button_width/2
            rect_y = text_start_y
            rect1 = pygame.Rect(rect_x, rect_y, self.vignette_button_width, self.vignette_button_height) # button to progress to the first vignette
            self.options.append((rect1, None))
            pygame.draw.rect(self.window, self.gold, rect1)
            if self.show_postgame == False:
                text = self.arial2.render(f"Click here to continue to the next reports", True, self.black)
            if self.show_postgame == True:
                text = self.arial2.render(f"Click here to exit the program", True, self.black)
            coords = self.center_text(text, self.vignette_button_width, self.vignette_button_height, rect_x, rect_y)
            self.window.blit(text, coords)
            text_start_y += 200            
        if self.multiple_choice_made == False:
            text = self.arial2.render(f"The choice you made was:", True, self.black)
            self.window.blit(text, (text_start_x, text_start_y))
            text_start_y += 50
            text = self.arial2.render(f"{self.option_choice}", True, self.black)
            self.window.blit(text, (text_start_x+30, text_start_y))
            text_start_y += 50
            text = self.arial2.render(f"{self.multiple_choice_school} has been randomly chosen as a school for you to answer a multiple choice question on.", True, self.black)
            if self.show_logo == True:
                logo_text_width = text.get_width()
                logo_height = self.multiple_choice_logo.get_height()
                self.window.blit(self.multiple_choice_logo, (text_start_x+logo_text_width+20, text_start_y-logo_height+40))

            self.window.blit(text, (text_start_x, text_start_y))
            text_start_y += 50
            text = self.arial2.render(f"Please choose the correct statement regarding {self.multiple_choice_school} below by clicking on it. There is only one correct statement.", True, self.black)
            self.window.blit(text, (text_start_x, text_start_y))
            text_start_y += 100
        for i in self.questions:
            rect_x = self.window_width/2-self.vignette_button_width*1.25
            rect_y = text_start_y
            rect1 = pygame.Rect(rect_x, rect_y, self.vignette_button_width*2.5, self.vignette_button_height) # button to progress to the first vignette
            if self.multiple_choice_made == False:
                self.options.append((rect1, i[1]))
            if self.multiple_choice_made == False:
                pygame.draw.rect(self.window, self.gold, rect1)
            if self.multiple_choice_made == True:
                if i[1] == False:
                    pygame.draw.rect(self.window, self.crimson, rect1)
                if i[1] == True:
                    pygame.draw.rect(self.window, self.darkolivegreen3, rect1)
            text = self.arial2.render(i[0], True, self.black)
            coords = self.center_text(text, self.vignette_button_width*2.5, self.vignette_button_height, rect_x, rect_y)
            text_start_y += self.vignette_button_height + 20
            self.window.blit(text, coords)

    def endconditions(self):
        self.show_introduction = False
        self.show_end_round_screen = True
        self.show_performance_information = False
        self.show_postgame = True
        self.show_vignette_buttons = False

game = EyeTracker()
game.check_participant_number()
game.choose_school_conditions()
game.create_output_file()
game.create_game_board()
game.create_vignettes()
game.create_vignette_buttons()
game.choose_cases()
async def main():
    while True:
        if game.time > game.vignette_time + game.vignette_timer-1 and game.show_postgame == False and game.show_end_round_screen == False:
            if game.counter == 0:
                game.randomisation_done = False
                game.counter += 1
        if game.time > game.vignette_time + game.vignette_timer and game.show_postgame == False and game.show_end_round_screen == False:
            game.show_vignette_buttons = True
        else:
            game.show_vignette_buttons = False
        game.window.fill(game.white) #fills the game screen with white
        if game.show_performance_information == True:
            game.draw_game_board()
            game.draw_vignette()
            if game.show_vignette_buttons == True:
                game.draw_vignette_buttons()
        if game.show_introduction == True:
            game.draw_introduction_screen()
        if game.show_end_round_screen == True:
            game.draw_end_round_screen()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.finish_game()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    count = 0
                    game.increase_click_counter()
                    xy = pygame.mouse.get_pos()
                    x = xy[0]
                    y = xy[1]
                    if game.show_vignette_buttons == True:
                        if game.option_choice == None:
                            for i in game.vignette_buttons_1:
                                if game.click_box(x, y, i[0]) == True:
                                    game.button_clicked = True
                                    game.button_chosen = i
                                    game.option_choice = i[2]
                                    game.option_chosen = True
                                    game.vignette_choices.append((game.option_choice, game.school1))

                            for i in game.vignette_buttons_2:
                                if game.click_box(x, y, i[0]) == True:
                                    game.button_clicked = True
                                    game.button_chosen = i
                                    game.option_choice = i[2]
                                    game.option_chosen = True
                                    game.vignette_choices.append((game.option_choice, game.school2))

                    if game.show_introduction == True:
                        for i in game.options:
                            if game.click_box(x, y, i[0]) == True:
                                game.show_introduction = False
                                game.show_performance_information = True
                                game.vignette_time = game.time
                    if game.show_end_round_screen == True:
                        for i in game.options:
                            if game.multiple_choice_made == True:
                                if game.click_box(x, y, i[0]) == True:
                                    if game.show_postgame == False:
                                        game.multiple_choices.append((game.roundnumber, game.multiple_choice_correct, game.multiple_choice_school, game.multiple_choice_vignette))
                                        game.show_end_round_screen = False
                                        game.multiple_choice_vignette = None
                                        game.multiple_choice_school = None
                                        game.multiple_choice_logo = None
                                        game.option_choice = None
                                        game.show_performance_information = True
                                        game.vignette_time = game.time
                                        game.randomisation_done = False
                                    if game.show_postgame == True:
                                        game.multiple_choices.append((game.roundnumber, game.multiple_choice_correct, game.multiple_choice_school, game.multiple_choice_vignette))
                                        game.finish_game()
                            if game.multiple_choice_made == False:
                                if game.click_box(x, y, i[0]) == True:
                                    game.multiple_choice_made = True
                                    game.multiple_choice_correct = i[1]


                    if count == 0:
                        game.button_clicked = False
                        game.button_chosen = None
        if game.option_chosen == True:
            game.option_chosen = False
            game.show_vignette_buttons = False
            game.counter = 0
            game.show_performance_information = False
            game.show_end_round_screen = True
            game.vignette_time = game.time
            game.vignette_number += 1
            if game.vignette_number == game.roundstandard:
                game.endconditions()

        game.clock.tick(60)
        game.time += 1/60
        pygame.display.update()
        await asyncio.sleep(0)

asyncio.run(main())