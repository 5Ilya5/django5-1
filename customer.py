class Customer(models.Model):
    name = models.CharField(blank=False, max_length=120, unique=True)\