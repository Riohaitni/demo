# from datetime import datetime
# from django.db import models
# from django.contrib.auth.models import User
#
#
# # #danh sach loi moi ket ban
# class FriendInvitation(models.Model):
#     sender = models.ForeignKey(User, related_name='sent_invitations', on_delete=models.CASCADE)
#     receiver = models.ForeignKey(User, related_name='received_invitations', on_delete=models.CASCADE)
#     # status = models.CharField(max_length=20,choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')],default='pending')
#     sent_at = models.DateTimeField(auto_now_add=True)
#     current_time = models.DateTimeField(default=datetime.now)
#
#     def __str__(self):
#         return f"{self.sender.username} -> {self.receiver.username} (sent at {self.sent_at})"
#
#
#
#
# # danh sach ban be
# class Friendship(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friend_list')
#     friends = models.ManyToManyField(User, related_name='friends')
#     current_time = models.DateTimeField(default=datetime.now)
#
#     def __str__(self):
#         return f"Friend List of {self.user.username} (created at {self.current_time})"
#
#
# # danh sach chap nhan ket bạn
# # class FriendRequest(models.Model):
# #     sender = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
# #     receiver = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
# #     accepted = models.BooleanField(default=False)
# #     created_at = models.DateTimeField(auto_now_add=True)
# #     current_time = models.DateTimeField(default=datetime.now)
# #     def __str__(self):
# #         return f"{self.sender.username} -> {self.receiver.username} ({'Accepted' if self.accepted else 'Pending'}) (created at {self.created_at})"
#
#
#
# class FriendRequest(models.Model):
#     sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
#     receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
#     is_accepted = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return f"{self.sender.username} to {self.receiver.username}"
##################################################################################################
# trong models.py
from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import datetime


class FriendRequest(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_requests')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_requests')
    is_accepted = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} to {self.receiver.username}"


class Friendship(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='friend_list')
    friends = models.ManyToManyField(User, related_name='friends')
    current_time = models.DateTimeField(default=False)

    def __str__(self):
        return f"Friend List of {self.user.username} (created at {self.current_time})"
