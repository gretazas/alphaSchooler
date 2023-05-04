from django.shortcuts import render
from .forms import FeedbackForm
from django.contrib import messages


def feedback(request):
    ''' View that renders feedbak form '''
    if request.method == 'POST':
        form = FeedbackForm(request.POST)

        if form.is_valid():
            form.save()
            messages.info(request, f'Thank you for your feedback!')
            return render(request, 'feedback/feedback.html')
    else:
        form = FeedbackForm()
    return render(request, 'feedback/feedback.html', {'form': form, 'on_feedback_page': True})


def contact(request):
    ''' View that renders contact info '''
    return render(request, 'feedback/contact.html')
