class Item(models.Model):
    name = models.CharField(max_length=120)
    price = models.IntegerField(default=0, unique=False)