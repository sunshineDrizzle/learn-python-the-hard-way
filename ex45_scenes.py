import ex45_statuses
import time


class Scenes:
    pass


class Gate(Scenes):

    def enter(self):
        print("你到达怪兽基地的大门前，发现有两个小怪兽在看守，你有如下选择：")
        print("1. 上前打倒两个小怪兽，试图快速解决，快速潜入大门。")
        print("2. 扔一颗小石子到对面，试图引开看守的注意力，伺机潜入大门。")
        print("3. 等待外出的怪兽队伍回来，乔装打扮，混进队伍里进入大门。")

        choice = input("> ")
        if choice == "1":
            print("勇士，你的身手虽然不错，但是这两个小怪兽死缠着你，使得你被巡逻队伍发现了！")
            ex45_statuses.death("Gate")
        elif choice == "2":
            print("小石子只引开了一个小怪兽，你只能重新想办法了！")
            return self.enter()
        elif choice == "3":
            print("你成功地混进了大门，依据情报部门的地图悄悄地来到保管能量水晶的密室门前！")
            return "AdytumDoor"
        else:
            print("请正确选择选项！")
            return self.enter()


class AdytumDoor(Scenes):

    def __init__(self):
        self.count = 0

    def enter(self):
        print("你发现密室门前有一只怪兽精英在看守，密室大门需要密码来正常打开。你有如下选择：")
        print("1. 迅速打败它，试图闯入密室！")
        print("2. 继续扮着小怪兽的模样和它讲笑话，试图在套出密室密码后在解决它。")
        print("3. 用小石子引开它，试图从背后偷袭，迅速解决战斗，并闯入密室。")

        choice = input("> ")
        if choice == "1":
            print("你没想到怪兽精英有两下子，没有被你迅速解决，反而被它按下了警报！")
            ex45_statuses.death("AdytumDoor1")
        elif choice == "2":
            print("你成功地套出了密码，并偷袭成功打晕精英，进入密室！")
            return "Adytum"
        elif choice == "3":
            self.count += 1
            if self.count == 3:
                print("由于你扔了太多次小石子，该精英确定是有人捣鬼，便通知巡逻队伍进行搜索。")
                print("你被抓现形，结局悲惨！")
                ex45_statuses.death("AdytumDoor2")

            print("没想到该精英训练有素，就是不离开密室的门！再想想办法")
            return self.enter()
        else:
            print("请选择合适的选项！")
            return self.enter()


class Adytum(Scenes):

    def enter(self):
        print("你成功进入了密室，趁着没人发现有异动，赶紧去破坏掉能量水晶！")
        print("想要接近水晶，必须要通过一个机关，外部技术人员通过通讯设备教你通过机关的步法")
        print("如果有一步错误或是过关时间大于10秒，水晶会自动攻击你，你是无法抵挡水晶的攻击的！")
        print("字母\"w s a d\"分别代表向“前 后 左 右”一步！")
        print("准备好了就按下回车键！")
        input("> ")

        steps = ""
        time1 = time.time()
        print("向前一步")
        steps += input("> ")
        print("向左一步")
        steps += input("> ")
        print("向前一步")
        steps += input("> ")
        print("向右一步")
        steps += input("> ")
        print("向前两步")
        steps += input("> ")
        print("向右一步")
        steps += input("> ")
        print("向前一步")
        steps += input("> ")
        time2 = time.time()

        t = time2 - time1
        if steps != "wawdwwdw" or t > 10:
            print("Goodbye，你被水晶激光打中了！")
            ex45_statuses.death("Adytum")

        print("恭喜你成功接近并破坏了能量水晶！怪兽们的能力大减，在外面守候多时的部队发起了必胜的进攻！")
        ex45_statuses.finished()
