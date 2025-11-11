This repository contains source code and instructions for deploying a simple experiment where participants are asked to read a series of paired performance reports and make a simple choice based on these reports. The experiment is designed to pair with in-person eye-tracking to track the effects of attention to individual reports on the participants' decision-making. However, the experiment can also be utilised in different contexts. The results of each fully run instance of the program will be stored in the appropriate folder.

The experiment is ready to deploy on a 1920*1080 screen, but also includes functionality to adapt the material to other screen sizes (upscaling and downscaling). To adapt the visual assets to a new screen size, new vignettes need to be generated using the vignette screen capture program. This program will ask whether the deployment is online or in person. For in-person deployment, the program should be run on the same device and using the same screen as the final experiment, in which case the appropriate screen size will be automatically detected. For online deployment, no size adjustment is necessary. If desired, the multiplier used can also be adjusted manually in the source code.

The experiment makes use of vignettes specifically designed for the original experiment. If a researcher wishes to adapt the content of the texts without changing the visual format, this can be done by editing files in the vignette texts folder. Note that the files make use of special characters to denote names and paragraph breaks.

The source code includes 20 pre-set treatment conditions, 20 fictional school names and a list of 10000 random combinations of these. These combinations are pairs of school/condition pairs shown at once, such that the same thematic condition cannot be shown next to one another and each condition and school only appears once. Source code for generating such a list is also included. If the same schools are used, visual assets for a school logo for each school are included. Please note that if school names are changed, the source code assumes logo files named after the school. If logos are not desired, the condition 'self.show_logo' can be changed to FALSE.

Custom fonts are included. If other fonts are desired, they need to be added to the fonts folder, preferably in .ttf format.

For new deployment, the following steps should be followed:

1. Run randomizer
2. Run screen capture
3. Run main experiment

The experiment is designed to be deployed in person, but can also be deployed online using pygbag for WebAssembly conversion. The code is already asynchronous to support pygbag deployment and dependencies are designed to be portable, but additional functionality is needed to store results. Additionally, assets may need to be reproduced for online deployment using the screen capture program. For new pygbag deployment, the following steps should be followed:

1. Run randomizer
2. Run screen capture
3. Run the pygbag WebAssembly conversion. Due to a known issue with sound in Safari, it is recommended that the option ume_block 0 is used. If the command is run in the console in the same location as the source code folder (not in the folder itself) and no file names have been changed, the following command can be used:

--ume_block 0 eye_tracker_code_public

This will host a local server at http://localhost:8000 and generate a new 'build' folder, which can be deployed online. To deploy the program online, simply convert the entire folder (including the build folder, source code nd dependencies) into a .zip folder and upload it to the server where you are hosting your program. Additional information on pygbag deployment can be found through the links below:

https://pypi.org/project/pygbag/
https://jackwhitworth.com/blog/how-to-run-pygame-in-the-browser/

It is recommended that prior to deploying any part of the experiment, the requisite dependencies are installed, as detailed below:
Python:
The software utilises python3, available at:
https://www.python.org/downloads/
The software has been tested in a Windows 11 environment, but should run without issue on other systems.

Pygame:
The experiment makes use of pygame, a simple game design package, available at:
https://www.pygame.org/news
Pygame needs to be installed using pip, as detailed in the following website:
https://www.pygame.org/wiki/GettingStarted
