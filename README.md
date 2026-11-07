# ET574-D-HW4-ISLAM
This is a Python Homework based on dices

# ET-574 Homework 4: Dice Game Simulator

**Student:** Rahatul Islam  
**Course:** ET-574, Section D  
**Instructor:** Professor Joan Sun

## Project Description

This Python program simulates a dice game using object-oriented programming. It uses two six-sided dice and determines the outcome based on their total.

- **7 or 11:** Win
- **2, 3, or 12:** Lose
- **4, 5, 6, 8, 9, or 10:** Roll Again

The player can choose to play another round or exit the program.

## Running the Program

To play the game:

'python main.py


To run the unit tests:

'python -m unittest -v'


## AI Usage Documentation

**AI Tool:** ChatGPT by OpenAI.

**Purpose:** I used ChatGPT to help understand the homework requirements, develop the Python classes, create the game menu, and understand unit testing and GitHub commands.

**Representative Prompts:**
- Help me understand and guide my Python dice game homework step by step.
- Make sure to notify if I miss any of the professor's instructions.
- Help me add three additional unit tests.
- Help me correct the placement and indentation of my tests.

**Evaluation and Modifications:** I reviewed the suggested Python code and ran the game in GitHub Codespaces. I also corrected the placement and indentation of the additional unit tests so they would run correctly.

## Additional Unit Tests

I added three tests using controlled dice values:

1. **Winning round:** Dice values 3 and 4 produce a total of 7, resulting in "Win".
2. **Losing round:** Dice values 1 and 1 produce a total of 2, resulting in "Lose".
3. **Roll Again:** Dice values 2 and 3 produce a total of 5, resulting in "Roll Again".

ChatGPT suggested these scenarios, and I adopted all three after reviewing their expected results. I did not reject any of these scenarios.

## Reflection on AI Use

I used AI to support the development of the dice game and to understand how unit tests work. It helped me identify useful test scenarios and explained the code required to test them.

I had to modify the placement and indentation of my tests because they were initially outside the correct class. After correcting this, I ran the unit tests again.

I verified the results using `python -m unittest -v` in GitHub Codespaces. All 10 tests passed successfully.

This assignment helped me better understand Python classes, methods, and unit testing. I also learned that AI-generated suggestions need to be reviewed and tested instead of simply copied.
