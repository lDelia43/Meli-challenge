from django.test import TestCase, Client
from django.urls import reverse
from .models import DnaSequence
from .utils import is_mutant

class DnaTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.mutant_dna = ["ATCGGA", "CAGTGC", "TTATGT", "AGAAGG", "CCCCTA", "TCACTG"]
        self.human_dna = ["ATCGGA", "CAGTGC", "TTATTT", "AGACGG", "CGTCAA", "TCACTG"]

    def test_is_mutant_function(self):
        self.assertTrue(is_mutant(self.mutant_dna))
        self.assertFalse(is_mutant(self.human_dna))

    def test_mutant_endpoint_with_mutant_dna(self):
        response = self.client.post(reverse('mutant'), data={"dna": self.mutant_dna}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"is_mutant": True})

    def test_mutant_endpoint_with_human_dna(self):
        response = self.client.post(reverse('mutant'), data={"dna": self.human_dna}, content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"is_mutant": False})

    def test_mutant_endpoint_with_invalid_data(self):
        response = self.client.post(reverse('mutant'), data={"invalid_key": self.mutant_dna}, content_type='application/json')
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json(), {"error": "Invalid DNA data"})

    def test_stats_endpoint(self):
        for i in range(40):
            DnaSequence.objects.create(dna=f"mutant_{i}", is_mutant=True)
        for i in range(100): 
            DnaSequence.objects.create(dna=f"human_{i}", is_mutant=False)
        response = self.client.get(reverse('stats'))
        self.assertEqual(response.status_code, 200)
        stats_data = response.json()
        self.assertEqual(stats_data["count_mutant_dna"], 40)
        self.assertEqual(stats_data["count_human_dna"], 100)
        self.assertEqual(stats_data["ratio"], 0.4)
