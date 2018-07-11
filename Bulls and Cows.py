import random

def dead(count):
    print("厉害了，第%r次你就猜中了! Game Over!" %count)


def inputRange():
    print("---------接下来我们输入需要猜测的数字范围--------")
    left = input("请输入最小的数字： ")
    if left.isdigit():
        left = int(left)
    else:
        print("亲，请输入数字!")
        inputRange()
    right = input("请输入最大的数字： ")
    if right.isdigit():
        right = int(right)
    else:
        print("亲，请输入数字!")
        inputRange()
    if right > left:
        print("需要猜的范围是%r ~ %r,包含左右边界。" %(left, right))
    else:
        print("最大数字必须大于最小数字")
        inputRange()
    return left, right

def randomInt(left, right):
    answer = random.randint(left, right)
    return answer

def compare(x):
    if x.isdigit():
        x = int(x)
        return x
    else:
        print("请输入正整数，不要乱输入哦-----")
        return -1

def guess(left, right, answer, count):
    #print("debug--Information: answer is %r--count is %r" %(answer, count))
    print("debug--Information: rang is %r ~ %r" %(left, right))
    userGuess = input("请输入您猜测的数字：")
    if userGuess.isdigit() and left <= int(userGuess) <= right:
        if answer == int(userGuess):
            count = count + 1
            dead(count)
        elif answer < int(userGuess):
            right = int(userGuess)
            count = count + 1
            print("数字大了，范围缩小了。")
            guess(left, right, answer, count)
        elif answer > int(userGuess):
            left = int(userGuess)
            count = count + 1
            print("数字小了，范围缩小了。")
            guess(left, right, answer, count)
    else:
        print("输入的必须是数字并且要在%r ~ %r之间。" %(left, right))
        count = count + 1
        guess(left, right, answer, count)




#游戏主题
left, right = inputRange()#首先输入需要猜测的范围
answer = randomInt(left, right)#有系统产生随机数，以供猜测
count = 0
guess(left, right, answer, count)#用户开始猜测


