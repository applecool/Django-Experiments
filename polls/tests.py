from django.test import TestCase

from .models import Question

import datetime

from django.utils import timezone
from django.core.urlresolvers import reverse

# Create your tests here.


class QuestionMethodTests(TestCase):
	def test_published_recently_with_future_question(self):
		time = timezone.now() + datetime.timedelta(days=30)
		future_question = Question(pub_date=time)
		self.assertEqual(future_question.was_published_in_last_7_days(), False)

	def test_published_recently_with_recent_question(self):
		time = timezone.now() - datetime.timedelta(hours=1)
		recent_question = Question(pub_date=time)
		self.assertEqual(recent_question.was_published_in_last_7_days, True)

class QuestionViewTests(TestCase):
	def test_index_view_with_no_questions(self):
		response = self.client.get(reverse('polls:index'))
		self.assertEqual(response.status_code, 200)
		self.assertContains(response, "You haven't uploaded any questions yet.")
		self.assertQuerysetEqual(response.context["latest_question_list"], [])

class QuestionIndexDetailTests(TestCase):
	def test_detail_view_with_a_past_question(self):
		past_question = create_question(question_text="Past question", days=-5)
		response = self.client.get(reverse('polls:detail', args=(past_question.id,)))
		self.assertContains(response,past_question.question_text, status_code=200)
