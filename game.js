const canvas = document.getElementById('pong');
const ctx = canvas.getContext('2d');

// Game constants
const PADDLE_WIDTH = 12;
const PADDLE_HEIGHT = 90;
const BALL_RADIUS = 10;
const PADDLE_MARGIN = 18;
const PLAYER_COLOR = "#4CAF50";
const AI_COLOR = "#E91E63";
const BALL_COLOR = "#FFEB3B";
const NET_COLOR = "#fff";
const NET_WIDTH = 4;
const NET_SEGMENT = 24;

// Game state
const player = {
    x: PADDLE_MARGIN,
    y: canvas.height / 2 - PADDLE_HEIGHT / 2,
    width: PADDLE_WIDTH,
    height: PADDLE_HEIGHT,
    color: PLAYER_COLOR,
};

const ai = {
    x: canvas.width - PADDLE_MARGIN - PADDLE_WIDTH,
    y: canvas.height / 2 - PADDLE_HEIGHT / 2,
    width: PADDLE_WIDTH,
    height: PADDLE_HEIGHT,
    color: AI_COLOR,
    speed: 4.5,
};

const ball = {
    x: canvas.width / 2,
    y: canvas.height / 2,
    vx: 5 * (Math.random() < 0.5 ? 1 : -1),
    vy: 3 * (Math.random() * 2 - 1),
    radius: BALL_RADIUS,
    color: BALL_COLOR,
    speed: 5,
};

let animationId;

// Draw net
function drawNet() {
    for (let y = 0; y < canvas.height; y += NET_SEGMENT * 2) {
        ctx.fillStyle = NET_COLOR;
        ctx.fillRect(canvas.width/2 - NET_WIDTH/2, y, NET_WIDTH, NET_SEGMENT);
    }
}

// Draw a paddle
function drawPaddle(paddle) {
    ctx.fillStyle = paddle.color;
    ctx.fillRect(paddle.x, paddle.y, paddle.width, paddle.height);
}

// Draw the ball
function drawBall() {
    ctx.beginPath();
    ctx.arc(ball.x, ball.y, ball.radius, 0, Math.PI*2);
    ctx.fillStyle = ball.color;
    ctx.fill();
    ctx.closePath();
}

// Draw everything
function draw() {
    ctx.clearRect(0, 0, canvas.width, canvas.height);
    drawNet();
    drawPaddle(player);
    drawPaddle(ai);
    drawBall();
}

// Ball and paddle collision
function collide(ball, paddle) {
    return (
        ball.x - ball.radius < paddle.x + paddle.width &&
        ball.x + ball.radius > paddle.x &&
        ball.y + ball.radius > paddle.y &&
        ball.y - ball.radius < paddle.y + paddle.height
    );
}

// Move the ball
function moveBall() {
    ball.x += ball.vx;
    ball.y += ball.vy;

    // Top and bottom wall collision
    if (ball.y - ball.radius < 0 || ball.y + ball.radius > canvas.height) {
        ball.vy *= -1;
        ball.y = ball.y - ball.radius < 0 ? ball.radius : canvas.height - ball.radius;
    }

    // Left paddle collision
    if (collide(ball, player)) {
        ball.x = player.x + player.width + ball.radius;
        ball.vx *= -1.08; // Slightly increase speed
        // Add a bit of "spin" based on where the ball hits the paddle
        let collidePoint = (ball.y - (player.y + player.height / 2)) / (player.height / 2);
        ball.vy = ball.speed * collidePoint;
    }

    // Right paddle (AI) collision
    if (collide(ball, ai)) {
        ball.x = ai.x - ball.radius;
        ball.vx *= -1.08;
        let collidePoint = (ball.y - (ai.y + ai.height / 2)) / (ai.height / 2);
        ball.vy = ball.speed * collidePoint;
    }

    // Left or right wall (reset)
    if (ball.x - ball.radius < 0 || ball.x + ball.radius > canvas.width) {
        resetBall();
    }
}

// Move the AI paddle
function moveAI() {
    let target = ball.y - (ai.y + ai.height / 2);
    if (Math.abs(target) > 7) {
        ai.y += ai.speed * Math.sign(target);
    }
    // Boundaries
    if (ai.y < 0) ai.y = 0;
    if (ai.y + ai.height > canvas.height) ai.y = canvas.height - ai.height;
}

// Mouse movement controls player's paddle
canvas.addEventListener('mousemove', function(e) {
    let rect = canvas.getBoundingClientRect();
    let mouseY = e.clientY - rect.top;
    player.y = mouseY - player.height / 2;
    // Boundaries
    if (player.y < 0) player.y = 0;
    if (player.y + player.height > canvas.height) player.y = canvas.height - player.height;
});

// Reset ball to center
function resetBall() {
    ball.x = canvas.width / 2;
    ball.y = canvas.height / 2;
    ball.vx = 5 * (Math.random() < 0.5 ? 1 : -1);
    ball.vy = 3 * (Math.random() * 2 - 1);
}

// Game loop
function game() {
    moveBall();
    moveAI();
    draw();
    animationId = requestAnimationFrame(game);
}

// Start the game
draw();
game();