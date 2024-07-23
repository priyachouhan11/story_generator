# story_generator/views.py
import random

from django.shortcuts import render
from .models import StoryElements

def generate_story(request):
    story = (
        f"{random.choice(StoryElements.sentence_starters)} "
        f"{random.choice(StoryElements.characters)} "
        f"{random.choice(StoryElements.settings)} "
        f"{random.choice(StoryElements.conflicts)} "
        f"{random.choice(StoryElements.endings)}"
    )
    return render(request, 'index.html', {'story': story})
