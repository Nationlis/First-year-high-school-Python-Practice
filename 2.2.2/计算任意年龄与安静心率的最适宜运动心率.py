"""
活动二 ：计算任意年龄与安静心率的运动心率
在程序运行时输入年龄和安静心率，
计算出最适宜运动心率。
最适宜运动心率=（220-年龄-安静心率） X （60%~80%）+安静心率
"""



age=float(input('请输入age='))              #输入年龄
                                            #输入安静时的心率
low=(220-age-HRrest)*0.6+HRrest             #计算最低心率
high=(220-age-HRrest)*0.8+HRrest            #计算最低心率
print(                               )      #显示最适宜运动心率的范围
input("运行完毕，请按回车键退出...")

