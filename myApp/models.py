from django.db import models
# from django.core.exceptions import ValidationError
# from django.utils.translation import gettext_lazy as _
from customUser.models import MyUser



# def validate_latt(value):
#     if value > 90 or value < -90 :
#         raise ValidationError(
#             _('%(value)s is not in range'),
#             params={'value': value},
#         )

# def validate_long(value):
#     if value > 180 or value < -180 :
#         raise ValidationError(
#             _('%(value)s is not in range'),
#             params={'value': value},
#         )


## all validations must be done also in serializers beacause of the api

class Coordinates (models.Model) :
    lattitude = models.DecimalField(max_digits=6, decimal_places=4, blank=False)
    longitude = models.DecimalField(max_digits=7, decimal_places=4, blank=False)
    heartRate = models.IntegerField(null=True, blank=True)
    person = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(null=True, blank=True)


    def __str__(self) :
        return f'lattitude : {self.lattitude} | longitude : {self.longitude} => {self.person.first_name} {self.person.last_name}'