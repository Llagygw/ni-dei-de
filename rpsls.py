#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#coding:gbk
"""
第一个小项目：Rock-paper-scissors-lizard-Spock
作者：陈姿睿
日期：
"""

import random



# 0 - 石头
# 1 - 史波克
# 2 - 纸
# 3 - 蜥蜴
# 4 - 剪刀

# 以下为完成游戏所需要用到的自定义函数

def name_to_number(name):
    """
    将游戏对象对应到不同的整数
    """

    # 使用if/elif/else语句将各游戏对象对应到不同的整数
    # 不要忘记返回结果
  
    if name == "石头":
        name = 0
        return name
    elif name == "史波克":
        name = 1
        return name
    elif name == "纸":
        name = 2
        return name
    elif name == "蜥蜴":
        name = 3
        return name
    elif name == "剪刀":
        name = 4
        return name
    else:
        print('Errror:No correct Name')
        name = -1
        return name
       


    



def number_to_name(number):
    """
    将整数 (0, 1, 2, 3, or 4)对应到游戏的不同对象
    """

    # 使用if/elif/else语句将不同的整数对应到游戏的不同对象
    # 不要忘记返回结果
    if number == 0:
       number = "石头"
       return number
    elif number == 1:
       number = "史波克"
       return number
    elif number == 2:
       number = "纸"
       return number
    elif number == 3:
       number = "蜥蜴"
       return number
    elif number == 4:
       number = "剪刀"
       return number
    


def rpsls(choice_name):
    
    """
    用户玩家任意给出一个选择，根据RPSLS游戏规则，在屏幕上输出对应的结果

    """


    # 输出"-------- "进行分割
    # 显示用户输入提示，用户通过键盘将自己的游戏选择对象输入，存入变量player_choice

    # 调用name_to_number()函数将用户的游戏选择对象转换为相应的整数，存入变量player_choice_number

    # 利用random.randrange()自动产生0-4之间的随机整数，作为计算机随机选择的游戏对象，存入变量comp_number

    # 调用number_to_name()函数将计算机产生的随机数转换为对应的游戏对象

    # 在屏幕上显示计算机选择的随机对象

    # 利用if/elif/else 语句，根据RPSLS规则对用户选择和计算机选择进行判断，并在屏幕上显示判断结果

    # 如果用户和计算机选择一样，则显示“您和计算机出的一样呢”，如果用户获胜，则显示“您赢了”，反之则显示“计算机赢了”

    pass #根据以上提示编写执行代码，代码完成后删除掉pass
    
 
    comp_number = random.randrange(5)
    
    while(name_to_number(choice_name) == -1):
        print ("please enter again")
        choice_name=input() 
  
    player_number = name_to_number(choice_name)
    print("您的选择为: " + choice_name)

    print("机器的选择为: " + number_to_name(comp_number))

    difference = (int(player_number) - comp_number) % 5

    draws = 0

    playerwins = 0

    computerwins = 0
    
    if difference in [1, 2]:
        print ("您获胜了!")
        choice_name=input() 
        rpsls(choice_name)



    elif difference == 0:
        print ("您和机器打平了!")
        choice_name=input() 
        rpsls(choice_name)


    else:
        print ("电脑获胜了!")
        choice_name=input() 
        rpsls(choice_name)
        
   

    

# 对程序进行测试
print("欢迎使用RPSLS游戏")
print("----------------")
print("请输入您的选择:")
choice_name=input() 
rpsls(choice_name)



# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




