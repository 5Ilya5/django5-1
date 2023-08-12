class Order(models.Model):
    customer = models.ForeignKey(Customer, related_name='orders', null=True, blank=True)
    item = models.ForeignKey(Item, related_name='orders', null=True, blank=True)
    order_date = models.DateField(auto_now=True)
    is_cancelled = models.BooleanField(default=False)
    is_delivered = models.BooleanField(default=False)
    quantity = models.IntegerField()