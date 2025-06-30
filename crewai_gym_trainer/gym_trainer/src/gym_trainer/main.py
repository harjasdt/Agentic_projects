#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from gym_trainer.crew import GymTrainer

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    inputs = {
        'user_name': 'Harjas',
        'user_email':'singh.harjas2002@gmail.com',
        'user_lifestyle':'i have a sittign job and minimal body movement',
        'user_profile':'curently my height is 180cm and weight is 90 Kg.',
        'user_goal': "Loose 5kg of weight "
    }

    # inputs = {
    #     'user_name': 'Harjas',
    #     'user_goal': "My email id is harjas@emample.com and singh.harjas2002@gmail.com.What record do you have about me"
    # }

    
    try:
        GymTrainer().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")
