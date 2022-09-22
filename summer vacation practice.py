# import requests
#
# url = "https://movie.douban.com/j/chart/top_list"
# chansu = {
#     "type": "24",
#     "interval_id": "100:90",
#     "action": "",
#     "start": 0,
#     "limit": 20,
# }
# hea = {
#   "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36"
# }
# nr=requests.get(url,params=chansu,headers=hea)
# print(nr.json())
#

# for i in range(1,10):
#     for f in range(1,i+1):
#          print(f"{i}X{f}={i * f}",end=" ")        #99*法表
#     print()


# for i in range(2,101):
#     for e in range(2,i):
#         if i % e ==0:
#             break              #一百以内的质素
#     else:
#         print(i)

# for i in range(1,11):
#     if i <=5:
#         print("* "* i)
#     else:                  #
#         print("* "*(10-i))


# cai = 0
# age_cai = input("请输入你想的整数:")
# while cai < 3:
#     cai_age = input("请输入你猜的数:")
#     if cai_age != age_cai:
#         print("猜错了！")
#     else:
#         print("真聪明。")           #数字游戏
#         break
#     cai += 1
#     if cai == 3:
#         jhui = input("[重新开始]或者[退出游戏]")
#         if jhui in (f"重新开始"):
#             cai = 0
#         elif jhui in (f"退出游戏"):
#             continue


# year = 0
# principal = float(input("请输入你要存入的金额:"))
# interest = float(input("请输入现在的利息:"))
# profit = float(input("请输入你想要到达的利润:"))
# while (principal) <= (profit):             # 计算利润
#     year+=1
#     principal = principal + (principal * interest)  #== principal += (principal * interest)
#     print (year,"年",principal,"元")



# high = float(input("请输入小球的高度:"))
# frequency = int(input("请输入反弹的次数:"))
# length = 0
# for i in range(frequency):
#     length += high + high/2      #小球反弹
#     high = high / 2
#
#     print(high,"米",length,"米")



# last_day = int(input("请输入要计算的天数:"))
# zosu = 1
# while last_day >=1:
#     zosu = (zosu + 1 ) * 2            #猴子吃桃
#     last_day -= 1
#     print(zosu)


# number = float(input("请输入你要计算的数:"))
# osu = 0
# jisu =0
# hui = 0
# while number >=1 :
#     if number % 2 ==0:
#         osu = number
#     else:
#         jisu = number
#     hui=osu - jisu
#     print(hui)
#     number-= 1
#
#
#
































