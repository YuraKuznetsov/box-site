// Поточні розміри ящика та крайні варіанти
boxDimensions = {
    minLen: 200, maxLen: 600,
    minWid: 100, maxWid: 400,
    minHei: 50, maxHei: 700,
};

function createBox(parentClassName, boxClassName) {
    this.scene = document.querySelector(parentClassName);
    this.instance = document.querySelector(boxClassName);
    this.sides = this.instance.children;
    this.length = 300;
    this.width = 100;
    this.height = 200;

    this.showFront = function showFront() {
        this.instance.style.transform = "rotateY(0deg)";
        this.instance.style.transform += `translateZ(${(this.width / -2) + 'px'})`;
    }

    this.showTop = function showTop() {
        this.instance.style.transform = `translateZ(${(this.height / -2) + 'px'})`;
        this.instance.style.transform += "rotateX(-90deg)";
    }

    this.showSide = function showSide() {
        this.instance.style.transform = `translateZ(${(this.length / -2) + 'px'})`;
        this.instance.style.transform += "rotateY(-90deg)";
    }

    this.updateSize = function updateSize(lenInput, widInput, heiInput) {
        this.length = lenInput.value;
        this.width = widInput.value;
        this.height = heiInput.value;
    }

    this.view = function changeSize() {
        // Змінюємо розмір сцени
        this.scene.style.width = this.length + "px";
        this.scene.style.height = this.height + "px";
    
        // Змінюємо саму коробочку
        this.instance.style.width = this.length + 'px';
        this.instance.style.height = this.height + 'px';
        this.instance.style.transform = `translateZ(${(-this.width / 2) + 'px'})`;
    
        // FRONT
        this.sides[0].style.width = this.length + 'px';
        this.sides[0].style.height = this.height + 'px';
        this.sides[0].style.transform = "rotateY(0deg)";
        this.sides[0].style.transform += `translateZ(${(this.width / 2) + 'px'})`;
    
        // BACK
        this.sides[1].style.width = this.length + 'px';
        this.sides[1].style.height = this.height + 'px';
        this.sides[1].style.transform = "rotateY(180deg)";
        this.sides[1].style.transform += `translateZ(${(this.width / 2) + 'px'})`;
    
        // RIGHT
        this.sides[2].style.width = this.width + 'px';
        this.sides[2].style.height = this.height + 'px';
        this.sides[2].style.transform = "rotateY(90deg)";
        this.sides[2].style.transform += `translateZ(${(this.length / 2) + 'px'})`;
        this.sides[2].style.left = ((this.length - this.width) / 2) + 'px';
    
        // LEFT
        this.sides[3].style.width = this.width + 'px';
        this.sides[3].style.height = this.height + 'px';
        this.sides[3].style.transform = "rotateY(-90deg)";
        this.sides[3].style.transform += `translateZ(${(this.length / 2) + 'px'})`;
        this.sides[3].style.left = ((this.length - this.width) / 2) + 'px';
    
        // TOP
        this.sides[4].style.width = this.length + 'px';
        this.sides[4].style.height = this.width + 'px';
        this.sides[4].style.transform = "rotateX(90deg)";
        this.sides[4].style.transform += `translateZ(${(this.height / 2) + 'px'})`;
        this.sides[4].style.top = ((this.height - this.width) / 2) + 'px';
    
        // BOTTOM
        this.sides[5].style.width = this.length + 'px';
        this.sides[5].style.height = this.width + 'px';
        this.sides[5].style.transform = "rotateX(-90deg)";
        this.sides[5].style.transform += `translateZ(${(this.height / 2) + 'px'})`;
        this.sides[5].style.top = ((this.height - this.width) / 2) + 'px';
    }
}

box = new createBox(".size__scene", ".box-size");


// ПЕРЕВІРКА РОЗМІРУ ЯЩИКА
function isValidValue(min, max, value) {
    if (min <= parseInt(value) && parseInt(value) <= max) 
        return true;
    return false;
}

function lastCheck() {
    const lengthInput = document.querySelector("#in1");
    const widthInput = document.querySelector("#in2");
    const heightInput = document.querySelector("#in3");

    // Перевіряємо чи немає інвалідних полів
    if (!isValidValue(boxDimensions['minLen'], boxDimensions['maxLen'], lengthInput.value) ||
        !isValidValue(boxDimensions['minWid'], boxDimensions['maxWid'], widthInput.value) ||
        !isValidValue(boxDimensions['minHei'], boxDimensions['maxHei'], heightInput.value))
        return;

    // Оновлюємо розміри
    box.updateSize(lengthInput, widthInput, heightInput);
    // Змінюємо корoбку на екрані
    box.view();
    // Повертаємо обрану кнопку
    resetRadio();
}

function onChange(minProperty, maxProperty, id) {
    const sizeInput = document.querySelector(`#${id}`);
    const value = sizeInput.value;

    if (!isValidValue(boxDimensions[minProperty], boxDimensions[maxProperty], value)) {
        sizeInput.style.background = "rgba(226, 9, 9, 0.16)";
        sizeInput.style.color = "white";
    }
}

function onInput(minProperty, maxProperty, id) {
    const sizeInput = document.querySelector(`#${id}`);

    if (!isValidValue(boxDimensions[minProperty], boxDimensions[maxProperty], sizeInput.value)) 
        return;
    
    sizeInput.style.background = "white";
    sizeInput.style.color = "black";

    lastCheck();
}

function isFocusOnInputs() {
    const inputs = document.querySelectorAll(".size__input");

    for (input of inputs) {
        if (document.activeElement === input) {
            return true;
        }
    }
    return false;
}

window.addEventListener("keydown", function(event) {
    if (isFocusOnInputs()) 
        return;
    
    if (!['1', '2', '3'].includes(event.key)) 
        return;

    switch (event.key) {
        case '1':
            box.showFront();
            break;
        case '2':
            box.showSide();
            break;
        case '3':
            box.showTop();
            break;
    }
})