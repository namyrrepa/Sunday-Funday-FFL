# Sunday-Funday-FFL
 Repository for the Sunday Funday Fantasy Football League

GENERAL PURPOSE:

This repository serves multiple purposes :

1) It acts as a playground for me to become more familiar with GitHub's capabilities and uses

2) It will be the home for side project ideas that I have related to the SFFFL for which I've been the commissioner going on 9 years now and am always looking to improve/add value to. Also, there are a lot of things that I do for the league/want to do that take a lot of time... this repository will be the home for custom programs that do these tasks for me significantly faster!

3) Eventually, this will be the basis for what I've self-assigned as a "portfolio project" of creating a site for the SFFFL which is updated with weekly score updates, power ranking updates, game recaps, historical data, etc.

FILE/PROGRAM DESCRIPTIONS:

draft-selector.py
    Reason for Creation:
        In order to determine draft order for the league each year, I pick a random major sporting event and randomly assign each league member a competitor in the event. Draft order is then determined by the competitors' performance! I've always done it this way because it keeps order random (removing bias) and is a fun way to make sports outside of football entertaining. For example, this year I selected the PGA Tour Championship. The expected Top-12 golfers (based on gambling odds) were then paired to the 12 members of the league and each respective golfer's finish decided the draft order.
    
    How the Code Works:
        I wanted the program to be as variable driven as possible dependent on user inputs, that way it can be reused each year without needing internal editing. Also, I wanted a highly interactive and intuitive interface so that anyone can use it!

        To do this, the program follows these steps :

        1) asks how many teams are in the league
        2) creates a list of managers (league members) by asking user for names one by one until all members are accounted for
        3) asks the user if s/he would like to input team names. 
            - if yes, asks user line by line to enter each member's team name respectively, then creates a list that combines manager names with the appropriate team name.
            - if no, moves on to the next step
        4) asks user to input each potential match option using those inputs to create a list of inputted options
        5) randomized the list of match options, and then combines this randomized list with the appropriate SFFFL list (dependent upon whether or not team names were inputted)
        6) presents the final info utilizing this final list in an easily digestable way! (alongside some fun messages)

    Final Notes:
        Obiously, using user inputs throughout the code leaves room for potential errors later on... to combat this there are checks and iterations built throughout the program to ensure that correct inputs are being used at all times. The hope would be to use this code to create a clean and polished component to be added to the final SFFFL site!