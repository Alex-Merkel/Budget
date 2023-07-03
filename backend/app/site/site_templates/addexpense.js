function showExpensePopup(category) {
    var popup = document.getElementById("expense-popup");
    popup.style.display = "block";

    var expenseNameInput = document.getElementById("expense-name-input");
    expenseNameInput.value = '';

    var expenseValueInput = document.getElementById("expense-value-input");
    expenseValueInput.value = '';

    popup.setAttribute('data-category', category);
}

function saveExpense() {
    var expenseNameInput = document.getElementById('expense-name-input');
    var expenseValueInput = document.getElementById('expense-value-input');
    var category = document.getElementById('expense-popup').getAttribute('data-category');

    var expenseSection = document.createElement('div');
    expenseSection.classList.add('grid-item', 'bg-dark', 'border-gray');

    var expenseName = expenseNameInput.value;
    var expenseValue = expenseValueInput.value;

    if (!expenseName) {
        alert('Expense name is required.');
        return;
    }

    var expenseNameHeader = document.createElement('h5');
    expenseNameHeader.textContent = expenseName;
    expenseSection.appendChild(expenseNameHeader);

    var expenseValueInput = document.createElement('input');
    expenseValueInput.type = 'text';
    expenseValueInput.value = expenseValue;
    expenseValueInput.name = category;
    expenseSection.appendChild(expenseValueInput);

    var container = document.getElementById(category);
    container.insertBefore(expenseSection, container.lastElementChild);

    closePopup();
}


function closePopup() {
    var popup = document.getElementById("expense-popup");
    popup.style.display = "none";
}