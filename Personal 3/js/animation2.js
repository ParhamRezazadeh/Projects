var stage = new createjs.Stage("mycanvas")
createjs.Ticker.addEventListener("tick", stageBreakHandler);
var img =  new Image()
img.src = "img/horse.png"
img.onload = function(){
	var ss = new createjs.SpriteSheet({
		"images": ["img/horse.png"], 
		"frames": [
			[519,1352,468,225,0,-39.5,-6.05],
			[525,694,405,225,0,-39.5,-6.05],
			[402,1577,398,241,0,-37.5,-9.05],
			[0,1565,402,239,0,-33.5,-8.05],
			[521,920,430,233,0,-23.5,-14.05],
			[520,0,465,228,0,-7.5,-22.05],
			[515,238,479,228,0,-8.5,-24.05],
			[508,470,500,224,0,-2.5,-26.05],
			[0,470,508,231,0,-5.5,-20.05],
			[0,238,515,232,0,-9.5,-17.05],
			[0,0,520,238,0,-12.5,-11.05],
			[0,920,521,219,0,-18.5,-11.05],
			[0,701,525,219,0,-18.5,-11.05],
			[0,1352,519,213,0,-28.5,-10.05],
			[0,1139,520,213,0,-28.5,-10.05]
		],
		"animations" : {
			"run": [0,14,"run"]
		}
	})

	var sp = new createjs.Sprite(ss,"run")
	stage.addChild(sp)
	stage.update();
}

function stageBreakHandler(event){
	stage.update();
}