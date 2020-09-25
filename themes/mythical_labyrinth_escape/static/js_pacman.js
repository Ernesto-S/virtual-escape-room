
var world = [
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,2,1,1,1,1,1,2],
    [2,1,2,2,2,1,2,2,2,1,2,1,2,2,2,1,2,2,2,2,2,1,2,1,2,1,2,2,2],
    [2,1,1,1,2,1,1,1,2,1,2,1,2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2],
    [2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,1,2,2,2,2,2,1,2,2,2,1,2,2],
    [2,1,2,1,1,1,2,1,2,1,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,1,2,1,2,1,2,1,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,2,1,1,1,2,1,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,2,2,2,2,2,2,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,2,2,1,2,2,2,1,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,2,1,1,1,1,1,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,2,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,2,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,1,1,1,2,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,1,2,2,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,1,1,1,1,1,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,2,2,2,2,2,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,2,1,1,1,2,1,1,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,1,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,2,2,2,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,2,2,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,2,1,2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
    [2,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1,1,1,1,1,1,1,2],
    [2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2],
]

var pacman = {
    x:1,
    y:1
};

var score = 0;

var cherry = {
    x:-1,
    y:0
}

var ghost = {
    x:-1,
    y:0
}

function displayPacman(){
    document.getElementById("pacman").style.left = pacman.x*20+"px";
    document.getElementById("pacman").style.top = pacman.y*20+"px";
}

function displayCherry(){
    document.getElementById("cherry").style.left = cherry.x*20+"px";
    document.getElementById("cherry").style.top = cherry.y*20+"px";
}

function displayGhost(){
    document.getElementById("ghost").style.left = ghost.x*20+"px";
    document.getElementById("ghost").style.top = ghost.y*20+"px";
}

function displayScore(){
    document.getElementById("score").innerHTML = score;
}

function displayWorld(){
    var output = '';

    for(let i=0; i<world.length; i++){
        output+="<div class = 'row'>";
        for (let j = 0; j < world[i].length; j++) {
            if (world[i][j] == 2){
                output +="<div class = 'brick'></div>";
            }
            else if(world[i][j] == 1){
                output+="<div class = 'coin'></div>";
            }
            else if(world[i][j] == 0){
                output+="<div class = 'empty'></div>";
            }
            else if(world[i][j] == 3){
                output+="<div class = 'cherry'></div>";
            }
            else if(world[i][j] == 4){
                output+="<div class = 'empty'></div>";
            }
        }
        output+="</div>\n";
    }
    //console.log(output);
    document.getElementById('world').innerHTML = output;
}

displayWorld();
displayPacman();
displayScore();
displayCherry();
displayGhost();
var ghost_alive = false;
document.onkeydown = function(e){
    if (e.keyCode == 38 && world[pacman.y-1][pacman.x] != 2) { //up key
        pacman.y--;
        document.getElementById('pacman').style.transform = "rotate(270deg)";
    }
    else if (e.keyCode == 39 && world[pacman.y][pacman.x+1] != 2) { //right key
        pacman.x++;
        document.getElementById('pacman').style.transform = "rotate(0deg)";
    }
    else if (e.keyCode == 40 && world[pacman.y+1][pacman.x] != 2) { //down key
        pacman.y++;
        document.getElementById('pacman').style.transform = "rotate(90deg)";
    }
    else if (e.keyCode == 37 && world[pacman.y][pacman.x-1] != 2) { //left key
        pacman.x--;
        document.getElementById('pacman').style.transform = "rotate(180deg)";
    }


    var direction = Math.floor(Math.random() * 4);

    if (ghost_alive == true) {
        if (direction == 0 && world[ghost.y-1][ghost.x] != 2 ) { //up
            world[ghost.y][ghost.x] = 0;
            ghost.y--;
            world[ghost.y][ghost.x] = 4;
        }
        else if(direction == 1 && world[ghost.y][ghost.x+1] != 2){ //right
            world[ghost.y][ghost.x] = 0;
            ghost.x++;
            world[ghost.y][ghost.x] = 4;
        }
        else if(direction == 2 && world[ghost.y+1][ghost.x] != 2){ //down
            world[ghost.y][ghost.x] = 0;
            ghost.y++;
            world[ghost.y][ghost.x] = 4;
        }
        else if(direction == 3 && world[ghost.y][ghost.x-1] != 2){ //left
            world[ghost.y][ghost.x] = 0;
            ghost.x--;
            world[ghost.y][ghost.x] = 4;
        }       
    }
    

    if (world[pacman.y][pacman.x] == 1) {
        world[pacman.y][pacman.x] = 0;
        score+=10;

        if (score == 50) {
            cherry.x = 1 + Math.floor(Math.random() * 8);
            cherry.y = 1 + Math.floor(Math.random() * 8);
            ghost.x = 1 + Math.floor(Math.random() * 8);
            ghost.y = 1 + Math.floor(Math.random() * 8);
            world[cherry.y][cherry.x] = 3;
            world[ghost.y][ghost.x] = 4;
            ghost_alive = true;
        }
    }

    if (world[pacman.y][pacman.x] == 3) {
        world[pacman.y][pacman.x] = 0;
        score+=50;
        cherry.x = -1;
        cherry.y = 0;
    }

    if (world[pacman.y][pacman.x] == 4) {
        cherry.x = -1;
        cherry.y = 0;
        pacman.x = -1;
        pacman.y = 0;
        ghost.x = -1;
        ghost.y=0;
        score = "GAME OVER!";
    }

    var win = true;
    for (let index = 0; index < world.length; index++) {
        if (world[index].includes(1) == true){
            win = false;
            break
        }
    }

    if (win){
        cherry.x = -1;
        cherry.y = 0;
        pacman.x = -1;
        pacman.y = 0;
        ghost.x = -1;
        ghost.y=0;
        score = "WINNER!";
    }

    displayWorld();
    displayPacman();
    displayScore();
    displayCherry();
    displayGhost();
}
