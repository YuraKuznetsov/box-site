// РОБОТА З НАВІГАЦІЄЮ

// Отримуємо навігаційну планку
const navigation = document.querySelector(".nav");
const items = navigation.children;

// Навішуємо прослуховувач
navigation.addEventListener("click", function(e) {

    // Знімаємо активний клас з усіх елементів
    Array.from(items).forEach(elem => {
        elem.classList.remove("active");
    })

    // Відмічаємо як активне обране меню
    const activeItem = e.target;
    activeItem.classList.add("active");
})


//////////////////// Випадаючі списки //////////////////////

const selects = {
    layer: document.querySelector("#Layers"),
    marka: document.querySelector("#Marka"),
    profile: document.querySelector("#Profile"),
    colour: document.querySelector("#Colour"),
    print: document.querySelector("#Print"),
}

const options = {
    marks20: ['-', '20', '21', '22', '23', '24', '25', '26'],
    marks30: ['-', '30', '31', '32', '33', '34'],
    prof20: ['-', 'E', 'B', 'C'],
    prof30: ['-', 'EB', 'EC', 'BC'],
    fewColors: ['-', 'К', 'Ф'],
    manyColors: ['-', 'К', 'Ф', 'Б', 'М'],
}


function selectedLayers() {
    // Доступні менюшки
    selects.marka.disabled = false;
    selects.profile.disabled = false;

    // Очищення варіантів
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

function changeMarka() {
    selects.colour.disabled = false;
    clearComboBox(selects.colour);

    if ((selects.layer.value === 'Т' && (selects.marka.value === '20' || selects.marka.value === '26')) || 
        (selects.layer.value === 'П' && selects.marka.value === '30')) {
        fillComboBox(selects.colour, options.fewColors);
        selects.colour.value = '-'
        return;
    }

    fillComboBox(selects.colour, options.manyColors);

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