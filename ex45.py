import ex45_scenes

print('''
前一阵子怪兽们的力量突然增强，并且开始有怪兽头领开始组织军队来摧毁人类世界。
经天朝皇家情报局调查发现，原来是怪兽头领得到了一个能量水晶，这个水晶为它们提供了强大的力量。
经过一番调查，情报局掌握了怪兽基地的地图和保管水晶的位置，但是水晶能量强大，飞机、坦克等重装甲无法靠近轰炸。
因此决定派你这位特工潜入内部，摧毁水晶！
''')
scenes = {'Gate': ex45_scenes.Gate(), 'AdytumDoor': ex45_scenes.AdytumDoor(), 'Adytum': ex45_scenes.Adytum()}

current_scene = scenes["Gate"]
while 1:
    next_name = current_scene.enter()
    current_scene = scenes[next_name]
