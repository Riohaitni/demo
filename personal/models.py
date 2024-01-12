from django.db import models
from django.contrib.auth.models import User



#danh sach loi moi ket ban
class FriendInvitation(models.Model):
    sender = models.ForeignKey(User, related_name='sent_invitations', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='received_invitations', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected')], default='pending')
    sent_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({self.status})"


#danh sach ban be
class Friendship(models.Model):
    user = models.ForeignKey(User, related_name='user', on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name='friend', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.user.username} -> {self.friend.username}"

    


#danh sach chap nhan ket bạn
class FriendRequest(models.Model):
    sender = models.ForeignKey(User, related_name='friend_requests_sent', on_delete=models.CASCADE)
    receiver = models.ForeignKey(User, related_name='friend_requests_received', on_delete=models.CASCADE)
    accepted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender.username} -> {self.receiver.username} ({'Accepted' if self.accepted else 'Pending'})"


