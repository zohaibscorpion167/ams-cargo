from django.db import models

class LahoreAccount(models.Model):
    Date = models.DateField(null=False, blank=False)
    Delivery_Day = models.CharField(max_length=10, null=True, blank=True)
    Truck_Number = models.CharField(max_length=10, null=False, blank=False)
    Truck_Company = models.CharField(max_length=50, null=False, blank=False)
    Total_CTN = models.IntegerField(default=0,null=False, blank=False)
    To_Pay = models.IntegerField(default=0,null=False, blank=False)
    Truck_Rent = models.IntegerField(default=0,null=False, blank=False)
    Payment_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return str(self.Date)

    class Meta:
        verbose_name = 'Lahore Account'
        verbose_name_plural = 'Lahore Account'


class RawalpindiAccount(models.Model):
    Date = models.DateField(null=False, blank=False)
    VIA = models.CharField(max_length=50, null=True, blank=True)
    Truck_Number = models.CharField(max_length=10, null=False, blank=False)
    Truck_Company = models.CharField(max_length=50, null=False, blank=False)
    Total_CTN = models.IntegerField(default=0,null=False, blank=False)
    To_Pay = models.IntegerField(default=0,null=False, blank=False)
    Truck_Rent = models.IntegerField(default=0,null=False, blank=False)
    Karachi_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Lahore_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return str(self.Date)

    class Meta:
        verbose_name = 'Rawalpindi Account'
        verbose_name_plural = 'Rawalpindi Account'



class GujranwalaAccount(models.Model):
    Date = models.DateField(null=False, blank=False)
    VIA = models.CharField(max_length=50, null=True, blank=True)
    Truck_Number = models.CharField(max_length=10, null=False, blank=False)
    Truck_Company = models.CharField(max_length=50, null=False, blank=False)
    Total_CTN = models.IntegerField(default=0,null=False, blank=False)
    To_Pay = models.IntegerField(default=0,null=False, blank=False)
    Truck_Rent = models.IntegerField(default=0,null=False, blank=False)
    Karachi_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Lahore_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Rawalpindi_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return str(self.Date)

    class Meta:
        verbose_name = 'Gujranwala Account'
        verbose_name_plural = 'Gujranwala Account'


class FaislabadJhungAccount(models.Model):
    Date = models.DateField(null=False, blank=False)
    VIA = models.CharField(max_length=50, null=True, blank=True)
    Truck_Number = models.CharField(max_length=10, null=False, blank=False)
    Truck_Company = models.CharField(max_length=50, null=False, blank=False)
    Total_CTN = models.IntegerField(default=0,null=False, blank=False)
    To_Pay = models.IntegerField(default=0,null=False, blank=False)
    Truck_Rent = models.IntegerField(default=0,null=False, blank=False)
    Karachi_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Lahore_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    FSD_to_Jhung_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return str(self.Date)

    class Meta:
        verbose_name = 'Faislabad & Jhung Account'
        verbose_name_plural = 'Faislabad & Jhung Account'



class MultanAccount(models.Model):
    Date = models.DateField(null=False, blank=False)
    VIA = models.CharField(max_length=50, null=True, blank=True)
    Truck_Number = models.CharField(max_length=10, null=False, blank=False)
    Truck_Company = models.CharField(max_length=50, null=False, blank=False)
    Total_CTN = models.IntegerField(default=0,null=False, blank=False)
    To_Pay = models.IntegerField(default=0,null=False, blank=False)
    Truck_Rent = models.IntegerField(default=0,null=False, blank=False)
    Karachi_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0,null=True, blank=True)

    def __str__(self):
        return str(self.Date)

    class Meta:
        verbose_name = 'Multan Account'
        verbose_name_plural = 'Multan Account'



class GujratAccount(models.Model):
    Date = models.DateField(null=False, blank=False)
    VIA = models.CharField(max_length=50, null=True, blank=True)
    Truck_Number = models.CharField(max_length=10, null=False, blank=False)
    Truck_Company = models.CharField(max_length=50, null=False, blank=False)
    Total_CTN = models.IntegerField(default=0,null=False, blank=False)
    To_Pay = models.IntegerField(default=0,null=False, blank=False)
    Truck_Rent = models.IntegerField(default=0,null=False, blank=False)
    Karachi_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Lahore_Transit_Rent = models.IntegerField(default=0,null=True, blank=True)
    Payment_Date = models.DateField(null=True, blank=True)
    Amount = models.IntegerField(default=0,null=True, blank=True)
    
    def __str__(self):
        return str(self.Date)

    class Meta:
        verbose_name = 'Gujrat Account'
        verbose_name_plural = 'Gujrat Account'



class LahoreWeeklyClosing(models.Model):
    start_date = models.DateField(null=False, blank=False)
    end_date = models.DateField(null=False, blank=False)
    Previous_Balance = models.IntegerField(default=0,null=False, blank=False)
    Current_to_Pay = models.IntegerField(default=0,null=False, blank=False)
    Recovery = models.IntegerField(default=0,null=False, blank=False)
    
    def total_balance(self):
        return int(self.Previous_Balance+self.Current_to_Pay)

    def net_balance(self):
        return int(self.total_balance())-self.Recovery

    def __str__(self):
        return str(self.start_date)
