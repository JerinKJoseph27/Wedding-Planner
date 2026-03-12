from datetime import timedelta

from django.test import TestCase
from django.utils import timezone

from .forms import Bookingform


class BookingFormTests(TestCase):
	def valid_payload(self):
		return {
			'p_name': 'Jerin Joseph',
			'p_email': 'jerin@example.com',
			'p_phone': '9876543210',
			'p_when': (timezone.localdate() + timedelta(days=7)).isoformat(),
			'p_events': 'Wedding Decoration',
		}

	def test_valid_form_is_accepted(self):
		form = Bookingform(data=self.valid_payload())
		self.assertTrue(form.is_valid())

	def test_name_rejects_numbers(self):
		payload = self.valid_payload()
		payload['p_name'] = 'Jerin123'
		form = Bookingform(data=payload)
		self.assertFalse(form.is_valid())
		self.assertIn('p_name', form.errors)

	def test_phone_requires_valid_digit_count(self):
		payload = self.valid_payload()
		payload['p_phone'] = '12345'
		form = Bookingform(data=payload)
		self.assertFalse(form.is_valid())
		self.assertIn('p_phone', form.errors)

	def test_past_event_date_is_rejected(self):
		payload = self.valid_payload()
		payload['p_when'] = (timezone.localdate() - timedelta(days=1)).isoformat()
		form = Bookingform(data=payload)
		self.assertFalse(form.is_valid())
		self.assertIn('p_when', form.errors)

	def test_invalid_event_type_is_rejected(self):
		payload = self.valid_payload()
		payload['p_events'] = 'Random Event'
		form = Bookingform(data=payload)
		self.assertFalse(form.is_valid())
		self.assertIn('p_events', form.errors)
