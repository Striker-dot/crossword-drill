"""
URL configuration for the xword_data application.

This module defines URL patterns for the xword_data app, mapping URLs to
views. It includes:
- `DrillView` for handling drill requests.
- `AnswerView` for handling answer-related requests.

URL Patterns:
- `drill/`: Maps to `DrillView` for drill operations.
- `answer/<int:pk>/`: Maps to `AnswerView` for fetching answers by primary key.
"""
from django.urls import path
from xword_data.views import DrillView, AnswerView


urlpatterns = [
    path('drill/', DrillView.as_view(), name='xword-drill'),
    path('answer/<int:pk>/', AnswerView.as_view(), name='xword-answer'),
]
