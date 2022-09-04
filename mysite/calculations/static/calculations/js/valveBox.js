//////////////////// Випадаючі списки //////////////////////

const selects = {
    layer: document.querySelector("#Layers"),
    marka: document.querySelector("#Marka"),
    profile: document.querySelector("#Profile"),
    colour: document.querySelector("#Colour"),
    print: document.querySelector("#Print"),
}

const options = {
    marks20: ['20', '21', '22', '23', '24', '25', '26'],
    marks30: ['30', '31', '32', '33', '34'],
    prof20: ['E', 'B', 'C'],
    prof30: ['EB', 'EC', 'BC'],
    colors: ['Бурий', 'Білий'],
}


function selectedLayers() {

    // Очищення марки та профілю
    clearComboBox(selects.marka);
    clearComboBox(selects.profile);

    // Заповнюємо марку та профіль
    switch (selects.layer.value) {
        case 'Т':
            fillComboBox(selects.marka, options.marks20);
            fillComboBox(selects.profile, options.prof20);
            break;

        case 'П':
            fillComboBox(selects.marka, options.marks30);
            fillComboBox(selects.profile, options.prof30);
            break;
    }
}


function clearComboBox(comboBox) {
    while (comboBox.options.length > 0) {                
        comboBox.remove(0);
    }   
}

function fillComboBox(comboBox, array) {
    for (var i = 0; i < array.length; ++i) {
        comboBox[comboBox.length] = new Option(array[i], array[i]);
    }
}


////////////////////////  SUBMIT BUTTON  ////////////////////////

// Допустимі розміри ящика
boxDimensions = {
    minLen: 90, maxLen: 1080,
    minWid: 90, maxWid: 1080,
    minHei: 0, maxHei: 2000,
};

// Інпути
const inputs = document.querySelectorAll('.size__input');

// Відміняємо відправляння форми при натисканні ентера
for (let input of inputs) {
    input.addEventListener("keypress", function(event) {
        if (event.key === "Enter") {
            event.preventDefault();
        }
    })
}

// ПЕРЕВІРКА РОЗМІРУ ЯЩИКА
function isValidValue(min, max, value) {
    if (min <= parseInt(value) && parseInt(value) <= max) 
        return true;
    return false;
}

function onChange(minProperty, maxProperty, id) {
    const sizeInput = document.querySelector(`#${id}`);
    const value = sizeInput.value;

    if (!isValidValue(boxDimensions[minProperty], boxDimensions[maxProperty], value)) {
        sizeInput.style.background = "rgb(231, 68, 68)";
        sizeInput.style.color = "white";
    }
}

function onInput(minProperty, maxProperty, id) {
    const sizeInput = document.querySelector(`#${id}`);

    if (!isValidValue(boxDimensions[minProperty], boxDimensions[maxProperty], sizeInput.value)) 
        return;
    
    sizeInput.style.background = "#a1d6e2";
    sizeInput.style.color = "black";
}

// Сама кнопка
const submitButton = document.querySelector('.submitButton');

submitButton.addEventListener("click", function(event) {

    if (!isValidValue(boxDimensions['minLen'], boxDimensions['maxLen'], inputs[0].value) ||
        !isValidValue(boxDimensions['minWid'], boxDimensions['maxWid'], inputs[1].value) ||
        !isValidValue(boxDimensions['minHei'], boxDimensions['maxHei'], inputs[2].value)) {

        onChange('minLen', 'maxLen', 'in1');
        onChange('minWid', 'maxWid', 'in2');
        onChange('minHei', 'maxHei', 'in3');
        document.querySelector('.size').scrollIntoView({block: "center", behavior: "smooth"});
        event.preventDefault();
        return;
    }
    
    const layerSelect = document.querySelector('#Layers');
    let zagWid = parseInt(inputs[1].value) + parseInt(inputs[2].value) + 4, 
        zagLen;

    if (layerSelect.value === 'П') {
        zagLen = (parseInt(inputs[0].value) + parseInt(inputs[1].value)) * 2 + 40;
    } else {
        zagLen = (parseInt(inputs[0].value) + parseInt(inputs[1].value)) * 2 + 50;
    }

    if (zagLen < 440 || zagLen > 2200 || zagWid < 228 || zagWid > 2000) {
        alert('Недопустимий розмір заготовки');
        event.preventDefault();
    }
})


//////////////////////////////// Scroll to answers //////////////////////////////////////
function scrollToAnswers() {
    const lenInput = document.querySelector('#in1');
    if (lenInput.value !=='') {
        document.querySelector('.answers').scrollIntoView({block: "center", behavior: "smooth"});
    }
}



/////////////////////////////////  BURGER MENU  //////////////////////////////////////


