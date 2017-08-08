from django.http import HttpResponse

from timeRecord.models import User

# 数据库操作
def testdb(request):
    user = User(nickName='runoob',mobile='13051321091')
    user.save()
    return HttpResponse("<p>数据添加成功！</p>")