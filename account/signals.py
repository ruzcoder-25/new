# from django.db.models.signals import pre_save
# from django.dispatch import receiver
#
# from account.models import CustomUser
#
#
# @receiver(pre_save, sender=CustomUser)
# def username_ustudy(sender, instance,**kwargs):
#     if not instance.username.endswith('USTUDY'):
#         instance.username += "USTUDY"
#         print(instance.username)
#
#
#
#
