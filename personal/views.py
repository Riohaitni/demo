from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import FriendInvitation,Friendship,FriendRequest
from django.contrib import messages

# Create your views here.
def home(request, *args, **kwargs):
    context = {}
    return render(request, "snippets/home.html", context)

def dskb(request, *args, **kwargs):
    context = {}
    return render(request, "snippets/dskb.html", context)

def dsbb(request, *args, **kwargs):
    context = {}
    return render(request, "snippets/dsbb.html", context)

def dsloimoikb(request, *args, **kwargs):
    context = {}
    return render(request, "snippets/dsloimoikb.html", context)

def friend_invitations(request):
    # Lấy ra tất cả lời mời kết bạn
    invitations = FriendInvitation.objects.all()

    context = {'invitations': invitations}
    return render(request, 'snippets/dskb.html', context)


#danh sach loi moi ket ban
def send_friend_invitation(request, receiver_id):
    # Kiểm tra xem lời mời đã tồn tại chưa
    if FriendInvitation.objects.filter(sender=request.user, receiver_id=receiver_id).exists():
        messages.warning(request, 'Bạn đã gửi lời mời kết bạn đến người này rồi.')
    else:
        # Tạo lời mời mới
        FriendInvitation.objects.create(sender=request.user, receiver_id=receiver_id)
        messages.success(request, 'Lời mời kết bạn đã được gửi thành công.')

    return redirect('friend_invitations')


#danh sach ban be
def friend_list(request):
    # Lấy ra danh sách kết bạn của người dùng hiện tại
    friendships = Friendship.objects.filter(user=request.user)

    context = {'friendships': friendships}
    return render(request, 'snippets/dsbb.html', context)


#danh sach chap nhan ket ban
def friend_requests(request):
    # Lấy ra danh sách lời mời kết bạn chưa được chấp nhận của người dùng hiện tại
    friend_requests_received = FriendRequest.objects.filter(receiver=request.user, accepted=False)

    context = {'friend_requests_received': friend_requests_received}
    return render(request, 'snippets/dsloimoikb.html', context)

def accept_friend_request(request, request_id):
    # Xác nhận một lời mời kết bạn
    friend_request = FriendRequest.objects.get(pk=request_id)

    if friend_request.receiver == request.user:
        friend_request.accepted = True
        friend_request.save()
        messages.success(request, 'Lời mời kết bạn đã được chấp nhận.')
    else:
        messages.warning(request, 'Không thể chấp nhận lời mời kết bạn này.')

    return redirect('friend_requests')