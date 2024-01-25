from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from .models import Friendship, FriendInvitation, FriendRequest
from django.contrib import messages
from .models import User, Friendship
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def home(request, *args, **kwargs):
    context = {}
    return render(request, "snippets/home.html", context)


def dskb(request, *args, **kwargs):
    # if request.user.is_authenticated():

    return render(request, "snippets/dskb.html")


def dsbb(request, *args, **kwargs):
    context = {}
    return render(request, "snippets/dsbb.html", context)





# danh sach loi moi ket ban
def friend_invitation_view(request):
    user = request.user
    received_invitations = FriendInvitation.objects.filter(receiver=user)
    sent_invitations = FriendInvitation.objects.filter(sender=user)
    return render(request, 'snippets/dsloimoikb.html',
                  {'received_invitations': received_invitations, 'sent_invitations': sent_invitations})


def send_friend_invitation(request, receiver_id):
    # Kiểm tra xem lời mời đã tồn tại chưa
    if FriendInvitation.objects.filter(sender=request.user, receiver_id=receiver_id).exists():
        messages.warning(request, 'Bạn đã gửi lời mời kết bạn đến người này rồi.')
    else:
        # Tạo lời mời mới
        FriendInvitation.objects.create(sender=request.user, receiver_id=receiver_id)
        messages.success(request, 'Lời mời kết bạn đã được gửi thành công.')

    return redirect('friend_invitations')

# danh sach ban be
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


def loginPage(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Authenticate user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Login user
            login(request, user)
            return redirect(
                'dskb')  # Thay đổi 'your_redirect_url' thành URL bạn muốn chuyển hướng sau khi đăng nhập thành công
        else:
            error_message = "Mật khẩu hoặc tài khoảng không đúng."
            context = {'error_message': error_message}
            return render(request, 'snippets/login.html', context)
    return render(request, 'snippets/login.html')


def remove_friend(request, friend_id, FriendList=None):
    # Lấy đối tượng FriendList của người dùng hiện tại
    friend_list, created = FriendList.objects.get_or_create(user=request.user)
    # Lấy đối tượng người dùng bạn muốn xóa khỏi danh sách bạn bè
    friend_to_remove = User.objects.get(id=friend_id)
    # Xóa bạn bè nếu tồn tại trong danh sách
    if friend_to_remove in friend_list.friends.all():
        friend_list.friends.remove(friend_to_remove)
    return redirect('view_friend_list')


def base(request):
    return render(request, 'snippets/base.html')


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


def list(request):
    users = User.objects.all()
    return render(request, 'snippets/dskb.html', {'users': users})


@login_required
def friendship_view(request):
    user = request.user
    friendships = Friendship.objects.filter(user=user)
    return render(request, 'snippets/dsbb.html', {'friendships': friendships})


@login_required
def send_friend_request(request, receiver_id):
    if request.method == 'POST':
        receiver = get_object_or_404(User, id=receiver_id)
        sender = request.user

        # Kiểm tra xem lời mời đã được gửi trước đó hay chưa
        existing_request = FriendRequest.objects.filter(sender=sender, receiver=receiver, accepted=False)
        if not existing_request.exists():
            # Tạo một lời mời mới
            FriendRequest.objects.create(sender=sender, receiver=receiver)
            return JsonResponse({'status': 'success', 'message': 'Friend request sent successfully'})
        else:
            return JsonResponse({'status': 'error', 'message': 'Friend request already sent'})

    return JsonResponse({'status': 'error', 'message': 'Invalid request'})
#
# @login_required
# def accept_friend_request(request, friend_request_id):
#     friend_request = get_object_or_404(FriendRequest, id=friend_request_id, to_user=request.user)
#     friend_request.accepted = True
#     friend_request.save()
#     return JsonResponse({'status': 'success'})