"""
Views for handling drill and answer operations in the xword_data application.

This module defines the `DrillView` and `AnswerView` classes to manage the
drill and answer functionalities for crossword clues.

- `DrillView`: Handles displaying a random clue and processing user answers.
- `AnswerView`: Displays information about a clue and aggregates similar clues.
"""
from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views import View
from .models import Clue

class DrillView(View):
    """
    View for displaying a random clue and processing user answers.

    Handles GET requests to show a random clue and POST requests to validate
    the user's answer. Updates session data to track the number of correct
    answers and total drills.

    Methods:
    - get: Displays a random clue and initializes session data if needed.
    - post: Validates the user's answer, updates session data, and redirects
      to the answer view if correct.
    """
    def get(self, request):
        """
        Handles GET requests to display a random clue.

        Initializes or increments the correct answer count and total drills
        in the session, then renders the 'drill.html' template with the clue.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: The rendered 'drill.html' template with the clue.
        """
        clue = Clue.objects.order_by("?").first()
        # Initialize or increment the correct answer count and total drills in session
        if 'correct_answers' not in request.session:
            request.session['correct_answers'] = 0
        if 'total_drills' not in request.session:
            request.session['total_drills'] = 0
        request.session['total_drills'] += 1
        request.session.modified = True
        
        return render(request, 'drill.html', {'clue': clue, 'clue_id': clue.id})

    def post(self, request):
        """
        Handles POST requests to validate the user's answer.

        Checks if the submitted answer is correct, updates the session data,
        and redirects to the answer view if correct. If incorrect, it renders
        the 'drill.html' template again with an error message.

        Args:
            request: The HTTP request object.

        Returns:
            HttpResponse: A redirect to the answer view if the answer is correct,
            otherwise the rendered 'drill.html' template with an error message.
        """
        clue_id = request.POST.get("clue_id")
        answer = request.POST.get("answer", "").strip().upper()
        clue = get_object_or_404(Clue, pk=clue_id)
        
        if answer == clue.entry.entry_text.upper():
            # Initialize or increment the correct answer count in session
            if 'correct_answers' not in request.session:
                request.session['correct_answers'] = 0
            request.session['correct_answers'] += 1
            request.session.modified = True
            return redirect(reverse('xword-answer', args=(clue.id,)))
        
        return render(request, 'drill.html', {'clue': clue, 'clue_id': clue.id, 'error': "Your answer is not correct"})    
        
class AnswerView(View):
    
