def on_overlap_tile(sprite, location):
    global 当前关卡
    当前关卡 += 1
    if 当前关卡 <= 关卡总量:
        更新地图()
    else:
        game.over(True)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile1
    """),
    on_overlap_tile)

def on_overlap_tile2(sprite2, location2):
    game.over(False)
scene.on_overlap_tile(SpriteKind.player,
    assets.tile("""
        myTile4
    """),
    on_overlap_tile2)

def on_a_pressed():
    if monkey1.is_hitting_tile(CollisionDirection.BOTTOM):
        monkey1.vy = -320
controller.A.on_event(ControllerButtonEvent.PRESSED, on_a_pressed)

def 创建英雄():
    global monkey1
    monkey1 = sprites.create(assets.image("""
        monkey1
    """), SpriteKind.player)
    controller.move_sprite(monkey1, 100, 0)
    scene.camera_follow_sprite(monkey1)
    monkey1.ay = 980
def 初始化变量():
    global 当前关卡, 关卡总量
    scene.set_background_color(9)
    当前关卡 = 1
    关卡总量 = 3
def 更新地图():
    if 当前关卡 == 1:
        tiles.set_current_tilemap(tilemap("""
            级别1
        """))
    elif 当前关卡 == 2:
        tiles.set_current_tilemap(tilemap("""
            级别5
        """))
    elif 当前关卡 == 3:
        tiles.set_current_tilemap(tilemap("""
            级别6
        """))
monkey1: Sprite = None
关卡总量 = 0
当前关卡 = 0
初始化变量()
创建英雄()
更新地图()