# CS3321-Software-Analysis-and-Design-Team-4
- This is a forked version of the main development branch used to get Docker and Travis CI working. See the original project here **https://github.com/mietaust/CS3321-Software-Analysis-and-Design-Team-4**.
## Client Binaries - Couldn't figure out a good way to do this automatically along with the Server, so they're manually released. Use at own risk. 
- Client binary for Windows: https://mega.nz/file/PtUmjTBS#hkSJ-xaG29H9IKDqn6u1ty0Hn-6fAzfVJrqACw-c9Sk
- Client binary for Linux (largely untested): https://mega.nz/file/GlsGhbrC#hJQ52ojj49GToEcdoMf2saAFqm_7cqaV97iSyeLDr24

## Team 4 Info
### Members: Active Roles
* Nicholas Garrett: 
* Daniel Igbokwe: Scrum Master
* Timothy Lybek:
* Austin Mietchen: 
* Joshua Wheeler: Product Owner
## Documentation Methodology
* In Code (comments, descriptions, etc)
    * Will be dictated by the chosen style guides listed below.
* Project Backlog, User Stories, etc
    * Will be located in the "Projects" section of this repo using the "User-Stories" method of requirements setting. 
## Project Description
### Overview
Our team will be implementing a lite version of Monopoloy. This game will use a desktop client to handle user input and a remote server to handle game logic and keep track of the game's current status, as well as updating game clients to reflect the state of the game. 
### Minimum Technologies Used
* Frontend 
     * Language: Python
     * Testing Framework: unittest
     * https://google.github.io/styleguide/pyguide.html
     * IDE: Python: 3.9.5
     * UI Libraries/Frameworks: PyGame, ThorPy, tkinter
* Backend
     * Language: Java SE 17 
     * Testing Framework: JUnit 5.7.1
     * https://google.github.io/styleguide/javaguide.html
     * IDE: Intelli-J Idea
     * MS Framework: Javelin
     * Server Hosting: AWS

## Description of our MVP
Basic Client and Server that are cabaple of communicating and playing a limited ruleset version of Monopoly, including:
* Minimum of 2 players.
* Game Initialization and Completion.
    * Rules TBD, but including:
    * Buying property, property types, receiving payment, moving on the gameboard, going to jail, passing go, etc. 
* Basic user interface.
## Health monitoring strategies and methods
* Product backlog management for both Backend and Frontent.
* Utilize user stories.
* Playtesting.
* Regular meetings to play Essence "serious" games.

### License:
MIT License

Copyright (c) [2021] [Tim Lybeck, Nicholas Garrett, Daniel Igbokwe, Austin Mietchen, Joshua Wheeler]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
