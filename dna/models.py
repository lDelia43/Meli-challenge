from django.db import models

class DnaSequence(models.Model):
    dna = models.JSONField(unique=True)
    is_mutant = models.BooleanField()

    def __str__(self):
        return f"{'Mutant' if self.is_mutant else 'Human'}: {self.dna}"
