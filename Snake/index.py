import turtle
import time
import random


__author__ = "Karlbaey"
__copyright__ = "Copyright (c) 2025 Karlbaey"
__license__ = "GPLv3"
__version__ = "1.0.0"


# 设置游戏参数 
score = 0
high_score = 0
# 游戏速度，小蛇每走一步等待的时间。单位：s
delay = 0.1

# 初始化屏幕
wn = turtle.Screen()
wn.title("贪吃蛇")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)

# 分数显示
score_display = turtle.Turtle()
score_display.speed(0)
score_display.shape("square")
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(-290, 270)
score_display.write("分数: 0\n最高分: 0", align="left", font=("Noto Sans SC", 14, "normal"))

# 蛇头
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "stop"

# 食物
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

segments = []

# 初始化蛇身段
for i in range(3):
    new_segment = turtle.Turtle()
    new_segment.speed(0)
    new_segment.shape("square")
    new_segment.color("grey")
    new_segment.penup()
    new_segment.goto(-20 * (i+1), 0)
    segments.append(new_segment)

# 键盘控制函数
def go_up():
    if head.direction != "down" and head.direction != "up":
        head.direction = "up"

def go_down():
    if head.direction != "up" and head.direction != "down":
        head.direction = "down"

def go_left():
    if head.direction != "right" and head.direction != "left":
        head.direction = "left"

def go_right():
    if head.direction != "left" and head.direction != "right":
        head.direction = "right"

# 键盘绑定
wn.listen()
wn.onkeypress(go_up, "w")
wn.onkeypress(go_down, "s")
wn.onkeypress(go_left, "a")
wn.onkeypress(go_right, "d")
wn.onkeypress(go_up, "Up")
wn.onkeypress(go_down, "Down")
wn.onkeypress(go_left, "Left")
wn.onkeypress(go_right, "Right")

# 移动函数
def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)

# 主游戏循环
while True:
    wn.update()
    
    # 检测碰撞边界
    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
        # 隐藏身体
        for segment in segments:
            segment.goto(1000, 1000)
        
        # 清空身体列表
        segments.clear()
        
        # 重新初始化蛇身段
        for i in range(3):
            new_segment = turtle.Turtle()
            new_segment.speed(0)
            new_segment.shape("square")
            new_segment.color("grey")
            new_segment.penup()
            new_segment.goto(-20 * (i+1), 0)
            segments.append(new_segment)
    
    # 检测吃到食物
    if head.distance(food) < 20:
        # 移动食物到随机位置
        x = random.randint(-14, 14) * 20
        y = random.randint(-14, 14) * 20
        food.goto(x, y)
        
        # 添加身体
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        segments.append(new_segment)
        
        # 更新分数
        score += 10
        if score > high_score:
            high_score = score
        score_display.clear()
        score_display.write(f"分数: {score} 最高分: {high_score}", align="left", font=("Noto Sans SC", 14, "normal"))
    
    # 移动身体
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
    
    # 移动第一节到头部
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    # 检测碰撞身体
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
            
            # 隐藏身体
            for segment in segments:
                segment.goto(1000, 1000)
            
            # 清空身体列表
            segments.clear()
            
            # 重新初始化蛇身段
            for i in range(3):
                new_segment = turtle.Turtle()
                new_segment.speed(0)
                new_segment.shape("square")
                new_segment.color("grey")
                new_segment.penup()
                new_segment.goto(-20 * (i+1), 0)
                segments.append(new_segment)
            
            # 重置分数
            score = 0
            score_display.clear()
            score_display.write(f"分数: {score} \n 最高分: {high_score}", align="left", font=("Noto Sans SC", 14, "normal"))
    
    time.sleep(delay)