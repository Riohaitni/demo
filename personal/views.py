from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Friendship, FriendInvitation,  FriendRequest
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


#danh sach loi moi ket ban
def friend_invitations(request):
    # Lấy ra tất cả lời mời kết bạn
    invitations = FriendInvitation.objects.all()

    context = {'invitations': invitations}
    return render(request, 'snippets/dskb.html', context)

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
def friend_list(request, FriendList=None):
    # Lấy đối tượng FriendList của người dùng hiện tại
    friend_list, created = FriendList.objects.get_or_create(user=request.user)

    # Lấy danh sách bạn bè
    friends = friend_list.friends.all()

    context = {'friends': friends}
    return render(request, 'dsbb.html', context)


def add_friend(request, friend_id, FriendList=None):
    # Lấy đối tượng FriendList của người dùng hiện tại
    friend_list, created = FriendList.objects.get_or_create(user=request.user)

    # Lấy đối tượng người dùng bạn muốn thêm làm bạn bè
    friend_to_add = User.objects.get(id=friend_id)

    # Thêm bạn bè nếu chưa là bạn bè
    if friend_to_add not in friend_list.friends.all():
        friend_list.friends.add(friend_to_add)

    return redirect('view_friend_list')


def remove_friend(request, friend_id, FriendList=None):
    # Lấy đối tượng FriendList của người dùng hiện tại
    friend_list, created = FriendList.objects.get_or_create(user=request.user)

    # Lấy đối tượng người dùng bạn muốn xóa khỏi danh sách bạn bè
    friend_to_remove = User.objects.get(id=friend_id)

    # Xóa bạn bè nếu tồn tại trong danh sách
    if friend_to_remove in friend_list.friends.all():
        friend_list.friends.remove(friend_to_remove)

    return redirect('view_friend_list')


# danh sach chap nhan ket ban
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
