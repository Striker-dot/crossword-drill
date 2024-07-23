"""
This module defines models for puzzles, entries, and clues in the crossword application.

Models:
- Puzzle: Represents a puzzle with a title, date, byline, and publisher.
- Entry: Represents an entry in the crossword with unique text.
- Clue: Represents a clue in a puzzle associated with an entry and a puzzle, with an optional theme.
"""

from django.db import models

class Puzzle(models.Model):
    """
    Represents a crossword puzzle with a title, date, byline, and publisher.
    """
    title = models.CharField(max_length=255, blank=True)
    date = models.DateField()
    byline = models.CharField(max_length=255)
    publisher = models.CharField(max_length=12)
    
class Entry(models.Model):
    """
    Represents a unique entry in the crossword puzzle with text.
    """
    entry_text = models.CharField(max_length=50, unique=True)

class Clue(models.Model):
    """
    Represents a clue in a puzzle, associated with an entry and a puzzle,
    and optionally marked as a theme clue.
    """
    clue_text = models.CharField(max_length=512)
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    puzzle = models.ForeignKey(Puzzle, on_delete=models.CASCADE)
    theme = models.BooleanField(default=False)                                                         
