from django.template import Template, Context
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from mail_celery.celery import app
from django.apps import apps
Loan = apps.get_model('loan_app', 'Loan')
REPORT_TEMPLATE = """
Here's how you did till now:

{% for post in posts %}
        "{{ post.title }}": viewed {{ post.view_count }} times |

{% endfor %}
"""


@app.task
def mail_sender():
    for user in get_user_model().objects.all():
        posts = Post.objects.filter(author=user)
        if not posts:
            continue

        template = Template('./templates/mail')

        send_mail(
            'Not forget to pay youre debts',
            template.render(),
            'loanworkshop@lol.dev',
            [user.email],
            fail_silently=False,
        )