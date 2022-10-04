scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile1`, function (sprite, location) {
    if (true) {
        当前关卡 += 1
    } else {
    	
    }
})
scene.onOverlapTile(SpriteKind.Player, assets.tile`myTile4`, function (sprite, location) {
    game.over(false)
})
controller.A.onEvent(ControllerButtonEvent.Pressed, function () {
    if (monkey1.isHittingTile(CollisionDirection.Bottom)) {
        monkey1.vy = -320
    }
})
function 创建英雄 () {
    monkey1 = sprites.create(assets.image`monkey1`, SpriteKind.Player)
    controller.moveSprite(monkey1, 100, 0)
    scene.cameraFollowSprite(monkey1)
    monkey1.ay = 980
}
function 初始化变量 () {
    scene.setBackgroundColor(9)
    当前关卡 = 1
    关卡总量 = 3
}
function 更新地图 () {
    if (当前关卡 == 1) {
        tiles.setCurrentTilemap(tilemap`级别1`)
    } else if (当前关卡 == 2) {
        tiles.setCurrentTilemap(tilemap`级别5`)
    } else if (当前关卡 == 3) {
        tiles.setCurrentTilemap(tilemap`级别6`)
    }
}
let 关卡总量 = 0
let monkey1: Sprite = null
let 当前关卡 = 0
初始化变量()
创建英雄()
更新地图()
